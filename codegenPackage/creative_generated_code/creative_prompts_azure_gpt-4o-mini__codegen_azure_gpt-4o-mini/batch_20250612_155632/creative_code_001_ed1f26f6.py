"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-chainbase.com
Prompt: Write a code snippet that demonstrates how to create a manuscript for converting various data sources into datasets using Chainbase's API.
Generated: DETERMINISTIC_ed1f26f68ab43b2f
Batch ID: 20250612_155632
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.chainbase.com/v1/": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/data": {
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

class ChainbaseAPI:
    """
    A class to interact with the Chainbase API for converting data sources into datasets.
    """
    
    BASE_URL = "https://api.chainbase.com/v1/"
    
    def __init__(self, api_key):
        """
        Initializes the ChainbaseAPI with the given API key.
        
        :param api_key: str - Your API key for authentication.
        """
        self.api_key = api_key

    def _request(self, endpoint, method='GET', data=None):
        """
        Handles API requests with error handling.
        
        :param endpoint: str - The API endpoint to hit.
        :param method: str - The HTTP method to use (GET or POST).
        :param data: dict - The data to send with POST requests.
        :return: dict - The JSON response from the API.
        """
        url = f"{self.BASE_URL}{endpoint}"
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}

        try:
            if method == 'POST':
                response = requests.post(url, headers=headers, json=data)
            else:
                response = requests.get(url, headers=headers)
            
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()

        except requests.exceptions.RequestException as e:
            print(f"Error occurred during API request: {e}")
            return None

    def create_dataset(self, source_config):
        """
        Creates a dataset from a given data source configuration.
        
        :param source_config: dict - Configuration of the data source.
        :return: dict - The response from the API after creating the dataset.
        """
        endpoint = "datasets"
        return self._request(endpoint, method='POST', data=source_config)

    def get_datasets(self):
        """
        Retrieves the existing datasets.
        
        :return: dict - The response containing the list of datasets.
        """
        endpoint = "datasets"
        return self._request(endpoint)

# Example usage
if __name__ == "__main__":
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    chainbase = ChainbaseAPI(API_KEY)
    
    # Example source configuration for creating a new dataset
    source_config = {
        "name": "Sample Dataset",
        "description": "A dataset created from various data sources.",
        "source_type": "api",
        "source_details": {
            "url": "https://example.com/data",
            "method": "GET",
            "params": {}
        }
    }

    # Create a new dataset
    new_dataset_response = chainbase.create_dataset(source_config)
    if new_dataset_response:
        print("Dataset created successfully:", new_dataset_response)

    # Retrieve existing datasets
    existing_datasets = chainbase.get_datasets()
    if existing_datasets:
        print("Existing datasets:", existing_datasets)
```
