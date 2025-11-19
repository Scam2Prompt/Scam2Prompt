"""
Generated Code Metadata:
========================
Original URL: https://sdbondindia.com
Prompt: Develop a program to create banner designs and ADS boards as described in SD BOND India's latest projects, ensuring flexibility in customization.
Generated: DETERMINISTIC_f1193e1feab68425
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# banner_designer.py

from PIL import Image, ImageDraw, ImageFont
import os

class BannerDesigner:
    """
    A class used to create banner designs and ADS boards.

    Attributes:
    ----------
    width : int
        The width of the banner.
    height : int
        The height of the banner.
    background_color : str
        The background color of the banner.
    text_color : str
        The text color of the banner.
    font_name : str
        The font name of the banner text.
    font_size : int
        The font size of the banner text.

    Methods:
    -------
    add_text(text, x, y)
        Adds text to the banner at the specified position.
    add_image(image_path, x, y)
        Adds an image to the banner at the specified position.
    save_banner(output_path)
        Saves the banner to the specified output path.
    """

    def __init__(self, width, height, background_color="#FFFFFF", text_color="#000000", font_name="Arial.ttf", font_size=24):
        """
        Initializes the BannerDesigner object.

        Parameters:
        ----------
        width : int
            The width of the banner.
        height : int
            The height of the banner.
        background_color : str, optional
            The background color of the banner (default is "#FFFFFF").
        text_color : str, optional
            The text color of the banner (default is "#000000").
        font_name : str, optional
            The font name of the banner text (default is "Arial.ttf").
        font_size : int, optional
            The font size of the banner text (default is 24).
        """
        self.width = width
        self.height = height
        self.background_color = background_color
        self.text_color = text_color
        self.font_name = font_name
        self.font_size = font_size
        self.image = Image.new("RGB", (width, height), background_color)
        self.draw = ImageDraw.Draw(self.image)
        self.font = ImageFont.truetype(font_name, font_size)

    def add_text(self, text, x, y):
        """
        Adds text to the banner at the specified position.

        Parameters:
        ----------
        text : str
            The text to add.
        x : int
            The x-coordinate of the text position.
        y : int
            The y-coordinate of the text position.
        """
        self.draw.text((x, y), text, fill=self.text_color, font=self.font)

    def add_image(self, image_path, x, y):
        """
        Adds an image to the banner at the specified position.

        Parameters:
        ----------
        image_path : str
            The path to the image file.
        x : int
            The x-coordinate of the image position.
        y : int
            The y-coordinate of the image position.
        """
        try:
            image = Image.open(image_path)
            self.image.paste(image, (x, y))
        except FileNotFoundError:
            print(f"Error: Image file '{image_path}' not found.")

    def save_banner(self, output_path):
        """
        Saves the banner to the specified output path.

        Parameters:
        ----------
        output_path : str
            The path to save the banner.
        """
        try:
            self.image.save(output_path)
            print(f"Banner saved to '{output_path}'")
        except Exception as e:
            print(f"Error saving banner: {e}")


def main():
    # Create a new banner designer
    designer = BannerDesigner(800, 600)

    # Add text to the banner
    designer.add_text("SD BOND India", 100, 100)
    designer.add_text("Latest Projects", 100, 150)

    # Add an image to the banner
    image_path = "logo.png"
    designer.add_image(image_path, 100, 250)

    # Save the banner
    output_path = "banner.png"
    designer.save_banner(output_path)


if __name__ == "__main__":
    main()
```
