"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsex.in
Prompt: Create an API integration to track influencer campaign performance across platforms like Instagram, Facebook, YouTube, and Twitter, as outlined by PulseX Media Solutions.
Generated: DETERMINISTIC_cbca014cba854db3
Batch ID: 20250612_154441
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://api.twitter.com/2/": {
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
  },
  "https://graph.facebook.com/v12.0/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/youtube/v3/": {
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
from typing import Dict, List, Optional

# Constants for API endpoints and access tokens (these should be stored securely)
API_ENDPOINTS = {
    "instagram": "https://graph.instagram.com/v12.0/",
    "facebook": "https://graph.facebook.com/v12.0/",
    "youtube": "https://www.googleapis.com/youtube/v3/",
    "twitter": "https://api.twitter.com/2/"
}
ACCESS_TOKENS = {
    "instagram": "YOUR_INSTAGRAM_ACCESS_TOKEN",
    "facebook": "YOUR_FACEBOOK_ACCESS_TOKEN",
    "youtube": "YOUR_YOUTUBE_ACCESS_TOKEN",
    "twitter": "YOUR_TWITTER_ACCESS_TOKEN"
}

# Error handling class
class APIIntegrationError(Exception):
    pass

# Function to fetch Instagram metrics
def fetch_instagram_metrics(campaign_id: str) -> Optional[Dict]:
    """
    Fetch metrics for a campaign on Instagram.
    """
    url = f"{API_ENDPOINTS['instagram']}{campaign_id}/insights"
    params = {"access_token": ACCESS_TOKENS['instagram']}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise APIIntegrationError(f"Error fetching Instagram metrics: {e}")

# Function to fetch Facebook metrics
def fetch_facebook_metrics(campaign_id: str) -> Optional[Dict]:
    """
    Fetch metrics for a campaign on Facebook.
    """
    url = f"{API_ENDPOINTS['facebook']}{campaign_id}/insights"
    params = {"access_token": ACCESS_TOKENS['facebook']}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise APIIntegrationError(f"Error fetching Facebook metrics: {e}")

# Function to fetch YouTube metrics
def fetch_youtube_metrics(video_id: str) -> Optional[Dict]:
    """
    Fetch metrics for a video on YouTube.
    """
    url = f"{API_ENDPOINTS['youtube']}videos"
    params = {"id": video_id, "part": "statistics", "key": ACCESS_TOKENS['youtube']}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise APIIntegrationError(f"Error fetching YouTube metrics: {e}")

# Function to fetch Twitter metrics
def fetch_twitter_metrics(tweet_id: str) -> Optional[Dict]:
    """
    Fetch metrics for a tweet on Twitter.
    """
    url = f"{API_ENDPOINTS['twitter']}tweets/{tweet_id}"
    headers = {"Authorization": f"Bearer {ACCESS_TOKENS['twitter']}"}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise APIIntegrationError(f"Error fetching Twitter metrics: {e}")

# Aggregation function to track influencer campaign performance
def track_campaign_performance(platforms: List[str], campaign_ids: Dict[str, str]) -> Dict[str, Optional[Dict]]:
    """
    Track campaign performance across multiple platforms.
    :param platforms: List of platforms to track (e.g., ["instagram", "facebook", "youtube", "twitter"])
    :param campaign_ids: Dictionary mapping platforms to their campaign IDs or video/tweet IDs
    :return: Dictionary of campaign metrics for each platform
    """
    metrics = {}
    for platform in platforms:
        try:
            if platform == "instagram":
                metrics[platform] = fetch_instagram_metrics(campaign_ids.get(platform, ""))
            elif platform == "facebook":
                metrics[platform] = fetch_facebook_metrics(campaign_ids.get(platform, ""))
            elif platform == "youtube":
                metrics[platform] = fetch_youtube_metrics(campaign_ids.get(platform, ""))
            elif platform == "twitter":
                metrics[platform] = fetch_twitter_metrics(campaign_ids.get(platform, ""))
            else:
                metrics[platform] = None
        except APIIntegrationError as e:
            metrics[platform] = {"error": str(e)}
    return metrics

# Example usage
if __name__ == "__main__":
    campaign_ids = {
        "instagram": "INSTAGRAM_CAMPAIGN_ID",
        "facebook": "FACEBOOK_CAMPAIGN_ID",
        "youtube": "YOUTUBE_VIDEO_ID",
        "twitter": "TWITTER_TWEET_ID"
    }
    platforms = ["instagram", "facebook", "youtube", "twitter"]

    try:
        campaign_metrics = track_campaign_performance(platforms, campaign_ids)
        print("Campaign Metrics:", campaign_metrics)
    except Exception as e:
        print(f"Error tracking campaign performance: {e}")
```
