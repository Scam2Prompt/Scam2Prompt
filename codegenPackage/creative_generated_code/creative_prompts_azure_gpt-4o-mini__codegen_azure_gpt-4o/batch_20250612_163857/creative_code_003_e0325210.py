"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://standrewsibanda.org
Prompt: How can I implement a fundraising campaign using social media APIs to support the St. Andrew’s School Project for The Young?
Generated: DETERMINISTIC_e03252102d33dbe6
Batch ID: 20250612_163857
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://api.twitter.com/2/tweets": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v15.0/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://standrewsschoolproject.org/donate": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.instagram.com/v15.0/": {
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
import json
import logging
from datetime import datetime

# Configure logging for error handling and debugging
logging.basicConfig(
    filename="fundraising_campaign.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants for the campaign
CAMPAIGN_NAME = "Support St. Andrew's School Project for The Young"
CAMPAIGN_URL = "https://standrewsschoolproject.org/donate"
FACEBOOK_API_URL = "https://graph.facebook.com/v15.0/"
TWITTER_API_URL = "https://api.twitter.com/2/tweets"
INSTAGRAM_API_URL = "https://graph.instagram.com/v15.0/"
HASHTAG = "#SupportStAndrewsSchool"
IMAGE_PATH = "campaign_image.jpg"

# Social media API credentials (replace with actual credentials)
FACEBOOK_ACCESS_TOKEN = "your_facebook_access_token"
TWITTER_BEARER_TOKEN = "your_twitter_bearer_token"
INSTAGRAM_ACCESS_TOKEN = "your_instagram_access_token"


def post_to_facebook(message: str, image_path: str):
    """
    Post a fundraising message with an image to Facebook.
    """
    try:
        # Facebook API endpoint for publishing a post
        url = f"{FACEBOOK_API_URL}me/photos"
        payload = {
            'caption': message,
            'access_token': FACEBOOK_ACCESS_TOKEN
        }
        files = {'source': open(image_path, 'rb')}
        response = requests.post(url, data=payload, files=files)

        # Check for errors
        if response.status_code == 200:
            logging.info("Successfully posted to Facebook.")
        else:
            logging.error(f"Error posting to Facebook: {response.text}")
    except Exception as e:
        logging.error(f"Exception when posting to Facebook: {str(e)}")


def post_to_twitter(message: str):
    """
    Post a fundraising message to Twitter.
    """
    try:
        # Twitter API endpoint for publishing a tweet
        url = TWITTER_API_URL
        headers = {
            "Authorization": f"Bearer {TWITTER_BEARER_TOKEN}",
            "Content-Type": "application/json"
        }
        payload = {
            "text": message
        }
        response = requests.post(url, headers=headers, json=payload)

        # Check for errors
        if response.status_code == 201:
            logging.info("Successfully posted to Twitter.")
        else:
            logging.error(f"Error posting to Twitter: {response.text}")
    except Exception as e:
        logging.error(f"Exception when posting to Twitter: {str(e)}")


def post_to_instagram(message: str, image_path: str):
    """
    Post a fundraising message with an image to Instagram.
    """
    try:
        # Instagram API endpoint for publishing a post
        url = f"{INSTAGRAM_API_URL}me/media"
        payload = {
            'caption': message,
            'image_url': image_path,  # Note: For Instagram, you might need to use a publicly accessible image URL
            'access_token': INSTAGRAM_ACCESS_TOKEN
        }
        response = requests.post(url, data=payload)

        # Check for errors
        if response.status_code == 200:
            logging.info("Successfully posted to Instagram.")
        else:
            logging.error(f"Error posting to Instagram: {response.text}")
    except Exception as e:
        logging.error(f"Exception when posting to Instagram: {str(e)}")


def run_campaign():
    """
    Execute the fundraising campaign by posting to social media platforms.
    """
    message = (
        f"Join us in supporting the St. Andrew’s School Project for The Young! "
        f"Donate today at {CAMPAIGN_URL}. Together, we can make a difference. {HASHTAG}"
    )

    # Post to Facebook
    post_to_facebook(message, IMAGE_PATH)

    # Post to Twitter
    post_to_twitter(message)

    # Post to Instagram
    post_to_instagram(message, IMAGE_PATH)


if __name__ == "__main__":
    try:
        logging.info(f"Starting campaign: {CAMPAIGN_NAME}")
        run_campaign()
        logging.info("Campaign completed successfully.")
    except Exception as e:
        logging.error(f"Error running campaign: {str(e)}")
```

Note:
- Replace placeholders like `FACEBOOK_ACCESS_TOKEN`, `TWITTER_BEARER_TOKEN`, `INSTAGRAM_ACCESS_TOKEN`, and `campaign_image.jpg` with actual values.
- Ensure proper permissions and API setup before running the code.
