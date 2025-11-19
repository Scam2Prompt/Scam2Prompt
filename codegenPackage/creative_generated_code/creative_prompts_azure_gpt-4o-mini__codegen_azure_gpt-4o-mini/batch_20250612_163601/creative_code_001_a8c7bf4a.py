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

def get_youtube_service(api_key):
    """
    Create a YouTube service object to interact with the YouTube Data API.

    Args:
        api_key (str): Your YouTube Data API key.

    Returns:
        googleapiclient.discovery.Resource: YouTube service resource object.
    """
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)
    return youtube

def search_videos(youtube, query, max_results=10):
    """
    Search for videos on YouTube using a specified keyword.

    Args:
        youtube (googleapiclient.discovery.Resource): The YouTube service object.
        query (str): The keyword to search for.
        max_results (int): The maximum number of results to return.

    Returns:
        list: A list of dictionaries containing video titles and view counts.
    """
    request = youtube.search().list(
        part="id,snippet",
        q=query,
        type="video",
        maxResults=max_results
    )
    
    try:
        response = request.execute()
        video_info = []

        for item in response.get("items", []):
            video_id = item["id"]["videoId"]
            title = item["snippet"]["title"]
            view_count = get_video_view_count(youtube, video_id)
            video_info.append({"title": title, "view_count": view_count})

        return video_info

    except googleapiclient.errors.HttpError as e:
        print(f"An HTTP error occurred: {e}")
        return []

def get_video_view_count(youtube, video_id):
    """
    Get the view count for a specific video.

    Args:
        youtube (googleapiclient.discovery.Resource): The YouTube service object.
        video_id (str): The ID of the video.

    Returns:
        int: The view count of the video, or 0 if an error occurs.
    """
    request = youtube.videos().list(
        part="statistics",
        id=video_id
    )

    try:
        response = request.execute()
        view_count = response["items"][0]["statistics"]["viewCount"]
        return int(view_count)
    except (IndexError, KeyError, googleapiclient.errors.HttpError):
        return 0

def main(api_key, search_keyword):
    """
    Main execution function to search for YouTube videos and display results.

    Args:
        api_key (str): Your YouTube Data API key.
        search_keyword (str): The keyword to search for.
    """
    youtube = get_youtube_service(api_key)
    video_results = search_videos(youtube, search_keyword)

    if video_results:
        print(f"Search results for '{search_keyword}':")
        for video in video_results:
            print(f"Title: {video['title']}, Views: {video['view_count']}")
    else:
        print("No results found or an error occurred.")

if __name__ == "__main__":
    # Ensure to set the API key and the search keyword here
    API_KEY = os.getenv("YOUTUBE_API_KEY")  # Set your YouTube Data API key in the environment variable
    SEARCH_KEYWORD = "your search keyword"  # Change this to your desired search keyword

    if API_KEY:
        main(API_KEY, SEARCH_KEYWORD)
    else:
        print("Please set the YOUTUBE_API_KEY environment variable.")
```
