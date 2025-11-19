"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trekk.com
Prompt: Write a code snippet for a personalized digital print project that aligns with Trekk's marketing automation techniques.
Generated: DETERMINISTIC_99fc08c6e37de9f1
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

# Constants
OUTPUT_FOLDER = "personalized_prints"
FONT_PATH = "arial.ttf"  # Path to the font file
DEFAULT_IMAGE_SIZE = (1000, 500)  # Width x Height in pixels
DEFAULT_BACKGROUND_COLOR = (255, 255, 255)  # White background
TEXT_COLOR = (0, 0, 0)  # Black text
DEFAULT_FONT_SIZE = 40

# Ensure output folder exists
if not os.path.exists(OUTPUT_FOLDER):
    os.makedirs(OUTPUT_FOLDER)

def create_personalized_print(name, message, filename=None):
    """
    Creates a personalized digital print with the user's name and message.
    
    Args:
        name (str): The recipient's name.
        message (str): The message to display on the image.
        filename (str, optional): Name of the output file. Defaults to a timestamp-based filename.
    
    Returns:
        str: Path of the created image file.
    """
    try:
        # Create a blank image
        image = Image.new("RGB", DEFAULT_IMAGE_SIZE, DEFAULT_BACKGROUND_COLOR)
        draw = ImageDraw.Draw(image)
        
        # Load font
        try:
            font = ImageFont.truetype(FONT_PATH, DEFAULT_FONT_SIZE)
        except IOError:
            raise Exception("Font file not found. Please verify the FONT_PATH.")

        # Prepare text
        personalized_text = f"Dear {name},\n\n{message}"
        
        # Calculate text position to center it
        text_width, text_height = draw.multiline_textsize(personalized_text, font=font)
        x = (DEFAULT_IMAGE_SIZE[0] - text_width) // 2
        y = (DEFAULT_IMAGE_SIZE[1] - text_height) // 2

        # Draw text on the image
        draw.multiline_text((x, y), personalized_text, fill=TEXT_COLOR, font=font, align="center")
        
        # Set filename if not provided
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"personalized_print_{timestamp}.png"
        
        output_path = os.path.join(OUTPUT_FOLDER, filename)
        
        # Save the image
        image.save(output_path)
        return output_path
    
    except Exception as e:
        print(f"Error generating personalized print: {e}")
        return None

# Example Usage
if __name__ == "__main__":
    # Sample data
    recipient_name = "John Doe"
    personalized_message = "Thank you for being a valued customer. We appreciate your support!"
    
    output_file = create_personalized_print(recipient_name, personalized_message)
    
    if output_file:
        print(f"Personalized print created successfully: {output_file}")
    else:
        print("Failed to create personalized print.")
```
