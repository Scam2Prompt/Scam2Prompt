"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://christineheart.com
Prompt: Write a Python script that automates the posting of travel adventures and Polaroid photos to a blog similar to Christine Heart's.
Generated: DETERMINISTIC_4fee76ca30529021
Batch ID: 20250612_162404
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example-blog-api.com/posts": {
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
from datetime import datetime
from PIL import Image
from io import BytesIO

# Constants for the blog API
BLOG_API_URL = 'https://example-blog-api.com/posts'  # Replace with the actual blog API endpoint
API_KEY = 'your_api_key'  # Replace with your actual API key

# Function to resize and format the Polaroid photo
def process_photo(photo_path):
    """Opens a photo, resizes it, and adds a Polaroid-style border."""
    try:
        # Open the image
        with Image.open(photo_path) as img:
            # Resize image to a Polaroid size
            img = img.resize((600, 600))  # Example size
            # Create a new blank image with white background
            polaroid = Image.new('RGB', (img.width + 20, img.height + 40), 'white')
            # Paste the original image onto the Polaroid background
            polaroid.paste(img, (10, 10))
            # Save the processed image to a BytesIO object
            img_byte_arr = BytesIO()
            polaroid.save(img_byte_arr, format='JPEG')
            img_byte_arr.seek(0)
            return img_byte_arr
    except Exception as e:
        print(f"Error processing photo {photo_path}: {e}")
        return None

# Function to post a travel adventure to the blog
def post_adventure(title, content, photo_path):
    """Posts a travel adventure with an associated photo to the blog."""
    try:
        # Process the photo
        photo = process_photo(photo_path)
        if photo is None:
            print("Photo processing failed. Post will not be created.")
            return

        # Prepare the data for the API request
        post_data = {
            'title': title,
            'content': content,
            'date': datetime.utcnow().isoformat(),
            'api_key': API_KEY
        }
        files = {'photo': ('photo.jpg', photo, 'image/jpeg')}

        # Make the API request to post the adventure
        response = requests.post(BLOG_API_URL, data=post_data, files=files)

        # Check for HTTP errors
        response.raise_for_status()

        print(f"Post created successfully: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    adventure_title = "Exploring the Mountains"
    adventure_content = "Had an amazing time hiking in the beautiful mountains!"
    photo_path = "path/to/your/photo.jpg"  # Replace with the path to your Polaroid photo

    post_adventure(adventure_title, adventure_content, photo_path)
```

Make sure to install the required `Pillow` library for image processing before running this script:

```bash
pip install Pillow requests
```
