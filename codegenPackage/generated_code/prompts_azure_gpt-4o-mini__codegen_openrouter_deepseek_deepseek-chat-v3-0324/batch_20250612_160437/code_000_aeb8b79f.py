"""
Generated Code Metadata:
========================
Original URL: https://testungdhghh.blogspot.com
Prompt: Generate a code snippet for a simple blog post using Blogger's API.
Generated: DETERMINISTIC_aeb8b79fdc2f3ca2
Batch ID: 20250612_160437
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Environment variables for credentials
BLOGGER_API_KEY = os.getenv('BLOGGER_API_KEY')
BLOGGER_BLOG_ID = os.getenv('BLOGGER_BLOG_ID')
CREDENTIALS_FILE = 'credentials.json'  # Path to your OAuth 2.0 credentials file

def authenticate_blogger():
    """Authenticate with Blogger API using OAuth 2.0 credentials."""
    try:
        creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE)
        return build('blogger', 'v3', credentials=creds, developerKey=BLOGGER_API_KEY)
    except Exception as e:
        print(f"Authentication failed: {e}")
        return None

def create_blog_post(title, content):
    """Create a new blog post using Blogger API."""
    try:
        service = authenticate_blogger()
        if not service:
            return None
        
        body = {
            "kind": "blogger#post",
            "blog": {
                "id": BLOGGER_BLOG_ID
            },
            "title": title,
            "content": content
        }
        
        post = service.posts().insert(
            blogId=BLOGGER_BLOG_ID,
            body=body,
            isDraft=False
        ).execute()
        
        print(f"Post created with ID: {post['id']}")
        return post
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

# Example usage
if __name__ == "__main__":
    new_post = create_blog_post(
        title="My First Blog Post",
        content="This is the content of my first blog post using Blogger API."
    )
    
    if new_post:
        print(f"Post published at: {new_post.get('url', 'URL not available')}")
```
