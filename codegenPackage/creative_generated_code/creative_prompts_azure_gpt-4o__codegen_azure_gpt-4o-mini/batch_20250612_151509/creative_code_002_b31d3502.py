"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokenpocketn.shop
Prompt: Recommend an API or library to compress images for faster loading times while maintaining quality, and provide example code for implementation.
Generated: DETERMINISTIC_b31d35025e7b284a
Batch ID: 20250612_151509
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image
import logging

# Set up logging to handle potential errors during image processing
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def compress_image(input_path: str, output_path: str, quality: int = 85) -> None:
    """
    Compress an image to reduce its file size while maintaining quality.

    :param input_path: Path to the input image file.
    :param output_path: Path where the compressed image will be saved.
    :param quality: Quality of the output image (1-100). Higher is better quality.
    :raises FileNotFoundError: If the input file does not exist.
    :raises IOError: If there is an error saving the compressed image.
    """
    # Check if the input file exists
    if not os.path.exists(input_path):
        logging.error(f"Input file not found: {input_path}")
        raise FileNotFoundError(f"Input file not found: {input_path}")

    try:
        # Open the input image
        with Image.open(input_path) as img:
            # Convert the image to RGB if it's a PNG with transparency
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # Save the compressed image
            img.save(output_path, "JPEG", quality=quality)
            logging.info(f"Image compressed and saved to: {output_path}")
    except IOError as e:
        logging.error(f"Failed to save compressed image: {e}")
        raise IOError(f"Failed to save compressed image: {e}")

# Example Usage
if __name__ == "__main__":
    try:
        compress_image("input_image.jpg", "output_image.jpg", quality=85)
    except Exception as e:
        logging.error(f"Error compressing image: {e}")
```

Make sure to install the required library by running:
```bash
pip install Pillow
```

This code provides a function to compress images using the Pillow library, with appropriate error handling and logging for production use.
