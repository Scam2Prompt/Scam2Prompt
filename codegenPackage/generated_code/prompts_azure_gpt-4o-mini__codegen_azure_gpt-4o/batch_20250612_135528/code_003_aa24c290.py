"""
Generated Code Metadata:
========================
Original URL: https://starknetvietnam.wordpress.com
Prompt: Create an API call example for interacting with StarkNet's decentralized network for a dApp.
Generated: DETERMINISTIC_aa24c29019596b8f
Batch ID: 20250612_135528
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://alpha-mainnet.starknet.io/feeder_gateway": {
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

# Constants
BASE_URL = "https://alpha-mainnet.starknet.io/feeder_gateway"
ENDPOINT = "/get_block"
TIMEOUT = 10  # Timeout for the API call in seconds

def get_latest_block():
    """
    Fetches the latest block from StarkNet's decentralized network.

    Returns:
        dict: The latest block data if the request is successful.
        None: If the request fails or an error occurs.
    """
    url = f"{BASE_URL}{ENDPOINT}"
    
    try:
        # Make the API call
        response = requests.get(url, timeout=TIMEOUT)
        
        # Check if the response status code indicates success
        response.raise_for_status()
        
        # Parse the JSON response
        block_data = response.json()
        return block_data
    
    except requests.exceptions.Timeout:
        # Handle timeout errors
        print("Error: The request timed out.")
    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as req_err:
        # Handle other request-related errors
        print(f"Request error occurred: {req_err}")
    except ValueError:
        # Handle JSON parsing errors
        print("Error: Failed to parse the response as JSON.")
    
    return None

if __name__ == "__main__":
    # Example usage
    latest_block = get_latest_block()
    if latest_block:
        print("Latest Block Data:")
        print(latest_block)
    else:
        print("Failed to fetch the latest block.")
```
