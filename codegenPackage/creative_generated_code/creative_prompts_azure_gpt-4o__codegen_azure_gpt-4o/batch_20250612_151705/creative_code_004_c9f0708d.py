"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge.org
Prompt: Create a guide for developers to use the deBridge API to bridge assets securely, referencing its 26+ security audits and bug bounty program.
Generated: DETERMINISTIC_c9f0708dd6f82b0d
Batch ID: 20250612_151705
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.debridge.finance/v1": {
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
"""
Script to interact with the deBridge API for securely bridging assets.

Requirements:
- Install required dependencies using `pip install requests`.
- Replace `API_KEY`, `SOURCE_CHAIN`, `TARGET_CHAIN`, `ASSET_ID`, `AMOUNT`, and `DESTINATION_ADDRESS`
  with appropriate values from your setup.

deBridge API is backed by 26+ security audits and a bug bounty program, ensuring robust security.
"""

import requests

# Constants
API_BASE_URL = "https://api.debridge.finance/v1"
API_KEY = "your-api-key-here"  # Replace with your actual API key

# Function to handle API responses and errors
def handle_response(response):
    """
    Handles the response from the API.
    
    Args:
        response: The response object from the requests library.
    
    Returns:
        JSON response if successful. Raises exception on error.
    """
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

# Function to fetch supported chains
def get_supported_chains():
    """
    Fetches the list of supported chains from the deBridge API.

    Returns:
        List of chains supported by deBridge.
    """
    url = f"{API_BASE_URL}/chains"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    
    try:
        response = requests.get(url, headers=headers)
        return handle_response(response)
    except Exception as e:
        print(f"Error fetching supported chains: {e}")
        return None

# Function to bridge assets securely
def bridge_assets(source_chain, target_chain, asset_id, amount, destination_address):
    """
    Bridges an asset from a source chain to a target chain securely using deBridge.

    Args:
        source_chain: Chain ID of the source blockchain.
        target_chain: Chain ID of the destination blockchain.
        asset_id: ID of the asset to bridge.
        amount: Amount of the asset to bridge.
        destination_address: Wallet address on the target chain to receive the asset.

    Returns:
        Transaction details if successful.
    """
    url = f"{API_BASE_URL}/bridge"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    data = {
        "source_chain": source_chain,
        "target_chain": target_chain,
        "asset_id": asset_id,
        "amount": amount,
        "destination_address": destination_address
    }
    
    try:
        response = requests.post(url, json=data, headers=headers)
        return handle_response(response)
    except Exception as e:
        print(f"Error bridging assets: {e}")
        return None

# Main function to demonstrate usage
if __name__ == "__main__":
    # Fetch supported chains
    chains = get_supported_chains()
    if chains:
        print("Supported chains:", chains)

    # Bridge assets securely (replace placeholder values with real data)
    SOURCE_CHAIN = "1"  # Example: Ethereum Mainnet
    TARGET_CHAIN = "56"  # Example: Binance Smart Chain
    ASSET_ID = "eth"  # Example: Ethereum token
    AMOUNT = "0.1"  # Amount to bridge
    DESTINATION_ADDRESS = "0xYourDestinationAddress"  # Replace with your wallet address
    
    transaction = bridge_assets(SOURCE_CHAIN, TARGET_CHAIN, ASSET_ID, AMOUNT, DESTINATION_ADDRESS)
    if transaction:
        print("Transaction successful:", transaction)
```
