from drapixcol import *


# Create a canvas size 17x24, background color - sky_blue
width, height = 17, 24
canvas = create_canvas(width, height, sky_blue)

# Draws a tree trunk
repeat(canvas, 3, 7, 20, down, brown)
repeat(canvas, 3, 8, 20, down, brown)
repeat(canvas, 3, 9, 20, down, brown)

# Draws the first tier of the Christmas tree
repeat(canvas, 17, 0, 19, forward, green)
repeat(canvas, 17, 0, 18, forward, green) 

# Draws the second tier of the Christmas tree
repeat(canvas, 15, 1, 17, forward, green)
repeat(canvas, 15, 1, 16, forward, green)

# Draws the third tier of the Christmas tree
repeat(canvas, 13, 2, 15, forward, green)
repeat(canvas, 13, 2, 14, forward, green)

# Draws the fourth tier of the Christmas tree
repeat(canvas, 11, 3, 13, forward, green)
repeat(canvas, 11, 3, 12, forward, green) 

# Draws the fifth tier of the Christmas tree
repeat(canvas, 9, 4, 11, forward, green)
repeat(canvas, 9, 4, 10, forward, green)

# Draws the sixth tier of the Christmas tree
repeat(canvas, 7, 5, 9, forward, green)
repeat(canvas, 7, 5, 8, forward, green)

# Draws the seventh tier of the Christmas tree
repeat(canvas, 5, 6, 7, forward, green)
repeat(canvas, 5, 6, 6, forward, green)

# Draws the eighth tier of the Christmas tree
repeat(canvas, 3, 7, 5, forward, green)
repeat(canvas, 3, 7, 4, forward, green)
pixel(canvas, 8, 3, green)

# Draws a star
pixel(canvas, 8, 2, yellow)
repeat(canvas, 3, 7, 1, forward, yellow)
pixel(canvas, 8, 0 , yellow)

# Draws red ribbons on the Christmas tree
repeat(canvas, 5, 7, 4, down_right, red)
repeat(canvas, 10, 6, 7, down_right, red)
repeat(canvas, 10, 5, 10, down_right, red)
repeat(canvas, 8, 3, 12, down_right, red)
repeat(canvas, 5, 2, 15, down_right, red)
repeat(canvas, 2, 1, 18, down_right, red)

# Draws yellow ribbons
repeat(canvas, 5, 3, 18, up_right, yellow, step=2)
repeat(canvas, 2, 11, 18, up_right, yellow, step=2)
pixel(canvas, 7, 6, yellow)

# Draws blue ribbons
repeat(canvas, 3, 5, 12, up_right, blue, step=2)
repeat(canvas, 3, 7, 18, up_right, blue, step=2)
pixel(canvas, 15, 18, blue)

# Draws snow under the tree
repeat(canvas, 17, 0, 23, forward, white)
repeat(canvas, 7, 0, 22, forward, white)
repeat(canvas, 7, 10, 22, forward, white)

# Saves the canvas enlarged 100 times
save_canvas(canvas, in100times)
