# python3 -m pip install Pillow

from PIL import Image

width = 10
height = 10

pixel_data = []
for y in range(height):
    for x in range(width):
        if (x + y) % 2 == 0:
            pixel_data.append((255, 255, 255))  # White
        else:
            pixel_data.append((0, 0, 0))        # Black

img = Image.new('RGB', (width, height))
img.putdata(pixel_data)
img.save('output.png')