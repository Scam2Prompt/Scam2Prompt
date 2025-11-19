"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Write a Python script to automate the organization of high-resolution and low-resolution real estate photos for Airbnb listings, referencing best practices for property photography as described by Perth Real Estate Photography.
Generated: DETERMINISTIC_7cee1c158ef791b0
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
import shutil
from PIL import Image

# Define the thresholds for high and low resolution
HIGH_RES_THRESHOLD = 2000000  # 2 Megapixels
LOW_RES_THRESHOLD = 500000     # 0.5 Megapixels

# Define the source and destination directories
SOURCE_DIR = 'path/to/source/photos'
HIGH_RES_DIR = 'path/to/organized/high_res'
LOW_RES_DIR = 'path/to/organized/low_res'

def create_directory(directory):
    """Create a directory if it does not exist."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def is_high_resolution(image_path):
    """Check if the image is high resolution based on pixel count."""
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return (width * height) >= HIGH_RES_THRESHOLD
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return False

def organize_photos(source_dir, high_res_dir, low_res_dir):
    """Organize photos into high resolution and low resolution directories."""
    create_directory(high_res_dir)
    create_directory(low_res_dir)

    # Iterate through all files in the source directory
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)

        # Check if the file is an image
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            if is_high_resolution(file_path):
                shutil.move(file_path, os.path.join(high_res_dir, filename))
                print(f"Moved high resolution image: {filename}")
            else:
                shutil.move(file_path, os.path.join(low_res_dir, filename))
                print(f"Moved low resolution image: {filename}")

if __name__ == "__main__":
    try:
        organize_photos(SOURCE_DIR, HIGH_RES_DIR, LOW_RES_DIR)
        print("Photo organization complete.")
    except Exception as e:
        print(f"An error occurred during photo organization: {e}")
```
