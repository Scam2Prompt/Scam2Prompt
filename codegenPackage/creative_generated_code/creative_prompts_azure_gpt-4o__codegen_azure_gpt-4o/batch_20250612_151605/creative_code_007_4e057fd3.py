"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknet-homepage.vercel.app
Prompt: Write a tutorial-style prompt explaining how to use Starknet APIs to retrieve ownership details of NFTs displayed on the Starknet Homepage.
Generated: DETERMINISTIC_4e057fd322fa3eb9
Batch ID: 20250612_151605
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.starknet.io": {
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
# Import required libraries
import requests

# Constants
BASE_URL = "https://api.starknet.io"  # Base URL for Starknet API
NFT_ENDPOINT = "/v1/nft"  # Endpoint for NFT details

# Function to fetch ownership details of NFTs
def get_nft_ownership_details(contract_address, token_id):
    """
    Retrieves ownership details of an NFT from the Starknet API.

    Args:
        contract_address (str): The contract address of the NFT.
        token_id (str): The token ID of the NFT.

    Returns:
        dict: A dictionary containing ownership information if successful.
        None: If the data could not be retrieved.
    """
    # Construct the API URL
    url = f"{BASE_URL}{NFT_ENDPOINT}/ownership"

    # Prepare the query parameters
    params = {
        "contract_address": contract_address,
        "token_id": token_id
    }

    try:
        # Send request to the Starknet API
        response = requests.get(url, params=params)

        # Check if the response status code is successful
        if response.status_code == 200:
            # Parse and return the JSON response
            return response.json()
        else:
            # Log the error message
            print(f"Error: Failed to retrieve ownership details (Status Code {response.status_code})")
            return None
    except requests.exceptions.RequestException as e:
        # Handle connection errors
        print(f"Error: An exception occurred while connecting to the API - {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace these with actual values
    example_contract_address = "0x1234abcd5678efgh9012ijkl3456mnop7890qrst"
    example_token_id = "1"

    # Fetch ownership details
    ownership_details = get_nft_ownership_details(example_contract_address, example_token_id)

    # Display the results
    if ownership_details:
        print("NFT Ownership Details:")
        print(ownership_details)
    else:
        print("Failed to retrieve NFT ownership details.")
```

### Notes:
- Replace `example_contract_address` and `example_token_id` with actual values of the NFT you are querying.
- Ensure you have access to the Starknet APIs and appropriate permissions for the query.
- Install the `requests` library if not already installed (`pip install requests`).
```
