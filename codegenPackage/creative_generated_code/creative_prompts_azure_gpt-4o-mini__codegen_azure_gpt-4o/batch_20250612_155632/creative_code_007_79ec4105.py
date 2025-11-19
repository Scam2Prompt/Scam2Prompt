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
  "https://api.chainbase.com/v1/catalog": {
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

def list_available_datasets(api_key: str, base_url: str = "https://api.chainbase.com/v1/catalog") -> list:
    """
    Fetches and lists available datasets from Chainbase's data catalog.

    Parameters:
        api_key (str): The API key to authenticate the request.
        base_url (str): The base URL for Chainbase's data catalog API (default is "https://api.chainbase.com/v1/catalog").

    Returns:
        list: A list of available datasets for developers. Each dataset is represented as a dictionary.

    Raises:
        ValueError: If the API key is invalid or missing.
        Exception: For any other errors during the API call.
    """
    # Validate the API key
    if not api_key:
        raise ValueError("API key is required to interact with Chainbase.")

    # Prepare the request headers
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    try:
        # Send a GET request to the Chainbase data catalog
        response = requests.get(base_url, headers=headers)
        
        # Check for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        data = response.json()

        # Ensure the response structure matches the expected format
        if "datasets" in data:
            return data["datasets"]
        else:
            raise Exception("Unexpected response format from Chainbase API.")

    except requests.exceptions.HTTPError as http_err:
        raise Exception(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        raise Exception(f"Request error occurred: {req_err}")
    except Exception as err:
        raise Exception(f"An error occurred: {err}")

# Example usage:
# Replace 'your_api_key_here' with a valid API key to test the function.
# datasets = list_available_datasets(api_key="your_api_key_here")
# print(datasets)
```
