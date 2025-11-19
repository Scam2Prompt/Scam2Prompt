"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamasks.art
Prompt: Write a Python script that utilizes the features of AndreaMosaic for generating a mosaic from a collection of mask images.
Generated: DETERMINISTIC_49b3c25c2eb9ba54
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

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_mosaic(source_images_dir, mask_images_dir, output_image_path, tile_width, tile_height):
    """
    Generates a mosaic image from a collection of mask images using AndreaMosaic.

    Args:
        source_images_dir (str): Path to the directory containing source images.
        mask_images_dir (str): Path to the directory containing mask images.
        output_image_path (str): Path where the generated mosaic image will be saved.
        tile_width (int): Width of each tile in the mosaic.
        tile_height (int): Height of each tile in the mosaic.

    Raises:
        FileNotFoundError: If the source or mask image directory does not exist.
        RuntimeError: If the AndreaMosaic command fails to execute.
    """
    # Check if the source and mask image directories exist
    if not os.path.isdir(source_images_dir):
        logging.error(f"Source images directory '{source_images_dir}' does not exist.")
        raise FileNotFoundError(f"Source images directory '{source_images_dir}' does not exist.")

    if not os.path.isdir(mask_images_dir):
        logging.error(f"Mask images directory '{mask_images_dir}' does not exist.")
        raise FileNotFoundError(f"Mask images directory '{mask_images_dir}' does not exist.")

    # Construct the AndreaMosaic command
    command = [
        'andreamosaic',  # Ensure 'andreamosaic' is in your PATH or provide the full path
        '-source', source_images_dir,
        '-mask', mask_images_dir,
        '-output', output_image_path,
        '-tileWidth', str(tile_width),
        '-tileHeight', str(tile_height),
        '-overwrite'  # Overwrite the output file if it exists
    ]

    logging.info("Running AndreaMosaic command...")
    
    # Execute the command
    try:
        subprocess.run(command, check=True)
        logging.info(f"Mosaic generated successfully at '{output_image_path}'")
    except subprocess.CalledProcessError as e:
        logging.error("AndreaMosaic command failed to execute.")
        raise RuntimeError(f"AndreaMosaic failed with error code {e.returncode}")

if __name__ == "__main__":
    # Example usage
    try:
        generate_mosaic(
            source_images_dir='path/to/source/images',
            mask_images_dir='path/to/mask/images',
            output_image_path='path/to/output/mosaic_image.jpg',
            tile_width=50,
            tile_height=50
        )
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

Remember to replace `'path/to/source/images'`, `'path/to/mask/images'`, and `'path/to/output/mosaic_image.jpg'` with actual paths when you run the script. Ensure that the `andreamosaic` command is accessible in your system's PATH for this script to work correctly.
