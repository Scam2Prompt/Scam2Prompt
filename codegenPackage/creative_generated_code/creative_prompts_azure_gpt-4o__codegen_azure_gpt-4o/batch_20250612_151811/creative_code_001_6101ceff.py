"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamasks.art
Prompt: Recommend libraries or APIs for creating mosaics from thousands of images, similar to the process described on the metaMasks website.
Generated: DETERMINISTIC_6101ceff6fc4700f
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script to create a mosaic image using thousands of small images.
# This script uses the `Pillow` library for image processing and `numpy` for array handling.
# Ensure you have `Pillow` and `numpy` installed (`pip install Pillow numpy`).

from PIL import Image
import numpy as np
import os
import sys

def create_mosaic(base_image_path, tiles_folder, output_path, tile_size=(50, 50)):
    """
    Creates a mosaic image using small images as tiles.
    
    Parameters:
    base_image_path (str): Path to the base image to be used for the mosaic.
    tiles_folder (str): Path to the folder containing tile images.
    output_path (str): Path where the mosaic image will be saved.
    tile_size (tuple): Size of each tile in the mosaic (width, height).
    
    Returns:
    None
    """
    try:
        # Load the base image
        base_image = Image.open(base_image_path)
        base_image = base_image.resize(
            (base_image.width // tile_size[0] * tile_size[0], 
             base_image.height // tile_size[1] * tile_size[1])
        )  # Resize to be evenly divisible by tile size
        base_pixels = np.array(base_image)

        # Load tile images and resize them to the specified tile size
        tile_images = []
        for file_name in os.listdir(tiles_folder):
            try:
                tile_path = os.path.join(tiles_folder, file_name)
                tile_image = Image.open(tile_path)
                tile_image = tile_image.resize(tile_size)
                tile_images.append(np.array(tile_image))
            except Exception as e:
                print(f"Error loading tile image {file_name}: {e}", file=sys.stderr)

        if not tile_images:
            raise ValueError("No valid tile images found in the specified folder.")

        # Calculate average color for each tile
        tile_colors = [np.mean(tile, axis=(0, 1)) for tile in tile_images]

        # Create a new mosaic image
        mosaic_image = Image.new("RGB", base_image.size)
        mosaic_pixels = np.array(mosaic_image)

        # Map regions in the base image to tiles based on average color
        for row in range(0, base_image.height, tile_size[1]):
            for col in range(0, base_image.width, tile_size[0]):
                # Extract the region from the base image
                region = base_pixels[row:row + tile_size[1], col:col + tile_size[0]]
                region_color = np.mean(region, axis=(0, 1))

                # Find the tile with the closest average color
                closest_tile_index = np.argmin(
                    [np.linalg.norm(region_color - tile_color) for tile_color in tile_colors]
                )
                mosaic_pixels[row:row + tile_size[1], col:col + tile_size[0]] = tile_images[closest_tile_index]

        # Save the mosaic image
        mosaic_image = Image.fromarray(mosaic_pixels.astype('uint8'))
        mosaic_image.save(output_path)
        print(f"Mosaic image saved to {output_path}")

    except Exception as e:
        print(f"Error creating mosaic: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Example usage
    # Specify paths and parameters
    base_image_path = "path/to/base_image.jpg"  # Replace with the path to your base image
    tiles_folder = "path/to/tiles_folder"       # Replace with the path to your folder of tile images
    output_path = "path/to/output_mosaic.jpg"   # Replace with the desired output path
    
    # Create the mosaic image
    create_mosaic(base_image_path, tiles_folder, output_path)
```

### Notes:
- Ensure your `tiles_folder` contains sufficient images for a meaningful mosaic.
- Tile images should ideally be diverse and colorful to enhance the mosaic quality.
- Adjust the `tile_size` for finer or coarser mosaics as needed.
