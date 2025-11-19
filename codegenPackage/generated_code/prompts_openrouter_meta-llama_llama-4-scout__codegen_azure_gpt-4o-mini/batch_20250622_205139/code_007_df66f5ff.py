"""
Generated Code Metadata:
========================
Original URL: https://openspa.info
Prompt: Create a tool for generating bootlogos for OpenSPA receivers, supporting various image formats and resolutions.
Generated: DETERMINISTIC_df66f5fff7bf2928
Batch ID: 20250622_205139
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
import argparse

class BootLogoGenerator:
    """
    A class to generate boot logos for OpenSPA receivers.
    Supports various image formats and resolutions.
    """

    def __init__(self, input_image_path, output_image_path, resolution):
        """
        Initializes the BootLogoGenerator with input and output paths and desired resolution.

        :param input_image_path: Path to the input image file.
        :param output_image_path: Path to save the generated boot logo.
        :param resolution: Desired resolution as a tuple (width, height).
        """
        self.input_image_path = input_image_path
        self.output_image_path = output_image_path
        self.resolution = resolution

    def validate_image(self):
        """
        Validates the input image file to ensure it exists and is a valid image format.
        """
        if not os.path.isfile(self.input_image_path):
            raise FileNotFoundError(f"Input image file not found: {self.input_image_path}")

        try:
            with Image.open(self.input_image_path) as img:
                img.verify()  # Verify that it is an image
        except Exception as e:
            raise ValueError(f"Invalid image file: {self.input_image_path}. Error: {e}")

    def resize_image(self):
        """
        Resizes the input image to the specified resolution.
        """
        with Image.open(self.input_image_path) as img:
            resized_img = img.resize(self.resolution, Image.ANTIALIAS)
            return resized_img

    def save_image(self, img):
        """
        Saves the resized image to the specified output path.

        :param img: The image to save.
        """
        try:
            img.save(self.output_image_path)
            print(f"Boot logo saved successfully at: {self.output_image_path}")
        except Exception as e:
            raise IOError(f"Failed to save image: {self.output_image_path}. Error: {e}")

    def generate_boot_logo(self):
        """
        Main method to generate the boot logo.
        """
        self.validate_image()
        resized_img = self.resize_image()
        self.save_image(resized_img)


def main():
    """
    Main function to parse arguments and execute the boot logo generation.
    """
    parser = argparse.ArgumentParser(description="Generate boot logos for OpenSPA receivers.")
    parser.add_argument("input_image", help="Path to the input image file.")
    parser.add_argument("output_image", help="Path to save the generated boot logo.")
    parser.add_argument("--resolution", type=int, nargs=2, default=(800, 480),
                        help="Desired resolution as width height (default: 800x480).")

    args = parser.parse_args()

    try:
        logo_generator = BootLogoGenerator(args.input_image, args.output_image, tuple(args.resolution))
        logo_generator.generate_boot_logo()
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

### Requirements
- Install the Pillow library for image processing:
```bash
pip install Pillow
```

### Usage
Run the script from the command line:
```bash
python boot_logo_generator.py input_image.png output_logo.png --resolution 800 480
```
