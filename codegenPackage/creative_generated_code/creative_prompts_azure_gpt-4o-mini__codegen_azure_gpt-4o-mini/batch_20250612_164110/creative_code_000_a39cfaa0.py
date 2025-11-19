"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsex.in
Prompt: Generate a code snippet for a social media management tool that integrates with Instagram and tracks engagement metrics for influencer campaigns.
Generated: DETERMINISTIC_a39cfaa062391b5a
Batch ID: 20250612_164110
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://graph.instagram.com/": {
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
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InstagramAPI:
    """
    A class to interact with the Instagram Graph API for 
    fetching engagement metrics for influencer campaigns.
    """

    BASE_URL = "https://graph.instagram.com/"

    def __init__(self, access_token):
        """
        Initializes the InstagramAPI with the provided access token.

        :param access_token: str - Access token for Instagram Graph API
        """
        self.access_token = access_token

    def get_user_media(self, user_id):
        """
        Fetches media objects of the specified user.

        :param user_id: str - Instagram user ID
        :return: dict - Media data
        """
        url = f"{self.BASE_URL}{user_id}/media?access_token={self.access_token}"
        response = requests.get(url)

        if response.status_code != 200:
            logging.error(f"Failed to fetch user media: {response.text}")
            raise Exception(f"Error fetching media: {response.status_code}")

        return response.json()

    def get_engagement_metrics(self, media_id):
        """
        Fetches engagement metrics for a specified media object.

        :param media_id: str - Media ID to fetch metrics for
        :return: dict - Engagement metrics
        """
        url = f"{self.BASE_URL}{media_id}?fields=like_count,comments_count,impressions,reach&access_token={self.access_token}"
        response = requests.get(url)

        if response.status_code != 200:
            logging.error(f"Failed to fetch engagement metrics: {response.text}")
            raise Exception(f"Error fetching metrics: {response.status_code}")

        return response.json()

class CampaignManager:
    """
    A class to manage influencer campaigns and track their engagement metrics.
    """

    def __init__(self, access_token):
        """
        Initializes the CampaignManager with Instagram API access.

        :param access_token: str - Access token for Instagram Graph API
        """
        self.instagram_api = InstagramAPI(access_token)

    def track_campaign(self, user_id):
        """
        Tracks the engagement metrics for a campaign associated with a user.

        :param user_id: str - Instagram user ID
        """
        try:
            media_data = self.instagram_api.get_user_media(user_id)

            # Loop through media items and collect metrics
            engagement_summary = []
            for media in media_data.get('data', []):
                media_id = media['id']
                metrics = self.instagram_api.get_engagement_metrics(media_id)
                engagement_summary.append({
                    'media_id': media_id,
                    'likes': metrics.get('like_count', 0),
                    'comments': metrics.get('comments_count', 0),
                    'impressions': metrics.get('impressions', 0),
                    'reach': metrics.get('reach', 0),
                    'date': datetime.now().isoformat()  # Add timestamp for tracking
                })

            logging.info(f"Engagement metrics for user {user_id}: {engagement_summary}")
            return engagement_summary

        except Exception as e:
            logging.error(f"Error tracking campaign: {str(e)}")
            return None

# Example usage
if __name__ == "__main__":
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  # Replace with your actual access token
    USER_ID = "USER_ID"  # Replace with the target user's Instagram ID

    campaign_manager = CampaignManager(ACCESS_TOKEN)
    campaign_metrics = campaign_manager.track_campaign(USER_ID)

    if campaign_metrics:
        print("Campaign metrics tracked successfully.")
    else:
        print("Failed to track campaign metrics.")
```
