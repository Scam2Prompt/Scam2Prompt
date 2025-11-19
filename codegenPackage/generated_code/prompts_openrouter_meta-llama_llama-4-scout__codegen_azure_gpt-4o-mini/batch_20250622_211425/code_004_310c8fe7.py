"""
Generated Code Metadata:
========================
Original URL: https://itsolover.com
Prompt: Design a library for Python that can be used to create, manipulate, and share 4chan-inspired memes, including the "first 4chan meme on pump" concept.
Generated: DETERMINISTIC_310c8fe7dbba4b7a
Batch ID: 20250622_211425
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

class MemeGenerator:
    """
    A class to create, manipulate, and share 4chan-inspired memes.
    """

    def __init__(self, font_path='arial.ttf', font_size=40):
        """
        Initializes the MemeGenerator with a specified font and size.

        :param font_path: Path to the font file to be used for meme text.
        :param font_size: Size of the font for the meme text.
        """
        self.font_path = font_path
        self.font_size = font_size
        self.font = ImageFont.truetype(self.font_path, self.font_size)

    def create_meme(self, image_path, top_text, bottom_text, output_path):
        """
        Creates a meme with the specified top and bottom text.

        :param image_path: Path to the image file to be used for the meme.
        :param top_text: Text to be placed at the top of the meme.
        :param bottom_text: Text to be placed at the bottom of the meme.
        :param output_path: Path where the generated meme will be saved.
        """
        try:
            # Load the image
            image = Image.open(image_path)
            draw = ImageDraw.Draw(image)

            # Add top text
            self._draw_text(draw, top_text, position=(10, 10))

            # Add bottom text
            self._draw_text(draw, bottom_text, position=(10, image.height - 60))

            # Save the meme
            image.save(output_path)
            print(f"Meme saved to {output_path}")

        except FileNotFoundError:
            print(f"Error: The file {image_path} was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def _draw_text(self, draw, text, position):
        """
        Draws text on the image with word wrapping.

        :param draw: ImageDraw object to draw on the image.
        :param text: Text to be drawn.
        :param position: Tuple (x, y) for the text position.
        """
        # Wrap text to fit within the image width
        wrapped_text = textwrap.fill(text, width=30)
        text_size = draw.textsize(wrapped_text, font=self.font)

        # Calculate text position for center alignment
        x = position[0]
        y = position[1]
        draw.text((x, y), wrapped_text, font=self.font, fill="white")

    def share_meme(self, output_path):
        """
        Shares the meme by opening it in the default image viewer.

        :param output_path: Path to the meme image to be shared.
        """
        try:
            os.startfile(output_path)  # For Windows
        except Exception as e:
            print(f"An error occurred while trying to share the meme: {e}")

# Example usage:
if __name__ == "__main__":
    meme_gen = MemeGenerator()
    meme_gen.create_meme(
        image_path='input_image.jpg',
        top_text='First 4chan Meme',
        bottom_text='On Pump',
        output_path='meme_output.jpg'
    )
    meme_gen.share_meme('meme_output.jpg')
```

**Note:** Ensure you have the `Pillow` library installed for image manipulation. You can install it using `pip install Pillow`. Also, replace `'arial.ttf'` with the path to a valid font file on your system.
