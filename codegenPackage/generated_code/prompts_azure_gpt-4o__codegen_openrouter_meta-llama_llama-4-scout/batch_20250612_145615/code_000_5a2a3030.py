"""
Generated Code Metadata:
========================
Original URL: https://labelmystuff.com
Prompt: Write code to generate a printable template for customized clothing labels, incorporating user input for name, font style, and label size, as described on Labelmystuff.com.
Generated: DETERMINISTIC_5a2a3030a09be6ce
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw, ImageFont

def generate_label(name: str, font_style: str, label_size: tuple) -> Image:
    """
    Generate a printable template for customized clothing labels.

    Args:
    - name (str): The name to be printed on the label.
    - font_style (str): The font style for the name (e.g., 'Arial', 'Times New Roman').
    - label_size (tuple): The size of the label in pixels (width, height).

    Returns:
    - Image: A PIL Image object representing the generated label.
    """

    # Define available font styles
    available_fonts = ['Arial', 'Times New Roman', 'Courier New', 'Helvetica']

    # Check if the requested font style is available
    if font_style not in available_fonts:
        raise ValueError(f"Font style '{font_style}' not available. Available fonts: {available_fonts}")

    # Set the font size based on the label size
    font_size = int(min(label_size) * 0.5)

    try:
        # Load the font
        font = ImageFont.truetype(f"{font_style}.ttf", font_size)
    except OSError:
        raise FileNotFoundError(f"Font '{font_style}' not found.")

    # Create a new image with a white background
    img = Image.new('RGB', label_size, color = (73, 109, 137))
    d = ImageDraw.Draw(img)

    # Calculate the text position to center it
    text_width, text_height = font.getsize(name)
    text_x = (label_size[0] - text_width) / 2
    text_y = (label_size[1] - text_height) / 2

    # Draw the text
    d.text((text_x, text_y), name, font=font, fill=(255, 255, 0))

    return img

def main():
    name = input("Enter the name: ")
    font_style = input("Enter the font style (e.g., Arial, Times New Roman): ")
    label_width = int(input("Enter the label width (in pixels): "))
    label_height = int(input("Enter the label height (in pixels): "))

    try:
        label = generate_label(name, font_style, (label_width, label_height))
        label.save('clothing_label.png')
        print("Label saved as 'clothing_label.png'")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
