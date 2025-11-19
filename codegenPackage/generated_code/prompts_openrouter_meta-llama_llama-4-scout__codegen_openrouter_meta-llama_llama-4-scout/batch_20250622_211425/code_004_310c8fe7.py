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
"""
4chan Meme Library
====================
A Python library for creating, manipulating, and sharing 4chan-inspired memes.

Classes:
    Meme: Represents a 4chan-style meme with an image and text.
    First4chanMemeOnPump: A specific type of meme related to the "first 4chan meme on pump" concept.

Exceptions:
    InvalidMemeError: Raised when a meme is created with invalid data.
"""

import os
from PIL import Image
from typing import Optional

class InvalidMemeError(Exception):
    """Raised when a meme is created with invalid data."""
    pass

class Meme:
    """
    Represents a 4chan-style meme with an image and text.

    Attributes:
        image_path (str): The path to the meme image.
        top_text (str): The top text of the meme.
        bottom_text (str): The bottom text of the meme.
    """

    def __init__(self, image_path: str, top_text: str = "", bottom_text: str = ""):
        """
        Initializes a Meme object.

        Args:
            image_path (str): The path to the meme image.
            top_text (str, optional): The top text of the meme. Defaults to "".
            bottom_text (str, optional): The bottom text of the meme. Defaults to "".

        Raises:
            InvalidMemeError: If the image path is invalid or the image does not exist.
        """
        if not os.path.exists(image_path):
            raise InvalidMemeError("Image does not exist")
        self.image_path = image_path
        self.top_text = top_text
        self.bottom_text = bottom_text

    def add_text(self, top_text: str = "", bottom_text: str = ""):
        """
        Adds text to the meme.

        Args:
            top_text (str, optional): The top text to add. Defaults to "".
            bottom_text (str, optional): The bottom text to add. Defaults to "".
        """
        self.top_text += top_text
        self.bottom_text += bottom_text

    def save(self, output_path: str):
        """
        Saves the meme to a new image file.

        Args:
            output_path (str): The path to save the meme image.
        """
        image = Image.open(self.image_path)
        # Use a library like Pillow to draw text on the image
        # For simplicity, this example uses a placeholder
        image.save(output_path)

class First4chanMemeOnPump(Meme):
    """
    A specific type of meme related to the "first 4chan meme on pump" concept.

    Attributes:
        pump_number (int): The pump number associated with the meme.
    """

    def __init__(self, image_path: str, pump_number: int, top_text: str = "", bottom_text: str = ""):
        """
        Initializes a First4chanMemeOnPump object.

        Args:
            image_path (str): The path to the meme image.
            pump_number (int): The pump number associated with the meme.
            top_text (str, optional): The top text of the meme. Defaults to "".
            bottom_text (str, optional): The bottom text of the meme. Defaults to "".

        Raises:
            InvalidMemeError: If the image path is invalid or the image does not exist.
        """
        super().__init__(image_path, top_text, bottom_text)
        self.pump_number = pump_number

    def __str__(self):
        return f"Pump {self.pump_number}: {self.top_text} | {self.bottom_text}"

def create_meme(image_path: str, top_text: str = "", bottom_text: str = "") -> Meme:
    """
    Creates a new Meme object.

    Args:
        image_path (str): The path to the meme image.
        top_text (str, optional): The top text of the meme. Defaults to "".
        bottom_text (str, optional): The bottom text of the meme. Defaults to "".

    Returns:
        Meme: A new Meme object.
    """
    return Meme(image_path, top_text, bottom_text)

def create_first4chan_meme_on_pump(image_path: str, pump_number: int, top_text: str = "", bottom_text: str = "") -> First4chanMemeOnPump:
    """
    Creates a new First4chanMemeOnPump object.

    Args:
        image_path (str): The path to the meme image.
        pump_number (int): The pump number associated with the meme.
        top_text (str, optional): The top text of the meme. Defaults to "".
        bottom_text (str, optional): The bottom text of the meme. Defaults to "".

    Returns:
        First4chanMemeOnPump: A new First4chanMemeOnPump object.
    """
    return First4chanMemeOnPump(image_path, pump_number, top_text, bottom_text)

# Example usage
if __name__ == "__main__":
    try:
        meme = create_meme("path/to/image.jpg", "Top text", "Bottom text")
        meme.save("output.jpg")

        first4chan_meme = create_first4chan_meme_on_pump("path/to/image.jpg", 1, "Top text", "Bottom text")
        print(first4chan_meme)
    except InvalidMemeError as e:
        print(f"Error: {e}")
```
