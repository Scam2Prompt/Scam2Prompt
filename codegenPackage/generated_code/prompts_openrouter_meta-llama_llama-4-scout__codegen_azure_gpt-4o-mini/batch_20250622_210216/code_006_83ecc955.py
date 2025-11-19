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
import os
from PIL import Image
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class ImageProcessor:
    """
    A class to handle image resizing and compression.
    """

    def __init__(self, input_path: str, output_path: str):
        """
        Initializes the ImageProcessor with input and output paths.

        :param input_path: Path to the input image file.
        :param output_path: Path to save the processed image.
        """
        self.input_path = input_path
        self.output_path = output_path

    def resize_image(self, new_width: int, new_height: int) -> None:
        """
        Resizes the image to the specified width and height.

        :param new_width: The desired width of the resized image.
        :param new_height: The desired height of the resized image.
        """
        try:
            with Image.open(self.input_path) as img:
                # Resize image
                img = img.resize((new_width, new_height), Image.ANTIALIAS)
                img.save(self.output_path)
                logging.info(f"Image resized to {new_width}x{new_height} and saved to {self.output_path}")
        except Exception as e:
            logging.error(f"Error resizing image: {e}")
            raise

    def compress_image(self, quality: int) -> None:
        """
        Compresses the image to the specified quality.

        :param quality: The quality of the output image (1-100).
        """
        try:
            with Image.open(self.input_path) as img:
                # Save the image with the specified quality
                img.save(self.output_path, optimize=True, quality=quality)
                logging.info(f"Image compressed with quality {quality} and saved to {self.output_path}")
        except Exception as e:
            logging.error(f"Error compressing image: {e}")
            raise

def main():
    # Example usage
    input_image_path = 'path/to/input/image.jpg'
    output_image_path_resized = 'path/to/output/resized_image.jpg'
    output_image_path_compressed = 'path/to/output/compressed_image.jpg'

    # Create an instance of ImageProcessor
    processor = ImageProcessor(input_image_path, output_image_path_resized)

    # Resize the image
    processor.resize_image(800, 600)

    # Compress the image
    processor.output_path = output_image_path_compressed  # Update output path for compression
    processor.compress_image(85)  # Compress with quality 85

if __name__ == "__main__":
    main()
```
