"""
Generated Code Metadata:
========================
Original URL: https://metamasks.art
Prompt: Explain how to zoom in on individual masks in a mosaic created with AndreaMosaic software.
Generated: DETERMINISTIC_0bfc171cb11c05f8
Batch ID: 20250612_140120
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import cv2
import numpy as np

def zoom_on_mask(mosaic_image_path, mask_image_path, zoom_factor=2.0, output_path='zoomed_mask.png'):
    """
    Zooms in on an individual mask in a mosaic image.

    Parameters:
    - mosaic_image_path (str): Path to the mosaic image file.
    - mask_image_path (str): Path to the mask image file.
    - zoom_factor (float): Factor by which to zoom in on the mask.
    - output_path (str): Path to save the zoomed mask image.

    Returns:
    - None: Saves the zoomed mask image to the specified output path.
    """
    try:
        # Load the mosaic and mask images
        mosaic_image = cv2.imread(mosaic_image_path)
        mask_image = cv2.imread(mask_image_path)

        # Check if images are loaded successfully
        if mosaic_image is None:
            raise FileNotFoundError(f"Mosaic image not found at {mosaic_image_path}")
        if mask_image is None:
            raise FileNotFoundError(f"Mask image not found at {mask_image_path}")

        # Get the dimensions of the mask image
        mask_height, mask_width = mask_image.shape[:2]

        # Calculate the center of the mask
        center_x, center_y = mask_width // 2, mask_height // 2

        # Calculate the new dimensions for the zoomed image
        new_width = int(mask_width / zoom_factor)
        new_height = int(mask_height / zoom_factor)

        # Calculate the cropping coordinates
        x1 = max(center_x - new_width // 2, 0)
        y1 = max(center_y - new_height // 2, 0)
        x2 = min(center_x + new_width // 2, mask_width)
        y2 = min(center_y + new_height // 2, mask_height)

        # Crop the mask image
        zoomed_mask = mask_image[y1:y2, x1:x2]

        # Save the zoomed mask image
        cv2.imwrite(output_path, zoomed_mask)
        print(f"Zoomed mask saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    zoom_on_mask('path/to/mosaic_image.png', 'path/to/mask_image.png', zoom_factor=2.0, output_path='zoomed_mask.png')
```
