import arcade
import curses
import sys
import os
import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Space Invaders"
CHARACTER_SCALING = 1
PLAYER_MOVE_SPEED = 10


class Actor:
    def __init__(self, color, shape_of_actor):
        self.speed = 0
        self.color = None
        self.shape_of_actor = None

    def get_position(self):
        pass

    def set_position(self):
        pass

    def is_hit_by_bullet(self):
        # Object hit by bullet if bullet and object occupy the same space
        pass

    def remove_items_from_screen(self):
        # After an item has been hit we need to remove it from the screen
        pass

    def move_bullet(self):
        # move bullet either up or down depending on who shoots it.
        pass

    def fire_bullet(self):
        # fire bullet from either the alien or spaceship
        pass


class Battleship(Actor):
    def __init__(self):
        self.shape_of_actor = "battleship.png"
        self.lives = 3
        self.score = 0

    def update_score(self, actor_hit):
        if actor_hit == 'alien':
            self.score += 10
        elif actor_hit == 'battleship':
            self.score -= 10
        return self.score


class Player(arcade.Sprite):
    def __init__(self):
        directory = os.path.dirname(__file__)
        filename = os.path.join(directory, "battleship.png")
        super().__init__(filename, CHARACTER_SCALING)

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.left < 0:
            self.left = 0
        elif self.right > SCREEN_WIDTH - 1:
            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > SCREEN_HEIGHT - 1:
            self.top = SCREEN_HEIGHT - 1


# Main game window that will have canvas on it and will have all the objects on it. Ship, aliens, barriers, bullets
class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player_list = None
        self.player_sprite = None
        self.alien_list = None

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.alien_list = arcade.SpriteList()

        self.player_sprite = Player()
        self.player_sprite.center_x = 250
        self.player_sprite.center_y = 1
        self.player_list.append(self.player_sprite)

        # for i in range(1, 50):
        alien = Alien()
        alien.center_x = random.randint(1, SCREEN_WIDTH)
        alien.center_y = random.randint(1, SCREEN_HEIGHT)
        self.alien_list.append(alien)

        # battleship = Battleship()
        # aliens = Alien()
        # barriers = Barrier()

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.alien_list.draw()

    def on_update(self, delta_time):
        self.player_list.update()
        self.alien_list.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVE_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVE_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_y = 0


class Alien(arcade.Sprite):
    def __init__(self):
        directory = os.path.dirname(__file__)
        filename = os.path.join(directory, "alien.png")
        super().__init__(filename, CHARACTER_SCALING)
        self.change_x = 5

    def update(self):
        if self.center_x >= SCREEN_WIDTH:
            self.center_y = self.center_y - 5
            self.change_x = -5
        elif self.center_x <= 0:
            self.center_y = self.center_y - 5
            self.change_x = 5
        self.center_x += self.change_x
        self.center_y += self.change_y
        # if self.left < 0:
        #     self.left = 0
        # elif self.right > SCREEN_WIDTH - 1:
        #     self.right = SCREEN_WIDTH - 1

        # if self.bottom < 0:
        #     self.bottom = 0
        # elif self.top > SCREEN_HEIGHT - 1:
        #     self.top = SCREEN_HEIGHT - 1

    def move_side_to_side(self):
        # loop that moves left and then right until end of game
        # touch wall a bounce back
        alien_place_x += alien_place_x_speed
        for alien in aliens:
            alien.move(alien_place_x_speed, 0)
        if alien_place_x >= 200 or alien_place_x <= 0:
            alien_place_x_speed = -1 * alien_place_x_speed
            for alien in aliens:
                alien.move(0, 5)

    def hit(self):
        # alien disappers once hit
        pass

    def get_pictures(self):
        # get both pictures for up alien and down alien
        picture = pygame.image.load(yellowsquare.piskel)
        for alien in aliens:
            alien.draw()
            # hek=llo

# Get input from the user move left, move right, when bullet is fired


class Input_Service:
    def __init__(self, window):
        self.window = arcade.open_window(500, 500)
        self.directions = {}
        self.directions[curses.KEY_LEFT] = (-1, 0)
        self.directions[curses.KEY_RIGHT] = (1, 0)
        self.current = (250, 0)

    def get_direction(self):
        key = self.window.getch()
        if key == curses.ascii.ESC:
            sys.exit()
        self.current = self.directions.get(key, self.current)
        return self.current


# Produce output and update the screen
class Output_Service:
    def __init__(self):
        pass


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
