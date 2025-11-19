"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://todosobreguitarra.com
Prompt: Write a Python script that fetches and displays guitar lesson videos from a YouTube channel, inspired by the resources available on Todo sobre Guitarra.
Generated: DETERMINISTIC_c48b61d4565c5dc4
Batch ID: 20250612_162051
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://www.youtube.com/watch?v={video_id": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/youtube/v3/search": {
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

# YouTube Data API v3 configuration
API_KEY = 'YOUR_YOUTUBE_API_KEY'  # Replace with your actual YouTube API key
CHANNEL_ID = 'YOUR_CHANNEL_ID'  # Replace with the desired YouTube channel ID
BASE_URL = 'https://www.googleapis.com/youtube/v3/search'

def fetch_guitar_lessons(api_key, channel_id):
    """
    Fetch guitar lesson videos from a specified YouTube channel.

    Args:
        api_key (str): YouTube Data API key for authorization.
        channel_id (str): The ID of the YouTube channel to fetch videos from.

    Returns:
        list: A list of dictionaries containing video titles and URLs.
    """
    # API parameters for the search request
    params = {
        'part': 'snippet',
        'channelId': channel_id,
        'maxResults': 10,  # Fetching the latest 10 videos
        'order': 'date',  # Ordering results by date
        'type': 'video',  # We only want videos
        'key': api_key
    }

    try:
        # Sending HTTP GET request to the YouTube API
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Raise an error for bad responses (4xx and 5xx)

        # Parsing the JSON response
        data = response.json()

        # Extracting video titles and URLs
        videos = []
        for item in data.get('items', []):
            video_title = item['snippet']['title']
            video_id = item['id']['videoId']
            video_url = f'https://www.youtube.com/watch?v={video_id}'
            videos.append({'title': video_title, 'url': video_url})

        return videos

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data from YouTube: {e}")
        return []

def display_videos(videos):
    """
    Display video titles and URLs.

    Args:
        videos (list): A list of dictionaries containing video details.
    """
    if not videos:
        print("No videos found.")
        return

    print("Guitar Lesson Videos:\n")
    for video in videos:
        print(f"Title: {video['title']}\nURL: {video['url']}\n")

def main():
    """
    Main function to fetch and display guitar lesson videos.
    """
    videos = fetch_guitar_lessons(API_KEY, CHANNEL_ID)
    display_videos(videos)

if __name__ == '__main__':
    main()
```

**Note:** Replace `YOUR_YOUTUBE_API_KEY` and `YOUR_CHANNEL_ID` with your actual YouTube Data API key and the target YouTube channel ID for the script to work correctly.
