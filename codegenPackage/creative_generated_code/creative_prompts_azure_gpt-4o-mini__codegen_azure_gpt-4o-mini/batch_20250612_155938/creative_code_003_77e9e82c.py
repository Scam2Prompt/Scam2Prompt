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
import googleapiclient.errors

# Define the YouTube API key and the video IDs to analyze
API_KEY = os.getenv('YOUTUBE_API_KEY')  # Ensure the API key is stored in an environment variable
VIDEO_IDS = ['VIDEO_ID_1', 'VIDEO_ID_2']  # Replace with actual video IDs

def get_youtube_service():
    """
    Initializes the YouTube API service object.
    
    Returns:
        googleapiclient.discovery.Resource: YouTube API service object.
    """
    youtube_service = googleapiclient.discovery.build('youtube', 'v3', developerKey=API_KEY)
    return youtube_service

def get_video_metrics(youtube_service, video_ids):
    """
    Fetches performance metrics for the given video IDs.
    
    Args:
        youtube_service (Resource): The YouTube API service object.
        video_ids (list): List of video IDs to fetch metrics for.

    Returns:
        list: List of metrics for each video.
    """
    try:
        # Making the API call to fetch video statistics
        request = youtube_service.videos().list(
            part='statistics',
            id=','.join(video_ids)
        )
        response = request.execute()
        
        # Extracting statistics from response
        metrics = []
        for item in response.get('items', []):
            stats = item.get('statistics', {})
            metrics.append({
                'video_id': item['id'],
                'view_count': stats.get('viewCount', 0),
                'like_count': stats.get('likeCount', 0),
                'dislike_count': stats.get('dislikeCount', 0),
                'comment_count': stats.get('commentCount', 0),
            })
        return metrics

    except googleapiclient.errors.HttpError as e:
        print(f"An HTTP error occurred: {e}")
        return []

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    """
    Main function to execute the video metrics retrieval process.
    """
    youtube_service = get_youtube_service()
    metrics = get_video_metrics(youtube_service, VIDEO_IDS)

    # Print out the gathered metrics for each video
    for metric in metrics:
        print(f"Video ID: {metric['video_id']}")
        print(f"Views: {metric['view_count']}")
        print(f"Likes: {metric['like_count']}")
        print(f"Dislikes: {metric['dislike_count']}")
        print(f"Comments: {metric['comment_count']}")
        print("-" * 30)

if __name__ == "__main__":
    main()
```
