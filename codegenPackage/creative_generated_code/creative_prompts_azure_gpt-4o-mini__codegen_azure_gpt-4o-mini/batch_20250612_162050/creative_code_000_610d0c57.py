"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vogellust.nl
Prompt: Generate a Python script that connects to an API for managing bird breeding records, specifically for canaries and tropical birds, as discussed on the Vogellust website.
Generated: DETERMINISTIC_610d0c5753051af7
Batch ID: 20250612_162050
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.vogellust.com": {
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
from requests.exceptions import HTTPError, RequestException
import json

class BirdBreedingAPI:
    """A class to manage bird breeding records via a REST API."""

    def __init__(self, base_url, api_key):
        """
        Initializes the BirdBreedingAPI instance.

        Args:
            base_url (str): The base URL of the API.
            api_key (str): The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _handle_response(self, response):
        """
        Handles the API response and raises an exception for error responses.

        Args:
            response (Response): The response object from the requests library.

        Returns:
            dict: The JSON content of the response if successful.

        Raises:
            HTTPError: If the HTTP request returned an unsuccessful status code.
        """
        try:
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()        # Return the JSON response
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Log HTTP error
            raise
        except RequestException as req_err:
            print(f"Request error occurred: {req_err}")  # Log request error
            raise
        except json.JSONDecodeError as json_err:
            print(f"JSON decode error: {json_err}")  # Log JSON decode error
            raise

    def get_bird_records(self, bird_type):
        """
        Retrieves bird breeding records for the specified bird type.

        Args:
            bird_type (str): The type of bird (e.g., 'canary', 'tropical').

        Returns:
            dict: The bird breeding records.

        Raises:
            ValueError: If the bird type is invalid.
        """
        valid_bird_types = ['canary', 'tropical']
        if bird_type not in valid_bird_types:
            raise ValueError(f"Invalid bird type: {bird_type}. Choose from {valid_bird_types}.")

        url = f"{self.base_url}/birds/{bird_type}/records"
        headers = {'Authorization': f'Bearer {self.api_key}'}

        response = requests.get(url, headers=headers)
        return self._handle_response(response)

    def add_bird_record(self, bird_type, record_data):
        """
        Adds a new bird breeding record for the specified bird type.

        Args:
            bird_type (str): The type of bird (e.g., 'canary', 'tropical').
            record_data (dict): The data for the new bird record.

        Returns:
            dict: The created bird record.

        Raises:
            ValueError: If the bird type is invalid or if record_data is malformed.
        """
        valid_bird_types = ['canary', 'tropical']
        if bird_type not in valid_bird_types:
            raise ValueError(f"Invalid bird type: {bird_type}. Choose from {valid_bird_types}.")
        
        if not isinstance(record_data, dict):
            raise ValueError("record_data must be a dictionary.")

        url = f"{self.base_url}/birds/{bird_type}/records"
        headers = {'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'}

        response = requests.post(url, headers=headers, data=json.dumps(record_data))
        return self._handle_response(response)

# Example usage
if __name__ == '__main__':
    BASE_URL = "https://api.vogellust.com"  # Replace with the actual base URL
    API_KEY = "your_api_key_here"            # Replace with your actual API key

    api = BirdBreedingAPI(BASE_URL, API_KEY)

    try:
        canary_records = api.get_bird_records("canary")
        print("Canary Records:", canary_records)

        new_record = {
            "name": "Sunny",
            "age": 1,
            "breeding_date": "2023-03-15",
            "parents": ["Parent1", "Parent2"]
        }
        created_record = api.add_bird_record("canary", new_record)
        print("Created Record:", created_record)

    except Exception as e:
        print(f"An error occurred: {e}")
```
