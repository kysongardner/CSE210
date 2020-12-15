import arcade
import curses
import sys
import os
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Space Invaders"
CURRENT_FOLDER = os.path.dirname(__file__)
CHARACTER_SCALING = 1
PLAYER_MOVE_SPEED = 5
BULLET_SPEED = 5

# TODO:
# 1) create an Alien class that has guns (just like player really)
# 2) modify gun class so that you can tell it to fire up or down at creation
# 3) create a General class that controls the group of aliens (see on_update)
# 4) finish BulletAlienCollisionHandler class (on_collision)
# 5) create a BulletShieldCollisionHandler class (on_collision)
# 6) create a BulletPlayerCollisionHandler class (on_collision)
# 7) create a Shield class

# ------------------------------------------------------------------------------
# Game Base Classes (to inherit from)
# ------------------------------------------------------------------------------
class Actor(arcade.Sprite):
    
    def __init__(self, tag):
        super().__init__()
        self._game_view = None
        self._tag = tag
    
    def get_tag(self):
        return self._tag
        
    def get_gameview(self):
        return self._game_view

    def on_draw(self):
        pass

    def on_key_press(self, key):
        pass
    
    def on_key_release(self, key):
        pass
    
    def on_update(self):
        pass

    def set_gameview(self, game_view):
        self._game_view = game_view

    def setup(self):
        pass


class CollisionHandler:


    def __init__(self):
        self._game_view = None

    def on_collision(self):
        pass

    def set_gameview(self, game_view):
        self._game_view = game_view

    def get_gameview(self):
        return self._game_view


class Bullet(Actor):
    
    def __init__(self, tag):
        super().__init__(tag)
    
    def on_draw(self):
        super().draw()

    def on_update(self):
        self.center_y += self.change_y
        self._limit_vertical_position()

    def setup(self):
        filename = CURRENT_FOLDER + "/bullet.png"
        texture = arcade.load_texture(filename)
        self.texture = texture
        self.scale = CHARACTER_SCALING

    def _limit_vertical_position(self):
        if self.bottom < 0:
            self.get_gameview().remove_actor(self)
        elif self.top > SCREEN_HEIGHT - 1:
            self.get_gameview().remove_actor(self)



class Guns(Actor):

    MIN_CHARGE = 120

    def __init__(self, player, bullet_direction_UP_or_DOWN):
        self.charge = 0
        self.player = player
        self.triggered = False
        self.bullet_direction_UP_or_DOWN = bullet_direction_UP_or_DOWN

    def fire(self):
        self.triggered = True

    def on_update(self):
        self.charge += 1
        if self.triggered and self.charge >= self.MIN_CHARGE:
            self._add_bullet()
            self.charge = 0
            self.triggered = False
    
    def _add_bullet(self):
        tag = "player_bullet"
        if self.bullet_direction_UP_or_DOWN == "DOWN":
            tag = "alien_bullet"
        bullet = Bullet(tag)
        bullet.center_x = self.player.center_x
        bullet.center_y = self.player.center_y
        if self.bullet_direction_UP_or_DOWN == "UP":
            bullet.change_y = BULLET_SPEED
        elif self.bullet_direction_UP_or_DOWN == "DOWN":
            bullet.change_y = -BULLET_SPEED
        bullet.setup()
        self.player.get_gameview().add_actor(bullet)
    

class Player(Actor):

    def __init__(self):
        super().__init__("player")
        self.lives = 3
        self.score = 0
        self.guns = Guns(self, "UP")

    def on_draw(self):
        super().draw()

    def on_key_press(self, key):
        if key == arcade.key.LEFT:
            self.change_x = -PLAYER_MOVE_SPEED
        if key == arcade.key.RIGHT:
            self.change_x = PLAYER_MOVE_SPEED
        if key == arcade.key.SPACE:
            self.guns.fire()

    def on_key_release(self, key):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.change_x = 0

    def on_update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self._limit_horizontal_position()
        self._limit_vertical_position()
        self.guns.on_update()

    def setup(self):
        filename = CURRENT_FOLDER + "/battleship.png"
        texture = arcade.load_texture(filename)
        self.texture = texture
        self.scale = CHARACTER_SCALING

    def _limit_horizontal_position(self):
        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

    def _limit_vertical_position(self):
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

class Alien(Actor):
    
    def __init__(self, position_x, position_y):
        super().__init__("alien")
        self.lives = 3
        self.score = 0
        self.guns = Guns(self, "DOWN")
        self.center_x = position_x
        self.center_y = position_y
        self.barrier_left = self.center_x - 50
        self.barrier_right = self.center_x + 50
        self.change_x = 1
        self.change_y = 0

    def on_draw(self):
        super().draw()

    def on_update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self._limit_horizontal_position()
        self._limit_vertical_position()
        self.guns.fire()
        self.guns.on_update()

    def setup(self):
        filename = CURRENT_FOLDER + "/alien.png"
        texture = arcade.load_texture(filename)
        self.texture = texture
        self.scale = CHARACTER_SCALING

    def _limit_horizontal_position(self):
        if self.left <= self.barrier_left:
            self.change_x += 1
            self.center_y -= 5
        elif self.right >= self.barrier_right:
            self.change_x -= 1
            self.center_y -= 5

    def _limit_vertical_position(self):
        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1

    class Score(Actor):
        def __init__(self):
            self.score = 0
            self.text_score = "Score:" + self.score
        
        def update_score(self):
            player_bullets = self.get_gameview().get_actors_by_tag("player_bullet")
            aliens = self.get_gameview().get_actors_by_tag("alien")
            for bullet in player_bullets:
                for alien in aliens:
                    collided = arcade.check_for_collision(bullet, alien)
                    if collided:
                        self.score += 10

        def on_update(self):
            self.update_score()
            


