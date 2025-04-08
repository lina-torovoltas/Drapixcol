from PIL import Image
import cv2



black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 0, 255
yellow = 255, 255, 0
green = 0, 128, 0
brown = 75, 57, 37
sky_blue = 0, 191, 255
light_sky_blue = 135, 206, 250
violet = 105, 0, 198
grey = 128, 128, 128
orange = 255, 102, 0
pink = 255,151,187
light_green = 159, 236, 83
dark_red = 196, 30, 58
null = 0, 0, 0, 0

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

in2times= 200
in5times = 500
in10times = 1000
in50times = 5000
in100times = 10000
in200times = 20000
in500times = 50000
in1000times = 100000



def create_canvas(width, height, color, transparence=255):
    if width > 1920 or height > 1080:
        raise Exception("You have exceeded the allowed width (1920) or height (1080).")

    if color == null:
        return Image.new("RGBA", (width, height), color)
    
    return Image.new("RGBA", (width, height), (*color, transparence))

    

def pixel(canvas, x, y, color, transparence=225):
  canvas.putpixel((x, y), (*color, transparence))



def forward(x, y, step=1):
  return x + step, y

def down(x, y, step=1):
  return x, y + step

def up(x, y, step=1):
  return x, y - step

def back(x, y, step=1):
  return x - step, y



def down_right(x, y, step=1):
  return x + step, y + step

def up_right(x, y, step=1):
  return x + step, y - step

def down_left(x, y, step=1):
  return x - step, y + step

def up_left(x, y, step=1):
  return x - step, y - step
    


def save_canvas(canvas, size=100):
    canvas.save("result.png")

    img = cv2.imread("result.png", cv2.IMREAD_UNCHANGED)
    if img is None:
        print("Unable to load image from 'result.png'")
        return None

    if size != 100:
        width = int(img.shape[1] * size / 100)
        height = int(img.shape[0] * size / 100)
        dim = (width, height)
        
        img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
        
        cv2.imwrite("result.png", img)



def repeat(canvas, time=1, x=0, y=0, where=forward, color=black, transparence=opaque, step=1):
    directions = {
        forward: forward,
        down: down,
        up: up,
        back: back,
        down_right: down_right,
        up_right: up_right,
        down_left: down_left,
        up_left: up_left
    }
    
    move = directions.get(where, forward)
    
    for _ in range(time):
        pixel(canvas, x, y, color, transparence)
        x, y = move(x, y, step)
