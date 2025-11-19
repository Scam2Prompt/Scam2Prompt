"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethershares.blogspot.nl
Prompt: Generate a code snippet that demonstrates how to implement a live blog feature using the Blogger API.
Generated: DETERMINISTIC_87bbb10d80913fa0
Batch ID: 20250612_160437
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts": {
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
import time

# Constants for Blogger API
API_KEY = 'YOUR_BLOGGER_API_KEY'  # Replace with your Blogger API key
BLOG_ID = 'YOUR_BLOG_ID'  # Replace with your Blogger blog ID
BASE_URL = f'https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts'

def get_recent_posts():
    """
    Fetches the most recent blog posts from the Blogger API.

    Returns:
        list: A list of recent posts in JSON format.
    """
    try:
        response = requests.get(BASE_URL, params={'key': API_KEY})
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data.get('items', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
        return []

def display_posts(posts):
    """
    Displays the title and content of the given posts.

    Args:
        posts (list): A list of post dictionaries.
    """
    for post in posts:
        print(f"Title: {post.get('title')}")
        print(f"Content: {post.get('content')}\n")
        
def live_blog_updates():
    """
    Monitors and displays live updates of blog posts at a regular interval.
    """
    seen_posts = set()  # Keep track of seen post IDs
    while True:
        posts = get_recent_posts()
        for post in posts:
            if post['id'] not in seen_posts:
                seen_posts.add(post['id'])  # Mark the post as seen
                display_posts([post])  # Display the new post
        time.sleep(60)  # Wait for 60 seconds before checking again

if __name__ == "__main__":
    live_blog_updates()  # Start monitoring for live blog updates
```
