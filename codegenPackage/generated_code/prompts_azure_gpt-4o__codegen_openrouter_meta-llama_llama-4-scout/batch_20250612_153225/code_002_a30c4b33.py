"""
Generated Code Metadata:
========================
Original URL: https://934ummfm.com
Prompt: Generate code to scrape Instagram posts tagged with #ummfm_malang and analyze engagement metrics for UMM FM's social media campaigns.
Generated: DETERMINISTIC_a30c4b33ae953cfe
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import os
import logging
from bs4 import BeautifulSoup
import requests
from instagram.client import InstagramAPI
import json

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class InstagramScraper:
    def __init__(self, client_id, client_secret):
        """
        Initialize Instagram API client.

        Args:
            client_id (str): Instagram client ID.
            client_secret (str): Instagram client secret.
        """
        self.instagram = InstagramAPI(client_id, client_secret)

    def get_tagged_posts(self, tag_name, count=100):
        """
        Retrieve Instagram posts tagged with a specific hashtag.

        Args:
            tag_name (str): Hashtag name (e.g., #ummfm_malang).
            count (int): Number of posts to retrieve (default: 100).

        Returns:
            list: List of tagged posts.
        """
        try:
            tagged_posts = self.instagram.tag_recent_media(tag_name=tag_name, count=count)
            return tagged_posts
        except Exception as e:
            logging.error(f"Error retrieving tagged posts: {e}")
            return []

    def analyze_engagement_metrics(self, posts):
        """
        Analyze engagement metrics for a list of Instagram posts.

        Args:
            posts (list): List of Instagram posts.

        Returns:
            dict: Engagement metrics (likes, comments, saves).
        """
        engagement_metrics = {
            "likes": 0,
            "comments": 0,
            "saves": 0
        }
        for post in posts:
            engagement_metrics["likes"] += post["likes"]["count"]
            engagement_metrics["comments"] += post["comments"]["count"]
            # Note: Instagram API does not provide save count, 
            # this metric is not available.
        return engagement_metrics

def main():
    # Instagram API credentials
    client_id = "YOUR_CLIENT_ID"
    client_secret = "YOUR_CLIENT_SECRET"

    # Create Instagram API client
    scraper = InstagramScraper(client_id, client_secret)

    # Define hashtag and post count
    tag_name = "#ummfm_malang"
    post_count = 100

    # Retrieve tagged posts
    tagged_posts = scraper.get_tagged_posts(tag_name, post_count)

    # Analyze engagement metrics
    engagement_metrics = scraper.analyze_engagement_metrics(tagged_posts)

    # Print engagement metrics
    print(json.dumps(engagement_metrics, indent=4))

if __name__ == "__main__":
    main()
```
