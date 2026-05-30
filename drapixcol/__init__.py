from PIL import Image
import cv2
import numpy as np



black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 128, 0)
brown = (75, 57, 37)
sky_blue = (0, 191, 255)
light_sky_blue = (135, 206, 250)
violet = (105, 0, 198)
grey = (128, 128, 128)
orange = (255, 102, 0)
pink = (255, 151, 187)
light_green = (159, 236, 83)
dark_red = (196, 30, 58)
null = (0, 0, 0, 0)

forward = "forward"
down = "down"
back = "back"
up = "up"
down_right = "down_right"
up_right = "up_right"
down_left = "down_left"
up_left = "up_left"

translucent = 112
transparent = 0
on80 = 180
on60 = 135
on40 = 90
on20 = 45
opaque = 255

in2times = 200
in5times = 500
in10times = 1000
in50times = 5000
in100times = 10000
in200times = 20000
in500times = 50000
in1000times = 100000



def create_canvas(width, height, color, transparence=255):
    if width > 1920 or height > 1080 or width <= 0 or height <= 0:
        raise ValueError("Allowed dimensions are 1x1 to 1920x1080.")

    if color == null:
        return Image.new("RGBA", (width, height), color)
    
    return Image.new("RGBA", (width, height), (*color, transparence))


def pixel(canvas, x, y, color, transparence=225):
    if 0 <= x < canvas.width and 0 <= y < canvas.height:
        canvas.putpixel((x, y), (*color, transparence))


def save_canvas(canvas, size=100):
    if size > 30000: 
        size = 30000
    elif size <= 0:
        size = 100

    if size == 100:
        canvas.save("result.png")
    else:
        img = cv2.cvtColor(np.array(canvas), cv2.COLOR_RGBA2BGRA)
        width = max(1, int(img.shape[1] * size / 100))
        height = max(1, int(img.shape[0] * size / 100))
        
        img_resized = cv2.resize(img, (width, height), interpolation=cv2.INTER_AREA)
        cv2.imwrite("result.png", img_resized)


def repeat(canvas, time=1, x=0, y=0, where=forward, color=black, transparence=opaque, step=1):
    directions = {
        "forward":    lambda x, y, s: (x + s, y),
        "down":       lambda x, y, s: (x, y + s),
        "up":         lambda x, y, s: (x, y - s),
        "back":       lambda x, y, s: (x - s, y),
        "down_right": lambda x, y, s: (x + s, y + s),
        "up_right":   lambda x, y, s: (x + s, y - s),
        "down_left":  lambda x, y, s: (x - s, y + s),
        "up_left":    lambda x, y, s: (x - s, y - s)
    }
    
    move = directions.get(where, directions["forward"])
    
    for _ in range(time):
        pixel(canvas, x, y, color, transparence)
        x, y = move(x, y, step)
