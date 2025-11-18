"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thumbsmaker.com
Prompt: Create a workflow automation script for managing YouTube Shorts and Reels thumbnail creation, inspired by ThumbsMaker’s process, using design libraries like PIL or Canva API.
Generated: DETERMINISTIC_d57f0f5acc53a235
Batch ID: 20250612_153224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.canva.com/api/v1/templates/{template_id}/thumbnail": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import os
import requests
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants for configuration
THUMBNAIL_WIDTH = 1280
THUMBNAIL_HEIGHT = 720
DEFAULT_FONT_SIZE = 40
THUMBNAIL_OUTPUT_DIR = 'thumbnails'
API_KEY = os.getenv('CANVA_API_KEY')  # Get Canva API key from environment

# Ensure the output directory exists
os.makedirs(THUMBNAIL_OUTPUT_DIR, exist_ok=True)

def create_thumbnail(title: str, output_filename: str) -> None:
    """Creates a thumbnail image with the specified title.

    Args:
        title (str): The title to be displayed on the thumbnail.
        output_filename (str): The name of the file to save the thumbnail.

    Raises:
        ValueError: If the title is empty or too long.
        RuntimeError: If the thumbnail creation fails.
    """
    if not title or len(title) > 50:  # Basic validation
        raise ValueError("Title must be a non-empty string and less than 50 characters.")

    try:
        # Create a blank image
        thumbnail = Image.new('RGB', (THUMBNAIL_WIDTH, THUMBNAIL_HEIGHT), color='white')
        draw = ImageDraw.Draw(thumbnail)

        # Load a default font
        font = ImageFont.load_default()

        # Calculate text size and position
        text_width, text_height = draw.textsize(title, font=font)
        text_x = (THUMBNAIL_WIDTH - text_width) / 2
        text_y = (THUMBNAIL_HEIGHT - text_height) / 2

        # Draw the title on the thumbnail
        draw.text((text_x, text_y), title, fill='black', font=font)

        # Save the thumbnail to the specified output directory
        thumbnail_path = os.path.join(THUMBNAIL_OUTPUT_DIR, output_filename)
        thumbnail.save(thumbnail_path)
        print(f"Thumbnail created successfully: {thumbnail_path}")

    except Exception as e:
        raise RuntimeError(f"Failed to create thumbnail: {e}")

def create_thumbnail_with_canva(template_id: str, output_filename: str) -> None:
    """Creates a thumbnail using Canva API with a specified template.

    Args:
        template_id (str): The ID of the Canva template to use.
        output_filename (str): The name of the file to save the thumbnail.

    Raises:
        RuntimeError: If the API request fails or is unsuccessful.
    """
    try:
        url = f"https://www.canva.com/api/v1/templates/{template_id}/thumbnail"
        headers = {
            'Authorization': f'Bearer {API_KEY}',
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise RuntimeError(f"Canva API error: {response.status_code} - {response.text}")

        with open(os.path.join(THUMBNAIL_OUTPUT_DIR, output_filename), 'wb') as f:
            f.write(response.content)
            print(f"Thumbnail created successfully using Canva: {output_filename}")

    except Exception as e:
        raise RuntimeError(f"Failed to create thumbnail with Canva: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        create_thumbnail("Amazing YouTube Shorts!", "youtube_shorts_thumbnail.png")
        create_thumbnail_with_canva("your_template_id", "canva_thumbnail.png")
    except ValueError as ve:
        print(f"Value Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
```
