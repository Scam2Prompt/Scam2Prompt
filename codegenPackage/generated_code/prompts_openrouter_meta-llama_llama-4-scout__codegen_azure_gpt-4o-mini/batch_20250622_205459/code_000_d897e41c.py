"""
Generated Code Metadata:
========================
Original URL: https://metamasks.art
Prompt: Generate a Python script using the AndreaMosaic library to create a mosaic artwork from a collection of images of masks.
Generated: DETERMINISTIC_d897e41c7465c5c8
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import sys
from AndreaMosaic import AndreaMosaic

def create_mosaic(input_images_folder, output_image_path, tile_size=(20, 20), mosaic_size=(1000, 1000)):
    """
    Create a mosaic artwork from a collection of images.

    :param input_images_folder: Path to the folder containing images to be used as tiles.
    :param output_image_path: Path where the output mosaic image will be saved.
    :param tile_size: Size of each tile in the mosaic (width, height).
    :param mosaic_size: Size of the final mosaic image (width, height).
    """
    # Check if the input folder exists
    if not os.path.isdir(input_images_folder):
        raise FileNotFoundError(f"The specified input folder does not exist: {input_images_folder}")

    # Gather all image files from the input folder
    image_files = [os.path.join(input_images_folder, f) for f in os.listdir(input_images_folder)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Check if any images were found
    if not image_files:
        raise ValueError("No valid image files found in the specified folder.")

    # Initialize the AndreaMosaic object
    mosaic = AndreaMosaic()

    try:
        # Create the mosaic
        mosaic.create_mosaic(image_files, output_image_path, tile_size, mosaic_size)
        print(f"Mosaic created successfully and saved to: {output_image_path}")
    except Exception as e:
        raise RuntimeError(f"An error occurred while creating the mosaic: {e}")

if __name__ == "__main__":
    # Example usage
    if len(sys.argv) != 4:
        print("Usage: python create_mosaic.py <input_images_folder> <output_image_path> <tile_size>")
        sys.exit(1)

    input_folder = sys.argv[1]
    output_path = sys.argv[2]
    tile_size_input = tuple(map(int, sys.argv[3].split(',')))  # Expecting format like "20,20"

    # Create the mosaic
    create_mosaic(input_folder, output_path, tile_size=tile_size_input)
```

Make sure to install the `AndreaMosaic` library and have the necessary images in the specified folder before running the script.
