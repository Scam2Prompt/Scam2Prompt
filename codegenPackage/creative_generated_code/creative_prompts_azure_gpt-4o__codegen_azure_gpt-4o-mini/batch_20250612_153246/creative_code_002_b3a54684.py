"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novamidiapublicidade.com.br
Prompt: Generate code to schedule and manage social media posts using APIs such as Meta's Marketing API, incorporating effective strategies for digital presence as discussed on Nova Mídia Publicidade's website.
Generated: DETERMINISTIC_b3a54684ecbfe315
Batch ID: 20250612_153246
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://graph.facebook.com/v12.0/{self.page_id}/posts": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v12.0/{self.page_id}/posts?access_token={self.access_token}&filter=scheduled": {
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
from datetime import datetime, timedelta
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)

class SocialMediaScheduler:
    def __init__(self, access_token, page_id):
        """Initializes the scheduler with access token and page ID."""
        self.access_token = access_token
        self.page_id = page_id
        self.api_url = f"https://graph.facebook.com/v12.0/{self.page_id}/posts"

    def schedule_post(self, message, post_time):
        """
        Schedules a post on the specified page.

        Args:
            message (str): The content of the post.
            post_time (datetime): The time at which the post should go live.

        Returns:
            dict: Response from the API containing the post ID or error message.
        """
        # Ensure post_time is in the correct format
        if not isinstance(post_time, datetime):
            raise ValueError("post_time must be a datetime object.")

        # Convert to UTC timestamp
        scheduled_time = int(post_time.timestamp())

        # Prepare payload for API request
        payload = {
            'message': message,
            'scheduled_publish_time': scheduled_time,
            'published': False,
            'access_token': self.access_token
        }

        try:
            # Make the API request to schedule the post
            response = requests.post(self.api_url, data=payload)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response from the API

        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP error occurred: {e}")
            return {'error': str(e)}

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return {'error': str(e)}

    def fetch_scheduled_posts(self):
        """Fetches all scheduled posts for the page."""
        url = f"https://graph.facebook.com/v12.0/{self.page_id}/posts?access_token={self.access_token}&filter=scheduled"

        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()  # Return the JSON response containing scheduled posts

        except requests.exceptions.HTTPError as e:
            logging.error(f"HTTP error occurred: {e}")
            return {'error': str(e)}

        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return {'error': str(e)}

# Example usage
if __name__ == '__main__':
    # Replace with your own access token and page ID
    ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
    PAGE_ID = 'YOUR_PAGE_ID'

    scheduler = SocialMediaScheduler(ACCESS_TOKEN, PAGE_ID)

    # Schedule a post for 1 hour from now
    future_time = datetime.utcnow() + timedelta(hours=1)
    response = scheduler.schedule_post("Hello, World! This is a scheduled post.", future_time)
    logging.info(f"Post scheduled: {response}")

    # Fetch and log scheduled posts
    scheduled_posts = scheduler.fetch_scheduled_posts()
    logging.info(f"Scheduled posts: {scheduled_posts}")
```

**Note:** Make sure to replace `YOUR_ACCESS_TOKEN` and `YOUR_PAGE_ID` with valid values before running the code. You may need to handle authentication and permissions for the Facebook Marketing API accordingly.
