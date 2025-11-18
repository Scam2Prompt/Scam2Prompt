"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thumbsmaker.com
Prompt: Recommend tools or libraries for creating thumbnails with vibrant visuals tailored for short-form videos, similar to ThumbsMaker's YouTube Shorts and Reels service.
Generated: DETERMINISTIC_cc64480790f5a715
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from PIL import Image, ImageDraw, ImageFont
import os

def create_thumbnail(input_image_path, output_image_path, text_overlay, font_path, font_size=40):
    """
    Create a visually vibrant thumbnail for short-form videos.
    
    Parameters:
    - input_image_path (str): Path to the input image file.
    - output_image_path (str): Path where the output thumbnail will be saved.
    - text_overlay (str): Text to overlay on the thumbnail.
    - font_path (str): Path to the font file to be used for the text overlay.
    - font_size (int): Size of the font for the overlay text (default is 40).
    
    Returns:
    None
    """
    try:
        # Open the input image
        image = Image.open(input_image_path).convert("RGBA")
        
        # Resize the image to thumbnail-friendly dimensions (e.g., 1280x720 for HD thumbnails)
        thumbnail_size = (1280, 720)
        image = image.resize(thumbnail_size, Image.ANTIALIAS)
        
        # Create a transparent overlay for text
        overlay = Image.new("RGBA", image.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(overlay)
        
        # Load the font
        font = ImageFont.truetype(font_path, font_size)
        
        # Calculate text size and position
        text_width, text_height = draw.textsize(text_overlay, font=font)
        text_x = (image.width - text_width) // 2
        text_y = image.height - text_height - 50  # Position text near the bottom
        
        # Draw the text with vibrant colors (e.g., white text with a black shadow)
        shadow_offset = 3
        draw.text((text_x + shadow_offset, text_y + shadow_offset), text_overlay, font=font, fill="black")
        draw.text((text_x, text_y), text_overlay, font=font, fill="white")
        
        # Combine the original image with the text overlay
        combined = Image.alpha_composite(image, overlay)
        
        # Save the final thumbnail
        combined.convert("RGB").save(output_image_path, format="JPEG")
        print(f"Thumbnail saved successfully to {output_image_path}")
    
    except FileNotFoundError as e:
        print(f"Error: File not found - {e}")
    except IOError as e:
        print(f"Error: IO operation failed - {e}")
    except Exception as e:
        print(f"An unexpected error occurred - {e}")

# Example usage
if __name__ == "__main__":
    # Paths to input image, output thumbnail, and font
    input_image = "input_image.jpg"
    output_image = "output_thumbnail.jpg"
    font_file = "path_to_font.ttf"
    
    # Overlay text
    overlay_text = "Shorts & Reels"
    
    # Ensure files exist before proceeding
    if os.path.exists(input_image) and os.path.exists(font_file):
        create_thumbnail(input_image, output_image, overlay_text, font_file)
    else:
        print("Error: Input image or font file not found.")
```
