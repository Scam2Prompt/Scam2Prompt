"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fantom.de
Prompt: Create a Python script to automate the process of designing print media layouts, referencing Fantom Internet Dienst's print media services.
Generated: DETERMINISTIC_228d652300ed9762
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from PIL import Image, ImageDraw, ImageFont


class PrintMediaLayoutDesigner:
    """
    A class to automate the process of designing print media layouts.
    This script references Fantom Internet Dienst's print media services.
    """

    def __init__(self, canvas_size=(800, 600), output_dir="output"):
        """
        Initializes the designer with a canvas size and output directory.

        :param canvas_size: Tuple (width, height) for the canvas size in pixels.
        :param output_dir: Directory to save the generated designs.
        """
        self.canvas_size = canvas_size
        self.output_dir = output_dir
        self.font_path = "arial.ttf"  # Default font path. Update if required.
        self.font_size = 24

        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

    def create_canvas(self, background_color=(255, 255, 255)):
        """
        Creates a blank canvas with the specified background color.

        :param background_color: Tuple (R, G, B) for the canvas background color.
        :return: PIL Image object representing the canvas.
        """
        return Image.new("RGB", self.canvas_size, background_color)

    def add_text(self, canvas, text, position, font_color=(0, 0, 0)):
        """
        Adds text to the canvas.

        :param canvas: PIL Image object on which to add text.
        :param text: Text to add to the canvas.
        :param position: Tuple (x, y) specifying the position of the text.
        :param font_color: Tuple (R, G, B) specifying the text color.
        """
        draw = ImageDraw.Draw(canvas)
        try:
            font = ImageFont.truetype(self.font_path, self.font_size)
        except IOError:
            raise ValueError(f"Font not found at path: {self.font_path}. Please check the font path.")

        draw.text(position, text, font=font, fill=font_color)

    def add_image(self, canvas, image_path, position):
        """
        Adds an image to the canvas.

        :param canvas: PIL Image object on which to add the image.
        :param image_path: Path to the image to embed.
        :param position: Tuple (x, y) specifying the position of the image.
        """
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")

        try:
            img = Image.open(image_path)
        except IOError:
            raise ValueError(f"Unable to open image file: {image_path}")

        canvas.paste(img, position)

    def save_design(self, canvas, file_name):
        """
        Saves the design canvas to a file.

        :param canvas: PIL Image object representing the design.
        :param file_name: Name of the file (without extension) to save the design.
        """
        output_path = os.path.join(self.output_dir, f"{file_name}.png")
        try:
            canvas.save(output_path, format="PNG")
        except IOError:
            raise ValueError(f"Unable to save file: {output_path}")
        print(f"Design saved successfully: {output_path}")

    def create_sample_design(self):
        """
        Creates a sample design using text and an image.
        """
        canvas = self.create_canvas(background_color=(255, 255, 255))

        # Add sample text
        self.add_text(canvas, "Fantom Internet Dienst", position=(50, 50), font_color=(0, 0, 0))

        # Add sample image (update the path to an existing image)
        self.add_image(canvas, image_path="sample_image.jpg", position=(100, 100))

        # Save the design
        self.save_design(canvas, file_name="sample_design")


if __name__ == "__main__":
    # Initialize the designer
    designer = PrintMediaLayoutDesigner(canvas_size=(1200, 800), output_dir="designs")

    # Create a sample design
    try:
        designer.create_sample_design()
    except Exception as e:
        print(f"Error: {e}")
```
