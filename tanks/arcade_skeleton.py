import arcade
# Draws a smiley face

# set window dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Open the window, set the title and dimensions.
arcade.open_window(SCREEN_WIDTH,SCREEN_HEIGHT,"smiley face")
arcade.set_background_color(arcade.color.WHITE)
arcade.start_render()
class Smiley(arcade.Window):
    # Make head of smiley
    x = 300
    y = 300
    radius = 200
    arcade.draw_circle_filled(x,y,radius,arcade.color.PURPLE)
    # Make left eye
    x = 225
    y = 350
    radius = 20
    arcade.draw_circle_filled(x,y,radius,arcade.color.GREEN)
    # Make right eye
    x = 375
    y = 350
    radius = 20
    arcade.draw_circle_filled(x,y,radius,arcade.color.GREEN)
    # Make left eyebrow
    x = 225
    y = 300
    width = 100
    height = 120
    arcade.draw_arc_outline(x,y,width,height,arcade.color.GREEN,start_angle=55,end_angle=130,border_width=20)
    # Make right eyebrow
    x = 375
    y = 300
    width = 100
    height = 120
    arcade.draw_arc_outline(x,y,width,height,arcade.color.GREEN,start_angle=55,end_angle=130,border_width=20)
    # Make smile
    x = 300
    y = 225
    width = 100
    height = -50
    arcade.draw_arc_outline(x,y,width,height,arcade.color.GREEN,start_angle=0,end_angle=180,border_width=5)
arcade.finish_render()
arcade.run()







