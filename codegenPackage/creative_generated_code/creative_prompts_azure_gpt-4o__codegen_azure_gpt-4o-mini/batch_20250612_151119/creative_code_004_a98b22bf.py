"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.cc-community.net
Prompt: Write a script to extract statistics (e.g., total members, posts, and topics) from a XenForo-based forum like CC-Community Board using its API.
Generated: DETERMINISTIC_a98b22bf134034a6
Batch ID: 20250612_151119
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://your-forum-url.com/api": {
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

class XenForoAPI:
    """Class to interact with the XenForo API for extracting forum statistics."""

    def __init__(self, base_url, api_key):
        """
        Initialize the XenForoAPI with a base URL and an API key.
        
        :param base_url: Base URL of the XenForo forum API
        :param api_key: API key for authentication
        """
        self.base_url = base_url.rstrip('/')  # Ensure no trailing slash
        self.api_key = api_key

    def _make_request(self, endpoint):
        """
        Make a GET request to the specified API endpoint.
        
        :param endpoint: API endpoint to call
        :return: JSON response from the API
        :raises Exception: If the request fails or returns a bad response
        """
        url = f"{self.base_url}/{endpoint}?api_key={self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.RequestException as e:
            raise Exception(f"API request failed: {e}")

    def get_statistics(self):
        """
        Retrieve statistics from the forum (total members, posts, and topics).
        
        :return: Dictionary containing forum statistics
        :raises Exception: If the statistics retrieval fails
        """
        try:
            stats = self._make_request("statistics")
            return {
                "total_members": stats.get("totalMembers", 0),
                "total_posts": stats.get("totalPosts", 0),
                "total_topics": stats.get("totalTopics", 0)
            }
        except Exception as e:
            raise Exception(f"Failed to retrieve statistics: {e}")


def main():
    """
    Main function to execute the script and print forum statistics.
    """
    # Replace these values with your XenForo forum details
    BASE_URL = "https://your-forum-url.com/api"
    API_KEY = "your_api_key_here"

    # Create an instance of the XenForoAPI
    forum_api = XenForoAPI(BASE_URL, API_KEY)

    try:
        # Retrieve and print statistics
        statistics = forum_api.get_statistics()
        print("Forum Statistics:")
        print(f"Total Members: {statistics['total_members']}")
        print(f"Total Posts: {statistics['total_posts']}")
        print(f"Total Topics: {statistics['total_topics']}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
