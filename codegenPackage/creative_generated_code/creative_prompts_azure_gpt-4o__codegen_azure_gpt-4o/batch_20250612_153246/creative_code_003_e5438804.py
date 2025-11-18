"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lagraveusenormande.fr
Prompt: Develop a program to create laser engraving designs for wedding place cards or baptism plaques, referencing the customization options mentioned on "La Graveuse Normande."
Generated: DETERMINISTIC_e5438804180e03f7
Batch ID: 20250612_153246
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

# Define constants for the design
OUTPUT_DIRECTORY = "engraved_designs"
FONT_PATH = "path/to/your/font.ttf"  # Replace with the path to your font file
IMAGE_SIZE = (800, 400)  # Width, Height in pixels
BACKGROUND_COLOR = (255, 255, 255)  # White background
TEXT_COLOR = (0, 0, 0)  # Black text
DEFAULT_FONT_SIZE = 40

# Create output directory if it doesn't exist
if not os.path.exists(OUTPUT_DIRECTORY):
    os.makedirs(OUTPUT_DIRECTORY)


def create_design(name: str, event: str, custom_message: str, font_size: int = DEFAULT_FONT_SIZE):
    """
    Creates a laser engraving design for a specific name and event.
    
    Args:
        name (str): Name of the person for whom the design is created.
        event (str): The event (e.g., "Wedding", "Baptism").
        custom_message (str): Custom message to appear on the design.
        font_size (int, optional): Font size for the text. Defaults to DEFAULT_FONT_SIZE.

    Returns:
        str: Path to the saved design image.
    """
    try:
        # Initialize the image
        img = Image.new("RGB", IMAGE_SIZE, BACKGROUND_COLOR)
        draw = ImageDraw.Draw(img)

        # Load the font
        try:
            font = ImageFont.truetype(FONT_PATH, font_size)
        except IOError:
            raise Exception(f"Font not found at {FONT_PATH}. Please check the path.")

        # Prepare text to engrave
        text_lines = [
            f"Event: {event}",
            f"Name: {name}",
            f"Message: {custom_message}"
        ]

        # Calculate text positioning for centering
        y_position = 50  # Starting Y position
        for line in text_lines:
            text_width, text_height = draw.textsize(line, font=font)
            x_position = (IMAGE_SIZE[0] - text_width) // 2
            draw.text((x_position, y_position), line, fill=TEXT_COLOR, font=font)
            y_position += text_height + 20  # Add spacing between lines

        # Generate the file name and save the image
        file_name = f"{name.lower().replace(' ', '_')}_{event.lower().replace(' ', '_')}.png"
        file_path = os.path.join(OUTPUT_DIRECTORY, file_name)
        img.save(file_path)

        return file_path

    except Exception as e:
        print(f"Error creating design: {e}")
        return None


def main():
    """
    Main function to demonstrate laser engraving designs creation.
    """
    print("Welcome to the Laser Engraving Design Generator!")

    # Collect user inputs
    name = input("Enter the name for the design: ")
    event = input("Enter the event (e.g., Wedding, Baptism): ")
    custom_message = input("Enter a custom message: ")

    # Generate the design
    print("Generating your design...")
    design_path = create_design(name, event, custom_message)

    if design_path:
        print(f"Design created successfully! Saved at: {design_path}")
    else:
        print("Failed to create the design. Please try again.")


if __name__ == "__main__":
    main()
```
