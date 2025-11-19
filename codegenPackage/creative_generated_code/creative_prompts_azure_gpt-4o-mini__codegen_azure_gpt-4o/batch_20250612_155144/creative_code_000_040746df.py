"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pooleth.net
Prompt: Generate a code snippet that demonstrates how to create a blog post using the Hatena Blog API, including features like tagging and scheduling.
Generated: DETERMINISTIC_040746dfc7c3db31
Batch ID: 20250612_155144
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://blog.hatena.ne.jp/{user_id}/{blog_id}/atom/entry": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://www.w3.org/2005/Atom": {
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
import datetime
from requests.auth import HTTPBasicAuth

# Hatena Blog API Configuration
API_BASE_URL = "https://blog.hatena.ne.jp/{user_id}/{blog_id}/atom/entry"
USER_ID = "your_hatena_user_id"  # Replace with your Hatena user ID
BLOG_ID = "your_blog_id"         # Replace with your blog ID
USERNAME = "your_username"       # Replace with your Hatena username
API_KEY = "your_api_key"         # Replace with your Hatena API key

# Blog Post Data
TITLE = "My First Blog Post"
CONTENT = """<p>This is the content of the blog post.</p>"""
TAGS = ["Python", "API", "Hatena"]
SCHEDULE_DATE = "2023-10-31T10:00:00+09:00"  # Scheduled publishing date and time in ISO 8601 format

def create_blog_post():
    """
    Creates a blog post on Hatena Blog using the API.
    """
    # Construct the XML payload for the blog post
    payload = f"""<?xml version="1.0" encoding="utf-8"?>
    <entry xmlns="http://www.w3.org/2005/Atom">
        <title>{TITLE}</title>
        <content type="text/html">{CONTENT}</content>
        <category term="{','.join(TAGS)}" />
        <updated>{SCHEDULE_DATE}</updated>
        <published>{SCHEDULE_DATE}</published>
    </entry>
    """

    # Send the request to the Hatena Blog API
    try:
        response = requests.post(
            API_BASE_URL.format(user_id=USER_ID, blog_id=BLOG_ID),
            auth=HTTPBasicAuth(USERNAME, API_KEY),
            headers={
                "Content-Type": "application/xml",
                "Accept": "application/xml"
            },
            data=payload
        )

        # Handle the response
        if response.status_code == 201:  # HTTP 201 Created
            print("Blog post created successfully.")
        else:
            print(f"Failed to create blog post. Status code: {response.status_code}")
            print(f"Response: {response.text}")
    except requests.exceptions.RequestException as e:
        # Handle connection and other errors
        print(f"An error occurred while creating the blog post: {e}")

# Run the function (entry point)
if __name__ == "__main__":
    create_blog_post()
```
