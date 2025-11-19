"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://manta.expert
Prompt: "Generate a Python script that utilizes Manta's API for data analysis."
Generated: DETERMINISTIC_17c2e8f02e5ef73d
Batch ID: 20250612_155952
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.manta.com/v1": {
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
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MantaAPI:
    """
    A class to interact with Manta's API for data analysis.
    """

    BASE_URL = "https://api.manta.com/v1"  # Base URL for Manta API

    def __init__(self, api_key):
        """
        Initializes the MantaAPI class.

        :param api_key: Your Manta API key for authentication.
        """
        self.api_key = api_key

    def _make_request(self, endpoint, params=None):
        """
        Makes a GET request to the specified API endpoint.

        :param endpoint: The API endpoint (str).
        :param params: Query parameters to include in the request (dict).
        :return: Parsed JSON response if successful, else raises an Exception.
        """
        url = f"{self.BASE_URL}/{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            logging.info(f"Request to {url} succeeded with status code {response.status_code}.")
            return response.json()
        except requests.exceptions.HTTPError as http_err:
            logging.error(f"HTTP error occurred: {http_err}")
            raise
        except requests.exceptions.RequestException as err:
            logging.error(f"Error occurred: {err}")
            raise

    def analyze_data(self, dataset_id):
        """
        Analyzes data from the specified dataset using Manta's API.

        :param dataset_id: The ID of the dataset to analyze.
        :return: Analysis results as a JSON object.
        """
        logging.info(f"Starting analysis for dataset ID: {dataset_id}")
        endpoint = f"datasets/{dataset_id}/analyze"

        try:
            results = self._make_request(endpoint)
            logging.info(f"Analysis completed for dataset ID: {dataset_id}")
            return results
        except Exception as e:
            logging.error(f"Failed to analyze dataset ID {dataset_id}: {e}")
            raise

if __name__ == "__main__":
    # Example usage of MantaAPI for data analysis
    API_KEY = "your_api_key_here"  # Replace with your actual API key
    dataset_id = "example_dataset_id"  # Replace with your actual dataset ID

    try:
        manta_api = MantaAPI(API_KEY)
        analysis_results = manta_api.analyze_data(dataset_id)
        print(json.dumps(analysis_results, indent=2))  # Print formatted results
    except Exception as e:
        logging.critical(f"An error occurred during data analysis: {e}")
```
