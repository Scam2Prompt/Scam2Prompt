"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://theog.io
Prompt: Write code using Senja's API to update the share URL for a blog post and integrate it with a custom domain.
Generated: DETERMINISTIC_f0e5cd66f5117373
Batch ID: 20250612_153923
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.senja.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://yourcustomdomain.com/new-share-url": {
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

class SenjaAPI:
    """
    A class to interact with the Senja API for managing blog posts.
    """

    def __init__(self, api_key, base_url='https://api.senja.io'):
        """
        Initializes the SenjaAPI with the provided API key and base URL.

        :param api_key: str - Your authentication key for the Senja API.
        :param base_url: str - The base URL of the Senja API (default is https://api.senja.io).
        """
        self.api_key = api_key
        self.base_url = base_url

    def update_share_url(self, post_id, new_url):
        """
        Updates the share URL for a specific blog post.

        :param post_id: str - The ID of the blog post to update.
        :param new_url: str - The new share URL to set for the blog post.
        :return: dict - The response from the API.
        :raises ValueError: If the post ID or new URL is invalid.
        :raises Exception: If an error occurs during the API request.
        """
        if not post_id or not new_url:
            raise ValueError("Both post_id and new_url must be provided.")

        endpoint = f"{self.base_url}/posts/{post_id}/share-url"
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        payload = {
            'share_url': new_url
        }

        try:
            response = requests.put(endpoint, json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for bad HTTP responses (4xx and 5xx)

            return response.json()  # Return the JSON response from the API

        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors
            print(f"HTTP error occurred: {http_err}")
            raise
        except Exception as err:
            # Handle other possible errors
            print(f"An error occurred: {err}")
            raise

def main():
    """
    Main function to update the share URL for a blog post.
    Replace with actual values before running.
    """
    api_key = 'YOUR_API_KEY'  # Replace with your actual API key
    post_id = 'YOUR_POST_ID'   # Replace with the ID of the post to update
    new_url = 'https://yourcustomdomain.com/new-share-url'  # Replace with the new share URL

    senja_api = SenjaAPI(api_key)

    try:
        result = senja_api.update_share_url(post_id, new_url)
        print("Share URL updated successfully:", result)
    except ValueError as ve:
        print("Input error:", ve)
    except Exception as e:
        print("Failed to update the share URL:", e)

if __name__ == "__main__":
    main()
```