class BulletAlienCollisionHandler(CollisionHandler):

    def __init__(self, bullet, alien):
        pass

    def on_collision(self):
        player_bullets = self.get_gameview().get_actors_by_tag("player_bullet")
        alien_bullets = self.get_gameview().get_actors_by_tag("alien_bullet")
        players = self.get_gameview().get_actors_by_tag("player")
        aliens = self.get_gameview().get_actors_by_tag("alien")
        
        # Remove alien and battleship bullet
        for bullet in player_bullets:
            for alien in aliens:
                collided = arcade.check_for_collision(bullet, alien)
                if collided:
                    self.get_gameview().remove_actor(alien)
                    self.get_gameview().remove_actor(bullet)

        # Remove alien bullet and battleship
        for bullet in alien_bullets:
            for player in players:
                collided = arcade.check_for_collision(bullet, player)
                if collided:
                    self.get_gameview().remove_actor(bullet)
                    self.get_gameview().remove_actor(player)
                    self.get_gameview().game_over()

        # Remove battleship if alien and battleship collide
        for alien in aliens:
            for player in players:
                collided = arcade.check_for_collision(alien, player)
                if collided:
                    self.get_gameview().remove_actor(player)
                    self.get_gameview().game_over()

# ------------------------------------------------------------------------------
# Game View Classes
# ------------------------------------------------------------------------------
class GameView(arcade.View):
    
    def __init__(self):
        super().__init__()
        self._actors = []
        self._collision_handlers = []
    
    def add_actor(self, actor):
        if actor not in self._actors:
            self._actors.append(actor)
            actor.set_gameview(self)

    def add_handler(self, handler):
        if handler not in self._collision_handlers:
            self._collision_handlers.append(handler)
            handler.set_gameview(self)
    
    def get_actors(self):
        return self._actors
    
    def get_actors_by_tag(self, tag):
        actors = []
        for actor in self._actors:
            if actor.get_tag() == tag:
                actors.append(actor)
        return actors

    def on_draw(self):
        arcade.start_render()
        for actor in self._actors:
            actor.on_draw()
        
    def on_key_press(self, key, modifiers):
        for actor in self._actors:
            actor.on_key_press(key)

    def on_key_release(self, key, modifiers):
        for actor in self._actors:
            actor.on_key_release(key)

    def on_update(self, delta_time):
        for actor in self._actors:
            actor.on_update() 
        for handler in self._collision_handlers:
            handler.on_collision()

    def remove_actor(self, actor):
        if actor in self._actors:
            self._actors.remove(actor)

    def setup(self):
        for actor in self._actors:
            actor.setup()
    
    def game_over(self):
        for actor in self._actors:
            actor.change_x = 0
            actor.change_y = 0


class GameFactory:

    def create_mainview(self):
        player = Player()
        alien1 = Alien(150, 500)
        alien2 = Alien(200, 500)
        alien3 = Alien(250, 500)
        alien4 = Alien(300, 500)
        alien5 = Alien(350, 500)
        alien6 = Alien(400, 500)
        alien7 = Alien(450, 500)
        alien8 = Alien(500, 500)
        alien9 = Alien(550, 500)
        alien10 = Alien(600, 500)
        alien11 = Alien(650, 500)
        alien12 = Alien(150, 450)
        alien13 = Alien(200, 450)
        alien14 = Alien(250, 450)
        alien15 = Alien(300, 450)
        alien16 = Alien(350, 450)
        alien17 = Alien(400, 450)
        alien18 = Alien(450, 450)
        alien19 = Alien(500, 450)
        alien20 = Alien(550, 450)
        alien21 = Alien(600, 450)
        alien22 = Alien(650, 450)
        
        alien_list = []
        alien_list.append(alien1)
        alien_list.append(alien2)
        alien_list.append(alien3)
        alien_list.append(alien4)
        alien_list.append(alien5)
        alien_list.append(alien6)
        alien_list.append(alien7)
        alien_list.append(alien8)
        alien_list.append(alien9)
        alien_list.append(alien10)
        alien_list.append(alien11)
        alien_list.append(alien12)
        alien_list.append(alien13)
        alien_list.append(alien14)
        alien_list.append(alien15)
        alien_list.append(alien16)
        alien_list.append(alien17)
        alien_list.append(alien18)
        alien_list.append(alien19)
        alien_list.append(alien20)
        alien_list.append(alien21)
        alien_list.append(alien22)
        
        main_view = GameView()
        main_view.add_actor(player)
        
        for alien in alien_list:
            main_view.add_actor(alien)
        
        
        bullet_alien_collision_handler = BulletAlienCollisionHandler(main_view._actors, alien_list)
        
        main_view.add_handler(bullet_alien_collision_handler)
        return main_view


if __name__ == "__main__":
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    factory = GameFactory()
    main_view = factory.create_mainview()
    main_view.setup()
    window.show_view(main_view)
    arcade.run()
    
