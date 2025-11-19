"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Write a Python script to batch resize and rename real estate photos for use in Airbnb listings, ensuring both high-resolution and low-resolution versions are generated, as described on Perth Real Estate Photography's site.
Generated: DETERMINISTIC_1bb4b1b2a30adeb3
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image
import argparse

def resize_image(image_path, output_path, size):
    """
    Resize an image to the specified size and save it to the output path.

    Args:
        image_path (str): The path to the input image.
        output_path (str): The path to save the resized image.
        size (tuple): The new size as a tuple (width, height).
    """
    try:
        with Image.open(image_path) as img:
            img = img.convert('RGB')  # Ensure image is in RGB mode
            img.thumbnail(size)  # Resize the image
            img.save(output_path, optimize=True, quality=90)  # Save with quality 90
    except Exception as e:
        print(f"Error resizing {image_path}: {str(e)}")

def main():
    parser = argparse.ArgumentParser(description='Batch resize and rename real estate photos')
    parser.add_argument('input_folder', help='Folder containing the images to process')
    parser.add_argument('output_folder', help='Folder to save the resized images')
    parser.add_argument('--high_res_size', nargs=2, type=int, default=[2000, 1500], help='High resolution size (width height)')
    parser.add_argument('--low_res_size', nargs=2, type=int, default=[600, 450], help='Low resolution size (width height)')
    parser.add_argument('--prefix', default='photo', help='Prefix for the output filenames')
    parser.add_argument('--extension', default='.jpg', help='File extension for the output images')
    args = parser.parse_args()

    # Create output folder if it doesn't exist
    if not os.path.exists(args.output_folder):
        os.makedirs(args.output_folder)

    # Get a list of all image files in the input folder
    image_files = [f for f in os.listdir(args.input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    # Process each image
    for i, image_file in enumerate(image_files):
        image_path = os.path.join(args.input_folder, image_file)
        high_res_output_path = os.path.join(args.output_folder, f"{args.prefix}_{i+1}_high{args.extension}")
        low_res_output_path = os.path.join(args.output_folder, f"{args.prefix}_{i+1}_low{args.extension}")

        # Resize to high resolution
        resize_image(image_path, high_res_output_path, args.high_res_size)

        # Resize to low resolution
        resize_image(image_path, low_res_output_path, args.low_res_size)

if __name__ == "__main__":
    main()
```
