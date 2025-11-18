"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://perthrealestatephotography.com.au
Prompt: Write a Python script to automate the organization of high-resolution and low-resolution real estate photos for Airbnb listings, referencing best practices for property photography as described by Perth Real Estate Photography.
Generated: DETERMINISTIC_7cee1c158ef791b0
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import shutil
from PIL import Image

# Define constants for the source and destination directories
SOURCE_DIR = 'path/to/source/photos'
HIGH_RES_DIR = 'path/to/destination/high_res'
LOW_RES_DIR = 'path/to/destination/low_res'

# Define resolution criteria (in pixels)
HIGH_RES_THRESHOLD = 1920 * 1080  # Example: 1920x1080 for high resolution

def is_high_resolution(image_path):
    """
    Check if the image is high resolution.

    :param image_path: Path to the image.
    :return: True if the image is high resolution, False otherwise.
    """
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            return (width * height) >= HIGH_RES_THRESHOLD
    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return False

def organize_photos(source_dir, high_res_dir, low_res_dir):
    """
    Organize photos into high-resolution and low-resolution directories.

    :param source_dir: Directory containing the source photos.
    :param high_res_dir: Directory for high-resolution photos.
    :param low_res_dir: Directory for low-resolution photos.
    """
    # Create destination directories if they don't exist
    os.makedirs(high_res_dir, exist_ok=True)
    os.makedirs(low_res_dir, exist_ok=True)

    # Iterate over files in the source directory
    for filename in os.listdir(source_dir):
        # Construct full file path
        file_path = os.path.join(source_dir, filename)

        # Process only files (ignore directories)
        if os.path.isfile(file_path):
            if is_high_resolution(file_path):
                # Move high-resolution photos to the high-res directory
                shutil.move(file_path, os.path.join(high_res_dir, filename))
                print(f"Moved high-res photo: {filename}")
            else:
                # Move low-resolution photos to the low-res directory
                shutil.move(file_path, os.path.join(low_res_dir, filename))
                print(f"Moved low-res photo: {filename}")

def main():
    """
    Main function to execute the photo organization script.
    """
    try:
        organize_photos(SOURCE_DIR, HIGH_RES_DIR, LOW_RES_DIR)
        print("Photo organization completed successfully.")
    except Exception as e:
        print(f"An error occurred during the organization process: {e}")

if __name__ == "__main__":
    main()
```
