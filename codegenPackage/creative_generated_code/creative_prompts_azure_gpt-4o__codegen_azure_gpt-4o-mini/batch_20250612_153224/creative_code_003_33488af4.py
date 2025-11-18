"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.lords.marketing
Prompt: Suggest tools or libraries for designing eye-catching marketing materials for pubs and bars, and write code to generate sample designs using those tools.
Generated: DETERMINISTIC_33488af408b11879
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from PIL import Image, ImageDraw, ImageFont

# Function to create a promotional poster for a pub or bar
def create_promotional_poster(text, output_file):
    """
    Generates a promotional poster with the given text and saves it to a file.

    Parameters:
    text (str): The promotional text to display on the poster.
    output_file (str): The filename where the poster image will be saved.
    """

    # Define poster dimensions and colors
    width, height = 800, 1200
    background_color = (255, 223, 186)
    text_color = (0, 51, 102)

    try:
        # Create a blank image with the background color
        img = Image.new('RGB', (width, height), background_color)
        draw = ImageDraw.Draw(img)

        # Load a font (ensure the font file is accessible in your environment)
        font_path = "arial.ttf"  # Change to a valid font path as needed
        font_size = 80
        font = ImageFont.truetype(font_path, font_size)

        # Center the text on the poster
        text_width, text_height = draw.textsize(text, font=font)
        text_x = (width - text_width) // 2
        text_y = (height - text_height) // 2

        # Draw the text on the image
        draw.text((text_x, text_y), text, fill=text_color, font=font)

        # Save the poster to the specified file
        img.save(output_file)

        print(f"Promotional poster saved as '{output_file}'")
    except Exception as e:
        print(f"An error occurred while creating the poster: {e}")

# Example usage
if __name__ == "__main__":
    # Define sample promotional texts
    sample_texts = [
        "Happy Hour: 5 PM to 7 PM",
        "Live Music Tonight!",
        "Trivia Night: Win Prizes!",
        "Join Us for Craft Beer Tasting!",
    ]

    # Randomly select a sample text
    selected_text = random.choice(sample_texts)

    # Specify output file name
    output_file = "pub_bar_poster.png"

    # Create promotional poster
    create_promotional_poster(selected_text, output_file)
```

Make sure to install the required library with:
```bash
pip install pillow
```

Also, ensure that the font file (`arial.ttf` or another TTF file) is accessible in your environment when you run the code.
