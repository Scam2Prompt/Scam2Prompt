"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getafreehomedelivary.blogspot.com
Prompt: Write a Python script that utilizes the Blogger API to fetch and display posts from a Blogger site.
Generated: DETERMINISTIC_29e57e03209c8a72
Batch ID: 20250612_155340
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/blogger/v3/blogs": {
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

# Constants for Blogger API
API_BASE_URL = "https://www.googleapis.com/blogger/v3/blogs"
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
BLOG_ID = "YOUR_BLOG_ID"  # Replace with your Blogger blog ID

def fetch_posts(blog_id, api_key):
    """
    Fetches posts from a Blogger blog using the Blogger API.

    Args:
        blog_id (str): The ID of the Blogger blog.
        api_key (str): The API key for accessing the Blogger API.

    Returns:
        list: A list of posts retrieved from the Blogger blog.
    """
    try:
        # Construct the URL to fetch posts
        url = f"{API_BASE_URL}/{blog_id}/posts?key={api_key}"
        response = requests.get(url)

        # Check if the request was successful
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        # Extract posts from the response
        posts = data.get("items", [])
        return posts
    except requests.exceptions.RequestException as e:
        print(f"Error fetching posts: {e}")
    except json.JSONDecodeError:
        print("Error decoding JSON response.")
    return []  # Return an empty list if an error occurs

def display_posts(posts):
    """
    Displays the fetched posts in a readable format.

    Args:
        posts (list): A list of posts to display.
    """
    if not posts:
        print("No posts available.")
        return

    print(f"Found {len(posts)} posts:\n")
    for index, post in enumerate(posts, start=1):
        title = post.get("title", "Untitled")
        published = post.get("published", "Unknown")
        url = post.get("url", "No URL available")
        print(f"Post {index}:")
        print(f"  Title: {title}")
        print(f"  Published: {published}")
        print(f"  URL: {url}\n")

def main():
    """
    Main function to fetch and display posts from a Blogger blog.
    """
    print("Fetching posts from Blogger...")
    posts = fetch_posts(BLOG_ID, API_KEY)
    display_posts(posts)

if __name__ == "__main__":
    # Entry point of the script
    main()
```

**Notes:**
- Replace `YOUR_API_KEY` and `YOUR_BLOG_ID` with your actual Blogger API key and blog ID.
- Ensure you have the `requests` library installed (`pip install requests`) before running this script.
