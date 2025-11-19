"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepecoin.news
Prompt: Develop an API call to retrieve the latest updates from the Pepecoin subreddit, specifically focusing on community growth and engagement.
Generated: DETERMINISTIC_5a30c592b0714a24
Batch ID: 20250612_160002
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.reddit.com/r/pepecoin/about.json": {
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

def fetch_pepecoin_subreddit_statistics():
    """
    Fetches the latest statistics related to community growth and engagement from the Pepecoin subreddit.

    Returns:
        dict: A dictionary containing subreddit statistics like subscriber count and active user count.
    """
    # Base URL for Reddit's API
    reddit_api_url = "https://www.reddit.com/r/pepecoin/about.json"

    # Set the headers to mimic a browser request
    headers = {
        "User-Agent": "PepecoinStatsBot/1.0"
    }

    try:
        # Make the GET request to Reddit's API
        response = requests.get(reddit_api_url, headers=headers)
        
        # Raise an exception if the request fails
        response.raise_for_status()

        # Parse the JSON response
        subreddit_data = response.json()

        # Extract relevant statistics from the response
        statistics = {
            "subscribers": subreddit_data["data"]["subscribers"],
            "active_users": subreddit_data["data"]["active_user_count"]
        }

        return statistics

    except requests.exceptions.RequestException as e:
        # Handle request-related errors (e.g., network issues, invalid URL)
        print(f"Error fetching data from Reddit API: {e}")
        return {"error": "Failed to fetch data from Reddit API"}

    except KeyError as e:
        # Handle missing keys in the JSON response
        print(f"Error parsing subreddit data: Missing key {e}")
        return {"error": "Unexpected API response structure"}

if __name__ == "__main__":
    # Fetch subreddit statistics
    stats = fetch_pepecoin_subreddit_statistics()

    # Print the retrieved statistics for debugging purposes
    print(stats)
```
