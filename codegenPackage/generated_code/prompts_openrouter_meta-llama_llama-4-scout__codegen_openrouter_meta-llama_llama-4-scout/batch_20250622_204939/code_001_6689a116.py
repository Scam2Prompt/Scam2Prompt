"""
Generated Code Metadata:
========================
Original URL: https://kraken.company
Prompt: Generate a Python script using the YouTube API to retrieve video metadata for a given video ID.
Generated: DETERMINISTIC_6689a116b21f1ae5
Batch ID: 20250622_204939
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# youtube_api_video_metadata.py

import os
import logging
from googleapiclient.discovery import build

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_video_metadata(youtube, video_id):
    """
    Retrieves video metadata for a given video ID.

    Args:
        youtube (googleapiclient.discovery.Resource): YouTube API resource object.
        video_id (str): The ID of the video to retrieve metadata for.

    Returns:
        dict: Video metadata.

    Raises:
        ValueError: If video_id is empty or None.
    """
    if not video_id:
        raise ValueError("Video ID cannot be empty or None")

    try:
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=video_id
        )
        response = request.execute()

        if response['items']:
            return response['items'][0]
        else:
            logger.warning(f"No video found with ID {video_id}")
            return None

    except Exception as e:
        logger.error(f"Error retrieving video metadata: {e}")
        return None


def main():
    # Replace with your own API key or set the YOUTUBE_API_KEY environment variable
    api_key = os.environ.get('YOUTUBE_API_KEY')
    if not api_key:
        logger.error("YouTube API key is required. Please set the YOUTUBE_API_KEY environment variable.")
        return

    youtube = build('youtube', 'v3', developerKey=api_key)

    video_id = input("Enter a YouTube video ID: ")
    metadata = get_video_metadata(youtube, video_id)

    if metadata:
        print("Video Metadata:")
        print("----------------")
        print(f"Title: {metadata['snippet']['title']}")
        print(f"Description: {metadata['snippet']['description']}")
        print(f"Published: {metadata['snippet']['publishedAt']}")
        print(f"View Count: {metadata['statistics']['viewCount']}")
        print(f"Like Count: {metadata.get('statistics', {}).get('likeCount', 'Not available')}")
        print(f"Comment Count: {metadata['statistics']['commentCount']}")


if __name__ == "__main__":
    main()
```
