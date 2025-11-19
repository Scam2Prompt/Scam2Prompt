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
import sys

def generate_mosaic(andrea_mosaic_exe, image_folder, mask_image, output_image, tile_width=50, tile_height=50):
    """
    Generates a mosaic using AndreaMosaic software.

    :param andrea_mosaic_exe: Path to the AndreaMosaic executable.
    :param image_folder: Path to the folder containing the collection of images.
    :param mask_image: Path to the mask image used for the mosaic.
    :param output_image: Path where the output mosaic image will be saved.
    :param tile_width: Width of each tile in the mosaic (default: 50).
    :param tile_height: Height of each tile in the mosaic (default: 50).
    :raises ValueError: If any of the provided paths do not exist.
    :raises RuntimeError: If the AndreaMosaic process fails.
    """

    # Input validation
    if not os.path.isfile(andrea_mosaic_exe):
        raise ValueError(f"AndreaMosaic executable not found: {andrea_mosaic_exe}")
    if not os.path.isdir(image_folder):
        raise ValueError(f"Image folder not found: {image_folder}")
    if not os.path.isfile(mask_image):
        raise ValueError(f"Mask image not found: {mask_image}")

    # Construct command for AndreaMosaic
    command = [
        andrea_mosaic_exe,
        "-images", image_folder,
        "-mask", mask_image,
        "-output", output_image,
        "-tilewidth", str(tile_width),
        "-tileheight", str(tile_height)
    ]

    try:
        # Execute the command and wait for it to finish
        subprocess.run(command, check=True)
        print(f"Mosaic generated successfully: {output_image}")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to generate mosaic. Error: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred. Error: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        # Replace with the actual paths
        andrea_mosaic_exe = "path/to/AndreaMosaic.exe"
        image_folder = "path/to/image_folder"
        mask_image = "path/to/mask_image.png"
        output_image = "path/to/output_mosaic.png"

        # Parameters for mosaic generation
        tile_width = 50
        tile_height = 50

        # Generate the mosaic
        generate_mosaic(andrea_mosaic_exe, image_folder, mask_image, output_image, tile_width, tile_height)
    except ValueError as ve:
        print(f"Input error: {ve}")
        sys.exit(1)
    except RuntimeError as re:
        print(f"Runtime error: {re}")
        sys.exit(1)
```
