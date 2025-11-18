"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://p-1px.pages.dev
Prompt: Generate a script to track updates and news from Over Protocol, pulling data from Over Foundation's social media channels and Medium blog.
Generated: DETERMINISTIC_e8823cc7ecefcfaa
Batch ID: 20250612_151143
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.twitter.com/2/users/{user_id}/tweets": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.medium.com/v1/users/{user_id}/posts": {
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
from datetime import datetime

# Constants
TWITTER_API_URL = "https://api.twitter.com/2/users/{user_id}/tweets"
MEDIUM_API_URL = "https://api.medium.com/v1/users/{user_id}/posts"
TWITTER_BEARER_TOKEN = "YOUR_TWITTER_BEARER_TOKEN"  # Replace with your Twitter API Bearer token
MEDIUM_API_TOKEN = "YOUR_MEDIUM_API_TOKEN"  # Replace with your Medium API token
OVER_TWITTER_USER_ID = "YOUR_OVER_TWITTER_USER_ID"  # Replace with Over Protocol's Twitter user ID
OVER_MEDIUM_USER_ID = "YOUR_OVER_MEDIUM_USER_ID"  # Replace with Over Protocol's Medium user ID

# Function to fetch tweets from Over Protocol's Twitter account
def fetch_twitter_updates():
    try:
        headers = {"Authorization": f"Bearer {TWITTER_BEARER_TOKEN}"}
        response = requests.get(TWITTER_API_URL.format(user_id=OVER_TWITTER_USER_ID), headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse JSON response
        tweets = response.json()["data"]
        updates = [
            {
                "text": tweet["text"],
                "timestamp": tweet["created_at"]
            }
            for tweet in tweets
        ]
        return updates
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Twitter updates: {e}")
        return []

# Function to fetch posts from Over Protocol's Medium blog
def fetch_medium_updates():
    try:
        headers = {"Authorization": f"Bearer {MEDIUM_API_TOKEN}"}
        response = requests.get(MEDIUM_API_URL.format(user_id=OVER_MEDIUM_USER_ID), headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Parse JSON response
        posts = response.json()["data"]
        updates = [
            {
                "title": post["title"],
                "url": post["url"],
                "timestamp": post["created_at"]
            }
            for post in posts
        ]
        return updates
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Medium updates: {e}")
        return []

# Function to format updates for display
def format_updates(updates, source):
    print(f"Updates from {source}:\n")
    for update in updates:
        timestamp = datetime.strptime(update["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        print(f"- {formatted_timestamp}: {update.get('text', update.get('title'))}")
        if "url" in update:
            print(f"  URL: {update['url']}\n")

# Main function to track updates
def main():
    print("Fetching updates from Over Protocol...\n")
    
    # Fetch updates from Twitter
    twitter_updates = fetch_twitter_updates()
    format_updates(twitter_updates, "Twitter")
    
    # Fetch updates from Medium
    medium_updates = fetch_medium_updates()
    format_updates(medium_updates, "Medium")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace placeholders (`YOUR_TWITTER_BEARER_TOKEN`, `YOUR_MEDIUM_API_TOKEN`, etc.) with appropriate API credentials.
- Ensure you have the necessary permissions and tokens to access Twitter and Medium APIs.
- Install required dependencies using `pip install requests` before running the script.
