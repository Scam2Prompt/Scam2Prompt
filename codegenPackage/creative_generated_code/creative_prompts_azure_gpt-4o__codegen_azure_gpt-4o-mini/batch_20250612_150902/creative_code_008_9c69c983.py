"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealy.gg
Prompt: Provide an example of how to use Zealy's API to create a community focused on AI Agent and Meme categories.
Generated: DETERMINISTIC_9c69c983d241b0a9
Batch ID: 20250612_150902
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.zealy.com/v1": {
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

class ZealyAPI:
    """
    A class to interact with Zealy's API to manage communities.
    """

    BASE_URL = "https://api.zealy.com/v1"

    def __init__(self, api_key):
        """
        Initializes the ZealyAPI with the provided API key.

        Parameters:
            api_key (str): The API key for authenticating requests.
        """
        self.api_key = api_key
        self.headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

    def create_community(self, name, categories):
        """
        Creates a new community in Zealy.

        Parameters:
            name (str): The name of the community.
            categories (list): A list of category names for the community.

        Returns:
            dict: Response from the API containing the community details.

        Raises:
            Exception: If the API request fails.
        """
        url = f"{self.BASE_URL}/communities"
        data = {
            "name": name,
            "categories": categories
        }

        try:
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response if successful
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to create community: {str(e)}")

if __name__ == "__main__":
    # Example usage of the ZealyAPI to create a community
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    community_name = "AI Agents & Memes"
    categories = ["AI Agents", "Memes"]

    zealy_api = ZealyAPI(API_KEY)
    try:
        community_response = zealy_api.create_community(community_name, categories)
        print("Community created successfully:", community_response)
    except Exception as e:
        print(e)
```
