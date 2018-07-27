import arcade
# Draws a smiley face

# set window dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Open the window, set the title and dimensions.
arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,"smiley face")
arcade.start_render()
class Smiley:
        def draw(self):
        """put smiley drawing here"""
        # Make head of smiley
        x = 300
        y = 300
        radius = 200
        arcade.draw_circle_filled(x,y,radius,arcade.color.BLUE)
        # Make left eye
        x = 225
        y = 350
        radius = 20
        arcade.draw_circle_filled(x,y,radius,arcade.color.RED)
        # Make right eye
        x = 375
        y = 350
        radius = 20
        arcade.draw_circle_filled(x,y,radius,arcade.color.RED)
        # Make left eyebrow
        x = 225
        y = 300
        width = 100
        height = 120
        arcade.draw_arc_outline(x,y,width,height,arcade.color.RED,start_angle=55,end_angle=130,border_width=20)
        # Make right eyebrow
        x = 375
        y = 300
        width = 100
        height = 120
        arcade.draw_arc_outline(x,y,width,height,arcade.color.RED,start_angle=55,end_angle=130,border_width=20)
        # Make smile
        x = 300
        y = 200
        width = 100
        height = -50
        arcade.draw_arc_outline(x,y,width,height,arcade.color.RED,start_angle=0,end_angle=180,border_width=5)
        arcade.finish_render()
class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)
    def setup(self):
        # Set up your game here
        pass
    def on_draw(self):
        arcade.start_render()
    def on_key_press(self, key, modifier):
        if key == arcade.key.UP:
            self.smiley.change_y == 5
    def update(self,delta_time):
        """all the logic to move and game logic goes here"""
        pass
def main():
    game = MyGame(SCREEN_WIDTH,SCREEN_HEIGHT)
    game.setup()
    arcade.run()
if __name__ == "__main__":
    main()








