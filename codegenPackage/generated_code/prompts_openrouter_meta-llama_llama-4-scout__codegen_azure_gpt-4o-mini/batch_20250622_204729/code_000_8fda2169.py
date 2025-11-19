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
import os
from PIL import Image, ImageDraw, ImageFont
import json

class BusinessCardGenerator:
    def __init__(self, config_file):
        """
        Initialize the BusinessCardGenerator with configuration settings.

        :param config_file: Path to the JSON configuration file containing card sizes and layouts.
        """
        self.config = self.load_config(config_file)
        self.font_path = "arial.ttf"  # Default font path, can be changed as needed

    def load_config(self, config_file):
        """
        Load the configuration from a JSON file.

        :param config_file: Path to the JSON configuration file.
        :return: Parsed JSON configuration as a dictionary.
        """
        try:
            with open(config_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            raise ValueError(f"Error loading configuration: {e}")

    def create_business_card(self, name, title, company, contact_info, layout, output_file):
        """
        Create a business card image based on the provided details and layout.

        :param name: Name of the individual.
        :param title: Job title of the individual.
        :param company: Company name.
        :param contact_info: Contact information (phone, email, etc.).
        :param layout: Layout settings for the business card.
        :param output_file: Path to save the generated business card image.
        """
        width, height = layout['size']
        card_image = Image.new('RGB', (width, height), color='white')
        draw = ImageDraw.Draw(card_image)

        # Load font
        try:
            font = ImageFont.truetype(self.font_path, layout['font_size'])
        except IOError:
            raise ValueError("Font file not found. Please check the font path.")

        # Draw text on the card
        draw.text((layout['name_position'][0], layout['name_position'][1]), name, fill='black', font=font)
        draw.text((layout['title_position'][0], layout['title_position'][1]), title, fill='black', font=font)
        draw.text((layout['company_position'][0], layout['company_position'][1]), company, fill='black', font=font)
        draw.text((layout['contact_position'][0], layout['contact_position'][1]), contact_info, fill='black', font=font)

        # Save the generated card
        card_image.save(output_file)
        print(f"Business card saved to {output_file}")

def main():
    # Configuration file path
    config_file = 'business_card_config.json'
    
    # Create an instance of the BusinessCardGenerator
    generator = BusinessCardGenerator(config_file)

    # Example business card details
    name = "John Doe"
    title = "Software Engineer"
    company = "Ram Digi Medias Pvt Ltd"
    contact_info = "Phone: 123-456-7890\nEmail: john.doe@example.com"

    # Select layout from configuration
    layout = generator.config['layouts'][0]  # Example: using the first layout

    # Output file path
    output_file = 'business_card.png'

    # Generate the business card
    generator.create_business_card(name, title, company, contact_info, layout, output_file)

if __name__ == "__main__":
    main()
```

**Note:** Ensure you have a valid `business_card_config.json` file with the appropriate structure and a valid font file (`arial.ttf`) in the same directory or adjust the path accordingly. The JSON configuration file should contain card sizes and layouts, for example:

```json
{
    "layouts": [
        {
            "size": [350, 200],
            "font_size": 20,
            "name_position": [20, 20],
            "title_position": [20, 60],
            "company_position": [20, 100],
            "contact_position": [20, 140]
        }
    ]
}
```
