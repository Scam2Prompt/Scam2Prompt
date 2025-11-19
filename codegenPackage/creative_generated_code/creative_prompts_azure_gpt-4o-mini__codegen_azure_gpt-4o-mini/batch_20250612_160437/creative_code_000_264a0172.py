"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rerfiet.blogspot.com
Prompt: What are some best practices for setting up a blog on Blogger, including API integration?
Generated: DETERMINISTIC_264a01728044229b
Batch ID: 20250612_160437
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.googleapis.com/blogger/v3/blogs/{self.blog_id}/posts/": {
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

class BloggerAPI:
    """
    A class to interact with the Blogger API for creating and managing blog posts.
    """

    def __init__(self, api_key, blog_id):
        """
        Initializes the BloggerAPI instance with API key and blog ID.

        Parameters:
            api_key (str): Your Blogger API key.
            blog_id (str): The ID of your Blogger blog.
        """
        self.api_key = api_key
        self.blog_id = blog_id
        self.base_url = f"https://www.googleapis.com/blogger/v3/blogs/{self.blog_id}/posts/"

    def create_post(self, title, content):
        """
        Creates a new blog post.

        Parameters:
            title (str): The title of the blog post.
            content (str): The content of the blog post.

        Returns:
            dict: The response from the API containing the created post information.
        """
        try:
            # Prepare the post data
            post_data = {
                'kind': 'blogger#post',
                'title': title,
                'content': content
            }
            # Make the API request to create a new post
            response = requests.post(
                self.base_url + "?key=" + self.api_key,
                json=post_data
            )
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the created post data
        except requests.exceptions.RequestException as e:
            print(f"Error creating post: {e}")
            return None

    def get_posts(self):
        """
        Retrieves all posts from the blog.

        Returns:
            list: A list of blog posts.
        """
        try:
            # Make the API request to retrieve posts
            response = requests.get(self.base_url + "?key=" + self.api_key)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json().get('items', [])  # Return the list of posts
        except requests.exceptions.RequestException as e:
            print(f"Error retrieving posts: {e}")
            return []

if __name__ == "__main__":
    # Example usage of the BloggerAPI class
    API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
    BLOG_ID = "YOUR_BLOG_ID"  # Replace with your actual blog ID

    # Create a Blogger API client
    blogger_client = BloggerAPI(API_KEY, BLOG_ID)

    # Create a new blog post
    new_post = blogger_client.create_post("My First Blog Post", "<p>This is the content of my first post!</p>")
    if new_post:
        print("Post created successfully:", new_post)

    # Retrieve and print all blog posts
    posts = blogger_client.get_posts()
    print("Retrieved posts:", posts)
```
