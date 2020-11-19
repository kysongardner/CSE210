import arcade
import curses
import sys


class Actor:
    def __init__(self, speed, color, shape_of_actor):
        self.speed = 0
        self.color = arcade.color.GREEN
        self.color = arcade.sprite.BLACK
        self.shape_of_actor = None

    def get_position(self):
        pass

    def set_position(self):
        pass

    def been_hit_by_bullet(self):
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
    def __init__(self, start_position, lives):
        # 50 on the x axis will be the center of the map... The Y will always be 0.
        self.start_position = 50, 0
        self.lives = 3
        self.shape_of_actor = None

    def move_left(self):
        pass

    def move_right(self):
        pass


class Game_Window:
    # We need to draw the window and set dimensions etc.
    def load_game(self):
        arcade.open_window(500, 500, "Space Invaders")
        arcade.set_background_color(arcade.color.BLACK)
        arcade.start_render()
        battleship = arcade.sprite('battleship.piskel')


class Gameplay:
    def game_loop(self):
        # Draw Canvas
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

