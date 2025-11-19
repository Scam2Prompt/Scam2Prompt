"""
Generated Code Metadata:
========================
Original URL: https://crownadvertise.com
Prompt: Design a business card using a template and AI-powered design tools, similar to Crown Advertising's services for Paratha Kabab House Canada.
Generated: DETERMINISTIC_168250e583ac24ff
Batch ID: 20250622_210655
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

class BusinessCard:
    def __init__(self, name, title, phone, email, website, logo_path):
        """
        Initialize the BusinessCard with user details and logo path.

        :param name: Name of the individual
        :param title: Job title of the individual
        :param phone: Phone number
        :param email: Email address
        :param website: Website URL
        :param logo_path: Path to the logo image
        """
        self.name = name
        self.title = title
        self.phone = phone
        self.email = email
        self.website = website
        self.logo_path = logo_path
        self.card_width = 600
        self.card_height = 300
        self.background_color = (255, 255, 255)  # White background
        self.text_color = (0, 0, 0)  # Black text

    def create_card(self):
        """
        Create a business card image and save it to a file.
        """
        try:
            # Create a blank image for the business card
            card = Image.new('RGB', (self.card_width, self.card_height), self.background_color)
            draw = ImageDraw.Draw(card)

            # Load and position the logo
            logo = Image.open(self.logo_path)
            logo.thumbnail((100, 100))  # Resize logo
            card.paste(logo, (20, 20))

            # Define font sizes
            name_font = ImageFont.truetype("arial.ttf", 24)
            title_font = ImageFont.truetype("arial.ttf", 18)
            contact_font = ImageFont.truetype("arial.ttf", 16)

            # Draw text on the card
            draw.text((150, 20), self.name, fill=self.text_color, font=name_font)
            draw.text((150, 60), self.title, fill=self.text_color, font=title_font)
            draw.text((150, 100), f"Phone: {self.phone}", fill=self.text_color, font=contact_font)
            draw.text((150, 130), f"Email: {self.email}", fill=self.text_color, font=contact_font)
            draw.text((150, 160), f"Website: {self.website}", fill=self.text_color, font=contact_font)

            # Save the card to a file
            output_path = "business_card.png"
            card.save(output_path)
            print(f"Business card created successfully: {output_path}")

        except FileNotFoundError as e:
            print(f"Error: {e}. Please check the logo path.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    business_card = BusinessCard(
        name="John Doe",
        title="Owner",
        phone="(123) 456-7890",
        email="john.doe@example.com",
        website="www.parathakababhouse.ca",
        logo_path="path/to/logo.png"  # Update with the actual logo path
    )
    business_card.create_card()
```
