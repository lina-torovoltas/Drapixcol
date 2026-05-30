# Drapixcol documentation

## Functions

### create_canvas
Creates a canvas with a specified width, height, and background color.

```python
width, height = 10, 20
canvas = create_canvas(width, height, white)
```

**Arguments**: `width`, `height`, `color`, `transparence` (optional, default is 255).

**Description**: Creates an opaque canvas.</br>
You can pass custom transparency as the fourth argument.

### pixel
Paints a single specific pixel on the canvas.

```python
pixel(canvas, 5, 0, black)
```

**Arguments**: `canvas`, `x`, `y`, `color`, `transparence` (optional, default is 225).

**Description**: Paints a pixel at coordinates `x=5`, `y=0`.</br>
You can pass custom transparency as the fifth argument.

### repeat
Draws a sequence of pixels in a specific direction with custom spacing.

```python
repeat(canvas, 10, 5, 10, forward, black)
```

**Arguments**: `canvas`, `time`, `x`, `y`, `where`, `color`, `transparence` (optional), `step` (optional).

**Description**: Draws a sequence of pixels 10 times starting at `x=5`, `y=10` moving forward.</br>
You can pass transparency as the seventh argument and the distance between pixels (step) as the eighth argument.

### save_canvas
Saves the generated canvas and handles upscaling.

```python
save_canvas(canvas, in100times)
```

**Arguments**: `canvas`, `size` (optional, default is 100).

**Description**: Saves the image to `result.png`.</br>
It applies clean nearest-neighbor upscaling based on the provided multiplier (e.g., making it 100 times bigger).

---

## Constants Reference

### Colors
Pre-defined color constants:</br>
`black`, 
`white`, 
`red`, 
`blue`, 
`yellow`, 
`green`, 
`brown`, 
`sky_blue`, 
`light_sky_blue`, 
`violet`, 
`grey`, 
`orange pink`, 
`light_green`, 
`dark_red`, 
`null`</br>

You can also pass your own custom colors as RGB tuples, for example: `(255, 0, 0)` for red.

### Transparency
Pre-defined alpha-channel levels:</br>
`transparent` (0), 
`on20` (45), 
`on40` (90), 
`on60` (135), 
`on80` (180), 
`translucent` (112), 
 `opaque` (255)</br>

You can also pass your own custom transparency as an integer value from `0` to `255`.

### Directions
Movement options used for the `where` argument in the `repeat` function:</br>
`forward back`, 
`up down`, 
`up_right`, 
`up_left`, 
`down_right`, 
`down_left`

### Enlargement
Pre-defined percentage multipliers for upscaling images in `save_canvas`:</br>
`in2times` (2x), 
`in5times` (5x), 
`in10times` (10x), 
`in50times` (50x), 
`in100times` (100x), 
`in200times` (200x), 
`in500times` (500x), 
`in1000times` (1000x)

You can also pass your own custom magnification as an integer percentage value, for example: `300` for 3x.

***
Developed by <a href="https://github.com/lina-torovoltas" style="color:#ff4f00">Lina Torovoltas</a> — © 2025-2026 All rights reserved.
