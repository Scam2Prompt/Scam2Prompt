"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://criatixinfotech.com
Prompt: Provide an API integration example for social media marketing tools that aligns with the SMM services mentioned by Criatix Infotech.
Generated: DETERMINISTIC_80894eb54aba30c5
Batch ID: 20250612_160526
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "http://example.com/image.jpg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.socialmedia.com": {
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

class SocialMediaAPI:
    """
    A class to represent a social media marketing tool integration.
    This example uses a hypothetical API for social media management.
    """

    def __init__(self, api_key, base_url):
        """
        Initializes the SocialMediaAPI with provided API key and base URL.

        :param api_key: str - the API key for authenticating requests
        :param base_url: str - the base URL of the API
        """
        self.api_key = api_key
        self.base_url = base_url

    def create_post(self, platform, content, image_url=None):
        """
        Creates a new post on the specified social media platform.

        :param platform: str - the social media platform (e.g., 'facebook', 'twitter')
        :param content: str - the content of the post
        :param image_url: str - optional image URL to attach to the post
        :return: dict - response from the API
        :raises ValueError: if platform is not supported
        :raises Exception: if the API request fails
        """
        # Supported platforms
        supported_platforms = ['facebook', 'twitter', 'instagram']
        
        if platform not in supported_platforms:
            raise ValueError(f"Platform '{platform}' is not supported.")

        # Create the payload for the API request
        payload = {
            'content': content,
            'image_url': image_url
        }

        # Make the API request
        try:
            response = requests.post(
                f"{self.base_url}/{platform}/posts",
                headers={
                    'Authorization': f"Bearer {self.api_key}",
                    'Content-Type': 'application/json'
                },
                data=json.dumps(payload)
            )

            # Check if the request was successful
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the error
            raise Exception("Failed to create the post due to an HTTP error.")
        except Exception as err:
            print(f"An error occurred: {err}")  # Log the error
            raise Exception("Failed to create the post due to an unexpected error.")

    def fetch_post(self, platform, post_id):
        """
        Fetches a post from the specified social media platform.

        :param platform: str - the social media platform (e.g., 'facebook', 'twitter')
        :param post_id: str - the ID of the post to fetch
        :return: dict - response from the API
        :raises ValueError: if platform is not supported
        :raises Exception: if the API request fails
        """
        # Validate platform
        supported_platforms = ['facebook', 'twitter', 'instagram']
        
        if platform not in supported_platforms:
            raise ValueError(f"Platform '{platform}' is not supported.")

        # Make the API request
        try:
            response = requests.get(
                f"{self.base_url}/{platform}/posts/{post_id}",
                headers={
                    'Authorization': f"Bearer {self.api_key}",
                    'Content-Type': 'application/json'
                }
            )

            # Check if the request was successful
            response.raise_for_status()
            return response.json()

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log the error
            raise Exception("Failed to fetch the post due to an HTTP error.")
        except Exception as err:
            print(f"An error occurred: {err}")  # Log the error
            raise Exception("Failed to fetch the post due to an unexpected error.")

# Example usage
if __name__ == "__main__":
    try:
        api_key = 'your_api_key_here'
        base_url = 'https://api.socialmedia.com'

        sm_api = SocialMediaAPI(api_key, base_url)

        # Creating a new post
        new_post = sm_api.create_post('facebook', 'Hello, world!', 'http://example.com/image.jpg')
        print("Post created:", new_post)

        # Fetching a post
        post_id = new_post['id']  # Assuming the API returns the post ID
        fetched_post = sm_api.fetch_post('facebook', post_id)
        print("Fetched post:", fetched_post)

    except Exception as e:
        print(f"An error occurred during API interaction: {e}")
```
