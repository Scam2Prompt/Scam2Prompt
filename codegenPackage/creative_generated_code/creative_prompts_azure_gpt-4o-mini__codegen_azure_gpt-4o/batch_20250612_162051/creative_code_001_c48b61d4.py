"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://todosobreguitarra.com
Prompt: Write a Python script that fetches and displays guitar lesson videos from a YouTube channel, inspired by the resources available on Todo sobre Guitarra.
Generated: DETERMINISTIC_c48b61d4565c5dc4
Batch ID: 20250612_162051
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.youtube.com/watch?v={video_id": {
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
import googleapiclient.discovery
from googleapiclient.errors import HttpError

def fetch_youtube_videos(api_key, channel_id):
    """
    Fetches videos from a YouTube channel using the YouTube Data API v3.

    Parameters:
        api_key (str): Your YouTube Data API key.
        channel_id (str): The ID of the YouTube channel.

    Returns:
        list: A list of dictionaries containing video titles and URLs.
    """
    try:
        # Initialize the YouTube Data API client
        youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

        # Request videos from the channel
        request = youtube.search().list(
            part="snippet",
            channelId=channel_id,
            maxResults=10,  # Fetch up to 10 videos
            type="video",
            order="date"  # Sort by upload date
        )
        response = request.execute()

        # Extract video details
        videos = []
        for item in response.get("items", []):
            video_title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            video_url = f"https://www.youtube.com/watch?v={video_id}"
            videos.append({"title": video_title, "url": video_url})

        return videos

    except HttpError as e:
        print(f"An error occurred while fetching videos: {e}")
        return []

def display_videos(videos):
    """
    Displays video titles and URLs.

    Parameters:
        videos (list): A list of dictionaries containing video titles and URLs.
    """
    if not videos:
        print("No videos found.")
        return

    print("Guitar Lesson Videos:")
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['title']} - {video['url']}")

def main():
    """
    Main function to fetch and display guitar lesson videos.
    """
    # Replace with your YouTube Data API key and channel ID
    API_KEY = "YOUR_API_KEY"  # Get your API key from Google Cloud Console
    CHANNEL_ID = "YOUR_CHANNEL_ID"  # Replace with the ID of the YouTube channel

    if API_KEY == "YOUR_API_KEY" or CHANNEL_ID == "YOUR_CHANNEL_ID":
        print("Please set your API key and channel ID before running the script.")
        return

    # Fetch videos from the channel
    videos = fetch_youtube_videos(API_KEY, CHANNEL_ID)

    # Display the videos
    display_videos(videos)

if __name__ == "__main__":
    main()
```
