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

# Create a new image in 'RGB' mode
img = Image.new('RGB', (width, height))

# Put the pixel data into the image
img.putdata(pixel_data)

# Save the image as a PNG file
img.save('output.png')