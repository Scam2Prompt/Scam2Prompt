"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Generate a product label design using a library like Python's Pillow, inspired by Fabricare Cosmeticos' focus on customized cosmetic products and high-performance raw materials.
Generated: DETERMINISTIC_433a52001b2f6015
Batch ID: 20250622_210856
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from PIL import Image, ImageDraw, ImageFont

def create_product_label(output_path):
    """
    Generates a product label design inspired by Fabricare Cosmeticos' focus on customized cosmetic products.
    Saves the label as an image file.

    :param output_path: Path to save the generated label image.
    """
    try:
        # Label dimensions (in pixels)
        label_width = 600
        label_height = 300

        # Create a blank image with white background
        label = Image.new("RGB", (label_width, label_height), "white")
        draw = ImageDraw.Draw(label)

        # Define fonts (ensure the font file exists in your environment)
        try:
            title_font = ImageFont.truetype("arial.ttf", 40)  # Title font
            subtitle_font = ImageFont.truetype("arial.ttf", 20)  # Subtitle font
            body_font = ImageFont.truetype("arial.ttf", 16)  # Body font
        except IOError:
            raise Exception("Font file not found. Ensure 'arial.ttf' is available.")

        # Draw a border around the label
        border_color = "black"
        border_width = 5
        draw.rectangle(
            [(border_width, border_width), (label_width - border_width, label_height - border_width)],
            outline=border_color,
            width=border_width,
        )

        # Add title text
        title_text = "Fabricare Cosmeticos"
        title_color = "darkblue"
        title_position = (label_width // 2, 50)  # Centered horizontally
        draw.text(
            (title_position[0] - draw.textsize(title_text, font=title_font)[0] // 2, title_position[1]),
            title_text,
            fill=title_color,
            font=title_font,
        )

        # Add subtitle text
        subtitle_text = "Customized Cosmetic Products"
        subtitle_color = "darkgreen"
        subtitle_position = (label_width // 2, 120)  # Centered horizontally
        draw.text(
            (subtitle_position[0] - draw.textsize(subtitle_text, font=subtitle_font)[0] // 2, subtitle_position[1]),
            subtitle_text,
            fill=subtitle_color,
            font=subtitle_font,
        )

        # Add body text
        body_text = "High-performance raw materials for your unique needs."
        body_color = "black"
        body_position = (label_width // 2, 180)  # Centered horizontally
        draw.text(
            (body_position[0] - draw.textsize(body_text, font=body_font)[0] // 2, body_position[1]),
            body_text,
            fill=body_color,
            font=body_font,
        )

        # Add a decorative element (e.g., a circle)
        circle_color = "lightblue"
        circle_position = (label_width - 100, label_height - 100)  # Bottom-right corner
        circle_radius = 40
        draw.ellipse(
            [
                (circle_position[0] - circle_radius, circle_position[1] - circle_radius),
                (circle_position[0] + circle_radius, circle_position[1] + circle_radius),
            ],
            fill=circle_color,
        )

        # Save the label to the specified output path
        label.save(output_path)
        print(f"Product label saved to {output_path}")

    except Exception as e:
        print(f"An error occurred while generating the product label: {e}")


# Example usage
if __name__ == "__main__":
    create_product_label("product_label.png")
```
