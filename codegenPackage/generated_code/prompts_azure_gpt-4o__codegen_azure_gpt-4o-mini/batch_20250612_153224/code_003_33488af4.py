"""
Generated Code Metadata:
========================
Original URL: https://www.lords.marketing
Prompt: Suggest tools or libraries for designing eye-catching marketing materials for pubs and bars, and write code to generate sample designs using those tools.
Generated: DETERMINISTIC_33488af408b11879
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Function to create a sample marketing poster for a pub
def create_pub_poster(title, subtitle, image_path, output_path):
    """
    Generates a marketing poster for a pub or bar.

    Parameters:
    title (str): The main title of the poster.
    subtitle (str): The subtitle or tagline of the poster.
    image_path (str): Path to the background image.
    output_path (str): Path where the generated poster will be saved.
    """
    try:
        # Load the background image
        background = Image.open(image_path)
        width, height = background.size

        # Create a drawing context
        draw = ImageDraw.Draw(background)

        # Define fonts (ensure the font file is available in the working directory)
        title_font = ImageFont.truetype("arial.ttf", 80)
        subtitle_font = ImageFont.truetype("arial.ttf", 40)

        # Calculate text size and position for title
        title_size = draw.textsize(title, font=title_font)
        title_position = ((width - title_size[0]) // 2, height // 4)

        # Calculate text size and position for subtitle
        subtitle_size = draw.textsize(subtitle, font=subtitle_font)
        subtitle_position = ((width - subtitle_size[0]) // 2, height // 2)

        # Draw the title and subtitle on the image
        draw.text(title_position, title, font=title_font, fill="white")
        draw.text(subtitle_position, subtitle, font=subtitle_font, fill="yellow")

        # Save the final poster
        background.save(output_path)
        print(f"Poster saved successfully at {output_path}")

    except FileNotFoundError as e:
        print(f"Error: {e}. Please check the image path.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage
if __name__ == "__main__":
    # Define poster details
    poster_title = "Happy Hour Specials!"
    poster_subtitle = "Join us for drinks and fun!"
    background_image_path = "pub_background.jpg"  # Ensure this image exists
    output_image_path = "pub_poster.png"

    # Create the poster
    create_pub_poster(poster_title, poster_subtitle, background_image_path, output_image_path)
```

### Requirements:
- Ensure you have the `Pillow` library installed for image manipulation:
  ```bash
  pip install Pillow
  ```
- Ensure you have a background image named `pub_background.jpg` in the same directory as the script.
- The font file `arial.ttf` should be available in the working directory or adjust the path to a valid font file on your system.
