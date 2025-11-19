"""
Generated Code Metadata:
========================
Original URL: https://fsromain.com
Prompt: How can I implement picture editing techniques to enhance my social media content, based on Romain Ferri’s recommendations?
Generated: DETERMINISTIC_77aaacf949896fa2
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageEnhance, ImageFilter
import os

class ImageEditor:
    """
    A class to perform various image editing techniques to enhance social media content.
    """

    def __init__(self, image_path):
        """
        Initializes the ImageEditor with the path to the image.

        :param image_path: str - Path to the image file
        """
        self.image_path = image_path
        self.image = self.load_image()

    def load_image(self):
        """
        Loads the image from the specified path.

        :return: Image object
        """
        try:
            image = Image.open(self.image_path)
            return image
        except Exception as e:
            raise FileNotFoundError(f"Error loading image: {e}")

    def enhance_brightness(self, factor):
        """
        Enhances the brightness of the image.

        :param factor: float - Factor by which to enhance brightness (1.0 means no change)
        :return: Image object
        """
        enhancer = ImageEnhance.Brightness(self.image)
        return enhancer.enhance(factor)

    def enhance_contrast(self, factor):
        """
        Enhances the contrast of the image.

        :param factor: float - Factor by which to enhance contrast (1.0 means no change)
        :return: Image object
        """
        enhancer = ImageEnhance.Contrast(self.image)
        return enhancer.enhance(factor)

    def apply_blur(self, radius):
        """
        Applies a blur effect to the image.

        :param radius: float - Radius of the blur
        :return: Image object
        """
        return self.image.filter(ImageFilter.GaussianBlur(radius))

    def save_image(self, output_path):
        """
        Saves the edited image to the specified output path.

        :param output_path: str - Path to save the edited image
        """
        try:
            self.image.save(output_path)
            print(f"Image saved successfully at {output_path}")
        except Exception as e:
            raise IOError(f"Error saving image: {e}")

def main():
    """
    Main function to demonstrate image editing techniques.
    """
    input_image_path = 'input.jpg'  # Path to the input image
    output_image_path = 'output.jpg'  # Path to save the edited image

    # Create an instance of ImageEditor
    editor = ImageEditor(input_image_path)

    # Enhance brightness and contrast
    bright_image = editor.enhance_brightness(1.5)  # Increase brightness by 50%
    contrast_image = editor.enhance_contrast(1.3)  # Increase contrast by 30%

    # Apply blur effect
    blurred_image = editor.apply_blur(2)  # Apply a blur with radius 2

    # Save the final edited image
    editor.image = blurred_image  # Set the final image to the blurred one
    editor.save_image(output_image_path)

if __name__ == "__main__":
    main()
```

Make sure to install the Pillow library if you haven't already:

```bash
pip install Pillow
```
