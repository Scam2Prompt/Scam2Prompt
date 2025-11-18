"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamasks.art
Prompt: Write Python code to generate a mosaic image using AndreaMosaic software or similar tools. Include steps for integrating mask images as input.
Generated: DETERMINISTIC_64ffa645d1588f8c
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import subprocess
from PIL import Image

# Function to ensure AndreaMosaic is installed and accessible
def check_andreamosaic_installed():
    """Checks if AndreaMosaic executable is available."""
    andreamosaic_path = "AndreaMosaic.exe"  # Path to AndreaMosaic executable
    if not os.path.exists(andreamosaic_path):
        raise FileNotFoundError(
            "AndreaMosaic executable not found. Ensure it's installed and the path is correct."
        )
    return andreamosaic_path

# Function to generate a mosaic image
def create_mosaic_image(base_image_path, tile_images_folder, output_image_path, mask_image_path=None):
    """
    Generates a mosaic image using AndreaMosaic software.

    Parameters:
        base_image_path (str): Path to the base image to be converted into a mosaic.
        tile_images_folder (str): Path to folder containing tile images.
        output_image_path (str): Path to save the generated mosaic image.
        mask_image_path (str): (Optional) Path to a mask image to influence mosaic generation.
    """
    # Validate input paths
    if not os.path.exists(base_image_path):
        raise FileNotFoundError(f"Base image not found at {base_image_path}")
    if not os.path.exists(tile_images_folder):
        raise FileNotFoundError(f"Tile images folder not found at {tile_images_folder}")
    if mask_image_path and not os.path.exists(mask_image_path):
        raise FileNotFoundError(f"Mask image not found at {mask_image_path}")

    # Ensure AndreaMosaic is installed
    andreamosaic_path = check_andreamosaic_installed()

    # Construct the command to execute AndreaMosaic
    command = [
        andreamosaic_path,         # Execute AndreaMosaic
        base_image_path,           # Input base image
        tile_images_folder,        # Folder containing tiles
        output_image_path          # Output mosaic image
    ]

    # Add mask image to the command if provided
    if mask_image_path:
        command.append(f"-mask:{mask_image_path}")

    # Execute the command
    try:
        subprocess.run(command, check=True)
        print(f"Mosaic image generated successfully: {output_image_path}")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error generating mosaic image: {e}")

# Example usage
if __name__ == "__main__":
    # Input parameters
    base_image = "base_image.jpg"
    tile_images = "tile_images_folder/"
    output_image = "output_mosaic.jpg"
    mask_image = "mask_image.png"  # Optional mask image (set to None if not using a mask)

    # Create the mosaic image
    try:
        create_mosaic_image(base_image, tile_images, output_image, mask_image)
    except Exception as e:
        print(f"An error occurred: {e}")
```

**Note**: This script assumes `AndreaMosaic.exe` is installed and accessible in the current directory. Modify paths accordingly.
