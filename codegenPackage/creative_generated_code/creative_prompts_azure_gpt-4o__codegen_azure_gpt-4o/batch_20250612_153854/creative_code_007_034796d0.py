"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monadmakeyournft.vercel.app
Prompt: Recommend a framework or library to implement text effects and font styling (e.g., Verdana, Impact) on a drawing canvas for an NFT creation tool like Monad Whiteboard NFT.
Generated: DETERMINISTIC_034796d0b23ae83e
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python script using Pillow (PIL) library to implement text effects and font styling
# on a drawing canvas for an NFT creation tool.

from PIL import Image, ImageDraw, ImageFont
import os

def create_text_image(canvas_size=(800, 600), text="Monad NFT", font_path="arial.ttf",
                      font_size=60, font_color="blue", background_color="white",
                      output_path="nft_text_image.png"):
    """
    Create an image with styled text on a canvas.

    Args:
        canvas_size (tuple): Size of the canvas (width, height).
        text (str): Text to display on the canvas.
        font_path (str): Path to the font file (e.g., .ttf).
        font_size (int): Size of the font.
        font_color (str or tuple): Color of the font (e.g., "blue" or (255, 0, 0)).
        background_color (str or tuple): Background color of the canvas.
        output_path (str): Path to save the generated image.

    Returns:
        None. Saves the image to the specified output path.
    """
    try:
        # Create a blank image with the specified background color
        image = Image.new("RGB", canvas_size, background_color)

        # Initialize the drawing context
        draw = ImageDraw.Draw(image)

        # Load the font
        if not os.path.exists(font_path):
            raise FileNotFoundError(f"Font file not found at path: {font_path}")
        font = ImageFont.truetype(font_path, font_size)

        # Calculate text position to center it on the canvas
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (canvas_size[0] - text_width) // 2
        text_y = (canvas_size[1] - text_height) // 2

        # Draw the text with styling
        draw.text((text_x, text_y), text, font=font, fill=font_color)

        # Save the image to the output path
        image.save(output_path)
        print(f"Image saved successfully to {output_path}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Ensure you specify a valid font path (download if needed)
    create_text_image(canvas_size=(800, 600), text="Monad NFT",
                      font_path="arial.ttf", font_size=72, font_color="black",
                      background_color="white", output_path="nft_text_image.png")
```

> **Note:** Replace `"arial.ttf"` with a valid path to a `.ttf` font file available on your system. You can download fonts (e.g., Verdana, Impact) and provide their paths.
