"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getdolphin.io
Prompt: Generate an example of using the Dolphin API to automate data retrieval from external sources.
Generated: DETERMINISTIC_c7d216d9392c30d8
Batch ID: 20250612_161616
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dolphin.com/v1": {
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
from requests.exceptions import HTTPError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DolphinAPI:
    """
    A class to interact with the Dolphin API for data retrieval.
    """

    def __init__(self, base_url, api_key):
        """
        Initializes the DolphinAPI with base URL and API key.

        :param base_url: The base URL for the Dolphin API
        :param api_key: The API key for authentication
        """
        self.base_url = base_url
        self.api_key = api_key

    def get_data(self, endpoint, params=None):
        """
        Retrieves data from the specified API endpoint.

        :param endpoint: The API endpoint to query
        :param params: Optional dictionary of query parameters
        :return: JSON response from the API
        :raises HTTPError: If the API request fails
        """
        url = f"{self.base_url}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses (4xx, 5xx)
            logging.info("Data retrieved successfully from %s", url)
            return response.json()  # Return the JSON response
        except HTTPError as http_err:
            logging.error("HTTP error occurred: %s", http_err)
            raise
        except Exception as err:
            logging.error("An error occurred: %s", err)
            raise

def main():
    """
    Main function to demonstrate the Dolphin API data retrieval.
    """
    # Replace with your actual base URL and API key
    base_url = "https://api.dolphin.com/v1"
    api_key = "YOUR_API_KEY"

    # Create an instance of the DolphinAPI class
    dolphin_api = DolphinAPI(base_url, api_key)

    # Specify the endpoint and parameters
    endpoint = "data"
    params = {"type": "example", "limit": 10}

    try:
        # Retrieve data from the Dolphin API
        data = dolphin_api.get_data(endpoint, params)
        print("Retrieved data:", data)
    except Exception as e:
        logging.error("Failed to retrieve data: %s", e)

if __name__ == "__main__":
    main()
```
