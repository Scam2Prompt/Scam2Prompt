"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allocate-mode.app
Prompt: Write a guide for developers on how to use the Mode Network API to track ecosystem updates and community voting results.
Generated: DETERMINISTIC_412ebb82d385c6eb
Batch ID: 20250612_150927
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.modenetwork.com/v1": {
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

class ModeNetworkAPI:
    """
    A class to interact with the Mode Network API for tracking ecosystem updates
    and community voting results.
    """

    BASE_URL = "https://api.modenetwork.com/v1"

    def __init__(self, api_key):
        """
        Initializes the ModeNetworkAPI instance with the provided API key.

        :param api_key: str - Your API key for authentication.
        """
        self.api_key = api_key

    def _make_request(self, endpoint, params=None):
        """
        Makes a GET request to the Mode Network API.

        :param endpoint: str - The API endpoint to request.
        :param params: dict - Optional parameters for the request.
        :return: dict - Parsed JSON response from the API.
        :raises Exception: If an error occurs during the request.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Accept": "application/json"
        }

        try:
            response = requests.get(f"{self.BASE_URL}/{endpoint}", headers=headers, params=params)
            response.raise_for_status()  # Raise an error for HTTP errors
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")
        except requests.exceptions.RequestException as req_err:
            raise Exception(f"Request error occurred: {req_err}")

    def get_ecosystem_updates(self):
        """
        Retrieves the latest ecosystem updates from the Mode Network.

        :return: dict - Latest ecosystem updates.
        """
        return self._make_request("ecosystem/updates")

    def get_voting_results(self):
        """
        Retrieves community voting results from the Mode Network.

        :return: dict - Community voting results.
        """
        return self._make_request("community/voting/results")

# Example usage:
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    mode_api = ModeNetworkAPI(API_KEY)

    try:
        # Fetch and print ecosystem updates
        updates = mode_api.get_ecosystem_updates()
        print("Ecosystem Updates:", updates)

        # Fetch and print voting results
        voting_results = mode_api.get_voting_results()
        print("Voting Results:", voting_results)

    except Exception as e:
        print(f"An error occurred: {e}")
```
