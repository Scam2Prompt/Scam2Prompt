"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bee-property.com
Prompt: Develop a system that uses professional property photography to enhance rental listings and increase conversion rates. Include tools or libraries for image processing and optimization.
Generated: DETERMINISTIC_c847e8279da104d8
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageEnhance
from pathlib import Path


class PropertyImageProcessor:
    """
    A class to process and optimize property images for rental listings.

    Features:
    - Resize images to a standard resolution for web optimization.
    - Enhance image quality (brightness, contrast, sharpness).
    - Compress images to reduce file size.
    """

    def __init__(self, output_directory="processed_images"):
        """
        Initializes the processor with an output directory.

        Args:
            output_directory (str): Directory to save processed images.
        """
        self.output_directory = Path(output_directory)
        self.output_directory.mkdir(parents=True, exist_ok=True)

    def process_image(self, input_image_path, output_resolution=(1280, 720), compression_quality=85):
        """
        Processes a single image by enhancing and resizing it, then compresses the file.

        Args:
            input_image_path (str): Path to the input image.
            output_resolution (tuple): Target resolution (width, height).
            compression_quality (int): JPEG compression quality (1-100).
        """
        try:
            # Load the image
            with Image.open(input_image_path) as img:
                # Enhance brightness
                enhancer = ImageEnhance.Brightness(img)
                img = enhancer.enhance(1.2)  # Increase brightness by 20%

                # Enhance contrast
                enhancer = ImageEnhance.Contrast(img)
                img = enhancer.enhance(1.3)  # Increase contrast by 30%

                # Enhance sharpness
                enhancer = ImageEnhance.Sharpness(img)
                img = enhancer.enhance(2.0)  # Increase sharpness

                # Resize the image
                img = img.resize(output_resolution, Image.ANTIALIAS)

                # Save the processed image
                output_path = self.output_directory / f"{Path(input_image_path).stem}_processed.jpg"
                img.save(output_path, "JPEG", quality=compression_quality)

                print(f"Processed image saved to: {output_path}")
        except Exception as e:
            print(f"Error processing image {input_image_path}: {e}")

    def batch_process_images(self, input_directory, output_resolution=(1280, 720), compression_quality=85):
        """
        Processes all images in a directory.

        Args:
            input_directory (str): Directory containing images to process.
            output_resolution (tuple): Target resolution (width, height).
            compression_quality (int): JPEG compression quality (1-100).
        """
        try:
            input_dir = Path(input_directory)
            if not input_dir.exists():
                raise FileNotFoundError(f"Input directory not found: {input_directory}")

            image_files = [f for f in input_dir.iterdir() if f.suffix.lower() in {".jpg", ".jpeg", ".png"}]

            if not image_files:
                print(f"No image files found in directory: {input_directory}")
                return

            for image_file in image_files:
                self.process_image(image_file, output_resolution, compression_quality)

        except Exception as e:
            print(f"Error processing batch images in directory {input_directory}: {e}")


if __name__ == "__main__":
    # Initialize the image processor
    processor = PropertyImageProcessor()

    # Example usage: Single image processing
    processor.process_image("example_property.jpg")

    # Example usage: Batch processing
    processor.batch_process_images("property_images")
```
This Python code leverages the `Pillow` library (PIL) for image processing and optimization. It includes resizing, enhancing, and compressing images for rental listings while adhering to clean coding practices. Error handling is implemented to ensure robust operation.
