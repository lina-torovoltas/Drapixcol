# Drapixcol
Python library for drawing with pixels<br />

The `create_canvas` function creates a canvas with a given width and color, example:<br />
```python
width, height = 10, 20
canvas = create_canvas(width, height, white)
```  
This code created an opaque canvas with a width of 10, a height of 20, and a white color,  
Also, this function can be passed transparency as the fourth argument.  

The `pixel` function paints a specific pixel a color, example:  
```python
pixel(canvas, 5, 0 , black)
```  
This code paints a pixel on the canvas "canvas" at coordinates x=5 y=0 black,  
You can also pass transparency to this function as the fifth argument.  

The `repeat` function draws a sequence of pixels in any direction and with any space between pixels, example:
```python
repeat(canvas, 10, 5, 10, forward, black)
```
