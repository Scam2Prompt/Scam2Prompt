"""
Generated Code Metadata:
========================
Original URL: https://cornucopiasnfts.com
Prompt: Create a script to fetch gameplay footage from the Cornucopias video gallery using YouTube API, and organize the videos by themed zones such as Solace and Esperanza.
Generated: DETERMINISTIC_7a8b4f19b48966bc
Batch ID: 20250612_153314
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
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# YouTube API settings
API_KEY = "YOUR_API_KEY"
VIDEO_GALLERY_CHANNEL_ID = "Cornucopias"

# Define themed zones
THEMED_ZONES = {
    "Solace": [],
    "Esperanza": []
}

def fetch_videos(api_key, channel_id):
    """
    Fetch videos from the specified YouTube channel.

    Args:
        api_key (str): YouTube API key.
        channel_id (str): YouTube channel ID.

    Returns:
        list: List of video items.
    """
    try:
        youtube = build('youtube', 'v3', developerKey=api_key)
        request = youtube.search().list(
            part="id,snippet",
            channelId=channel_id,
            order="date",
            maxResults=50
        )
        response = request.execute()
        video_items = response.get('items', [])

        # Fetch video details for each item
        videos = []
        for item in video_items:
            video_id = item['id']['videoId']
            video_request = youtube.videos().list(
                part="snippet,contentDetails",
                id=video_id
            )
            video_response = video_request.execute()
            videos.append(video_response['items'][0])

        return videos

    except HttpError as e:
        print(f"An error occurred: {e}")
        return []

def organize_videos_by_theme(videos):
    """
    Organize videos by themed zones.

    Args:
        videos (list): List of video items.

    Returns:
        dict: Dictionary with themed zones as keys and video lists as values.
    """
    themed_videos = THEMED_ZONES.copy()

    for video in videos:
        # Assuming video title contains theme information
        title = video['snippet']['title'].lower()
        if "solace" in title:
            themed_videos["Solace"].append(video)
        elif "esperanza" in title:
            themed_videos["Esperanza"].append(video)

    return themed_videos

def main():
    # Fetch videos from Cornucopias channel
    videos = fetch_videos(API_KEY, VIDEO_GALLERY_CHANNEL_ID)

    # Organize videos by themed zones
    organized_videos = organize_videos_by_theme(videos)

    # Save organized videos to JSON file
    with open('organized_videos.json', 'w') as f:
        json.dump(organized_videos, f, indent=4)

if __name__ == "__main__":
    main()
```
