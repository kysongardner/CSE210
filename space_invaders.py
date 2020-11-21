import arcade
import curses
import sys

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
        
    def movement(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.shape_of_actor.change_x = -PLAYER_MOVE_SPEED
        elif key == arcade.key.RIGHT:
            self.shape_of_actor.change_x = PLAYER_MOVE_SPEED
    
    def update_score(self, actor_hit):
        if actor_hit == 'alien':
            self.score += 10
        elif actor_hit == 'battleship':
            self.score -= 10
        return self.score


# Main game window that will have canvas on it and will have all the objects on it. Ship, aliens, barriers, bullets
class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.player_list = None
        self.player_sprite = None

        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):

        self.player_list = arcade.SpriteList()
        image_source = ":resources:CSE210/battleship.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = 250
        self.player_sprite.center_y = 250
        self.player_list.append(self.player_sprite)
        battleship = Battleship()
        # aliens = Alien()
        # barriers = Barrier()
    
    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()

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
        pass

    def get_pictures(self):
        # get both pictures for up alien and down alien
        picture = pygame.image.load(yellowsquare.piskel)
        for alien in aliens:
            alien.draw()
            #hek=llo

Class Blocks:
    def make_barrier(self):
    	"""
	Making a 2D block grid of solid color sprites close together without margin
	"""
	barrier_width = 5
	barrier_height = 10
	barrier_width_count = 20
	barrier_height_count = 5
	x_start = 380
	y_start = 150
	for x in range(x_start, x_start + barrier_width_count * barrier_width, barrier_width):
	    for y in range(y_start, y_start + barrier_height_count * barrier_height, barrier_height):
		barrier_sprite = arcade.SpriteSolidColor(barrier_width, barrier_height. Arcade.color.GREEN)
		barrier_sprite.center_x = x
		barrier_sprite.center_y = y
		self.barrier_list.append(barrier_sprite)

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
