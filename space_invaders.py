import arcade


class Actor:
    def __init__(self, speed, color, shape_of_actor):
        self.speed = 0
        self.color = arcade.color.GREEN
        self.color = arcade.sprite.BLACK

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


class Battleship(Actor):
    def __init__(self, start_position, lives):
        # 50 on the x axis will be the center of the map... The Y will always be 0.
        self.start_position = 50, 0
        self.lives = 3

    def move_left(self):
        pass

    def move_right(self):
        pass

    def fire_bullet(self):
        pass


class Game_Window:
    # We need to draw the window and set dimensions etc.
    pass


class Gameplay:
    def game_loop(self):
        # Draw Canvas
        pass


class Game_Play_Info:
    def __init__(self, score, lives):
        self.score = 0
        self.lives = 3
