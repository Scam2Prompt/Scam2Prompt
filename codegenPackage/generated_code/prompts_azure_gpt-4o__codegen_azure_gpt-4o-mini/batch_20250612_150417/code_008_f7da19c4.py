"""
Generated Code Metadata:
========================
Original URL: https://impresionentabloide.com
Prompt: Create a script to convert customer designs into print-ready formats for large-format printing, following the specifications for vinyl and canvas printing described on the "Impresion en Tabloide" website.
Generated: DETERMINISTIC_f7da19c4e94cdc6d
Batch ID: 20250612_150417
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
from pathlib import Path

class PrintReadyConverter:
    """
    A class to convert customer designs into print-ready formats for large-format printing.
    Supports conversion for vinyl and canvas printing.
    """

    def __init__(self, input_dir: str, output_dir: str):
        """
        Initializes the converter with input and output directories.

        :param input_dir: Directory containing customer design files.
        :param output_dir: Directory to save converted print-ready files.
        """
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def convert_images(self):
        """
        Converts all images in the input directory to print-ready formats.
        """
        for image_file in self.input_dir.glob('*'):
            if image_file.suffix.lower() in ['.jpg', '.jpeg', '.png', '.tiff']:
                try:
                    self._process_image(image_file)
                except Exception as e:
                    print(f"Error processing {image_file}: {e}")

    def _process_image(self, image_file: Path):
        """
        Processes a single image file and saves it in the output directory.

        :param image_file: The image file to process.
        """
        print(f"Processing {image_file}...")
        with Image.open(image_file) as img:
            # Resize image to meet large-format printing specifications
            img = self._resize_image(img)

            # Convert to CMYK color mode for print
            img = img.convert('CMYK')

            # Save the processed image
            output_file = self.output_dir / f"{image_file.stem}_print_ready{image_file.suffix}"
            img.save(output_file, quality=95)
            print(f"Saved print-ready image to {output_file}")

    def _resize_image(self, img: Image.Image) -> Image.Image:
        """
        Resizes the image to the required dimensions for vinyl or canvas printing.

        :param img: The image to resize.
        :return: Resized image.
        """
        # Example dimensions for large-format printing (in pixels)
        target_width = 3000  # Example width
        target_height = 2000  # Example height

        # Resize image while maintaining aspect ratio
        img.thumbnail((target_width, target_height), Image.ANTIALIAS)
        return img

if __name__ == "__main__":
    # Define input and output directories
    input_directory = "path/to/customer/designs"
    output_directory = "path/to/print/ready"

    # Create a converter instance and convert images
    converter = PrintReadyConverter(input_directory, output_directory)
    converter.convert_images()
```
