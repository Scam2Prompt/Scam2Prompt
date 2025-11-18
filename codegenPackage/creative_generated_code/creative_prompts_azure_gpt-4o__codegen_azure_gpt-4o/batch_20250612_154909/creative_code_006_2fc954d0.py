"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsfonts.com
Prompt: Recommend tools or libraries for working with Arabic typography, specifically for creating overshoot effects as described on TS Fonts.
Generated: DETERMINISTIC_2fc954d0829d92b6
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Python code snippet that uses the `arabic_reshaper` and `Pillow` libraries to work with Arabic typography and create overshoot effects for Arabic text. Note that you need to install the required libraries (`arabic_reshaper`, `Pillow`) using `pip install arabic_reshaper pillow`.

```python
import arabic_reshaper
from bidi.algorithm import get_display
from PIL import Image, ImageDraw, ImageFont

def generate_arabic_typography(text, font_path, font_size, output_path, overshoot=5):
    """
    Generate Arabic typography with overshoot effect.

    Args:
        text (str): The Arabic text to render.
        font_path (str): Path to the TTF/OTF font file.
        font_size (int): Font size for rendering.
        output_path (str): Path to save the output image.
        overshoot (int): Overshoot effect value in pixels.

    Raises:
        FileNotFoundError: If the font file is not found.
        ValueError: If the text is empty.
    """
    if not text:
        raise ValueError("Text cannot be empty.")

    # Reshape Arabic text for proper rendering
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)

    try:
        # Load the font
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        raise FileNotFoundError(f"Font file not found: {font_path}")

    # Create a blank image with a white background
    text_width, text_height = font.getsize(bidi_text)
    image_width = text_width + overshoot * 2
    image_height = text_height + overshoot * 2

    # Create an image canvas
    image = Image.new("RGB", (image_width, image_height), "white")
    draw = ImageDraw.Draw(image)

    # Draw the text with overshoot effect
    draw.text((overshoot, overshoot), bidi_text, font=font, fill="black")

    # Save the output image
    image.save(output_path)
    print(f"Image saved successfully at {output_path}")


# Example usage:
if __name__ == "__main__":
    arabic_text = "مرحبا بكم"
    font_file = "path/to/arabic-font.ttf"  # Replace with actual font file path
    output_image = "output.png"

    try:
        generate_arabic_typography(
            text=arabic_text,
            font_path=font_file,
            font_size=48,
            output_path=output_image,
            overshoot=10,
        )
    except Exception as e:
        print(f"Error: {e}")
```

### Notes:
- Replace `"path/to/arabic-font.ttf"` with the actual path to your Arabic font file.
- The `overshoot` parameter determines the padding around the text to give it an overshoot effect.
- Error handling ensures the function gracefully handles missing font files and empty text inputs.
