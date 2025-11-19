"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starkscan-sepolia.netlify.app
Prompt: What are the steps to access contract events using the Starkscan API, and can you provide a code example?
Generated: DETERMINISTIC_93c143f3bf5c1f7f
Batch ID: 20250612_163817
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.starkscan.co/api/v1": {
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

class StarkscanAPI:
    """
    A class to interact with the Starkscan API to access contract events.
    """

    BASE_URL = "https://api.starkscan.co/api/v1"  # Base URL for the Starkscan API

    def __init__(self, api_key):
        """
        Initialize the StarkscanAPI with the required API key.

        :param api_key: str - Your API key for authentication
        """
        self.api_key = api_key

    def get_contract_events(self, contract_address, from_block=None, to_block=None):
        """
        Fetch events for a specific contract.

        :param contract_address: str - The address of the contract to query
        :param from_block: int - Optional; the starting block number
        :param to_block: int - Optional; the ending block number
        :return: dict - The JSON response from the API
        :raises: Exception - Raises an exception if the API call fails
        """
        # Construct the URL for the API request
        url = f"{self.BASE_URL}/events?contract={contract_address}"

        # Add optional parameters to the request
        params = {}
        if from_block is not None:
            params['from_block'] = from_block
        if to_block is not None:
            params['to_block'] = to_block

        # Set up headers for the request, including the API key
        headers = {
            "Authorization": f"Bearer {self.api_key}"
        }

        try:
            # Make the request to the Starkscan API
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses

            # Return the JSON response
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            raise Exception(f"HTTP error occurred: {http_err}")  # Handle HTTP errors
        except Exception as err:
            raise Exception(f"An error occurred: {err}")  # Handle other errors

# Example usage
if __name__ == "__main__":
    # Replace with your actual API key and contract address
    API_KEY = "your_api_key"
    CONTRACT_ADDRESS = "0xYourContractAddress"

    # Create an instance of the StarkscanAPI
    starkscan_api = StarkscanAPI(api_key=API_KEY)

    # Fetch contract events
    try:
        events = starkscan_api.get_contract_events(CONTRACT_ADDRESS)
        print("Contract Events:", events)  # Print the fetched events
    except Exception as e:
        print("Error:", e)  # Handle any errors that occur during the fetching
```
