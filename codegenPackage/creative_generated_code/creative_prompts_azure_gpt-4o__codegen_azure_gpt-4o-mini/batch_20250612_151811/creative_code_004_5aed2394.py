"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamasks.art
Prompt: Suggest open-source alternatives to AndreaMosaic for creating artistic mosaics and provide example code for using one of them.
Generated: DETERMINISTIC_5aed2394a66ba731
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import cv2
import os
from matplotlib import pyplot as plt

def create_mosaic(target_image_path, tile_images_folder, output_image_path, tile_size=(30, 30)):
    """
    Create an artistic mosaic from a target image using a collection of tile images.
    
    Parameters:
    - target_image_path (str): Path to the target image.
    - tile_images_folder (str): Folder containing tile images.
    - output_image_path (str): Path to save the generated mosaic image.
    - tile_size (tuple): Size of each tile in the mosaic.
    
    Raises:
    - FileNotFoundError: If the target image or tile images folder does not exist.
    - Exception: For any other unexpected errors.
    """
    
    # Check if the target image exists
    if not os.path.isfile(target_image_path):
        raise FileNotFoundError(f"Target image not found: {target_image_path}")
    
    # Check if the tile images folder exists
    if not os.path.isdir(tile_images_folder):
        raise FileNotFoundError(f"Tile images folder not found: {tile_images_folder}")

    try:
        # Load the target image
        target_image = cv2.imread(target_image_path)
        target_image = cv2.cvtColor(target_image, cv2.COLOR_BGR2RGB)  # Convert to RGB
        
        # Calculate the dimensions of the mosaic
        height, width, _ = target_image.shape
        mosaic_rows = height // tile_size[0]
        mosaic_cols = width // tile_size[1]

        # Load tile images
        tile_images = []
        for filename in os.listdir(tile_images_folder):
            file_path = os.path.join(tile_images_folder, filename)
            if os.path.isfile(file_path):
                tile_image = cv2.imread(file_path)
                tile_image = cv2.resize(tile_image, tile_size)
                tile_images.append(tile_image)

        # Create the mosaic
        mosaic_image = np.zeros((mosaic_rows * tile_size[0], mosaic_cols * tile_size[1], 3), dtype=np.uint8)
        
        for i in range(mosaic_rows):
            for j in range(mosaic_cols):
                # Select a random tile
                tile = np.random.choice(tile_images)
                mosaic_image[i * tile_size[0]:(i + 1) * tile_size[0], j * tile_size[1]:(j + 1) * tile_size[1]] = tile
        
        # Save the mosaic image
        cv2.imwrite(output_image_path, cv2.cvtColor(mosaic_image, cv2.COLOR_RGB2BGR))
        print(f"Mosaic image saved at: {output_image_path}")

    except Exception as e:
        raise Exception(f"An error occurred while creating the mosaic: {str(e)}")

# Example usage
if __name__ == "__main__":
    create_mosaic('path/to/target_image.jpg', 'path/to/tile_images/', 'path/to/output_mosaic.jpg')
```
