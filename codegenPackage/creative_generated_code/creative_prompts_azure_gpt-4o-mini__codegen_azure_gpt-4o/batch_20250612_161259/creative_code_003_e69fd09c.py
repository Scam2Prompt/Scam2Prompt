"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://333club.xyz
Prompt: Develop a library function that integrates Instagram API to showcase the latest events and promotions from a club, focusing on user engagement for special events.
Generated: DETERMINISTIC_e69fd09c861d3452
Batch ID: 20250612_161259
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://graph.instagram.com/": {
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
"""
instagram_api_integration.py

This module integrates with the Instagram API to fetch the latest posts for showcasing
events and promotions from a club. The focus is on user engagement for special events.
"""

import requests
from typing import List, Dict

class InstagramAPIError(Exception):
    """Custom exception for Instagram API errors."""
    pass

class InstagramAPI:
    """
    A class to interact with the Instagram API.
    
    Attributes:
        access_token (str): The access token for authenticating API requests.
        base_url (str): The base URL for the Instagram Graph API.
    """
    def __init__(self, access_token: str):
        """
        Initializes the InstagramAPI with the provided access token.
        
        Args:
            access_token (str): The access token for the Instagram API.
        """
        self.access_token = access_token
        self.base_url = "https://graph.instagram.com/"
    
    def get_latest_posts(self, user_id: str, limit: int = 5) -> List[Dict]:
        """
        Fetches the latest posts from a user's Instagram account.
        
        Args:
            user_id (str): The Instagram user ID.
            limit (int): The number of latest posts to fetch. Default is 5.
            
        Returns:
            List[Dict]: A list of dictionaries containing post data.
            
        Raises:
            InstagramAPIError: If an error occurs while fetching data.
        """
        endpoint = f"{self.base_url}{user_id}/media"
        params = {
            "fields": "id,caption,media_type,media_url,timestamp",
            "access_token": self.access_token,
            "limit": limit
        }
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()  # Raise HTTPError for bad HTTP response codes
            data = response.json()
            
            # Validate and return the data
            if "data" not in data:
                raise InstagramAPIError("Invalid response format: 'data' field missing.")
            
            return data["data"]
        except requests.exceptions.RequestException as e:
            raise InstagramAPIError(f"An error occurred while connecting to Instagram API: {e}")
        except ValueError:
            raise InstagramAPIError("An error occurred while parsing the response JSON.")

def showcase_events(posts: List[Dict]) -> None:
    """
    Displays the latest events and promotions based on Instagram posts.
    
    Args:
        posts (List[Dict]): A list of dictionaries containing Instagram post data.
    """
    print("Latest Events and Promotions:")
    for post in posts:
        print("-" * 40)
        print(f"Caption: {post.get('caption', 'No caption')}")
        print(f"Media Type: {post.get('media_type')}")
        print(f"Media URL: {post.get('media_url')}")
        print(f"Posted At: {post.get('timestamp')}")

# Example usage (replace ACCESS_TOKEN and USER_ID with actual values)
if __name__ == "__main__":
    ACCESS_TOKEN = "your_instagram_access_token_here"
    USER_ID = "your_instagram_user_id_here"
    
    try:
        # Initialize API client
        api_client = InstagramAPI(ACCESS_TOKEN)
        
        # Fetch latest posts
        latest_posts = api_client.get_latest_posts(USER_ID, limit=5)
        
        # Showcase events
        showcase_events(latest_posts)
    except InstagramAPIError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```

Please make sure to replace `ACCESS_TOKEN` and `USER_ID` with your actual Instagram API credentials and user ID before running the code. Also, ensure that you have the appropriate access permissions for the Instagram Graph API.
