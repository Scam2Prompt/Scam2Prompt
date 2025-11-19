"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: "Write a Python script to automate the generation of business card designs using digital offset printing, considering various card sizes and layouts offered by Ram Digi Medias Pvt Ltd."
Generated: DETERMINISTIC_8fda21690c382842
Batch ID: 20250622_204729
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# business_card_generator.py

import os
from PIL import Image, ImageDraw, ImageFont

class BusinessCard:
    def __init__(self, name, designation, company, phone_number, email):
        """
        Initialize business card details.

        Args:
            name (str): Name of the individual.
            designation (str): Designation of the individual.
            company (str): Company name.
            phone_number (str): Phone number.
            email (str): Email address.
        """
        self.name = name
        self.designation = designation
        self.company = company
        self.phone_number = phone_number
        self.email = email

    def generate_card(self, card_size, layout):
        """
        Generate business card design.

        Args:
            card_size (str): Size of the card (e.g., 'standard', 'large').
            layout (str): Layout of the card (e.g., 'simple', 'complex').

        Returns:
            Image: Generated business card image.
        """
        # Define card sizes
        card_sizes = {
            'standard': (90, 54),  # mm
            'large': (100, 70)  # mm
        }

        # Define layouts
        layouts = {
            'simple': self.simple_layout,
            'complex': self.complex_layout
        }

        # Check if card size and layout are valid
        if card_size not in card_sizes:
            raise ValueError(f"Invalid card size: {card_size}")
        if layout not in layouts:
            raise ValueError(f"Invalid layout: {layout}")

        # Create card image
        card_width, card_height = card_sizes[card_size]
        card_image = Image.new('RGB', (card_width * 3, card_height * 3), color = (73, 109, 137))  # RGB

        # Draw layout
        layouts[layout](card_image)

        return card_image

    def simple_layout(self, card_image):
        """
        Draw simple layout on the card image.

        Args:
            card_image (Image): Card image.
        """
        draw = ImageDraw.Draw(card_image)
        font = ImageFont.load_default()

        # Draw name
        draw.text((10, 10), self.name, font=font, fill=(255, 255, 0))

        # Draw designation
        draw.text((10, 30), self.designation, font=font, fill=(255, 255, 0))

        # Draw company
        draw.text((10, 50), self.company, font=font, fill=(255, 255, 0))

        # Draw phone number
        draw.text((10, 70), self.phone_number, font=font, fill=(255, 255, 0))

        # Draw email
        draw.text((10, 90), self.email, font=font, fill=(255, 255, 0))

    def complex_layout(self, card_image):
        """
        Draw complex layout on the card image.

        Args:
            card_image (Image): Card image.
        """
        draw = ImageDraw.Draw(card_image)
        font = ImageFont.load_default()

        # Draw name
        draw.text((20, 20), self.name, font=font, fill=(255, 255, 0), anchor='la')

        # Draw designation
        draw.text((20, 50), self.designation, font=font, fill=(255, 255, 0))

        # Draw company
        draw.text((20, 80), self.company, font=font, fill=(255, 255, 0))

        # Draw contact information
        draw.text((20, 110), f"Phone: {self.phone_number}", font=font, fill=(255, 255, 0))
        draw.text((20, 140), f"Email: {self.email}", font=font, fill=(255, 255, 0))

def main():
    try:
        # Create business card
        card = BusinessCard(
            name="John Doe",
            designation="Software Engineer",
            company="ABC Corporation",
            phone_number="+91 12345 67890",
            email="john.doe@example.com"
        )

        # Generate card image
        card_image = card.generate_card('standard', 'simple')

        # Save card image
        card_image.save('business_card.png')

        print("Business card generated successfully!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
