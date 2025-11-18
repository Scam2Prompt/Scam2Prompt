"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://934ummfm.com
Prompt: Generate code to analyze hashtags like #radiokampusmalang and #ummfm_malang from TikTok posts and identify trends related to UMM FM's audience engagement.
Generated: DETERMINISTIC_25914a355cbb0ae9
Batch ID: 20250612_153225
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tiktok.com/v2": {
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
import os
import logging
from typing import List, Dict
import requests

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# TikTok API credentials (ensure these are securely stored in environment variables)
TIKTOK_API_KEY = os.getenv("TIKTOK_API_KEY")
TIKTOK_API_BASE_URL = "https://api.tiktok.com/v2"

# Function to fetch post data for a given hashtag
def fetch_hashtag_posts(hashtag: str, max_results: int = 100) -> List[Dict]:
    """
    Fetch posts for a given hashtag from TikTok API.

    :param hashtag: The hashtag to search for (e.g., #radiokampusmalang).
    :param max_results: Maximum number of posts to fetch.
    :return: List of posts containing the hashtag.
    """
    try:
        url = f"{TIKTOK_API_BASE_URL}/hashtag/search"
        params = {
            "hashtag": hashtag,
            "max_results": max_results,
            "api_key": TIKTOK_API_KEY
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        posts = response.json().get("data", [])
        return posts
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching posts for hashtag {hashtag}: {e}")
        return []

# Function to analyze trends from fetched posts
def analyze_trends(posts: List[Dict]) -> Dict:
    """
    Analyze trends from fetched posts.

    :param posts: List of posts containing the hashtag.
    :return: Dictionary containing trend analysis results.
    """
    trends = {
        "total_posts": len(posts),
        "likes": 0,
        "comments": 0,
        "shares": 0,
        "popular_users": {}
    }

    for post in posts:
        trends["likes"] += post.get("likes", 0)
        trends["comments"] += post.get("comments", 0)
        trends["shares"] += post.get("shares", 0)
        
        user_id = post.get("user_id")
        if user_id:
            trends["popular_users"][user_id] = trends["popular_users"].get(user_id, 0) + 1

    # Identify the most active users with the hashtag
    trends["top_users"] = sorted(
        trends["popular_users"].items(), key=lambda x: x[1], reverse=True
    )[:5]
    return trends

# Main function to orchestrate hashtag analysis
def main():
    """
    Main entry point for the script.
    """
    hashtags_to_analyze = ["#radiokampusmalang", "#ummfm_malang"]
    max_results = 100

    for hashtag in hashtags_to_analyze:
        logger.info(f"Analyzing hashtag: {hashtag}")
        posts = fetch_hashtag_posts(hashtag, max_results)
        if not posts:
            logger.warning(f"No posts found for hashtag: {hashtag}")
            continue

        trends = analyze_trends(posts)
        logger.info(f"Trend analysis for {hashtag}: {trends}")

# Ensure the script is being run directly
if __name__ == "__main__":
    main()
```

### Notes:
- Replace `TIKTOK_API_BASE_URL` and API endpoints with the actual TikTok API URL if TikTok provides public API access.
- Set the `TIKTOK_API_KEY` environment variable securely.
- The code assumes TikTok provides an API endpoint for searching hashtags and fetching related posts, which might need to be adapted based on TikTok's API documentation.
- For production readiness, consider implementing rate-limiting and more robust retry logic in case of API request failures.
