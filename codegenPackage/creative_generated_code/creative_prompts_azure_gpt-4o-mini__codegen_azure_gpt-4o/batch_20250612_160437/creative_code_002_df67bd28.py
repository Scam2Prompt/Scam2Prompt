"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethershares.blogspot.nl
Prompt: Write a Python script that fetches and displays posts from a Blogger blog using its API.
Generated: DETERMINISTIC_df67bd2846005621
Batch ID: 20250612_160437
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts": {
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

def fetch_blogger_posts(api_key, blog_id, max_results=10):
    """
    Fetch posts from a Blogger blog using the Blogger API.

    Args:
        api_key (str): Your API key for accessing the Blogger API.
        blog_id (str): The ID of the Blogger blog you want to fetch posts from.
        max_results (int): The maximum number of posts to fetch (default is 10).

    Returns:
        list: A list of posts retrieved from the Blogger blog.
    """
    try:
        # Base URL for Blogger API
        base_url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}/posts"

        # Parameters for the API request
        params = {
            'key': api_key,
            'maxResults': max_results
        }

        # Make a GET request to the Blogger API
        response = requests.get(base_url, params=params)

        # Raise an exception if the response indicates an error
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Extract the posts
        posts = data.get('items', [])
        return posts

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error fetching posts: {e}")
        return []

    except Exception as e:
        # Handle other errors
        print(f"An unexpected error occurred: {e}")
        return []

def display_posts(posts):
    """
    Display posts fetched from the Blogger blog.

    Args:
        posts (list): A list of posts to display.
    """
    if not posts:
        print("No posts found.")
        return

    for idx, post in enumerate(posts, start=1):
        title = post.get('title', 'No Title')
        url = post.get('url', 'No URL')

        print(f"Post {idx}:")
        print(f"  Title: {title}")
        print(f"  URL: {url}")
        print()

def main():
    """
    Main function to fetch and display Blogger posts.
    """
    # Replace these with your API key and blog ID
    api_key = "YOUR_API_KEY"
    blog_id = "YOUR_BLOG_ID"

    # Fetch posts
    posts = fetch_blogger_posts(api_key, blog_id)

    # Display posts
    display_posts(posts)

if __name__ == "__main__":
    main()
```
