"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Recommend an API or library for quickly resizing and compressing images, considering the need to send high and low-resolution photos, as mentioned in the testimonial from Patricia.
Generated: DETERMINISTIC_83ecc955fa436685
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from PIL import Image
import io
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def resize_image(image_path, output_path, size):
    """
    Resize an image to a specified size.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the resized image.
        size (tuple): A tuple of two integers representing the new width and height.

    Returns:
        bool: True if the image was resized successfully, False otherwise.
    """
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Resize the image
            img = img.resize(size)
            # Save the resized image
            img.save(output_path)
            logger.info(f"Image resized and saved to {output_path}")
            return True
    except Exception as e:
        logger.error(f"Error resizing image: {e}")
        return False

def compress_image(image_path, output_path, quality):
    """
    Compress an image to a specified quality.

    Args:
        image_path (str): Path to the input image.
        output_path (str): Path to save the compressed image.
        quality (int): A value between 1 and 95 representing the compression quality.

    Returns:
        bool: True if the image was compressed successfully, False otherwise.
    """
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Save the image with the specified quality
            img.save(output_path, optimize=True, quality=quality)
            logger.info(f"Image compressed and saved to {output_path}")
            return True
    except Exception as e:
        logger.error(f"Error compressing image: {e}")
        return False

def generate_image_variations(image_path, output_dir):
    """
    Generate high and low resolution variations of an image.

    Args:
        image_path (str): Path to the input image.
        output_dir (str): Directory to save the image variations.

    Returns:
        dict: A dictionary containing the paths to the high and low resolution images.
    """
    try:
        # Define the image sizes
        high_res_size = (1920, 1080)  # High resolution size
        low_res_size = (640, 480)  # Low resolution size

        # Define the output file names
        high_res_output_path = f"{output_dir}/high_res_image.jpg"
        low_res_output_path = f"{output_dir}/low_res_image.jpg"

        # Resize the image to high resolution
        resize_image(image_path, high_res_output_path, high_res_size)

        # Resize the image to low resolution
        resize_image(image_path, low_res_output_path, low_res_size)

        # Compress the low resolution image
        compress_image(low_res_output_path, low_res_output_path, 80)

        # Return the paths to the image variations
        return {
            "high_res": high_res_output_path,
            "low_res": low_res_output_path
        }
    except Exception as e:
        logger.error(f"Error generating image variations: {e}")
        return None

# Example usage
if __name__ == "__main__":
    image_path = "input_image.jpg"
    output_dir = "output_images"

    import os
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    image_variations = generate_image_variations(image_path, output_dir)
    if image_variations:
        logger.info("Image variations generated successfully")
        logger.info(f"High resolution image: {image_variations['high_res']}")
        logger.info(f"Low resolution image: {image_variations['low_res']}")
    else:
        logger.error("Failed to generate image variations")
```
