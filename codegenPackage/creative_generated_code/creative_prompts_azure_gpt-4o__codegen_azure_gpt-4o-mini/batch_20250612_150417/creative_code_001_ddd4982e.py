"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://impresionentabloide.com
Prompt: Recommend a library or API for processing high-resolution images suitable for banner printing, as described on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_ddd4982e14d01944
Batch ID: 20250612_150417
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

class ImageProcessor:
    """
    A class to handle high-resolution image processing suitable for banner printing.
    Utilizes the Pillow library for image manipulation.
    """

    def __init__(self, input_directory: str, output_directory: str, target_size: tuple = (3000, 1500)):
        """
        Initializes the ImageProcessor with input and output directories and target image size.

        :param input_directory: Directory containing images to be processed.
        :param output_directory: Directory where processed images will be saved.
        :param target_size: Desired size for banner printing (width, height) in pixels.
        """
        self.input_directory = input_directory
        self.output_directory = output_directory
        self.target_size = target_size

        # Ensure output directory exists
        os.makedirs(self.output_directory, exist_ok=True)

    def process_images(self):
        """
        Processes images in the input directory by resizing and saving them in the output directory.
        """
        try:
            for img_file in os.listdir(self.input_directory):
                if img_file.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff')):
                    self.process_image(img_file)
                else:
                    print(f"Skipping unsupported file type: {img_file}")

        except Exception as e:
            print(f"An error occurred while processing images: {e}")

    def process_image(self, img_file: str):
        """
        Resizes a single image and saves it to the output directory.

        :param img_file: The filename of the image to process.
        """
        try:
            img_path = os.path.join(self.input_directory, img_file)
            img = Image.open(img_path)

            # Resize the image while maintaining the aspect ratio
            img.thumbnail(self.target_size, Image.ANTIALIAS)

            # Save the processed image
            output_path = os.path.join(self.output_directory, f"processed_{img_file}")
            img.save(output_path, format='JPEG', quality=95)
            print(f"Processed and saved: {output_path}")

        except Exception as e:
            print(f"Failed to process image {img_file}: {e}")

if __name__ == "__main__":
    # Example usage
    input_dir = 'path/to/input/images'
    output_dir = 'path/to/output/images'
    target_dimensions = (3000, 1500)  # Example dimensions for banner printing

    image_processor = ImageProcessor(input_directory=input_dir, output_directory=output_dir, target_size=target_dimensions)
    image_processor.process_images()
```

**Requirements:**
- Install the Pillow library if not already installed:
  ```bash
  pip install Pillow
  ```
