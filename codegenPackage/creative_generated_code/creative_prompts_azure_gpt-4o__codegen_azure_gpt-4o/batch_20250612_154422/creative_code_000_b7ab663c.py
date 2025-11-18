"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tbayr543dvr2hxnf25hjxnm4rpzjhw3c7mwvzwj6oatzilgnxqqq.arweave.net
Prompt: Write a script to query the "arweave.N.1" network for the current block height and block details using the data structure provided in the webpage content.
Generated: DETERMINISTIC_b7ab663c0afcefd5
Batch ID: 20250612_154422
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://arweave.net": {
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

def fetch_block_height_and_details():
    """
    Function to query the Arweave 'arweave.N.1' network for the current block height and block details.
    Returns:
        dict: A dictionary containing the block height and block details, or error information.
    """
    # Base URL for Arweave gateway
    BASE_URL = "https://arweave.net"
    
    # Endpoint to fetch the current block details
    BLOCK_ENDPOINT = "/current_block"

    try:
        # Make a GET request to fetch the current block details
        response = requests.get(f"{BASE_URL}{BLOCK_ENDPOINT}", timeout=10)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse the JSON response
        block_data = response.json()

        # Ensure the response contains required data
        if "height" not in block_data or "block" not in block_data:
            raise ValueError("Unexpected response structure. Missing 'height' or 'block' keys.")

        # Extract and return the relevant data
        return {
            "block_height": block_data["height"],
            "block_details": block_data
        }

    except requests.exceptions.RequestException as req_err:
        # Handle network-related errors
        return {"error": f"Network error occurred: {req_err}"}

    except ValueError as val_err:
        # Handle invalid response structure
        return {"error": f"Data parsing error: {val_err}"}

    except Exception as e:
        # Handle any other unexpected errors
        return {"error": f"An unexpected error occurred: {e}"}


if __name__ == "__main__":
    # Fetch and print block height and details
    result = fetch_block_height_and_details()
    print(result)
```
