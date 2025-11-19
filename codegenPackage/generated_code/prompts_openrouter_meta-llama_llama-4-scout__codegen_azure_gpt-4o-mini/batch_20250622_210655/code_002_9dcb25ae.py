"""
Generated Code Metadata:
========================
Original URL: https://thumbsmaker.com
Prompt: Write a Python script to automate the process of creating custom YouTube thumbnails using the ThumbsMaker design strategy, including a consultation and concept phase.
Generated: DETERMINISTIC_9dcb25ae238241b6
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import requests
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

class ThumbsMaker:
    def __init__(self, title, subtitle, output_path, font_path='arial.ttf'):
        """
        Initialize the ThumbsMaker with title, subtitle, output path, and font path.

        :param title: Title text for the thumbnail
        :param subtitle: Subtitle text for the thumbnail
        :param output_path: Path to save the generated thumbnail
        :param font_path: Path to the font file to be used
        """
        self.title = title
        self.subtitle = subtitle
        self.output_path = output_path
        self.font_path = font_path
        self.thumbnail_size = (1280, 720)  # Standard YouTube thumbnail size

    def create_thumbnail(self):
        """
        Create a custom YouTube thumbnail with the specified title and subtitle.
        """
        try:
            # Create a blank image with a white background
            thumbnail = Image.new('RGB', self.thumbnail_size, 'white')
            draw = ImageDraw.Draw(thumbnail)

            # Load fonts
            title_font = ImageFont.truetype(self.font_path, 80)
            subtitle_font = ImageFont.truetype(self.font_path, 40)

            # Calculate text size and position
            title_size = draw.textsize(self.title, font=title_font)
            subtitle_size = draw.textsize(self.subtitle, font=subtitle_font)

            title_position = ((self.thumbnail_size[0] - title_size[0]) // 2, (self.thumbnail_size[1] - title_size[1]) // 4)
            subtitle_position = ((self.thumbnail_size[0] - subtitle_size[0]) // 2, (self.thumbnail_size[1] - subtitle_size[1]) // 2)

            # Draw text on the thumbnail
            draw.text(title_position, self.title, fill='black', font=title_font)
            draw.text(subtitle_position, self.subtitle, fill='black', font=subtitle_font)

            # Save the thumbnail
            thumbnail.save(self.output_path)
            print(f'Thumbnail saved to {self.output_path}')

        except Exception as e:
            print(f'Error creating thumbnail: {e}')

def main():
    # User input for thumbnail details
    title = input("Enter the title for the thumbnail: ")
    subtitle = input("Enter the subtitle for the thumbnail: ")
    output_path = input("Enter the output path for the thumbnail (e.g., thumbnail.png): ")

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Create an instance of ThumbsMaker and generate the thumbnail
    thumbnail_maker = ThumbsMaker(title, subtitle, output_path)
    thumbnail_maker.create_thumbnail()

if __name__ == '__main__':
    main()
```

### Requirements:
- Install the Pillow library for image processing:
```bash
pip install Pillow
```

### Note:
- Ensure you have a valid font file (e.g., `arial.ttf`) in the same directory or provide the correct path to a font file in the `font_path` parameter.
