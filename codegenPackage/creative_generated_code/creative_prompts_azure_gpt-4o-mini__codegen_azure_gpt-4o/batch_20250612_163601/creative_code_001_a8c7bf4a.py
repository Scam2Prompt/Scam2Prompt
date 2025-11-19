"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stbot.xyz
Prompt: "Write a Python script that utilizes the YouTube Data API to search for videos based on a keyword and return their titles and view counts."
Generated: DETERMINISTIC_a8c7bf4a893521a3
Batch ID: 20250612_163601
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
import googleapiclient.errors
from googleapiclient.discovery import build

# Function to search YouTube videos based on a keyword
def search_youtube_videos(api_key, query, max_results=10):
    """
    Search for YouTube videos based on a keyword and return their titles and view counts.

    Args:
        api_key (str): The YouTube Data API key.
        query (str): The search query (keyword).
        max_results (int): Maximum number of results to return.

    Returns:
        list of dict: A list of dictionaries containing video titles and view counts.
    """
    try:
        # Build the YouTube API client
        youtube = build("youtube", "v3", developerKey=api_key)

        # Call the YouTube API to search for videos
        search_response = youtube.search().list(
            q=query,         # The search keyword
            part="id,snippet",
            maxResults=max_results,
            type="video"     # Only search for videos
        ).execute()

        # Extract video IDs from the search results
        video_ids = [item['id']['videoId'] for item in search_response.get('items', [])]

        if not video_ids:
            print(f"No videos found for query: {query}")
            return []

        # Call the API to fetch video details (e.g., view count) for the video IDs
        video_response = youtube.videos().list(
            part="snippet,statistics",
            id=",".join(video_ids)
        ).execute()

        # Extract video titles and view counts
        videos = []
        for video in video_response.get('items', []):
            title = video['snippet']['title']
            view_count = int(video['statistics'].get('viewCount', 0))  # Default to 0 if missing
            videos.append({"title": title, "view_count": view_count})

        return videos

    except googleapiclient.errors.HttpError as e:
        print(f"An HTTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    return []


# Main function to demonstrate the script
if __name__ == "__main__":
    # Ensure you replace 'YOUR_API_KEY' with your actual YouTube Data API key
    API_KEY = "YOUR_API_KEY"

    # Prompt the user for a search keyword
    keyword = input("Enter a keyword to search for YouTube videos: ").strip()

    # Search for videos and print the results
    videos = search_youtube_videos(API_KEY, keyword)
    if videos:
        print(f"\nTop {len(videos)} videos for the keyword '{keyword}':\n")
        for idx, video in enumerate(videos, 1):
            print(f"{idx}. {video['title']} (Views: {video['view_count']})")
    else:
        print("No results found.")
```
