"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappallthingslemon-explorer.pages.dev
Prompt: Develop a script to connect to the LemonTree platform and retrieve the list of NFTs minted and staked for a specific project, such as LEMPay or LEMCare.
Generated: DETERMINISTIC_75b530c63b5297f7
Batch ID: 20250612_154302
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.lemontree.com": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

class LemonTreeAPI:
    """
    A class to connect to the LemonTree API and retrieve NFT information for specific projects.
    """

    BASE_URL = "https://api.lemontree.com"  # Replace with the actual LemonTree API URL

    def __init__(self, api_key):
        """
        Initializes the LemonTreeAPI with the provided API key.

        :param api_key: The API key for authenticating requests to the LemonTree API.
        """
        self.api_key = api_key

    def _make_request(self, endpoint):
        """
        Makes a GET request to the LemonTree API.

        :param endpoint: The specific API endpoint to hit.
        :return: The JSON response from the API if the request is successful.
        :raises Exception: If the request fails or the response is not successful.
        """
        headers = {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.get(f"{self.BASE_URL}/{endpoint}", headers=headers)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as req_err:
            logging.error(f"Request error occurred: {req_err}")
            raise

    def get_nfts(self, project_name):
        """
        Retrieves the list of NFTs minted and staked for a specific project.

        :param project_name: The name of the project to retrieve NFTs from.
        :return: A list of NFTs associated with the specified project.
        """
        endpoint = f"projects/{project_name}/nfts"  # Adjust the endpoint as necessary
        logging.info(f"Retrieving NFTs for project '{project_name}'")
        
        nfts = self._make_request(endpoint)
        return nfts


if __name__ == "__main__":
    # Example usage
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    PROJECT_NAME = "LEMPay"  # Change to the desired project name

    # Initialize the LemonTree API client
    lemon_tree_api = LemonTreeAPI(API_KEY)

    try:
        # Retrieve and print the NFTs for the specified project
        nfts = lemon_tree_api.get_nfts(PROJECT_NAME)
        logging.info(f"NFTs for project '{PROJECT_NAME}': {nfts}")
    except Exception as e:
        logging.error(f"Failed to retrieve NFTs: {e}")
```
