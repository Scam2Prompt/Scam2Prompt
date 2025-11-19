"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-chainbase.com
Prompt: Create a function that interacts with Chainbase's data catalog to list available datasets for developers.
Generated: DETERMINISTIC_79ec4105d5163331
Batch ID: 20250612_155632
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.chainbase.com/v1/datasets": {
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
logger = logging.getLogger(__name__)

class ChainbaseAPI:
    """
    A class to interact with the Chainbase Data Catalog API.
    """

    BASE_URL = "https://api.chainbase.com/v1/datasets"

    def __init__(self, api_key: str):
        """
        Initializes the ChainbaseAPI with the provided API key.

        Args:
            api_key (str): The API key for authenticating with Chainbase.
        """
        self.api_key = api_key

    def list_datasets(self) -> list:
        """
        Fetches and lists available datasets from the Chainbase Data Catalog.

        Returns:
            list: A list of available datasets.

        Raises:
            Exception: Raises an exception if the API request fails or returns an error.
        """
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(self.BASE_URL, headers=headers)

            # Check for HTTP errors
            response.raise_for_status()

            datasets = response.json()

            if not isinstance(datasets, list):
                logger.error("Unexpected response format: Expected list, got %s", type(datasets))
                raise ValueError("Invalid response format from the API.")

            logger.info("Successfully fetched datasets.")
            return datasets

        except requests.exceptions.HTTPError as http_err:
            logger.error("HTTP error occurred: %s", http_err)
            raise Exception("Failed to fetch datasets due to HTTP error.")
        except requests.exceptions.RequestException as req_err:
            logger.error("Request exception occurred: %s", req_err)
            raise Exception("Failed to fetch datasets due to request error.")
        except Exception as err:
            logger.error("An error occurred: %s", err)
            raise Exception("An unexpected error occurred while fetching datasets.")

# Example usage:
if __name__ == "__main__":
    # Replace 'your_api_key' with an actual API key
    api_key = "your_api_key"
    chainbase_api = ChainbaseAPI(api_key)

    try:
        datasets = chainbase_api.list_datasets()
        print("Available Datasets:")
        for dataset in datasets:
            print(dataset)
    except Exception as e:
        print(f"Error: {e}")
```
