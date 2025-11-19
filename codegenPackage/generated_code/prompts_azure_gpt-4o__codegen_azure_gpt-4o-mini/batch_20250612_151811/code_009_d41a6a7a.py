"""
Generated Code Metadata:
========================
Original URL: https://metamasks.art
Prompt: Write a Python script to simulate the creation of mosaics using random mask images, mimicking the artistic approach of metaMasks.
Generated: DETERMINISTIC_d41a6a7a8dd3c71b
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import random
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def create_mosaic(base_image_path, mask_images_dir, output_image_path, mosaic_size=(10, 10)):
    """
    Create a mosaic image by applying random mask images to a base image.

    Parameters:
    - base_image_path (str): Path to the base image.
    - mask_images_dir (str): Directory containing mask images.
    - output_image_path (str): Path to save the output mosaic image.
    - mosaic_size (tuple): Size of the mosaic grid (rows, columns).
    """
    try:
        # Load the base image
        base_image = Image.open(base_image_path).convert("RGBA")
        base_width, base_height = base_image.size

        # Load mask images
        mask_images = load_mask_images(mask_images_dir)

        # Calculate the size of each tile in the mosaic
        tile_width = base_width // mosaic_size[1]
        tile_height = base_height // mosaic_size[0]

        # Create a new image for the mosaic
        mosaic_image = Image.new("RGBA", base_image.size)

        # Fill the mosaic with random masks
        for row in range(mosaic_size[0]):
            for col in range(mosaic_size[1]):
                # Select a random mask image
                mask_image = random.choice(mask_images)

                # Resize the mask to fit the tile
                mask_image_resized = mask_image.resize((tile_width, tile_height))

                # Calculate position to paste the mask
                position = (col * tile_width, row * tile_height)

                # Paste the mask onto the mosaic image
                mosaic_image.paste(mask_image_resized, position, mask_image_resized)

        # Composite the mosaic with the base image
        final_image = Image.alpha_composite(base_image, mosaic_image)

        # Save the final mosaic image
        final_image.save(output_image_path, format='PNG')
        print(f"Mosaic image saved to {output_image_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

def load_mask_images(mask_images_dir):
    """
    Load all mask images from the specified directory.

    Parameters:
    - mask_images_dir (str): Directory containing mask images.

    Returns:
    - list: List of loaded mask images.
    """
    mask_images = []
    try:
        for filename in os.listdir(mask_images_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                mask_image_path = os.path.join(mask_images_dir, filename)
                mask_image = Image.open(mask_image_path).convert("RGBA")
                mask_images.append(mask_image)
        if not mask_images:
            raise ValueError("No valid mask images found in the directory.")
    except Exception as e:
        print(f"Error loading mask images: {e}")
    return mask_images

if __name__ == "__main__":
    # Example usage
    BASE_IMAGE_PATH = "path/to/base_image.png"
    MASK_IMAGES_DIR = "path/to/mask_images"
    OUTPUT_IMAGE_PATH = "path/to/output_mosaic.png"

    create_mosaic(BASE_IMAGE_PATH, MASK_IMAGES_DIR, OUTPUT_IMAGE_PATH)
```
