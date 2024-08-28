from PIL import Image, ImageDraw
import random

# Image dimensions
width, height = 800, 600

# Background color
background_color = (29, 29, 29)  # Dark blue

# Create a new image with the specified background color
image = Image.new("RGB", (width, height), background_color)
draw = ImageDraw.Draw(image)

# Number of dots
num_dots = 1000000

# Draw random dots
for _ in range(num_dots):
    # Random position
    x = random.randint(0, width - 1)
    y = random.randint(0, height - 1)
    # Dot color
    color = (255, 255, 255)  # White dot
    # Draw a tiny dot
    draw.point((x, y), fill=color)

# Save the image
image.save("random_dots.png")

# Optionally show the image
image.show()
