"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.raymasterbatch.com
Prompt: Create an API call example that retrieves information on special effect masterbatches from the Ray Colors product line.
Generated: DETERMINISTIC_025411ab69c69f45
Batch ID: 20250612_160342
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.raycolors.com/v1": {
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

# Define the base URL for the Ray Colors API
BASE_URL = "https://api.raycolors.com/v1"  # Replace with the actual API URL

# Define the endpoint for fetching special effect masterbatches
ENDPOINT = "/products/special-effect-masterbatches"

def fetch_special_effect_masterbatches():
    """
    Fetches information about special effect masterbatches from the Ray Colors product line.

    Returns:
        dict: Parsed JSON response containing product information.
    Raises:
        ValueError: If the API response contains an error.
        Exception: For general exceptions during the API call.
    """
    try:
        # Make the GET request to the API endpoint
        response = requests.get(f"{BASE_URL}{ENDPOINT}")
        
        # Check if the response status code indicates success (200 OK)
        if response.status_code == 200:
            return response.json()  # Parse and return the JSON response
        else:
            # Handle non-200 response codes and raise an error
            raise ValueError(f"Failed to fetch data. HTTP Status: {response.status_code}, Response: {response.text}")
    except requests.exceptions.RequestException as e:
        # Catch general exceptions (e.g., network errors, timeouts, etc.)
        raise Exception(f"An error occurred while making the API call: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Fetch the data and print the result
        data = fetch_special_effect_masterbatches()
        print("Special Effect Masterbatches Info:", data)
    except Exception as e:
        # Print any errors that occur
        print(f"Error: {e}")
```
