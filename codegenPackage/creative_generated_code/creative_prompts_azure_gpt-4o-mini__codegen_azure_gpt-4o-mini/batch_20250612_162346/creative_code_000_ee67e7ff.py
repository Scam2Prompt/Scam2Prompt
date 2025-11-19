"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ccvrgwc498cas1f.blogspot.com
Prompt: Generate a code snippet that demonstrates how to create a simple blog using Blogger, referencing the theme images by Michael Elkan.
Generated: DETERMINISTIC_ee67e7ff70740a04
Batch ID: 20250612_162346
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/path/to/michael_elkan_theme_image.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/": {
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

# Constants for Blogger API access
API_KEY = 'YOUR_API_KEY'  # Replace with your actual Blogger API key
BLOG_ID = 'YOUR_BLOG_ID'   # Replace with your actual Blog ID
BASE_URL = f'https://www.googleapis.com/blogger/v3/blogs/{BLOG_ID}/posts/'

# Function to create a new blog post
def create_blog_post(title, content, labels=None, image_url=None):
    """
    Creates a new blog post on Blogger.
    
    :param title: Title of the blog post
    :param content: Content of the blog post in HTML format
    :param labels: List of labels for the post (optional)
    :param image_url: URL of the image to include in the post (optional)
    :return: Response from the Blogger API
    """
    # Prepare the post data
    post_data = {
        'kind': 'blogger#post',
        'title': title,
        'content': content,
        'labels': labels if labels else [],
    }
    
    # Add image if provided
    if image_url:
        post_data['images'] = [{'url': image_url}]
    
    try:
        # Make the API request to create the post
        response = requests.post(
            BASE_URL,
            params={'key': API_KEY},
            headers={'Content-Type': 'application/json'},
            data=json.dumps(post_data)
        )
        
        # Check for successful response
        response.raise_for_status()
        print("Post created successfully!")
        return response.json()
    
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Log HTTP error
    except Exception as err:
        print(f"An error occurred: {err}")  # Log other errors

# Example usage
if __name__ == '__main__':
    post_title = "My First Blog Post"
    post_content = "<p>This is the content of my first blog post!</p><img src='IMAGE_URL' />"  # Replace IMAGE_URL with the actual image URL
    post_labels = ["Introduction", "FirstPost"]
    theme_image_url = "https://example.com/path/to/michael_elkan_theme_image.jpg"  # Replace with an image from Michael Elkan's themes

    # Create a new blog post
    create_blog_post(post_title, post_content, post_labels, theme_image_url)
```
