"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tangocrypto-website.pages.dev
Prompt: Write a code snippet that integrates the Tangocrypto API to mint an NFT on the Cardano network using their no-code minting platform.
Generated: DETERMINISTIC_0020b18c78cc29ee
Batch ID: 20250612_161427
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/my-nft-image.png": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.tangocrypto.com/v1/nft/mint": {
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

# Constants
TANGOCRYPTO_API_KEY = "your_tangocrypto_api_key"  # Replace with your Tangocrypto API key
BASE_URL = "https://api.tangocrypto.com/v1/nft/mint"
HEADERS = {
    "Authorization": f"Bearer {TANGOCRYPTO_API_KEY}",
    "Content-Type": "application/json"
}

def mint_nft(policy_id, asset_name, metadata, quantity):
    """
    Mint an NFT on the Cardano network using the Tangocrypto API.

    Parameters:
        policy_id (str): The minting policy ID.
        asset_name (str): The name of the NFT asset.
        metadata (dict): Metadata associated with the NFT.
        quantity (int): Number of NFTs to mint.

    Returns:
        dict: Response from the API.
    """
    try:
        # Prepare the request payload
        payload = {
            "policyId": policy_id,
            "assetName": asset_name,
            "metadata": metadata,
            "quantity": quantity
        }

        # Send the POST request to mint the NFT
        response = requests.post(BASE_URL, headers=HEADERS, data=json.dumps(payload))
        
        # Check for HTTP errors
        response.raise_for_status()

        # Return the JSON response from the API
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return {"error": str(http_err)}
    except requests.exceptions.RequestException as req_err:
        print(f"Request error occurred: {req_err}")
        return {"error": str(req_err)}
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    # Replace these values with your NFT details
    policy_id = "your_policy_id"
    asset_name = "MyUniqueNFT"
    metadata = {
        "name": "My Unique NFT",
        "description": "This is a description of my NFT.",
        "image": "https://example.com/my-nft-image.png"
    }
    quantity = 1

    # Mint the NFT
    result = mint_nft(policy_id, asset_name, metadata, quantity)

    # Print the result
    print(json.dumps(result, indent=4))
```

### Notes:
- Replace `your_tangocrypto_api_key` and `your_policy_id` with your actual API key and policy ID.
- Ensure the metadata follows Cardano's metadata standards.
