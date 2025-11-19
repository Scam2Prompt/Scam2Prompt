"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getafreehomedelivary.blogspot.com
Prompt: Generate a code snippet for a simple blog setup using Blogger API that allows for post management.
Generated: DETERMINISTIC_7994bbe3aa728023
Batch ID: 20250612_155340
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/blogger/v3/blogs/{blog_id": {
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

class BloggerAPIClient:
    """
    A simple client to interact with the Blogger API for post management.
    """
    
    def __init__(self, api_key, blog_id):
        """
        Initialize the Blogger API client.

        :param api_key: API key for authenticating the requests.
        :param blog_id: ID of the blog to manage posts.
        """
        self.api_key = api_key
        self.blog_id = blog_id
        self.base_url = f"https://www.googleapis.com/blogger/v3/blogs/{blog_id}"

    def create_post(self, title, content):
        """
        Create a new post on the blog.

        :param title: Title of the blog post.
        :param content: Content of the blog post.
        :return: Response from the API.
        """
        url = f"{self.base_url}/posts?key={self.api_key}"
        payload = {
            "title": title,
            "content": content
        }
        try:
            response = requests.post(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error creating post: {e}")
            return None

    def get_posts(self):
        """
        Retrieve all posts from the blog.

        :return: List of posts or None in case of an error.
        """
        url = f"{self.base_url}/posts?key={self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json().get("items", [])
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving posts: {e}")
            return None

    def update_post(self, post_id, title, content):
        """
        Update an existing post on the blog.

        :param post_id: ID of the post to update.
        :param title: Updated title of the blog post.
        :param content: Updated content of the blog post.
        :return: Response from the API.
        """
        url = f"{self.base_url}/posts/{post_id}?key={self.api_key}"
        payload = {
            "title": title,
            "content": content
        }
        try:
            response = requests.put(url, json=payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error updating post: {e}")
            return None

    def delete_post(self, post_id):
        """
        Delete a post from the blog.

        :param post_id: ID of the post to delete.
        :return: True if the post was deleted successfully, False otherwise.
        """
        url = f"{self.base_url}/posts/{post_id}?key={self.api_key}"
        try:
            response = requests.delete(url)
            response.raise_for_status()
            return response.status_code == 204
        except requests.exceptions.RequestException as e:
            print(f"Error deleting post: {e}")
            return False


# Example usage:
if __name__ == "__main__":
    # Replace with your Blogger API key and Blog ID
    API_KEY = "your_api_key_here"
    BLOG_ID = "your_blog_id_here"
    
    client = BloggerAPIClient(API_KEY, BLOG_ID)

    # Create a post
    new_post = client.create_post("Test Title", "This is a test content.")
    if new_post:
        print("Created Post:", new_post)

    # Get all posts
    posts = client.get_posts()
    if posts:
        print("Posts:", posts)

    # Update a post
    if posts:
        updated_post = client.update_post(posts[0]['id'], "Updated Title", "Updated Content")
        if updated_post:
            print("Updated Post:", updated_post)

    # Delete the first post
    if posts:
        success = client.delete_post(posts[0]['id'])
        print("Deleted Post:", success)
```
