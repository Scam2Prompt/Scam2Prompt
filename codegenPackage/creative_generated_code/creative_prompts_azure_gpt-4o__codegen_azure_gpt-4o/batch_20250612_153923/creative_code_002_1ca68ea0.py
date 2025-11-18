"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theog.io
Prompt: Generate code to create and share OG images for Twitter using Senja.io templates, including customization options for SaaS-related content.
Generated: DETERMINISTIC_1ca68ea0313f7ba1
Batch ID: 20250612_153923
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://api.senja.io/templates": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.twitter.com/1.1/statuses/update.json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://upload.twitter.com/1.1/media/upload.json": {
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
import requests
from io import BytesIO
from PIL import Image
import os

# Constants
SENJA_API_URL = "https://api.senja.io/templates"
SENJA_API_KEY = "your_senja_api_key_here"  # Replace with your Senja API key
TWITTER_UPLOAD_URL = "https://upload.twitter.com/1.1/media/upload.json"
TWITTER_UPDATE_URL = "https://api.twitter.com/1.1/statuses/update.json"
TWITTER_API_KEY = "your_twitter_api_key_here"  # Replace with your Twitter API keys
TWITTER_API_SECRET_KEY = "your_twitter_api_secret_key_here"
TWITTER_ACCESS_TOKEN = "your_twitter_access_token_here"
TWITTER_ACCESS_SECRET = "your_twitter_access_secret_here"

# Function to generate OG image using Senja.io templates
def generate_og_image(template_id: str, customization_options: dict) -> str:
    """
    Generates an OG image using Senja.io templates.
    
    Parameters:
        template_id (str): The ID of the Senja.io template.
        customization_options (dict): The options to customize the image.

    Returns:
        str: The URL of the generated image.
    """
    headers = {
        "Authorization": f"Bearer {SENJA_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "template": template_id,
        "customizations": customization_options
    }

    try:
        response = requests.post(SENJA_API_URL, json=payload, headers=headers)
        response.raise_for_status()
        image_data = response.json()
        return image_data.get("image_url")  # Return the generated image URL
    except requests.exceptions.RequestException as e:
        print(f"Error generating image: {e}")
        return None

# Function to upload image to Twitter
def upload_image_to_twitter(image_url: str) -> str:
    """
    Uploads an image to Twitter's media API.

    Parameters:
        image_url (str): The URL of the image.

    Returns:
        str: The media ID for the uploaded image.
    """
    try:
        # Download the image from the provided URL
        response = requests.get(image_url)
        response.raise_for_status()
        image_data = BytesIO(response.content)

        # Upload the image to Twitter
        auth = (TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
        files = {"media": image_data}
        twitter_response = requests.post(TWITTER_UPLOAD_URL, auth=auth, files=files)
        twitter_response.raise_for_status()
        media_data = twitter_response.json()
        return media_data.get("media_id_string")  # Return the media ID
    except requests.exceptions.RequestException as e:
        print(f"Error uploading image to Twitter: {e}")
        return None

# Function to post a tweet with the uploaded image
def post_tweet_with_image(status: str, media_id: str):
    """
    Posts a tweet with the uploaded image.

    Parameters:
        status (str): The text content of the tweet.
        media_id (str): The media ID of the uploaded image.
    """
    try:
        auth = (TWITTER_API_KEY, TWITTER_API_SECRET_KEY)
        payload = {
            "status": status,
            "media_ids": media_id
        }
        response = requests.post(TWITTER_UPDATE_URL, auth=auth, json=payload)
        response.raise_for_status()
        print("Tweet posted successfully!")
    except requests.exceptions.RequestException as e:
        print(f"Error posting tweet: {e}")

# Example usage
if __name__ == "__main__":
    # Customize and generate OG image
    template_id = "your_template_id_here"  # Replace with your Senja.io template ID
    customization = {
        "title": "SaaS Growth Made Simple",
        "subtitle": "Unlock Your Potential in 2023",
        "background_color": "#ffdd00",
        "text_color": "#000000"
    }
    og_image_url = generate_og_image(template_id, customization)

    if og_image_url:
        # Upload the image to Twitter
        media_id = upload_image_to_twitter(og_image_url)

        if media_id:
            # Post a tweet with the image
            tweet_content = "Check out our latest SaaS growth tips! 🚀 #SaaS #Growth"
            post_tweet_with_image(tweet_content, media_id)
```

Note: Replace placeholder values like `your_senja_api_key_here`, `your_twitter_api_key_here`, etc., with actual API keys and template IDs. Install necessary libraries (`pip install requests pillow`) before running.
