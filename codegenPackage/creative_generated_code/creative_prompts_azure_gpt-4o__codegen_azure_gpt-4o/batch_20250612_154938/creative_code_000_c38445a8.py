"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gorodshansona.ru
Prompt: Write a Python script to interact with Immutable X's API for minting NFTs using the Immutable X Mint feature described on gorodshansona.ru.
Generated: DETERMINISTIC_c38445a8e297ac46
Batch ID: 20250612_154938
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.x.immutable.com/v1": {
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
from typing import List

# Constants
API_BASE_URL = "https://api.x.immutable.com/v1"  # Immutable X API base URL
MINT_ENDPOINT = "/mints"  # Endpoint for minting NFTs

# Replace these with your Immutable X API Key and Wallet Address
API_KEY = "your_api_key_here"
WALLET_ADDRESS = "your_wallet_address_here"

# Function to mint NFTs
def mint_nfts(token_data: List[dict]):
    """
    Mint NFTs using Immutable X API.
    :param token_data: List of token data dictionaries for minting.
                       Each dictionary should contain 'token_id', 'blueprint', and 
                       'destination_address'.
    :return: Response data from the API.
    """
    url = f"{API_BASE_URL}{MINT_ENDPOINT}"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "mints": [
            {
                "token_id": token["token_id"],
                "blueprint": token["blueprint"],
                "destination_address": token["destination_address"],
            }
            for token in token_data
        ],
    }

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()  # Raise HTTPError for bad responses
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error while interacting with Immutable X API: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Define the NFT data to be minted
    nft_data = [
        {
            "token_id": "1",
            "blueprint": "Example blueprint for NFT 1",
            "destination_address": WALLET_ADDRESS,
        },
        {
            "token_id": "2",
            "blueprint": "Example blueprint for NFT 2",
            "destination_address": WALLET_ADDRESS,
        },
    ]

    # Mint the NFTs
    result = mint_nfts(nft_data)
    if result:
        print("Minting Successful!")
        print(json.dumps(result, indent=4))
    else:
        print("Minting failed. Please check the error.")
```

Replace placeholders like `your_api_key_here` and `your_wallet_address_here` with your actual API key and wallet address. Ensure the `token_data` structure matches Immutable X's requirements.
