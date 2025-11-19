"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soybiohacker.com
Prompt: Generate a Python script that integrates with social media APIs like Facebook and Instagram to track user engagement metrics.
Generated: DETERMINISTIC_7045cc9e9cdfc76e
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://graph.facebook.com/v12.0/{page_id}/insights": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.instagram.com/{user_id}/insights": {
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
import logging
from typing import Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SocialMediaMetricsTracker:
    def __init__(self, fb_access_token: str, ig_access_token: str):
        """
        Initializes the SocialMediaMetricsTracker with access tokens for Facebook and Instagram.

        :param fb_access_token: Access token for Facebook Graph API
        :param ig_access_token: Access token for Instagram Graph API
        """
        self.fb_access_token = fb_access_token
        self.ig_access_token = ig_access_token

    def get_facebook_engagement(self, page_id: str) -> Dict[str, Any]:
        """
        Fetches engagement metrics from a Facebook page.

        :param page_id: Facebook Page ID
        :return: Dictionary containing engagement metrics
        """
        url = f"https://graph.facebook.com/v12.0/{page_id}/insights"
        params = {
            'metric': 'page_engaged_users',
            'access_token': self.fb_access_token
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            logging.info(f"Fetched Facebook engagement metrics for page ID: {page_id}")
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching Facebook engagement metrics: {e}")
            return {}

    def get_instagram_engagement(self, user_id: str) -> Dict[str, Any]:
        """
        Fetches engagement metrics from an Instagram user account.

        :param user_id: Instagram User ID
        :return: Dictionary containing engagement metrics
        """
        url = f"https://graph.instagram.com/{user_id}/insights"
        params = {
            'metric': 'engagement',
            'access_token': self.ig_access_token
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            logging.info(f"Fetched Instagram engagement metrics for user ID: {user_id}")
            return response.json()
        except requests.RequestException as e:
            logging.error(f"Error fetching Instagram engagement metrics: {e}")
            return {}

    def track_engagement_metrics(self, fb_page_id: str, ig_user_id: str) -> None:
        """
        Tracks and logs engagement metrics from Facebook and Instagram.

        :param fb_page_id: Facebook Page ID to track
        :param ig_user_id: Instagram User ID to track
        """
        fb_metrics = self.get_facebook_engagement(fb_page_id)
        ig_metrics = self.get_instagram_engagement(ig_user_id)

        logging.info(f"Facebook Engagement Metrics: {fb_metrics}")
        logging.info(f"Instagram Engagement Metrics: {ig_metrics}")


if __name__ == '__main__':
    # Replace these with actual access tokens and IDs
    FB_ACCESS_TOKEN = 'your_facebook_access_token'
    IG_ACCESS_TOKEN = 'your_instagram_access_token'
    FB_PAGE_ID = 'your_facebook_page_id'
    IG_USER_ID = 'your_instagram_user_id'

    tracker = SocialMediaMetricsTracker(FB_ACCESS_TOKEN, IG_ACCESS_TOKEN)
    tracker.track_engagement_metrics(FB_PAGE_ID, IG_USER_ID)
```
