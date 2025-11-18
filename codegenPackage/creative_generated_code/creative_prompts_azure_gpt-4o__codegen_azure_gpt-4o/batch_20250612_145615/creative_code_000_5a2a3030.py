"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://labelmystuff.com
Prompt: Write code to generate a printable template for customized clothing labels, incorporating user input for name, font style, and label size, as described on Labelmystuff.com.
Generated: DETERMINISTIC_5a2a3030a09be6ce
Batch ID: 20250612_145615
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

def create_clothing_label(name, font_style, label_size):
    """
    Generates a printable template for a customized clothing label.

    Args:
        name (str): The name to display on the label.
        font_style (str): Path to the .ttf font file for the desired font style.
        label_size (tuple): Size of the label in pixels (width, height).

    Raises:
        FileNotFoundError: If the specified font file does not exist.
        ValueError: If the label size is invalid.
    """

    # Validate label size
    if len(label_size) != 2 or not all(isinstance(dim, int) and dim > 0 for dim in label_size):
        raise ValueError("Label size must be a tuple of two positive integers (width, height).")

    # Check if font file exists
    if not os.path.exists(font_style):
        raise FileNotFoundError(f"Font file '{font_style}' not found.")

    # Create a blank image with a white background
    label = Image.new("RGB", label_size, "white")
    draw = ImageDraw.Draw(label)

    # Load the font
    try:
        font = ImageFont.truetype(font_style, size=min(label_size) // 5)  # Font size is relative to label size
    except Exception as e:
        raise Exception(f"Error loading font: {e}")

    # Calculate text size and position
    text_width, text_height = draw.textsize(name, font=font)
    text_x = (label_size[0] - text_width) // 2
    text_y = (label_size[1] - text_height) // 2

    # Draw the name onto the label
    draw.text((text_x, text_y), name, fill="black", font=font)

    return label


def save_label(label, output_path):
    """
    Saves the generated label image to the specified output path.

    Args:
        label (Image.Image): The label image to save.
        output_path (str): The file path to save the label image.

    Raises:
        ValueError: If output_path is not a valid string.
    """
    if not isinstance(output_path, str) or not output_path.strip():
        raise ValueError("Output path must be a valid, non-empty string.")

    try:
        label.save(output_path)
    except Exception as e:
        raise Exception(f"Error saving label: {e}")


def main():
    """
    Main function to interact with the user and generate a clothing label.
    """
    print("Welcome to the Clothing Label Generator!")

    # Get user inputs
    name = input("Enter the name to display on the label: ").strip()
    font_style = input("Enter the path to the .ttf font file: ").strip()
    label_width = int(input("Enter the label width in pixels: "))
    label_height = int(input("Enter the label height in pixels: "))
    output_path = input("Enter the output file path (e.g., label.png): ").strip()

    # Create and save the label
    try:
        label = create_clothing_label(name, font_style, (label_width, label_height))
        save_label(label, output_path)
        print(f"Label successfully created and saved at {output_path}.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
