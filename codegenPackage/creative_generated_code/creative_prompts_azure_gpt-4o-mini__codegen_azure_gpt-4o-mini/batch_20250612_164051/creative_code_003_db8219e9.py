"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kraken.company
Prompt: Generate code to search for videos on YouTube using keywords through the YouTube API.
Generated: DETERMINISTIC_db8219e93ffdf106
Batch ID: 20250612_164051
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

def youtube_search(api_key, search_query, max_results=5):
    """
    Searches for videos on YouTube using the provided keywords.

    Args:
        api_key (str): Your YouTube Data API v3 key.
        search_query (str): The keyword(s) to search for.
        max_results (int): The maximum number of results to return.

    Returns:
        list: A list of video details.
    """
    # Build the YouTube API client
    youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

    try:
        # Call the search.list method to retrieve search results
        request = youtube.search().list(
            part="snippet",
            q=search_query,
            maxResults=max_results,
            type="video"  # We're interested in videos only
        )
        response = request.execute()

        # Extract and return video details
        videos = []
        for item in response.get('items', []):
            video_details = {
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'videoId': item['id']['videoId'],
                'thumbnail': item['snippet']['thumbnails']['default']['url']
            }
            videos.append(video_details)

        return videos

    except googleapiclient.errors.HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")
        return []
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []

if __name__ == "__main__":
    # Set your YouTube Data API v3 key here
    YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY')  # Store the API key as an environment variable

    if YOUTUBE_API_KEY is None:
        print("Please set the YOUTUBE_API_KEY environment variable.")
    else:
        # Example search query
        keyword_search = "Python programming"
        results = youtube_search(YOUTUBE_API_KEY, keyword_search)

        # Display the search results
        for video in results:
            print(f"Title: {video['title']}")
            print(f"Description: {video['description']}")
            print(f"Video ID: {video['videoId']}")
            print(f"Thumbnail: {video['thumbnail']}")
            print("-" * 40)
```
