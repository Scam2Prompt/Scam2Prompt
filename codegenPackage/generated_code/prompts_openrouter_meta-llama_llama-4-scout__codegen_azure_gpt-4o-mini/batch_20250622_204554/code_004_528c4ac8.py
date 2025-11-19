"""
Generated Code Metadata:
========================
Original URL: https://www.sgeek-seo.com
Prompt: "Write a Python code snippet for optimizing website images for SEO."
Generated: DETERMINISTIC_528c4ac8058605ec
Batch ID: 20250622_204554
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def optimize_image(image_path, output_path, quality=85):
    """
    Optimize an image for web use by reducing its file size while maintaining quality.

    Parameters:
    - image_path (str): The path to the original image.
    - output_path (str): The path where the optimized image will be saved.
    - quality (int): The quality of the optimized image (1-100). Default is 85.

    Raises:
    - FileNotFoundError: If the original image does not exist.
    - IOError: If there is an error during image processing.
    """
    try:
        # Check if the image file exists
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"The image file {image_path} does not exist.")

        # Open the image file
        with Image.open(image_path) as img:
            # Convert image to RGB if it is in a different mode
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")

            # Save the optimized image
            img.save(output_path, "JPEG", quality=quality)
            logging.info(f"Optimized image saved to {output_path} with quality {quality}.")

    except FileNotFoundError as fnf_error:
        logging.error(fnf_error)
    except IOError as io_error:
        logging.error(f"An error occurred while processing the image: {io_error}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    input_image = "path/to/your/image.jpg"  # Replace with your image path
    output_image = "path/to/your/optimized_image.jpg"  # Replace with desired output path
    optimize_image(input_image, output_image)
```
