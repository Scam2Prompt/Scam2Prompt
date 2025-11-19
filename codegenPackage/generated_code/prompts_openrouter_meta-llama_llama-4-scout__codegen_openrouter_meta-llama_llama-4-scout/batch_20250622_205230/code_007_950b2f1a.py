"""
Generated Code Metadata:
========================
Original URL: https://pooledether.io
Prompt: How can I use Blogger's API to programmatically publish blog posts, and what are the advantages of using Blogger for blogging?
Generated: DETERMINISTIC_950b2f1a7df91ea9
Batch ID: 20250622_205230
URLs Found: 5
Malicious URLs: 0

Oracle Results:
{
  "https://accounts.google.com/o/oauth2/auth": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.googleapis.com/oauth2/v1/certs": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://oauth2.googleapis.com/token": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.blogger.com/feeds/": {
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
# blogger_api_publisher.py

import os
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.blogger.com/feeds/']

def authenticate_blogger_api():
    """Authenticate with Blogger API using OAuth credentials."""
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('blogger', 'v3', credentials=creds)

    return service

def create_blog_post(service, blog_id, post_title, post_content):
    """Create a new blog post using Blogger API."""
    try:
        post = {
            'title': post_title,
            'content': post_content
        }
        result = service.posts().insert(blogId=blog_id, body=post).execute()
        print(f'Blog post created: {result["id"]}')
    except Exception as e:
        print(f'Error creating blog post: {e}')

def main():
    """Publish a blog post using Blogger API."""
    blog_id = 'your_blog_id'
    post_title = 'Example Blog Post'
    post_content = 'This is an example blog post published using Blogger API.'

    service = authenticate_blogger_api()
    create_blog_post(service, blog_id, post_title, post_content)

if __name__ == '__main__':
    main()
```

```json
// credentials.json

{
  "installed":
  {
    "client_id": "YOUR_CLIENT_ID",
    "project_id": "YOUR_PROJECT_ID",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_secret": "YOUR_CLIENT_SECRET",
    "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"]
  }
}
```
