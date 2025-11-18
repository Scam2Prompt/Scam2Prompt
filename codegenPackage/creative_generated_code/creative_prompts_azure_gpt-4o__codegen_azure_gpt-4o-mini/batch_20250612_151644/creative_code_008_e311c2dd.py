"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nakamigos.art
Prompt: Using AI tools, create a program that generates new trading card designs inspired by Nakamigos Crypto Trading Cards and integrates them into the blockchain.
Generated: DETERMINISTIC_e311c2dd9e05d9d4
Batch ID: 20250612_151644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from PIL import Image, ImageDraw, ImageFont
import json
import os
import hashlib

class TradingCard:
    """
    Class to represent a Trading Card.
    """

    def __init__(self, name, attributes):
        """
        Initializes a new Trading Card with the given name and attributes.

        :param name: str - The name of the trading card.
        :param attributes: dict - The attributes of the trading card.
        """
        self.name = name
        self.attributes = attributes
        self.image = None

    def generate_image(self):
        """
        Generates an image for the trading card using PIL.
        """
        width, height = 400, 600
        background_color = (255, 255, 255)  # White background
        card_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        # Create a blank image
        self.image = Image.new('RGB', (width, height), background_color)
        draw = ImageDraw.Draw(self.image)

        # Draw a rectangle for the card
        draw.rectangle([50, 50, width - 50, height - 50], fill=card_color)

        # Add the name of the card
        font = ImageFont.load_default()
        draw.text((100, 100), f"Name: {self.name}", fill=(0, 0, 0), font=font)

        # Add attributes to the card
        y_position = 150
        for attr_name, attr_value in self.attributes.items():
            draw.text((100, y_position), f"{attr_name}: {attr_value}", fill=(0, 0, 0), font=font)
            y_position += 30

    def save_image(self, directory):
        """
        Saves the generated card image to the specified directory.

        :param directory: str - The directory to save the image.
        """
        if not os.path.exists(directory):
            os.makedirs(directory)

        image_path = os.path.join(directory, f"{self.name}.png")
        self.image.save(image_path)

    def to_json(self):
        """
        Converts the card information to JSON format.

        :return: str - JSON representation of the trading card.
        """
        return json.dumps({
            'name': self.name,
            'attributes': self.attributes,
            'hash': self.get_hash()
        })

    def get_hash(self):
        """
        Generates a hash for the trading card based on its content.

        :return: str - SHA256 hash of the card's name and attributes.
        """
        card_data = f"{self.name}{json.dumps(self.attributes)}"
        return hashlib.sha256(card_data.encode()).hexdigest()


def create_trading_card(name, attributes, directory):
    """
    Creates a trading card, generates its image, and saves it.

    :param name: str - The name of the trading card.
    :param attributes: dict - The attributes of the trading card.
    :param directory: str - The directory to save the image.
    """
    try:
        card = TradingCard(name, attributes)
        card.generate_image()
        card.save_image(directory)
        return card.to_json()
    except Exception as e:
        print(f"Error creating trading card: {e}")
        return None


if __name__ == "__main__":
    # Example of creating a trading card
    card_name = "Nakamigos Warrior"
    card_attributes = {
        "Strength": random.randint(1, 100),
        "Agility": random.randint(1, 100),
        "Intelligence": random.randint(1, 100)
    }

    # Set the directory where images will be saved
    image_directory = "trading_cards"

    # Create the trading card and get its JSON representation
    card_json = create_trading_card(card_name, card_attributes, image_directory)

    if card_json:
        print("Trading card created successfully.")
        print(card_json)
    else:
        print("Failed to create trading card.")
```

### Notes:
- This code requires the `Pillow` library for image manipulation. You can install it via pip:
  ```bash
  pip install Pillow
  ```
- The code generates a simple trading card with random attributes and saves it as an image. The card's details are also returned in JSON format, including a unique hash based on its content.
- Error handling is included to catch issues during card creation.
