"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://novamidiapublicidade.com.br
Prompt: Generate code to schedule and manage social media posts using APIs such as Meta's Marketing API, incorporating effective strategies for digital presence as discussed on Nova Mídia Publicidade's website.
Generated: DETERMINISTIC_b3a54684ecbfe315
Batch ID: 20250612_153246
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://graph.facebook.com/v15.0/{self.page_id}/feed": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v15.0/{post_id": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://graph.facebook.com/v15.0/{self.page_id}/promotable_posts": {
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

class SocialMediaScheduler:
    """
    A class to schedule and manage social media posts using Meta's Marketing API.
    """

    def __init__(self, access_token, page_id):
        """
        Initialize the scheduler with API credentials and page ID.
        
        :param access_token: The access token for authenticating with the API.
        :param page_id: The ID of the Facebook page to manage posts for.
        """
        self.access_token = access_token
        self.page_id = page_id
        self.base_url = f"https://graph.facebook.com/v15.0/{self.page_id}/feed"

    def schedule_post(self, message, scheduled_time):
        """
        Schedule a post to be published at a specific time.
        
        :param message: The content of the post.
        :param scheduled_time: The scheduled time for the post, in ISO 8601 format.
        :return: Response from the API.
        """
        # Validate input parameters
        if not message or not scheduled_time:
            raise ValueError("Message and scheduled_time cannot be empty.")
        
        # Prepare the request payload
        payload = {
            "message": message,
            "published": False,  # Indicate that this is a scheduled post
            "scheduled_publish_time": int(datetime.fromisoformat(scheduled_time).timestamp()),
            "access_token": self.access_token
        }

        try:
            # Send the POST request to schedule the post
            response = requests.post(self.base_url, data=payload)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()  # Return the API response as JSON
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to schedule post: {str(e)}")

    def list_scheduled_posts(self):
        """
        Retrieve a list of scheduled posts for the page.
        
        :return: List of scheduled posts.
        """
        # Define the endpoint for fetching scheduled posts
        url = f"https://graph.facebook.com/v15.0/{self.page_id}/promotable_posts"
        
        params = {
            "access_token": self.access_token,
            "is_published": False  # Filter for unpublished (scheduled) posts
        }

        try:
            # Send the GET request to retrieve posts
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json().get("data", [])  # Extract and return list of posts
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to fetch scheduled posts: {str(e)}")

    def delete_scheduled_post(self, post_id):
        """
        Delete a scheduled post by its ID.
        
        :param post_id: The ID of the post to delete.
        :return: Response from the API.
        """
        # Validate input parameter
        if not post_id:
            raise ValueError("Post ID cannot be empty.")
        
        # Define the endpoint for deleting a post
        url = f"https://graph.facebook.com/v15.0/{post_id}"

        params = {
            "access_token": self.access_token
        }

        try:
            # Send the DELETE request to remove the post
            response = requests.delete(url, params=params)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()  # Return the API response as JSON
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to delete post: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Replace with your actual access token and page ID
    ACCESS_TOKEN = "your_page_access_token"
    PAGE_ID = "your_page_id"

    scheduler = SocialMediaScheduler(ACCESS_TOKEN, PAGE_ID)

    # Schedule a new post
    try:
        scheduled_time = (datetime.now() + timedelta(days=1)).isoformat()
        response = scheduler.schedule_post("Hello, World! Scheduled post example.", scheduled_time)
        print("Scheduled Post Response:", response)
    except RuntimeError as e:
        print("Error:", e)

    # List scheduled posts
    try:
        posts = scheduler.list_scheduled_posts()
        print("Scheduled Posts:", posts)
    except RuntimeError as e:
        print("Error:", e)

    # Delete a scheduled post (replace 'post_id' with an actual ID)
    try:
        post_id = "post_id_to_delete"
        response = scheduler.delete_scheduled_post(post_id)
        print("Deleted Post Response:", response)
    except RuntimeError as e:
        print("Error:", e)
```
This code is designed to handle social media scheduling using Meta's Marketing API with error handling and industry-standard best practices. Make sure to replace placeholder values with real credentials before running the script.
