"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jumperbillijumper.de
Prompt: How can I analyze the performance metrics of videos on Jumperbillijumper using YouTube's data API?
Generated: DETERMINISTIC_77e9e82ca930b2a4
Batch ID: 20250612_155938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import googleapiclient.discovery
from googleapiclient.errors import HttpError

def get_video_metrics(video_ids, api_key):
    """
    Retrieves performance metrics for the given list of YouTube video IDs using the YouTube Data API.

    Args:
        video_ids (list): List of YouTube video IDs to fetch metrics for.
        api_key (str): API key for authenticating with the YouTube Data API.

    Returns:
        dict: A dictionary mapping video IDs to performance metrics.
    """
    # Initialize the YouTube API client
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    video_metrics = {}

    try:
        # Fetch video statistics for the provided video IDs
        response = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(video_ids)
        ).execute()

        # Process the API response
        for item in response.get("items", []):
            video_id = item["id"]
            snippet = item["snippet"]
            statistics = item["statistics"]

            video_metrics[video_id] = {
                "title": snippet.get("title"),
                "published_at": snippet.get("publishedAt"),
                "view_count": statistics.get("viewCount", 0),
                "like_count": statistics.get("likeCount", 0),
                "comment_count": statistics.get("commentCount", 0)
            }

    except HttpError as e:
        print(f"An HTTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return video_metrics


if __name__ == "__main__":
    # Replace with your YouTube Data API key
    API_KEY = os.getenv("YOUTUBE_API_KEY")

    # Replace with video IDs you want to analyze
    VIDEO_IDS = [
        "dQw4w9WgXcQ",  # Example video ID
        "VIDEO_ID_2",
        "VIDEO_ID_3"
    ]

    if not API_KEY:
        print("Error: Please set the YOUTUBE_API_KEY environment variable.")
    else:
        metrics = get_video_metrics(VIDEO_IDS, API_KEY)
        print("Video Performance Metrics:")
        for video_id, data in metrics.items():
            print(f"Video ID: {video_id}")
            print(f"  Title: {data['title']}")
            print(f"  Published At: {data['published_at']}")
            print(f"  View Count: {data['view_count']}")
            print(f"  Like Count: {data['like_count']}")
            print(f"  Comment Count: {data['comment_count']}")
            print()
```
