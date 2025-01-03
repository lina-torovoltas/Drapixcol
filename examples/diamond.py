from drapixcol import *


# Create a canvas size 17x14, background color - null
width, height = 17, 14
canvas = create_canvas(width, height, null)

# This code draws the structure of a diamond
repeat(canvas, 11, 3, 1, forward)
repeat(canvas, 17, 0, 5, forward)
repeat(canvas, 8, 1, 6, down_right)
repeat(canvas, 8, 8, 13, up_right)
repeat(canvas, 3, 0, 4, up_right)
repeat(canvas, 3, 0, 4, up_right)
repeat(canvas, 3, 14, 2, down_right)
repeat(canvas, 3, 4, 4, up_right)
repeat(canvas, 3, 10, 2, down_right)
repeat(canvas, 5, 4, 6, down_right)
repeat(canvas, 5, 8, 10, up_right)

# This code draws the diamond fill
repeat(canvas, 7, 2, 6, down_right, sky_blue)
repeat(canvas, 6, 3, 6, down_right, sky_blue)
repeat(canvas, 7, 8, 12, up_right, sky_blue)
repeat(canvas, 6, 8, 11, up_right, sky_blue)
pixel(canvas, 8, 9, sky_blue)
repeat(canvas, 3, 7, 8, forward, sky_blue)
repeat(canvas, 5, 6, 7, forward, sky_blue)
repeat(canvas, 7, 5, 6, forward, sky_blue)
repeat(canvas, 7, 5, 4, forward, sky_blue)
repeat(canvas, 5, 6, 3, forward, sky_blue)
repeat(canvas, 3, 7, 2, forward, sky_blue)
repeat(canvas, 3, 2, 4, up_right, sky_blue)
repeat(canvas, 3, 1, 4, up_right, sky_blue)
repeat(canvas, 3, 3, 4, up_right, sky_blue)
repeat(canvas, 3, 11, 2, down_right, sky_blue)
repeat(canvas, 3, 12, 2, down_right, sky_blue)
repeat(canvas, 3, 13, 2, down_right, sky_blue)

# Saves the canvas by enlarging it 100 times
save_canvas(canvas, in100times)
