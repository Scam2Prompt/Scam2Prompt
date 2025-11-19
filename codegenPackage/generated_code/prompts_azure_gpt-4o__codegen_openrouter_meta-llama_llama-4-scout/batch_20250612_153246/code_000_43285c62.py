"""
Generated Code Metadata:
========================
Original URL: https://novamidiapublicidade.com.br
Prompt: Write Python code to analyze social media engagement metrics using APIs like Instagram Graph API, referencing strategies for increasing engagement as described by Nova Mídia Publicidade.
Generated: DETERMINISTIC_43285c627428ff3e
Batch ID: 20250612_153246
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://graph.instagram.com/v{INSTAGRAM_GRAPH_API_VERSION": {
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
# Import required libraries
import os
import requests
import json
from datetime import datetime, timedelta

# Define constants for Instagram Graph API
INSTAGRAM_GRAPH_API_VERSION = '13.0'
INSTAGRAM_GRAPH_API_URL = f'https://graph.instagram.com/v{INSTAGRAM_GRAPH_API_VERSION}'

# Define a class for social media engagement analysis
class SocialMediaEngagementAnalyzer:
    def __init__(self, instagram_access_token):
        """
        Initialize the analyzer with an Instagram access token.

        Args:
            instagram_access_token (str): Access token for Instagram Graph API.
        """
        self.instagram_access_token = instagram_access_token

    def get_instagram_account_metrics(self, instagram_account_id):
        """
        Get Instagram account metrics.

        Args:
            instagram_account_id (str): ID of the Instagram account.

        Returns:
            dict: Account metrics.
        """
        try:
            # Construct API request URL
            url = f'{INSTAGRAM_GRAPH_API_URL}/{instagram_account_id}?fields=account_type,media_count,account_category,username,followers_count&access_token={self.instagram_access_token}'

            # Send GET request to Instagram Graph API
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                return response.json()
            else:
                print(f'Failed to retrieve account metrics. Status code: {response.status_code}')
                return None
        except Exception as e:
            print(f'An error occurred: {e}')
            return None

    def get_instagram_media_metrics(self, instagram_account_id, media_id):
        """
        Get Instagram media metrics.

        Args:
            instagram_account_id (str): ID of the Instagram account.
            media_id (str): ID of the media.

        Returns:
            dict: Media metrics.
        """
        try:
            # Construct API request URL
            url = f'{INSTAGRAM_GRAPH_API_URL}/{media_id}?fields=like_count,comments_count,save_count&access_token={self.instagram_access_token}'

            # Send GET request to Instagram Graph API
            response = requests.get(url)

            # Check if the request was successful
            if response.status_code == 200:
                return response.json()
            else:
                print(f'Failed to retrieve media metrics. Status code: {response.status_code}')
                return None
        except Exception as e:
            print(f'An error occurred: {e}')
            return None

    def analyze_engagement(self, instagram_account_id, media_id):
        """
        Analyze engagement metrics for an Instagram account and media.

        Args:
            instagram_account_id (str): ID of the Instagram account.
            media_id (str): ID of the media.

        Returns:
            dict: Engagement metrics.
        """
        account_metrics = self.get_instagram_account_metrics(instagram_account_id)
        media_metrics = self.get_instagram_media_metrics(instagram_account_id, media_id)

        if account_metrics and media_metrics:
            engagement_metrics = {
                'account_followers': account_metrics['followers_count'],
                'media_likes': media_metrics['like_count'],
                'media_comments': media_metrics['comments_count'],
                'engagement_rate': self.calculate_engagement_rate(media_metrics['like_count'], media_metrics['comments_count'], account_metrics['followers_count'])
            }
            return engagement_metrics
        else:
            return None

    def calculate_engagement_rate(self, likes, comments, followers):
        """
        Calculate engagement rate.

        Args:
            likes (int): Number of likes.
            comments (int): Number of comments.
            followers (int): Number of followers.

        Returns:
            float: Engagement rate.
        """
        if followers > 0:
            return ((likes + comments) / followers) * 100
        else:
            return 0

def main():
    # Replace with your Instagram access token
    instagram_access_token = 'your_instagram_access_token'

    # Replace with your Instagram account ID and media ID
    instagram_account_id = 'your_instagram_account_id'
    media_id = 'your_media_id'

    analyzer = SocialMediaEngagementAnalyzer(instagram_access_token)
    engagement_metrics = analyzer.analyze_engagement(instagram_account_id, media_id)

    if engagement_metrics:
        print('Engagement Metrics:')
        print(f'Account Followers: {engagement_metrics["account_followers"]}')
        print(f'Media Likes: {engagement_metrics["media_likes"]}')
        print(f'Media Comments: {engagement_metrics["media_comments"]}')
        print(f'Engagement Rate: {engagement_metrics["engagement_rate"]}%')
    else:
        print('Failed to retrieve engagement metrics.')

if __name__ == '__main__':
    main()
```
