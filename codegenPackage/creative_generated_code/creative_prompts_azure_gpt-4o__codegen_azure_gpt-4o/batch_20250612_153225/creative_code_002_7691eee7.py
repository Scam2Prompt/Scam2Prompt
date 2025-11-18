"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taramediaworks.com
Prompt: Generate code for integrating social media platforms like Facebook and Instagram into a marketing campaign, inspired by Tara Media Works' expertise in social media marketing.
Generated: DETERMINISTIC_7691eee7d67b84ba
Batch ID: 20250612_153225
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://graph.instagram.com/v12.0": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v12.0": {
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
from typing import Dict, Any

class SocialMediaMarketing:
    """
    A class to manage social media marketing campaigns on platforms like Facebook and Instagram.
    """

    def __init__(self, fb_access_token: str, insta_access_token: str):
        """
        Initializes the SocialMediaMarketing class with access tokens for Facebook and Instagram.
        :param fb_access_token: Facebook API access token
        :param insta_access_token: Instagram API access token
        """
        self.fb_access_token = fb_access_token
        self.insta_access_token = insta_access_token
        self.fb_base_url = "https://graph.facebook.com/v12.0"
        self.insta_base_url = "https://graph.instagram.com/v12.0"

    def create_facebook_post(self, page_id: str, message: str) -> Dict[str, Any]:
        """
        Creates a post on a Facebook page.
        :param page_id: Facebook page ID
        :param message: Message to post
        :return: API response as a dictionary
        """
        url = f"{self.fb_base_url}/{page_id}/feed"
        params = {
            "message": message,
            "access_token": self.fb_access_token
        }
        try:
            response = requests.post(url, params=params)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def create_instagram_post(self, user_id: str, image_url: str, caption: str) -> Dict[str, Any]:
        """
        Creates a post on Instagram for a user.
        :param user_id: Instagram user ID
        :param image_url: URL of the image to post
        :param caption: Caption for the post
        :return: API response as a dictionary
        """
        url = f"{self.insta_base_url}/{user_id}/media"
        params = {
            "image_url": image_url,
            "caption": caption,
            "access_token": self.insta_access_token
        }
        try:
            response = requests.post(url, params=params)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}

    def schedule_campaign(self, platform: str, content: Dict[str, Any], schedule_time: str) -> Dict[str, Any]:
        """
        Schedules a campaign post on Facebook or Instagram.
        :param platform: Platform name ('facebook' or 'instagram')
        :param content: Content dictionary containing page/user ID and post details
        :param schedule_time: Scheduled time for the post (ISO 8601 format)
        :return: API response as a dictionary
        """
        if platform.lower() == "facebook":
            url = f"{self.fb_base_url}/{content['page_id']}/feed"
            params = {
                "message": content['message'],
                "scheduled_publish_time": schedule_time,
                "published": False,
                "access_token": self.fb_access_token
            }
        elif platform.lower() == "instagram":
            url = f"{self.insta_base_url}/{content['user_id']}/media_publish"
            params = {
                "creation_id": content['media_id'],  # Media ID should be created beforehand
                "scheduled_publish_time": schedule_time,
                "access_token": self.insta_access_token
            }
        else:
            return {"error": "Unsupported platform"}

        try:
            response = requests.post(url, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
```

This Python code provides an integration for posting or scheduling content on Facebook and Instagram for a marketing campaign. Replace the placeholder API tokens and other details with actual credentials and parameters from the respective social media APIs before use.
