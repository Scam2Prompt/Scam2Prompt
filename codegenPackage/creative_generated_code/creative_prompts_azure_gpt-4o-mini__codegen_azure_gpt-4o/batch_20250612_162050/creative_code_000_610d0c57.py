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
  "https://api.vogellust.com/bird-breeding": {
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

# Constants
BASE_API_URL = "https://api.vogellust.com/bird-breeding"  # Replace with the actual API URL
API_TOKEN = "your_api_token_here"  # Replace with your API token
HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Content-Type": "application/json",
}

# Functions

def get_bird_records(bird_type):
    """
    Fetch all breeding records for a specific bird type.

    Args:
        bird_type (str): Type of bird (e.g., 'canary', 'tropical').

    Returns:
        list: List of bird breeding records, or None if an error occurred.
    """
    try:
        url = f"{BASE_API_URL}/{bird_type}/records"
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Parse JSON response
    except requests.RequestException as e:
        print(f"Error fetching records for {bird_type}: {e}")
        return None


def add_bird_record(bird_type, record_data):
    """
    Add a new breeding record for a specific bird type.

    Args:
        bird_type (str): Type of bird (e.g., 'canary', 'tropical').
        record_data (dict): Data for the new record.

    Returns:
        dict: Response from the API, or None if an error occurred.
    """
    try:
        url = f"{BASE_API_URL}/{bird_type}/records"
        response = requests.post(url, headers=HEADERS, json=record_data)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error adding record for {bird_type}: {e}")
        return None


def delete_bird_record(bird_type, record_id):
    """
    Delete a breeding record for a specific bird type.

    Args:
        bird_type (str): Type of bird (e.g., 'canary', 'tropical').
        record_id (int): ID of the record to delete.

    Returns:
        bool: True if the record was deleted successfully, False otherwise.
    """
    try:
        url = f"{BASE_API_URL}/{bird_type}/records/{record_id}"
        response = requests.delete(url, headers=HEADERS)
        response.raise_for_status()
        return True
    except requests.RequestException as e:
        print(f"Error deleting record {record_id} for {bird_type}: {e}")
        return False


# Example Usage
if __name__ == "__main__":
    # Fetch breeding records for canaries
    canary_records = get_bird_records("canary")
    if canary_records is not None:
        print("Canary Breeding Records:")
        print(json.dumps(canary_records, indent=2))

    # Add a new breeding record for tropical birds
    new_record = {
        "name": "Yellow-bellied Finch",
        "date_bred": "2023-10-01",
        "notes": "Healthy chick hatched successfully.",
    }
    response = add_bird_record("tropical", new_record)
    if response is not None:
        print("New record added successfully:")
        print(json.dumps(response, indent=2))

    # Delete a breeding record by ID
    record_id_to_delete = 123  # Replace with an actual record ID
    if delete_bird_record("canary", record_id_to_delete):
        print(f"Record {record_id_to_delete} deleted successfully.")
    else:
        print(f"Failed to delete record {record_id_to_delete}.")
```
