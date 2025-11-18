"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hieroglyphics.com
Prompt: Write a script using the YouTube Data API to fetch and display the latest videos uploaded by the Hieroglyphics Crew.
Generated: DETERMINISTIC_159180ffbbd67e46
Batch ID: 20250612_145121
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/youtube/v3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.youtube.com/watch?v={video": {
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
import requests

# You need to replace this with your own YouTube Data API v3 key.
API_KEY = 'YOUR_YOUTUBE_API_KEY'

# The channel ID for Hieroglyphics Crew. Replace with the actual channel ID.
CHANNEL_ID = 'UC...'

# Base URL for the YouTube Data API
BASE_URL = 'https://www.googleapis.com/youtube/v3'

def fetch_latest_videos(channel_id, api_key, max_results=5):
    """
    Fetches the latest videos uploaded by a YouTube channel.

    Args:
        channel_id (str): The ID of the YouTube channel.
        api_key (str): Your YouTube Data API v3 key.
        max_results (int): The maximum number of videos to fetch.

    Returns:
        list: A list of video details (title, videoId, description).
    """
    try:
        # Build the API endpoint for search
        endpoint = f"{BASE_URL}/search"
        params = {
            'part': 'snippet',
            'channelId': channel_id,
            'maxResults': max_results,
            'order': 'date',
            'type': 'video',
            'key': api_key
        }

        # Make the request
        response = requests.get(endpoint, params=params)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

        # Parse the response
        data = response.json()

        # Extract video information
        videos = []
        for item in data.get('items', []):
            video = {
                'title': item['snippet']['title'],
                'videoId': item['id']['videoId'],
                'description': item['snippet']['description'],
                'publishedAt': item['snippet']['publishedAt']
            }
            videos.append(video)
        
        return videos

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching videos: {e}")
        return []

def display_videos(videos):
    """
    Displays a list of videos with their titles and YouTube URLs.

    Args:
        videos (list): A list of video details.
    """
    if not videos:
        print("No videos found.")
        return
    
    print("Latest Videos:")
    for video in videos:
        print(f"Title: {video['title']}")
        print(f"URL: https://www.youtube.com/watch?v={video['videoId']}")
        print(f"Published At: {video['publishedAt']}")
        print(f"Description: {video['description']}")
        print("-" * 80)

if __name__ == '__main__':
    # Fetch the latest videos
    latest_videos = fetch_latest_videos(CHANNEL_ID, API_KEY)

    # Display the videos
    display_videos(latest_videos)
```

### Notes:
1. Replace `'YOUR_YOUTUBE_API_KEY'` with your actual YouTube API Key.
2. Replace `'UC...'` with the actual channel ID for Hieroglyphics Crew.
3. Install the `requests` library if you haven't already by running `pip install requests`.
4. Ensure you have appropriate error handling in place if the API key or channel ID is invalid.
