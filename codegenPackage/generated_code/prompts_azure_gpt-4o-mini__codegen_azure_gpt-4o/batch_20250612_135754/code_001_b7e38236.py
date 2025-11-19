"""
Generated Code Metadata:
========================
Original URL: https://blurapp.net
Prompt: Write a tutorial on how to implement a photo editing functionality similar to the Blur App, including features like eraser and size changer.
Generated: DETERMINISTIC_b7e382369926583d
Batch ID: 20250612_135754
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a Python implementation using the `Pillow` library for photo editing functionality, including blur, eraser, and size changer features.

```python
from PIL import Image, ImageFilter, ImageDraw
import os

class PhotoEditor:
    def __init__(self, image_path):
        """
        Initialize the PhotoEditor with an image.

        :param image_path: Path to the image file.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        
        self.image = Image.open(image_path)
        self.original_image = self.image.copy()  # Keep a copy of the original image for reset functionality

    def apply_blur(self, radius=5):
        """
        Apply a blur effect to the image.

        :param radius: The radius of the blur effect. Default is 5.
        """
        if radius < 0:
            raise ValueError("Blur radius must be non-negative.")
        self.image = self.image.filter(ImageFilter.GaussianBlur(radius))

    def erase_area(self, x, y, width, height):
        """
        Erase a rectangular area of the image by making it transparent.

        :param x: X-coordinate of the top-left corner of the rectangle.
        :param y: Y-coordinate of the top-left corner of the rectangle.
        :param width: Width of the rectangle.
        :param height: Height of the rectangle.
        """
        if self.image.mode != 'RGBA':
            self.image = self.image.convert('RGBA')  # Convert image to RGBA mode if not already
        
        # Create a transparent rectangle
        draw = ImageDraw.Draw(self.image)
        transparent_color = (0, 0, 0, 0)  # RGBA for transparent
        draw.rectangle([x, y, x + width, y + height], fill=transparent_color)

    def resize_image(self, new_width, new_height):
        """
        Resize the image to the specified dimensions.

        :param new_width: The new width of the image.
        :param new_height: The new height of the image.
        """
        if new_width <= 0 or new_height <= 0:
            raise ValueError("Width and height must be positive integers.")
        self.image = self.image.resize((new_width, new_height), Image.ANTIALIAS)

    def reset_image(self):
        """
        Reset the image to its original state.
        """
        self.image = self.original_image.copy()

    def save_image(self, output_path):
        """
        Save the edited image to the specified path.

        :param output_path: Path to save the edited image.
        """
        try:
            self.image.save(output_path)
        except Exception as e:
            raise IOError(f"Failed to save image: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the photo editor with an image
        editor = PhotoEditor("example.jpg")
        
        # Apply blur effect
        editor.apply_blur(radius=10)
        
        # Erase a rectangular area
        editor.erase_area(x=50, y=50, width=100, height=100)
        
        # Resize the image
        editor.resize_image(new_width=800, new_height=600)
        
        # Save the edited image
        editor.save_image("edited_example.jpg")
        
        print("Image editing completed successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
```

### Requirements:
- Install the `Pillow` library if not already installed:
  ```bash
  pip install pillow
  ```

This code is production-ready, well-documented, and includes error handling for common issues such as file not found, invalid dimensions, and save errors.
