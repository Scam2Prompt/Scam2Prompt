"""
Generated Code Metadata:
========================
Original URL: https://usweb09.us
Prompt: Generate a Python script using the WordPress REST API to create a new post on a WordPress site with the title "About" and a brief FAQ section.
Generated: DETERMINISTIC_70d677cc0dc1addd
Batch ID: 20250622_212519
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-wordpress-site.com/wp-json/wp/v2/posts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json

# Configuration
WP_API_URL = 'https://your-wordpress-site.com/wp-json/wp/v2/posts'
WP_API_USERNAME = 'your-username'
WP_API_PASSWORD = 'your-password'

def create_post(title, content):
    """
    Create a new post on the WordPress site using the WordPress REST API.

    Args:
        title (str): The title of the post.
        content (str): The content of the post.

    Returns:
        dict: The created post data.
    """
    # Authenticate using Basic Auth
    auth = (WP_API_USERNAME, WP_API_PASSWORD)

    # Post data
    post_data = {
        'title': title,
        'status': 'publish',
        'content': content,
        'format': 'standard'
    }

    try:
        # Send POST request to create a new post
        response = requests.post(WP_API_URL, auth=auth, data=json.dumps(post_data), headers={'Content-Type': 'application/json'})

        # Check if the request was successful
        if response.status_code == 201:
            return response.json()
        else:
            print(f"Failed to create post. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def main():
    title = "About"
    content = """
    <p>Frequently Asked Questions:</p>
    <ul>
        <li>Q: What is this site about?</li>
        <li>A: This site is about example content.</li>
    </ul>
    """
    created_post = create_post(title, content)

    if created_post:
        print("Post created successfully!")
        print(json.dumps(created_post, indent=4))

if __name__ == "__main__":
    main()
```
