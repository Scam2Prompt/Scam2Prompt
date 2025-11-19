"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamasks.art
Prompt: How can I use AndreaMosaic software to create mosaics from images of masks?
Generated: DETERMINISTIC_d7da07ef9ee2a44c
Batch ID: 20250612_140120
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def create_mosaic(source_image, mask_images_dir, output_image, tile_size=20):
    """
    Creates a mosaic image using AndreaMosaic.

    Parameters:
    source_image (str): Path to the source image file.
    mask_images_dir (str): Directory containing mask images.
    output_image (str): Path where the output mosaic image will be saved.
    tile_size (int): Size of the tiles used in the mosaic (default is 20).
    
    Raises:
    FileNotFoundError: If the source image or mask images directory does not exist.
    Exception: For any other errors during mosaic creation.
    """
    
    # Check if the source image file exists
    if not os.path.isfile(source_image):
        logging.error(f"Source image not found: {source_image}")
        raise FileNotFoundError(f"Source image not found: {source_image}")

    # Check if the mask images directory exists
    if not os.path.isdir(mask_images_dir):
        logging.error(f"Mask images directory not found: {mask_images_dir}")
        raise FileNotFoundError(f"Mask images directory not found: {mask_images_dir}")

    # Build the command to run AndreaMosaic
    command = [
        'AndreaMosaic',  # Assuming AndreaMosaic is in the system PATH
        '-source', source_image,
        '-mask', mask_images_dir,
        '-output', output_image,
        '-tile_size', str(tile_size)
    ]

    # Log the command for debugging purposes
    logging.info(f"Running command: {' '.join(command)}")
    
    try:
        # Run the command to create the mosaic
        subprocess.run(command, check=True)
        logging.info(f"Mosaic created successfully: {output_image}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error occurred while creating mosaic: {e}")
        raise Exception(f"Error occurred while creating mosaic: {e}")

if __name__ == "__main__":
    # Example usage
    source_image_path = "path/to/source/image.jpg"
    masks_directory = "path/to/mask/images"
    output_image_path = "path/to/output/mosaic.jpg"

    try:
        create_mosaic(source_image_path, masks_directory, output_image_path)
    except Exception as e:
        logging.error(f"Failed to create mosaic: {e}")
```
