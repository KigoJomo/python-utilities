from PIL import Image
import os

def convert_images_to_webp(directory):
    # Make sure the directory exists
    if not os.path.isdir(directory):
        print(f"The directory {directory} does not exist.")
        return
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check for PNG or JPG files
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            # Construct full file path
            file_path = os.path.join(directory, filename)
            # Open the image file
            with Image.open(file_path) as img:
                # Define the new filename with .webp extension
                new_filename = os.path.splitext(filename)[0] + '.webp'
                new_file_path = os.path.join(directory, new_filename)
                # Convert and save as WebP
                img.save(new_file_path, 'webp')
                print(f"Converted {filename} to {new_filename}")

# Specify the directory containing your images
directory = '/home/nova/Downloads/cace assets'

convert_images_to_webp(directory)
