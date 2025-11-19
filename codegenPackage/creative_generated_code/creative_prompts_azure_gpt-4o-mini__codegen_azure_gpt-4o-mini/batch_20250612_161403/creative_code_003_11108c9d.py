"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsfonts.com
Prompt: Explain how to modify an existing font from TS Fonts to better suit a unique branding project.
Generated: DETERMINISTIC_11108c9d8cbbbb6b
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Importing necessary libraries
from PIL import ImageFont, ImageDraw, Image
import os

def modify_font(input_font_path, output_font_path, new_size=None, new_color=None):
    """
    Modify an existing font to better suit a unique branding project.

    Args:
        input_font_path (str): Path to the existing font file.
        output_font_path (str): Path to save the modified font file.
        new_size (int, optional): New size for the font. If None, the original size is kept.
        new_color (tuple, optional): New color for the font in RGB format (e.g., (255, 0, 0)).
                                      If None, the original color is kept.
    
    Raises:
        IOError: If the input font file cannot be read or written.
        ValueError: If the new size is not a positive integer.
    """
    # Validate inputs
    if new_size is not None and (not isinstance(new_size, int) or new_size <= 0):
        raise ValueError("New size must be a positive integer.")
    
    if not os.path.isfile(input_font_path):
        raise IOError(f"The font file at {input_font_path} does not exist.")
    
    try:
        # Load the existing font
        font = ImageFont.truetype(input_font_path, size=new_size if new_size else 12)

        # Create an image to draw the modified font on
        dummy_image = Image.new('RGB', (100, 50), (255, 255, 255))
        draw = ImageDraw.Draw(dummy_image)
        
        # Set color if specified
        color = new_color if new_color else (0, 0, 0)  # Default to black
        
        # Draw text using the loaded font
        draw.text((10, 10), "Sample Text", font=font, fill=color)

        # Save the modified font representation as an image (for demonstration)
        dummy_image.save(output_font_path)
        print(f"Modified font saved successfully to {output_font_path}")

    except Exception as e:
        raise IOError(f"An error occurred while processing the font: {e}")

# Example usage
# modify_font("path/to/your/font.ttf", "output/font_sample.png", new_size=24, new_color=(255, 0, 0))
```

Make sure to replace `"path/to/your/font.ttf"` with the actual path of your font file when using the function.
