"""
Generated Code Metadata:
========================
Original URL: https://taramediaworks.com
Prompt: "Design a graphic for a social media post promoting a digital marketing service, including key elements and best practices."
Generated: DETERMINISTIC_9da94176b7f32624
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here is the Python code using the `Pillow` library to create a graphic for a social media post promoting a digital marketing service:

```python
from PIL import Image, ImageDraw, ImageFont
import os

def create_social_media_graphic(output_path="social_media_post.png"):
    try:
        # Define image dimensions and colors
        width, height = 1080, 1080  # Square image for social media
        background_color = (255, 255, 255)  # White background
        primary_color = (0, 123, 255)  # Blue for accents
        text_color = (0, 0, 0)  # Black text

        # Create a blank image
        image = Image.new("RGB", (width, height), background_color)
        draw = ImageDraw.Draw(image)

        # Load fonts (ensure the font file exists in the working directory)
        try:
            title_font = ImageFont.truetype("arial.ttf", 80)  # Title font
            subtitle_font = ImageFont.truetype("arial.ttf", 40)  # Subtitle font
            body_font = ImageFont.truetype("arial.ttf", 30)  # Body font
        except IOError:
            raise FileNotFoundError("Font file not found. Ensure 'arial.ttf' is available.")

        # Add title text
        title_text = "Boost Your Business!"
        title_width, title_height = draw.textsize(title_text, font=title_font)
        draw.text(((width - title_width) / 2, 100), title_text, fill=primary_color, font=title_font)

        # Add subtitle text
        subtitle_text = "Expert Digital Marketing Services"
        subtitle_width, subtitle_height = draw.textsize(subtitle_text, font=subtitle_font)
        draw.text(((width - subtitle_width) / 2, 250), subtitle_text, fill=text_color, font=subtitle_font)

        # Add body text
        body_text = (
            "✔ Increase your online presence\n"
            "✔ Drive more traffic to your website\n"
            "✔ Convert leads into customers\n"
            "Contact us today to get started!"
        )
        body_lines = body_text.split("\n")
        y_offset = 400
        for line in body_lines:
            line_width, line_height = draw.textsize(line, font=body_font)
            draw.text(((width - line_width) / 2, y_offset), line, fill=text_color, font=body_font)
            y_offset += line_height + 10

        # Add a call-to-action button
        button_text = "Learn More"
        button_width, button_height = draw.textsize(button_text, font=subtitle_font)
        button_x = (width - button_width) / 2
        button_y = y_offset + 50
        button_padding = 20

        # Draw button background
        draw.rectangle(
            [button_x - button_padding, button_y - button_padding,
             button_x + button_width + button_padding, button_y + button_height + button_padding],
            fill=primary_color
        )

        # Draw button text
        draw.text((button_x, button_y), button_text, fill=background_color, font=subtitle_font)

        # Save the image
        image.save(output_path)
        print(f"Social media graphic saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function to create the graphic
create_social_media_graphic()
```

### Notes:
- Ensure the `Pillow` library is installed (`pip install pillow`).
- Place the `arial.ttf` font file in the working directory or update the font path to a valid font file on your system.
- The generated image will be saved as `social_media_post.png` in the current directory.
