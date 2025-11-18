"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taramediaworks.com
Prompt: Generate code for integrating social media platforms like Facebook and Instagram into a marketing campaign, inspired by Tara Media Works' expertise in social media marketing.
Generated: DETERMINISTIC_7691eee7d67b84ba
Batch ID: 20250612_153225
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://graph.facebook.com/v12.0/me/feed": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v12.0/{media_id}/publish": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v12.0/me/media": {
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
from requests.exceptions import RequestException

class SocialMediaCampaign:
    """
    A class to represent a social media marketing campaign.
    This class integrates with Facebook and Instagram APIs to create and manage posts.
    """

    def __init__(self, fb_access_token: str, ig_access_token: str):
        """
        Initializes the SocialMediaCampaign with Facebook and Instagram access tokens.

        :param fb_access_token: Access token for Facebook API
        :param ig_access_token: Access token for Instagram API
        """
        self.fb_access_token = fb_access_token
        self.ig_access_token = ig_access_token
        self.fb_api_url = 'https://graph.facebook.com/v12.0/me/feed'
        self.ig_api_url = 'https://graph.facebook.com/v12.0/me/media'

    def post_to_facebook(self, message: str):
        """
        Posts a message to the Facebook feed.

        :param message: The message to post
        :return: Response from the Facebook API
        """
        try:
            payload = {
                'message': message,
                'access_token': self.fb_access_token
            }
            response = requests.post(self.fb_api_url, data=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except RequestException as e:
            print(f"Error posting to Facebook: {e}")
            return None

    def post_to_instagram(self, image_url: str, caption: str):
        """
        Posts an image to the Instagram feed.

        :param image_url: The URL of the image to post
        :param caption: The caption for the post
        :return: Response from the Instagram API
        """
        try:
            # Step 1: Create a media object
            media_payload = {
                'image_url': image_url,
                'caption': caption,
                'access_token': self.ig_access_token
            }
            media_response = requests.post(self.ig_api_url, data=media_payload)
            media_response.raise_for_status()
            media_id = media_response.json().get('id')

            # Step 2: Publish the media object
            publish_url = f'https://graph.facebook.com/v12.0/{media_id}/publish'
            publish_response = requests.post(publish_url, data={'access_token': self.ig_access_token})
            publish_response.raise_for_status()
            return publish_response.json()
        except RequestException as e:
            print(f"Error posting to Instagram: {e}")
            return None

# Example usage
if __name__ == "__main__":
    fb_token = 'YOUR_FACEBOOK_ACCESS_TOKEN'
    ig_token = 'YOUR_INSTAGRAM_ACCESS_TOKEN'

    campaign = SocialMediaCampaign(fb_access_token=fb_token, ig_access_token=ig_token)

    # Post to Facebook
    fb_response = campaign.post_to_facebook("Excited to launch our new campaign!")
    print("Facebook Response:", fb_response)

    # Post to Instagram
    ig_response = campaign.post_to_instagram("https://example.com/image.jpg", "Check out our new campaign!")
    print("Instagram Response:", ig_response)
```

**Note:** Replace `YOUR_FACEBOOK_ACCESS_TOKEN` and `YOUR_INSTAGRAM_ACCESS_TOKEN` with the actual access tokens for the Facebook and Instagram accounts you want to use.
