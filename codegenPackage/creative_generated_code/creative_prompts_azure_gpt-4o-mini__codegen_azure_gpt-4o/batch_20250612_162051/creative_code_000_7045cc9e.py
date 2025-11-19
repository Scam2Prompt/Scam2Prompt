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
  "https://graph.facebook.com/v12.0/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.instagram.com/v12.0/": {
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

# Set up logging for the script
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SocialMediaMetricsTracker:
    """
    A class to interact with Facebook and Instagram APIs to track user engagement metrics.
    """

    def __init__(self, facebook_access_token, instagram_access_token):
        """
        Initializes the tracker with the necessary API tokens.

        :param facebook_access_token: Access token for Facebook API
        :param instagram_access_token: Access token for Instagram API
        """
        self.facebook_access_token = facebook_access_token
        self.instagram_access_token = instagram_access_token
        self.facebook_api_url = "https://graph.facebook.com/v12.0/"
        self.instagram_api_url = "https://graph.instagram.com/v12.0/"
    
    def get_facebook_page_metrics(self, page_id):
        """
        Retrieves engagement metrics for a Facebook page.

        :param page_id: The ID of the Facebook page
        :return: A dictionary containing page engagement metrics
        """
        try:
            url = f"{self.facebook_api_url}{page_id}/insights"
            params = {
                'metric': 'page_impressions,page_engaged_users',
                'access_token': self.facebook_access_token
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            logging.info("Successfully retrieved Facebook page metrics.")
            return data
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching Facebook page metrics: {e}")
            return None
    
    def get_instagram_post_metrics(self, post_id):
        """
        Retrieves engagement metrics for an Instagram post.

        :param post_id: The ID of the Instagram post
        :return: A dictionary containing post engagement metrics
        """
        try:
            url = f"{self.instagram_api_url}{post_id}/insights"
            params = {
                'metric': 'impressions,reach,engagement',
                'access_token': self.instagram_access_token
            }
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            logging.info("Successfully retrieved Instagram post metrics.")
            return data
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching Instagram post metrics: {e}")
            return None

if __name__ == "__main__":
    # Access tokens (replace with your actual tokens)
    FACEBOOK_ACCESS_TOKEN = "your_facebook_access_token_here"
    INSTAGRAM_ACCESS_TOKEN = "your_instagram_access_token_here"

    # Example IDs (replace with your actual IDs)
    FACEBOOK_PAGE_ID = "your_facebook_page_id_here"
    INSTAGRAM_POST_ID = "your_instagram_post_id_here"

    # Initialize the tracker
    tracker = SocialMediaMetricsTracker(FACEBOOK_ACCESS_TOKEN, INSTAGRAM_ACCESS_TOKEN)

    # Fetch Facebook page metrics
    facebook_metrics = tracker.get_facebook_page_metrics(FACEBOOK_PAGE_ID)
    if facebook_metrics:
        print("Facebook Page Metrics:")
        print(json.dumps(facebook_metrics, indent=4))

    # Fetch Instagram post metrics
    instagram_metrics = tracker.get_instagram_post_metrics(INSTAGRAM_POST_ID)
    if instagram_metrics:
        print("Instagram Post Metrics:")
        print(json.dumps(instagram_metrics, indent=4))
```
