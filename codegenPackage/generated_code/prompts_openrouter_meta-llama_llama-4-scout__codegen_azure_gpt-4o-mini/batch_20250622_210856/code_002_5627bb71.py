"""
Generated Code Metadata:
========================
Original URL: https://fsromain.com
Prompt: Generate a Python script to analyze Instagram engagement metrics for influencers, inspired by Romain Ferri's work with creators and public figures.
Generated: DETERMINISTIC_5627bb71f73f32a3
Batch ID: 20250622_210856
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://graph.instagram.com": {
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
import requests
import pandas as pd
import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InstagramEngagementAnalyzer:
    def __init__(self, access_token: str):
        """
        Initialize the InstagramEngagementAnalyzer with an access token.

        :param access_token: Access token for Instagram Graph API
        """
        self.access_token = access_token
        self.base_url = "https://graph.instagram.com"

    def fetch_user_data(self, user_id: str) -> Dict:
        """
        Fetch user data from Instagram API.

        :param user_id: The ID of the Instagram user
        :return: User data as a dictionary
        """
        url = f"{self.base_url}/{user_id}?fields=id,username,media_count,followers_count,follows_count&access_token={self.access_token}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching user data: {e}")
            return {}

    def fetch_media_data(self, user_id: str) -> List[Dict]:
        """
        Fetch media data for a user from Instagram API.

        :param user_id: The ID of the Instagram user
        :return: List of media data dictionaries
        """
        url = f"{self.base_url}/{user_id}/media?fields=id,caption,like_count,comments_count,timestamp&access_token={self.access_token}"
        media_data = []
        try:
            response = requests.get(url)
            response.raise_for_status()
            media_data = response.json().get('data', [])
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching media data: {e}")
        return media_data

    def calculate_engagement_rate(self, media_data: List[Dict], followers_count: int) -> float:
        """
        Calculate the engagement rate based on media data and followers count.

        :param media_data: List of media data dictionaries
        :param followers_count: Number of followers of the user
        :return: Engagement rate as a float
        """
        total_engagements = sum(item['like_count'] + item['comments_count'] for item in media_data)
        if followers_count > 0:
            engagement_rate = (total_engagements / followers_count) * 100
            return engagement_rate
        return 0.0

    def analyze_engagement(self, user_id: str) -> None:
        """
        Analyze engagement metrics for a given user.

        :param user_id: The ID of the Instagram user
        """
        user_data = self.fetch_user_data(user_id)
        if not user_data:
            logging.warning("No user data found.")
            return

        media_data = self.fetch_media_data(user_id)
        if not media_data:
            logging.warning("No media data found.")
            return

        followers_count = user_data.get('followers_count', 0)
        engagement_rate = self.calculate_engagement_rate(media_data, followers_count)

        logging.info(f"User: {user_data['username']}")
        logging.info(f"Followers: {followers_count}")
        logging.info(f"Engagement Rate: {engagement_rate:.2f}%")

if __name__ == "__main__":
    # Replace with your actual access token and user ID
    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    USER_ID = "USER_ID"

    analyzer = InstagramEngagementAnalyzer(ACCESS_TOKEN)
    analyzer.analyze_engagement(USER_ID)
```
