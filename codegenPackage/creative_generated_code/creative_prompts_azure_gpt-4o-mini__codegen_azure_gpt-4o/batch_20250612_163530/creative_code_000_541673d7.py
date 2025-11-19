"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://magahat-3gz.pages.dev
Prompt: Generate a Python script that interacts with the Ord.io API to check the minting status of the MAGA•THE•DONALD•TRUMP collection, including the number of completed and pending mints.
Generated: DETERMINISTIC_541673d73580ab45
Batch ID: 20250612_163530
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ord.io/v1": {
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

def fetch_minting_status(api_url, collection_name):
    """
    Fetches the minting status of a given collection from the Ord.io API.

    Args:
        api_url (str): Base URL of the Ord.io API.
        collection_name (str): Name of the collection to check minting status.

    Returns:
        dict: A dictionary containing completed and pending mint statuses.
    """
    try:
        # Construct the API endpoint URL
        endpoint = f"{api_url}/collections/{collection_name}/minting-status"
        
        # Send a GET request to the Ord.io API
        response = requests.get(endpoint)

        # Raise an HTTPError if the response status code is not 200
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Extract relevant minting status information
        minting_status = {
            "completed_mints": data.get("completed_mints", 0),
            "pending_mints": data.get("pending_mints", 0)
        }

        return minting_status
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error occurred while accessing the API: {e}")
        return None
    
    except ValueError as e:
        # Handle JSON parsing errors
        print(f"Error occurred while parsing the response: {e}")
        return None


if __name__ == "__main__":
    # Define the API base URL and collection name
    ORD_IO_API_URL = "https://api.ord.io/v1"
    COLLECTION_NAME = "MAGA•THE•DONALD•TRUMP"

    # Fetch the minting status
    status = fetch_minting_status(ORD_IO_API_URL, COLLECTION_NAME)

    # Print the minting status if successfully retrieved
    if status:
        print(f"Minting Status for '{COLLECTION_NAME}':")
        print(f"Completed Mints: {status['completed_mints']}")
        print(f"Pending Mints: {status['pending_mints']}")
    else:
        print("Failed to retrieve minting status.")
```
