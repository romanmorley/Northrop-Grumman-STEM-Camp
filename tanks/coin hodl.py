import random
import arcade
import os

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):
    """
    This class is the coin on our screen. It is derived from
    the arcade library's "Sprite" class.
    """

    def reset_pos(self):
        # This moves the coin to a random spot above the screen
        self.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 100)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        # move the coin
        self.center_y -= 1

        # check if coin is past the bottom
        if self.top < 0:
            self.reset_pos()


class MyGame(arcade.Window):
    def __init__(self):
        """ initializer """
        # Call parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Coin HODL")
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        self.player_sprite_list = None
        self.coin_sprite_list = None

        self.player_sprite = None
        self.score = 0

        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.CADMIUM_GREEN)

    def setup(self):
        # set up game, set the variables
        self.player_sprite_list = arcade.SpriteList()
        self.coin_sprite_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("sprite.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_sprite_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            coin = Coin("bitcoin.png", SPRITE_SCALING_COIN)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            self.coin_sprite_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.coin_sprite_list.draw()
        self.player_sprite_list.draw()

        output = "Score: " + str(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE_SMOKE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        self.coin_sprite_list.update()
        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_sprite_list)
        for coin in hit_list:
            coin.kill()
            self.score += 1

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
