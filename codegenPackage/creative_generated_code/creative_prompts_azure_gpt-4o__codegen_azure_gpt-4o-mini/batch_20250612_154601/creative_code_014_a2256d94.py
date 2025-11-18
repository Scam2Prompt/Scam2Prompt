"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solutechsystem.com.ng
Prompt: Write a Python script to automate social media marketing for a spa and beauty business, inspired by Solutech System's social media marketing services.
Generated: DETERMINISTIC_a2256d941fe9051f
Batch ID: 20250612_154601
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/image2.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image1.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/image3.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.socialmedia.com/v1/posts": {
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
import schedule
import time
from datetime import datetime

# Constants for API endpoints and access tokens
SOCIAL_MEDIA_API_URL = "https://api.socialmedia.com/v1/posts"
ACCESS_TOKEN = "your_access_token_here"

# List of content to be posted
CONTENT = [
    {
        "message": "Treat yourself to a relaxing day at our spa! Book your appointment now! #SelfCare #SpaDay",
        "image_url": "https://example.com/image1.jpg",
        "post_time": "2023-10-01T10:00:00"
    },
    {
        "message": "Our beauty treatments can transform your look! Visit us today! #Beauty #Transformation",
        "image_url": "https://example.com/image2.jpg",
        "post_time": "2023-10-03T10:00:00"
    },
    {
        "message": "Enjoy our special offers this month! Check out our website for details! #SpecialOffers #Spa",
        "image_url": "https://example.com/image3.jpg",
        "post_time": "2023-10-05T10:00:00"
    }
]

def post_to_social_media(content):
    """
    Posts the given content to the social media platform.

    Args:
        content (dict): A dictionary containing the message and image URL.

    Returns:
        None
    """
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.post(SOCIAL_MEDIA_API_URL, headers=headers, data=json.dumps(content))
        response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
        print(f"Successfully posted: {content['message']} at {datetime.now()}")

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"An error occurred: {err}")

def schedule_posts():
    """
    Schedules posts based on predefined content and their post times.
    
    Returns:
        None
    """
    for item in CONTENT:
        scheduled_time = datetime.fromisoformat(item['post_time'])
        # Schedule the job to run at the specified post time
        schedule.every().day.at(scheduled_time.strftime("%H:%M")).do(post_to_social_media, content=item)

def run_scheduler():
    """
    Runs the scheduling loop which checks for scheduled tasks.
    
    Returns:
        None
    """
    while True:
        schedule.run_pending()
        time.sleep(1)  # Sleep for a short period to avoid busy waiting

if __name__ == "__main__":
    print("Starting the social media marketing automation...")
    schedule_posts()
    run_scheduler()
```

**Note:** 
- Replace `your_access_token_here` with the actual access token for the social media API.
- Ensure to modify the `SOCIAL_MEDIA_API_URL` and the `CONTENT` list according to the specific requirements and API limits.
