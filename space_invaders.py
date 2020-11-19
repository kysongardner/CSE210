import arcade
import curses
import sys

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Space Invaders"
OBJECT_SCALE = 1
PLAYER_MOVE_SPEED = 10

class Actor:
    def __init__(self, speed, color, shape_of_actor):
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
    def __init__(self, lives, score):
        lives = 3
        score = 0
        
    
    def show_battleship_sprite(self):
        player = arcade.SpriteList()
        image = "battleship.png"
        battleship_sprite = arcade.Sprite(image, OBJECT_SCALE)
        battleship_sprite.sprite_center_x = 20
        battleship_sprite.sprite_center_y = 0
        player.append(battleship_sprite)
        player.draw()
        
        

    def movement(self, key, modifiers):
        if key == arcade.key.LEFT:
            battleship_sprite.change_x = -PLAYER_MOVE_SPEED
        elif key == arcade.key.RIGHT:
            battlship_sprite.change_x = PLAYER_MOVE_SPEED
    
    def update_score(self, actor_hit):
        if actor_hit == 'alien':
            score += 10
        elif actor_hit == 'battleship':
            score -= 10
        return score


# Main game window that will have canvas on it and will have all the objects on it. Ship, aliens, barriers, bullets
class Game_Window(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.player = None
        self.batttleship_sprite = None

    def load_game(self):
        arcade.set_background_color(arcade.color.BLACK)
        battleship = Battleship(3, 0)
        battleship.show_battleship_sprite()
        arcade.start_render()

        
        # aliens = Alien()
        # barriers = Barrier()

# This will be the main game logic and game loop. Put all the methods of each objects in here in logical order.
class Gameplay:
    def game_loop(self):
        pass


class Game_Play_Info:
    def __init__(self, score, lives):
        self.score = 0
        self.lives = 3


class alien:
    def move_side_to_side(self):
        # loop that moves left and then right until end of game
        # touch wall a bounce back
        alien_place_x += alien_place_x_speed
        for alien in aliens:
            alien.move(alien_place_x_speed, 0)
        if alien_place_x >= 200 or alien_place_x <= 0:
            alien_place_x_speed = -1 * alien_place_x_speed
            for alien in aliens:
                alien.move(0,5)

    def hit(self):
        # alien disappers once hit 

    def get_pictures(self):
        # get both pictures for up alien and down alien
        picture = pygame.image.load(yellowsquare.piskel)
        for alien in aliens:
        alien.draw()
        #hek=llo

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
    game = Game_Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.load_game()
    arcade.run()

if __name__ == "__main__":
    main()
