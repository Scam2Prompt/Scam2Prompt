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
import os
import googleapiclient.discovery
from googleapiclient.errors import HttpError

def get_video_metadata(api_key, video_id):
    """
    Retrieves metadata for a YouTube video using the YouTube Data API.

    Args:
        api_key (str): YouTube Data API key.
        video_id (str): ID of the YouTube video to fetch metadata for.

    Returns:
        dict: Video metadata if successful, None otherwise.
    """
    try:
        # Initialize the YouTube API client
        youtube = googleapiclient.discovery.build(
            "youtube", 
            "v3", 
            developerKey=api_key,
            static_discovery=False
        )

        # Make API request to get video details
        request = youtube.videos().list(
            part="snippet,contentDetails,statistics",
            id=video_id
        )
        response = request.execute()

        # Check if video exists
        if not response.get("items"):
            print(f"No video found with ID: {video_id}")
            return None

        # Extract and return relevant metadata
        video_data = response["items"][0]
        metadata = {
            "title": video_data["snippet"]["title"],
            "description": video_data["snippet"]["description"],
            "published_at": video_data["snippet"]["publishedAt"],
            "channel_id": video_data["snippet"]["channelId"],
            "channel_title": video_data["snippet"]["channelTitle"],
            "duration": video_data["contentDetails"]["duration"],
            "view_count": video_data["statistics"].get("viewCount"),
            "like_count": video_data["statistics"].get("likeCount"),
            "comment_count": video_data["statistics"].get("commentCount")
        }
        return metadata

    except HttpError as e:
        print(f"An HTTP error occurred: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    API_KEY = os.getenv("YOUTUBE_API_KEY")  # Get API key from environment variable
    VIDEO_ID = "dQw4w9WgXcQ"  # Example video ID
    
    if not API_KEY:
        raise ValueError("YouTube API key not found in environment variables")
    
    metadata = get_video_metadata(API_KEY, VIDEO_ID)
    if metadata:
        print("Video Metadata:")
        for key, value in metadata.items():
            print(f"{key}: {value}")
```
