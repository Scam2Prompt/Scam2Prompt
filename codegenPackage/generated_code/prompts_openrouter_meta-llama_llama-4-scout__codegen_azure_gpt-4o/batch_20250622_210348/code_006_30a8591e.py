"""
Generated Code Metadata:
========================
Original URL: https://metis.com.tw
Prompt: "Create a customized label design for a product with specific branding requirements, including a unique shape and printing effects."
Generated: DETERMINISTIC_30a8591e456279fa
Batch ID: 20250622_210348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Certainly! Below is a Python script using the `Pillow` library to create a customized label design with branding requirements, including a unique shape and printing effects.

```python
from PIL import Image, ImageDraw, ImageFont

def create_custom_label(output_path, label_size=(500, 300), shape="ellipse", text="Brand Name", font_path="arial.ttf", font_size=40):
    """
    Creates a customized label design with specific branding requirements.

    Parameters:
        output_path (str): Path to save the generated label image.
        label_size (tuple): Size of the label (width, height).
        shape (str): Shape of the label ("ellipse" or "rectangle").
        text (str): Text to display on the label.
        font_path (str): Path to the font file.
        font_size (int): Size of the font.

    Returns:
        None
    """
    try:
        # Create a blank image with a transparent background
        label = Image.new("RGBA", label_size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(label)

        # Draw the label shape
        if shape == "ellipse":
            draw.ellipse([(0, 0), label_size], fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=5)
        elif shape == "rectangle":
            draw.rectangle([(0, 0), label_size], fill=(255, 255, 255, 255), outline=(0, 0, 0, 255), width=5)
        else:
            raise ValueError("Unsupported shape. Use 'ellipse' or 'rectangle'.")

        # Load the font
        try:
            font = ImageFont.truetype(font_path, font_size)
        except IOError:
            raise FileNotFoundError(f"Font file not found at {font_path}. Please provide a valid font path.")

        # Calculate text position to center it
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (label_size[0] - text_width) // 2
        text_y = (label_size[1] - text_height) // 2

        # Add text to the label
        draw.text((text_x, text_y), text, font=font, fill=(0, 0, 0, 255))

        # Apply a printing effect (e.g., gradient overlay)
        gradient = Image.new("RGBA", label_size, (0, 0, 0, 0))
        gradient_draw = ImageDraw.Draw(gradient)
        for y in range(label_size[1]):
            alpha = int(255 * (y / label_size[1]))
            gradient_draw.line([(0, y), (label_size[0], y)], fill=(255, 215, 0, alpha))
        label = Image.alpha_composite(label, gradient)

        # Save the label to the specified output path
        label.save(output_path, "PNG")
        print(f"Label saved successfully at {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
create_custom_label(
    output_path="custom_label.png",
    label_size=(500, 300),
    shape="ellipse",
    text="Premium Product",
    font_path="arial.ttf",
    font_size=40
)
```

**Note:** Ensure the `Pillow` library is installed (`pip install pillow`) and the `arial.ttf` font file is available in the specified path. Adjust the `font_path` to point to a valid font file on your system.
