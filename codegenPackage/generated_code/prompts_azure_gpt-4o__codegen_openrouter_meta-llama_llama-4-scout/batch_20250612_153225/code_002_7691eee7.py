"""
Generated Code Metadata:
========================
Original URL: https://taramediaworks.com
Prompt: Generate code for integrating social media platforms like Facebook and Instagram into a marketing campaign, inspired by Tara Media Works' expertise in social media marketing.
Generated: DETERMINISTIC_7691eee7d67b84ba
Batch ID: 20250612_153225
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.example.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.example.com/image.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
# social_media_integrator.py

import os
import json
from typing import Dict

# Facebook API
import facebook

# Instagram API
import instagram

class SocialMediaIntegrator:
    """
    Integrates social media platforms like Facebook and Instagram into a marketing campaign.
    """

    def __init__(self, facebook_app_id: str, facebook_app_secret: str, instagram_client_id: str, instagram_client_secret: str):
        """
        Initializes the SocialMediaIntegrator with API credentials.

        Args:
        - facebook_app_id (str): Facebook app ID
        - facebook_app_secret (str): Facebook app secret
        - instagram_client_id (str): Instagram client ID
        - instagram_client_secret (str): Instagram client secret
        """
        self.facebook_app_id = facebook_app_id
        self.facebook_app_secret = facebook_app_secret
        self.instagram_client_id = instagram_client_id
        self.instagram_client_secret = instagram_client_secret

        # Facebook API
        self.facebook_graph = facebook.GraphAPI(self.facebook_app_id, self.facebook_app_secret)

        # Instagram API
        self.instagram_api = instagram.Client(self.instagram_client_id, self.instagram_client_secret)

    def get_facebook_access_token(self, facebook_user_id: str) -> str:
        """
        Gets a Facebook access token for a given user.

        Args:
        - facebook_user_id (str): Facebook user ID

        Returns:
        - str: Facebook access token
        """
        try:
            # Get access token
            access_token = self.facebook_graph.get_access_token(facebook_user_id)
            return access_token
        except facebook.GraphAPIException as e:
            print(f"Error getting Facebook access token: {e}")
            return None

    def get_instagram_access_token(self, instagram_user_id: str) -> str:
        """
        Gets an Instagram access token for a given user.

        Args:
        - instagram_user_id (str): Instagram user ID

        Returns:
        - str: Instagram access token
        """
        try:
            # Get access token
            access_token = self.instagram_api.get_access_token(instagram_user_id)
            return access_token
        except instagram.InstagramAPIError as e:
            print(f"Error getting Instagram access token: {e}")
            return None

    def post_to_facebook(self, access_token: str, message: str, link: str) -> bool:
        """
        Posts to Facebook with a given access token.

        Args:
        - access_token (str): Facebook access token
        - message (str): Post message
        - link (str): Post link

        Returns:
        - bool: Whether the post was successful
        """
        try:
            # Post to Facebook
            self.facebook_graph.put_object(parent_object='me', connection_name='feed', message=message, link=link, access_token=access_token)
            return True
        except facebook.GraphAPIException as e:
            print(f"Error posting to Facebook: {e}")
            return False

    def post_to_instagram(self, access_token: str, caption: str, image_url: str) -> bool:
        """
        Posts to Instagram with a given access token.

        Args:
        - access_token (str): Instagram access token
        - caption (str): Post caption
        - image_url (str): Post image URL

        Returns:
        - bool: Whether the post was successful
        """
        try:
            # Post to Instagram
            self.instagram_api.post_media(caption=caption, image_url=image_url, access_token=access_token)
            return True
        except instagram.InstagramAPIError as e:
            print(f"Error posting to Instagram: {e}")
            return False

def main():
    # Load API credentials from environment variables
    facebook_app_id = os.environ.get('FACEBOOK_APP_ID')
    facebook_app_secret = os.environ.get('FACEBOOK_APP_SECRET')
    instagram_client_id = os.environ.get('INSTAGRAM_CLIENT_ID')
    instagram_client_secret = os.environ.get('INSTAGRAM_CLIENT_SECRET')

    # Create SocialMediaIntegrator instance
    integrator = SocialMediaIntegrator(facebook_app_id, facebook_app_secret, instagram_client_id, instagram_client_secret)

    # Get access tokens
    facebook_user_id = 'your_facebook_user_id'
    instagram_user_id = 'your_instagram_user_id'
    facebook_access_token = integrator.get_facebook_access_token(facebook_user_id)
    instagram_access_token = integrator.get_instagram_access_token(instagram_user_id)

    # Post to Facebook and Instagram
    if facebook_access_token and instagram_access_token:
        facebook_message = 'Hello from Facebook!'
        facebook_link = 'https://www.example.com'
        instagram_caption = 'Hello from Instagram!'
        instagram_image_url = 'https://www.example.com/image.jpg'

        facebook_post_success = integrator.post_to_facebook(facebook_access_token, facebook_message, facebook_link)
        instagram_post_success = integrator.post_to_instagram(instagram_access_token, instagram_caption, instagram_image_url)

        print(f"Facebook post successful: {facebook_post_success}")
        print(f"Instagram post successful: {instagram_post_success}")

if __name__ == '__main__':
    main()
```
