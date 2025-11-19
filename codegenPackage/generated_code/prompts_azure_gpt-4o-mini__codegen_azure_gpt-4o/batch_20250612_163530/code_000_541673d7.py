"""
Generated Code Metadata:
========================
Original URL: https://magahat-3gz.pages.dev
Prompt: Generate a Python script that interacts with the Ord.io API to check the minting status of the MAGA•THE•DONALD•TRUMP collection, including the number of completed and pending mints.
Generated: DETERMINISTIC_541673d73580ab45
Batch ID: 20250612_163530
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ord.io/v1/collections": {
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

def fetch_minting_status(collection_name):
    """
    Fetches the minting status of a given collection from the Ord.io API.

    Args:
        collection_name (str): The name of the collection to check.

    Returns:
        dict: A dictionary containing the number of completed and pending mints.
    """
    # Base URL for the Ord.io API
    base_url = "https://api.ord.io/v1/collections"

    # Construct the API endpoint for the specific collection
    endpoint = f"{base_url}/{collection_name}/minting-status"

    try:
        # Send a GET request to the API
        response = requests.get(endpoint)

        # Raise an exception if the request was unsuccessful
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Extract minting status details
        completed_mints = data.get("completed_mints", 0)
        pending_mints = data.get("pending_mints", 0)

        return {
            "completed_mints": completed_mints,
            "pending_mints": pending_mints
        }

    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        print(f"Error fetching minting status: {e}")
        return None
    except ValueError:
        # Handle JSON parsing errors
        print("Error parsing the response from the API.")
        return None


def main():
    """
    Main function to check the minting status of the MAGA•THE•DONALD•TRUMP collection.
    """
    # Collection name to query
    collection_name = "MAGA•THE•DONALD•TRUMP"

    print(f"Checking minting status for collection: {collection_name}")

    # Fetch minting status
    status = fetch_minting_status(collection_name)

    if status:
        # Display the minting status
        print(f"Completed Mints: {status['completed_mints']}")
        print(f"Pending Mints: {status['pending_mints']}")
    else:
        print("Failed to retrieve minting status.")


if __name__ == "__main__":
    # Entry point of the script
    main()
```
