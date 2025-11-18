"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ramdigi.com
Prompt: Create a script to automate the generation of business cards using client-provided data, ensuring compatibility with digital offset printing processes described on Ram Digi's website.
Generated: DETERMINISTIC_a0a17126aefd18a7
Batch ID: 20250612_151308
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
import json

# Configuration constants
OUTPUT_DIRECTORY = "business_cards"
CARD_DIMENSIONS = (1050, 600)  # Dimensions in pixels for 3.5 x 2 inches at 300 DPI
FONT_PATH = "fonts/arial.ttf"  # Update this path to a valid .ttf font file
FONT_SIZE = 40
MARGIN = 50  # Margin around the card
BACKGROUND_COLOR = (255, 255, 255)  # White background
TEXT_COLOR = (0, 0, 0)  # Black text

# Ensure output directory exists
os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

def generate_business_card(data):
    """
    Generates a business card based on the provided client data.

    :param data: Dictionary containing client data. Expected keys:
                 'name', 'title', 'phone', 'email', 'address'.
    """
    try:
        # Create blank card image
        card = Image.new("RGB", CARD_DIMENSIONS, BACKGROUND_COLOR)
        draw = ImageDraw.Draw(card)

        # Load font
        try:
            font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
        except IOError:
            raise FileNotFoundError(f"Font file not found at {FONT_PATH}. Update the FONT_PATH to a valid .ttf file.")

        # Determine text placement
        text_lines = [
            f"Name: {data['name']}",
            f"Title: {data['title']}",
            f"Phone: {data['phone']}",
            f"Email: {data['email']}",
            f"Address: {data['address']}"
        ]
        y_offset = MARGIN
        for line in text_lines:
            draw.text((MARGIN, y_offset), line, fill=TEXT_COLOR, font=font)
            y_offset += FONT_SIZE + 10  # Add padding between lines

        # Save the card to output directory
        output_path = os.path.join(OUTPUT_DIRECTORY, f"{data['name'].replace(' ', '_')}_card.png")
        card.save(output_path, "PNG")
        print(f"Business card successfully saved to: {output_path}")

    except Exception as e:
        print(f"Error generating business card: {e}")

def main():
    """
    Main function to read client data and generate business cards.
    """
    # Sample input file containing business card data
    input_file = "client_data.json"  # Ensure this file is available with proper JSON structure

    try:
        # Load client data from JSON file
        with open(input_file, "r") as file:
            clients_data = json.load(file)

        # Ensure data is in list format
        if not isinstance(clients_data, list):
            raise ValueError("Input JSON must contain a list of client data.")

        # Generate cards for each client
        for client_data in clients_data:
            generate_business_card(client_data)

    except FileNotFoundError:
        print(f"Input file '{input_file}' not found. Ensure the file exists.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from file '{input_file}'. Ensure it contains valid JSON.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
```

**Note:** Ensure the `client_data.json` file exists and contains a list of dictionaries with the expected keys: `name`, `title`, `phone`, `email`, and `address`. Also, update the `FONT_PATH` to point to a valid `.ttf` file for rendering text.
