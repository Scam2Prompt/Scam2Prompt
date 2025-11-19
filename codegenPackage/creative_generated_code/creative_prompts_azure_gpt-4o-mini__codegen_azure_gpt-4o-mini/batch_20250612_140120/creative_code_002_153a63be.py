"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamasks.art
Prompt: What are the steps to create a custom mosaic using the AndreaMosaic software, specifically with images of masks?
Generated: DETERMINISTIC_153a63be590c545a
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
import glob

def create_mosaic(mask_images_folder, output_mosaic_path, mosaic_size=(800, 600), tile_size=(50, 50), tile_overlap=0):
    """
    Create a custom mosaic using AndreaMosaic software with images of masks.

    Parameters:
    - mask_images_folder: str - Path to the folder containing mask images.
    - output_mosaic_path: str - Path where the output mosaic will be saved.
    - mosaic_size: tuple - Size of the output mosaic in pixels (width, height).
    - tile_size: tuple - Size of each tile in pixels (width, height).
    - tile_overlap: int - Overlap size for tiles in pixels.
    """

    # Validate input paths
    if not os.path.isdir(mask_images_folder):
        raise ValueError(f"The provided mask images folder does not exist: {mask_images_folder}")
    
    if not os.path.exists(os.path.dirname(output_mosaic_path)):
        raise ValueError(f"The output path directory does not exist: {os.path.dirname(output_mosaic_path)}")

    # Gather all mask images
    mask_images = glob.glob(os.path.join(mask_images_folder, '*.*'))
    if not mask_images:
        raise ValueError("No images found in the specified folder.")

    # Create the mosaic command for AndreaMosaic
    command = [
        "AndreaMosaic", # The command to call AndreaMosaic software
        "-mosaic", output_mosaic_path, # Output path for the mosaic
        "-size", f"{mosaic_size[0]}x{mosaic_size[1]}", # Set mosaic size
        "-tile", f"{tile_size[0]}x{tile_size[1]}", # Set tile size
        "-overlap", str(tile_overlap), # Set tile overlap
    ] + mask_images # Add all mask images to the command

    try:
        # Execute the mosaic creation process
        subprocess.run(command, check=True)
        print(f"Mosaic successfully created at: {output_mosaic_path}")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to create mosaic: {e}")
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred: {e}")

# Example usage (uncomment to run):
# create_mosaic("path/to/mask/images", "output/mosaic.png")
```
