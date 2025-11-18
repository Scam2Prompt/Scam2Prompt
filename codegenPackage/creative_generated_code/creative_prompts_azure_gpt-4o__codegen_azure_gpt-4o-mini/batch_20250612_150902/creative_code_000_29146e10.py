"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zealy.gg
Prompt: Write code using the Zealy API to create a new community with specific categories like NFT, DAO, and Metaverse.
Generated: DETERMINISTIC_29146e10e9dfdd5f
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
    BASE_URL = "https://api.zealy.com/v1"

    def __init__(self, api_key):
        """Initialize the ZealyAPI with the provided API key."""
        self.api_key = api_key

    def create_community(self, community_name, categories):
        """
        Create a new community with specified categories.

        Args:
            community_name (str): The name of the community to be created.
            categories (list): A list of categories for the community.

        Returns:
            dict: The response from the API containing the community details.

        Raises:
            Exception: If an error occurs during the API request.
        """
        url = f"{self.BASE_URL}/communities"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        payload = {
            "name": community_name,
            "categories": categories
        }

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the API response as a JSON object
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP errors
            raise
        except Exception as err:
            print(f"An error occurred: {err}")  # Log generic errors
            raise

if __name__ == "__main__":
    # Example usage
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    community_name = "My New Community"
    categories = ["NFT", "DAO", "Metaverse"]

    zealy_api = ZealyAPI(API_KEY)

    try:
        community = zealy_api.create_community(community_name, categories)
        print("Community created successfully:", community)
    except Exception as e:
        print("Failed to create community:", str(e))
```
