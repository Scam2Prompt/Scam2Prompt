"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-258--heuristic-davinci-1cf783.netlify.app
Prompt: Write code to handle Unicode font issues, specifically for the "Stratum Unicode" font, as mentioned on the webpage.
Generated: DETERMINISTIC_51948867efdd03dc
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import logging
from PIL import ImageFont, ImageDraw, Image

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UnicodeFontHandler:
    def __init__(self, font_path: str, font_size: int):
        """
        Initializes the UnicodeFontHandler with the specified font path and size.

        :param font_path: Path to the font file (e.g., Stratum Unicode)
        :param font_size: Size of the font
        """
        self.font_path = font_path
        self.font_size = font_size
        self.font = self.load_font()

    def load_font(self) -> ImageFont.FreeTypeFont:
        """
        Loads the font from the specified path.

        :return: An ImageFont object
        :raises FileNotFoundError: If the font file does not exist
        :raises ValueError: If the font size is not positive
        """
        if not os.path.isfile(self.font_path):
            logging.error(f"Font file not found: {self.font_path}")
            raise FileNotFoundError(f"Font file not found: {self.font_path}")

        if self.font_size <= 0:
            logging.error("Font size must be a positive integer.")
            raise ValueError("Font size must be a positive integer.")

        try:
            font = ImageFont.truetype(self.font_path, self.font_size)
            logging.info(f"Font loaded successfully: {self.font_path}")
            return font
        except Exception as e:
            logging.error(f"Failed to load font: {e}")
            raise

    def draw_text(self, image: Image.Image, text: str, position: tuple, color: str = "black") -> None:
        """
        Draws the specified text on the given image at the specified position.

        :param image: The image to draw on
        :param text: The text to draw
        :param position: A tuple (x, y) for the text position
        :param color: The color of the text (default is black)
        :raises ValueError: If the text is empty
        """
        if not text:
            logging.error("Text cannot be empty.")
            raise ValueError("Text cannot be empty.")

        try:
            draw = ImageDraw.Draw(image)
            draw.text(position, text, font=self.font, fill=color)
            logging.info(f"Text drawn on image at position {position}: {text}")
        except Exception as e:
            logging.error(f"Failed to draw text: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Path to the Stratum Unicode font file
        font_path = "path/to/StratumUnicode.ttf"
        font_size = 24

        # Create an instance of UnicodeFontHandler
        font_handler = UnicodeFontHandler(font_path, font_size)

        # Create a blank image
        image = Image.new("RGB", (400, 200), "white")

        # Draw some Unicode text
        unicode_text = "Hello, 世界!"  # Example Unicode text
        position = (10, 80)
        font_handler.draw_text(image, unicode_text, position)

        # Save the image
        image.save("output_image.png")
        logging.info("Image saved as output_image.png")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
