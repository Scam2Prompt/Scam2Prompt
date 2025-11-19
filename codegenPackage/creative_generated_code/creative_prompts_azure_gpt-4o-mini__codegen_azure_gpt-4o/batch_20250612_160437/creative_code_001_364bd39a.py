"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rerfiet.blogspot.com
Prompt: How can I use Blogger's API to automate post creation and management?
Generated: DETERMINISTIC_364bd39a6a75348d
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
from datetime import datetime

# Define constants for the Blogger API
API_KEY = "your_blogger_api_key"  # Replace with your Blogger API key
BLOG_ID = "your_blog_id"  # Replace with your Blog ID
BASE_URL = f"https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts"

# Function to create a new blog post
def create_post(title, content, labels=None):
    """
    Creates a new blog post using the Blogger API.

    Args:
        title (str): The title of the blog post.
        content (str): The HTML content of the blog post.
        labels (list, optional): A list of labels to tag the post with.

    Returns:
        dict: The response JSON from the Blogger API.
    """
    # Prepare the post data
    post_data = {
        "kind": "blogger#post",
        "title": title,
        "content": content
    }

    # Add labels if provided
    if labels:
        post_data["labels"] = labels

    try:
        # Send the POST request to create the blog post
        response = requests.post(
            BASE_URL,
            params={"key": API_KEY},
            json=post_data,
            headers={"Content-Type": "application/json"}
        )

        # Check if the request was successful
        response.raise_for_status()  # Raise error for HTTP errors
        return response.json()  # Return the API response
    except requests.exceptions.RequestException as e:
        # Handle any HTTP or network-related errors
        print(f"Error creating post: {e}")
        return None


# Function to get a list of blog posts
def get_posts():
    """
    Retrieves a list of blog posts from the Blogger API.

    Returns:
        dict: The response JSON containing the list of blog posts.
    """
    try:
        # Send the GET request to fetch posts
        response = requests.get(
            BASE_URL,
            params={"key": API_KEY},
            headers={"Content-Type": "application/json"}
        )

        # Check if the request was successful
        response.raise_for_status()  # Raise error for HTTP errors
        return response.json()  # Return the API response
    except requests.exceptions.RequestException as e:
        # Handle any HTTP or network-related errors
        print(f"Error retrieving posts: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Create a new post
    new_post = create_post(
        title="Automating Blogger API Post Creation",
        content="<p>This is a sample post created using the Blogger API.</p>",
        labels=["API", "Automation", "Python"]
    )

    if new_post:
        print("Post created successfully!")
        print("Post Details:", new_post)

    # Fetch and display existing posts
    posts = get_posts()
    if posts:
        print("\nExisting Posts:")
        for post in posts.get("items", []):
            print(f"- {post['title']} (Published on {post['published']})")
```

### Notes:
- Replace `your_blogger_api_key` and `your_blog_id` with your actual Blogger API key and Blog ID.
- Ensure you have enabled the Blogger API in your Google Cloud Console and have proper authentication setup.
- Install the `requests` package if not already installed (`pip install requests`).
