"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anshsofttech.com
Prompt: Recommend APIs or libraries for creating retina-ready images and text for web applications, inspired by Ansh Soft Tech's focus on vibrant and crisp visuals.
Generated: DETERMINISTIC_5e44b6a788075606
Batch ID: 20250612_151835
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script recommends APIs or libraries for creating retina-ready images and text in web applications.
It showcases techniques using the Pillow library for image manipulation and Cairo for text rendering.
Both libraries are widely used for producing vibrant and high-quality visuals.
"""

from PIL import Image, ImageDraw, ImageFont
import cairo
import os

# Generates a retina-ready image
def create_retina_image(output_path, width=1000, height=1000, scale_factor=2):
    """
    Creates a retina-ready image using the Pillow library.

    Parameters:
    - output_path (str): Path to save the image file.
    - width (int): Width of the image in pixels.
    - height (int): Height of the image in pixels.
    - scale_factor (int): Factor to scale image for retina displays.
    """
    try:
        # Create a blank image with high resolution
        image = Image.new("RGB", (width * scale_factor, height * scale_factor), "white")
        draw = ImageDraw.Draw(image)

        # Load a font (ensure the path is correct or use default PIL fonts)
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        if not os.path.exists(font_path):
            raise FileNotFoundError("Font file not found. Please provide a valid font path.")
        font = ImageFont.truetype(font_path, size=50 * scale_factor)

        # Draw vibrant visuals
        draw.rectangle([(50 * scale_factor, 50 * scale_factor), (600 * scale_factor, 400 * scale_factor)], fill="blue")
        draw.text((100 * scale_factor, 100 * scale_factor), "Retina Ready!", font=font, fill="white")

        # Downscale the image for normal viewing
        image = image.resize((width, height), Image.ANTIALIAS)
        image.save(output_path)
        print(f"Retina-ready image saved at {output_path}")
    except Exception as e:
        print(f"Error creating retina image: {e}")


# Generates retina-ready text using Cairo
def create_retina_text(output_path, text="Retina Ready", width=800, height=400, scale_factor=2):
    """
    Creates retina-ready text using the Cairo library.

    Parameters:
    - output_path (str): Path to save the text image file.
    - text (str): Text to render.
    - width (int): Width of the image canvas.
    - height (int): Height of the image canvas.
    - scale_factor (int): Factor to scale text for retina displays.
    """
    try:
        # High-resolution canvas
        surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width * scale_factor, height * scale_factor)
        context = cairo.Context(surface)

        # Set background color
        context.set_source_rgb(1, 1, 1)  # White background
        context.rectangle(0, 0, width * scale_factor, height * scale_factor)
        context.fill()

        # Set text properties
        context.set_source_rgb(0, 0, 1)  # Blue text
        context.select_font_face("Sans", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD)
        context.set_font_size(50 * scale_factor)

        # Render text
        context.move_to(100 * scale_factor, 200 * scale_factor)
        context.show_text(text)

        # Downscale image for viewing
        scaled_surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, width, height)
        scaled_context = cairo.Context(scaled_surface)
        scaled_context.set_source_surface(surface, 0, 0)
        scaled_context.paint()

        # Save output
        scaled_surface.write_to_png(output_path)
        print(f"Retina-ready text saved at {output_path}")
    except Exception as e:
        print(f"Error creating retina text: {e}")


# Example usage
if __name__ == "__main__":
    # Create retina-ready image
    create_retina_image("retina_image.png")

    # Create retina-ready text
    create_retina_text("retina_text.png")
```
