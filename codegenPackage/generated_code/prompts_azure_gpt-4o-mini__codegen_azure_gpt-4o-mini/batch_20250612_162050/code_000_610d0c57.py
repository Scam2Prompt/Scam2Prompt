"""
Generated Code Metadata:
========================
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

# Generated Code:
# ===============

```python
import requests
import json

class BirdBreedingAPI:
    """
    A class to interact with the Bird Breeding API for managing breeding records
    of canaries and tropical birds.
    """

    def __init__(self, base_url, api_key):
        """
        Initializes the API client with the base URL and API key.

        :param base_url: The base URL of the API.
        :param api_key: The API key for authentication.
        """
        self.base_url = base_url
        self.api_key = api_key

    def _get_headers(self):
        """
        Constructs the headers for the API request.

        :return: A dictionary containing the headers.
        """
        return {
            'Authorization': f'Bearer {self.api_key}',
            'Content-Type': 'application/json'
        }

    def get_bird_records(self, bird_type):
        """
        Retrieves breeding records for a specific type of bird.

        :param bird_type: The type of bird (e.g., 'canary', 'tropical').
        :return: A list of breeding records or an error message.
        """
        url = f"{self.base_url}/birds/{bird_type}/records"
        try:
            response = requests.get(url, headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the JSON response
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

    def add_bird_record(self, bird_type, record):
        """
        Adds a new breeding record for a specific type of bird.

        :param bird_type: The type of bird (e.g., 'canary', 'tropical').
        :param record: A dictionary containing the breeding record details.
        :return: The created record or an error message.
        """
        url = f"{self.base_url}/birds/{bird_type}/records"
        try:
            response = requests.post(url, headers=self._get_headers(), data=json.dumps(record))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the created record
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

    def update_bird_record(self, bird_type, record_id, updated_record):
        """
        Updates an existing breeding record for a specific type of bird.

        :param bird_type: The type of bird (e.g., 'canary', 'tropical').
        :param record_id: The ID of the record to update.
        :param updated_record: A dictionary containing the updated record details.
        :return: The updated record or an error message.
        """
        url = f"{self.base_url}/birds/{bird_type}/records/{record_id}"
        try:
            response = requests.put(url, headers=self._get_headers(), data=json.dumps(updated_record))
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the updated record
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

    def delete_bird_record(self, bird_type, record_id):
        """
        Deletes a breeding record for a specific type of bird.

        :param bird_type: The type of bird (e.g., 'canary', 'tropical').
        :param record_id: The ID of the record to delete.
        :return: A success message or an error message.
        """
        url = f"{self.base_url}/birds/{bird_type}/records/{record_id}"
        try:
            response = requests.delete(url, headers=self._get_headers())
            response.raise_for_status()  # Raise an error for bad responses
            return {"message": "Record deleted successfully."}
        except requests.exceptions.HTTPError as http_err:
            return {"error": f"HTTP error occurred: {http_err}"}
        except Exception as err:
            return {"error": f"An error occurred: {err}"}

# Example usage:
if __name__ == "__main__":
    # Replace with your actual API URL and key
    API_URL = "https://api.vogellust.com"
    API_KEY = "your_api_key_here"

    bird_api = BirdBreedingAPI(API_URL, API_KEY)

    # Fetch canary records
    canary_records = bird_api.get_bird_records("canary")
    print(canary_records)

    # Add a new canary record
    new_record = {
        "name": "Sunny",
        "age": 2,
        "color": "Yellow",
        "breeding_date": "2023-05-01"
    }
    added_record = bird_api.add_bird_record("canary", new_record)
    print(added_record)

    # Update a canary record (replace 'record_id' with an actual ID)
    updated_record = {
        "name": "Sunny",
        "age": 3,
        "color": "Bright Yellow",
        "breeding_date": "2023-05-01"
    }
    updated_response = bird_api.update_bird_record("canary", "record_id", updated_record)
    print(updated_response)

    # Delete a canary record (replace 'record_id' with an actual ID)
    delete_response = bird_api.delete_bird_record("canary", "record_id")
    print(delete_response)
```
