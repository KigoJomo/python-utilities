from PIL import Image, ImageDraw
import random

# Scaling factor
scale = 10

height = 2400
width = 3200

# High-resolution image dimensions
high_res_width, high_res_height = width * scale, height * scale

# Background color
background_color = (0, 0, 0)  # Dark gray
dot_color = (255, 255, 255)  # Dark gray

# Create a high-resolution image with the specified background color
image = Image.new("RGB", (high_res_width, high_res_height), background_color)
draw = ImageDraw.Draw(image)

# Number of dots
num_dots = 1000000

# Dot size (scaled up)
dot_size = 1 * scale

# Draw random dots
for _ in range(num_dots):
    # Random position
    x = random.randint(0, high_res_width - dot_size)
    y = random.randint(0, high_res_height - dot_size)
    # Dot color
    color = dot_color  # White dot
    # Draw a tiny dot
    draw.ellipse([x, y, x + dot_size, y + dot_size], fill=color)

# Scale down the image
image = image.resize((width, height), Image.LANCZOS)

# Save the image
image.save("high-res-image-2.png")

# Optionally show the image
image.show()
