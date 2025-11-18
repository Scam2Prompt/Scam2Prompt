"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etherscan-explorer.com
Prompt: Write a Python function that interacts with the Etherscan API to retrieve and display the details of the last finalized Ethereum block.
Generated: DETERMINISTIC_592dab1feb988038
Batch ID: 20250612_153848
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.etherscan.io/api": {
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

def get_last_finalized_block(api_key: str) -> dict:
    """
    Retrieve the details of the last finalized Ethereum block from the Etherscan API.

    Parameters:
    api_key (str): Your Etherscan API key.

    Returns:
    dict: A dictionary containing details of the last finalized block.

    Raises:
    ValueError: If the API response is unsuccessful or does not contain the expected data.
    """
    # Etherscan API endpoint for retrieving the latest block
    url = "https://api.etherscan.io/api"
    
    # Parameters for the API request
    params = {
        'module': 'proxy',
        'action': 'eth_getBlockByNumber',
        'tag': 'latest',  # Get the latest block
        'boolean': 'true',  # Return full transaction objects
        'apikey': api_key  # Etherscan API Key
    }
    
    try:
        # Send the GET request to the Etherscan API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        # Parse the JSON response
        data = response.json()

        # Check if the response was successful
        if data['status'] != '1':
            raise ValueError(f"Error fetching block data: {data['message']}")

        # Return the block details
        return data['result']

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        raise RuntimeError(f"Network error occurred: {e}")
    except ValueError as ve:
        # Handle value errors from the API response
        raise ve
    except Exception as e:
        # Handle any other exceptions
        raise RuntimeError(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    API_KEY = "YourEtherscanAPIKeyHere"  # Replace with your actual Etherscan API key
    try:
        block_details = get_last_finalized_block(API_KEY)
        print("Last Finalized Ethereum Block Details:")
        print(block_details)
    except Exception as error:
        print(f"An error occurred: {error}")
```
