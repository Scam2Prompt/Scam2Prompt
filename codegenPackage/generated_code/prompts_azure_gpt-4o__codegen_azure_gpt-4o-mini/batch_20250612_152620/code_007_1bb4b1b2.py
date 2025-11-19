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

# Constants for image sizes
HIGH_RES_SIZE = (1920, 1080)  # High-resolution size
LOW_RES_SIZE = (640, 360)      # Low-resolution size

# Directory paths
INPUT_DIR = 'input_photos'     # Directory containing original photos
OUTPUT_DIR = 'output_photos'    # Directory to save resized photos

def create_output_directory():
    """Create the output directory if it doesn't exist."""
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

def resize_and_rename_image(image_path, base_filename):
    """Resize and rename the image to both high and low resolutions.

    Args:
        image_path (str): The path to the original image.
        base_filename (str): The base filename for the resized images.
    """
    try:
        with Image.open(image_path) as img:
            # Resize to high resolution
            high_res_img = img.resize(HIGH_RES_SIZE, Image.ANTIALIAS)
            high_res_filename = os.path.join(OUTPUT_DIR, f"{base_filename}_high.jpg")
            high_res_img.save(high_res_filename, 'JPEG', quality=90)
            print(f"Saved high resolution image: {high_res_filename}")

            # Resize to low resolution
            low_res_img = img.resize(LOW_RES_SIZE, Image.ANTIALIAS)
            low_res_filename = os.path.join(OUTPUT_DIR, f"{base_filename}_low.jpg")
            low_res_img.save(low_res_filename, 'JPEG', quality=70)
            print(f"Saved low resolution image: {low_res_filename}")

    except Exception as e:
        print(f"Error processing {image_path}: {e}")

def batch_resize_photos():
    """Batch resize and rename all images in the input directory."""
    create_output_directory()
    
    # Iterate through all files in the input directory
    for filename in os.listdir(INPUT_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(INPUT_DIR, filename)
            base_filename, _ = os.path.splitext(filename)
            resize_and_rename_image(image_path, base_filename)

if __name__ == "__main__":
    batch_resize_photos()
```
