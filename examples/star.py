from drapixcolor import *


# Create a canvas size 5x5, background color - white, transparent
width, height = 5, 5
canvas = create_canvas(width, height, white, transparent)

# Draw a star
pixel(canvas, 2, 0, yellow)
pixel(canvas, 1, 1, yellow)
pixel(canvas, 3, 1, yellow)
pixel(canvas, 0, 2, yellow)
pixel(canvas, 4, 2, yellow)
pixel(canvas, 1, 3, yellow)
pixel(canvas, 3, 3, yellow)
pixel(canvas, 2, 4, yellow)

# Save the image, enlarging it 100 times
save_canvas(canvas, in100times)
