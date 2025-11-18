"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://upgrading-ethereum.info
Prompt: Write a Python script to query the Ethereum blockchain and retrieve information about the Capella upgrade, referencing the details provided in the "Upgrading Ethereum" handbook.
Generated: DETERMINISTIC_2844a9cc2752ada2
Batch ID: 20250612_151752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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

# Define constants for Ethereum blockchain API
ETHEREUM_MAINNET_RPC_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID"  # Replace with your Infura project ID
CAPELLA_UPGRADE_BLOCK = 16813384  # Example block number for Capella upgrade (replace with accurate block number from "Upgrading Ethereum" handbook)

def fetch_block_details(block_number):
    """
    Fetch details of a specific block from the Ethereum blockchain.

    Args:
        block_number (int): The block number to fetch details for.

    Returns:
        dict: Details of the Ethereum block if successful, None otherwise.
    """
    try:
        # Prepare the JSON-RPC payload
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBlockByNumber",
            "params": [hex(block_number), True],  # Convert block number to hexadecimal format
            "id": 1
        }

        # Send the request to the Ethereum RPC endpoint
        response = requests.post(ETHEREUM_MAINNET_RPC_URL, json=payload)

        # Check for HTTP errors
        response.raise_for_status()

        # Parse the response JSON
        block_data = response.json()

        # Check for errors in the API response
        if "error" in block_data:
            print(f"Error fetching block details: {block_data['error']['message']}")
            return None

        return block_data.get("result", None)

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Network error occurred: {e}")
        return None
    except Exception as e:
        # Handle any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None

def main():
    """
    Main function that queries the Ethereum blockchain for Capella upgrade details.
    """
    print("Fetching Capella upgrade block details...")

    # Retrieve block details for the Capella upgrade block
    block_details = fetch_block_details(CAPELLA_UPGRADE_BLOCK)

    if block_details:
        print("Capella Upgrade Block Details:")
        print(json.dumps(block_details, indent=4))
    else:
        print("Failed to retrieve block details.")

if __name__ == "__main__":
    main()
```

**Notes for usage:**  
1. Replace `YOUR_INFURA_PROJECT_ID` with a valid Infura project ID or another Ethereum provider's endpoint.  
2. Update `CAPELLA_UPGRADE_BLOCK` to the actual block number for the Capella upgrade from the "Upgrading Ethereum" handbook if not accurate.
