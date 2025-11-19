"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeihshlkdjr46fxka7faju5vgwqvmxiqb2pzzzioolpab5qvh37z7tm.ipfs.dweb.link
Prompt: Write a code snippet that demonstrates asset portability between Bitcoin and Ethereum networks using Hemi's Tunnels.
Generated: DETERMINISTIC_dc4170af291c0ac6
Batch ID: 20250612_164305
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.hemistunnels.io/v1`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.hemistunnels.io/v1": {
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
This script demonstrates asset portability between Bitcoin and Ethereum networks
using Hemi's Tunnels. It assumes Hemi's Tunnels API is properly configured and
available in your environment.
"""

import requests

# Constants
HEMIS_TUNNELS_API_URL = "https://api.hemistunnels.io/v1"
BITCOIN_NETWORK = "bitcoin"
ETHEREUM_NETWORK = "ethereum"

# Functions
def initiate_asset_transfer(asset_id, amount, source_network, destination_network):
    """
    Initiates an asset transfer between Bitcoin and Ethereum networks using Hemi's Tunnels.

    Parameters:
        asset_id (str): The ID of the asset to transfer.
        amount (float): The amount to transfer.
        source_network (str): The source network ('bitcoin' or 'ethereum').
        destination_network (str): The destination network ('ethereum' or 'bitcoin').

    Returns:
        dict: The response from Hemi's Tunnels API.
    """
    try:
        # Payload for API request
        payload = {
            "asset_id": asset_id,
            "amount": amount,
            "source_network": source_network,
            "destination_network": destination_network
        }

        # Make POST request to Hemi's Tunnels API
        response = requests.post(f"{HEMIS_TUNNELS_API_URL}/transfer", json=payload)

        # Raise an exception for HTTP errors
        response.raise_for_status()

        # Parse and return the response JSON
        return response.json()

    except requests.exceptions.RequestException as e:
        # Handle request exceptions
        print(f"Error initiating asset transfer: {str(e)}")
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Asset details
    asset_id = "btc"  # Example: Bitcoin's asset ID in Hemi's Tunnels
    amount = 0.01     # Example amount to transfer
    source_network = BITCOIN_NETWORK
    destination_network = ETHEREUM_NETWORK

    # Initiate asset transfer
    response = initiate_asset_transfer(asset_id, amount, source_network, destination_network)

    # Output the result
    if "error" in response:
        print("Asset transfer failed:", response["error"])
    else:
        print("Asset transfer successful:", response)
```

Note: Replace `https://api.hemistunnels.io/v1` and asset identifiers with appropriate values from Hemi's Tunnels documentation or your environment. Ensure proper authentication if required by the API.
