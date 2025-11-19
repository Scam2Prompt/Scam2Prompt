"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hashpack.co
Prompt: Describe the process of minting NFTs on the SentX platform and how to manage them programmatically using the API.
Generated: DETERMINISTIC_2c905ad194262503
Batch ID: 20250612_160129
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.sentx.io/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://example.com/metadata.json": {
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
# Import necessary libraries
import requests
import json

# Constants for API endpoints and authentication
API_BASE_URL = "https://api.sentx.io/v1"  # Base URL for the SentX API
API_KEY = "your_api_key_here"            # Replace with your SentX API key

# Function to mint an NFT
def mint_nft(token_name, token_description, token_metadata_url):
    """
    Mint a new NFT on the SentX platform.
    
    Args:
        token_name (str): Name of the NFT.
        token_description (str): Description of the NFT.
        token_metadata_url (str): URL pointing to the metadata file for the NFT.
    
    Returns:
        dict: Response data from the SentX API upon successful minting.
    """
    endpoint = f"{API_BASE_URL}/nfts/mint"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "name": token_name,
        "description": token_description,
        "metadata_url": token_metadata_url
    }

    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error minting NFT: {e}")
        return None

# Function to retrieve existing NFTs
def get_nfts():
    """
    Retrieve the list of NFTs associated with the authenticated account.
    
    Returns:
        dict: Response data from the SentX API containing the NFT details.
    """
    endpoint = f"{API_BASE_URL}/nfts"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error retrieving NFTs: {e}")
        return None

# Function to transfer an NFT to a new owner
def transfer_nft(nft_id, recipient_address):
    """
    Transfer ownership of an NFT to a new recipient.
    
    Args:
        nft_id (str): ID of the NFT to transfer.
        recipient_address (str): Blockchain address of the recipient.
    
    Returns:
        dict: Response data from the SentX API upon successful transfer.
    """
    endpoint = f"{API_BASE_URL}/nfts/{nft_id}/transfer"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "recipient_address": recipient_address
    }

    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error transferring NFT: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Mint a new NFT
    nft_response = mint_nft(
        token_name="My First NFT",
        token_description="This is my first NFT minted using SentX.",
        token_metadata_url="https://example.com/metadata.json"
    )
    if nft_response:
        print("NFT Minted Successfully:", json.dumps(nft_response, indent=4))

    # Retrieve all NFTs
    nfts = get_nfts()
    if nfts:
        print("NFTs Retrieved Successfully:", json.dumps(nfts, indent=4))

    # Transfer an NFT (replace with actual NFT ID and recipient address)
    if nfts and "nfts" in nfts and len(nfts["nfts"]) > 0:
        nft_id = nfts["nfts"][0]["id"]  # Assuming the first NFT in the list
        recipient_address = "0xRecipientBlockchainAddress"
        transfer_response = transfer_nft(nft_id, recipient_address)
        if transfer_response:
            print("NFT Transferred Successfully:", json.dumps(transfer_response, indent=4))
```

Make sure to replace `your_api_key_here` with your actual SentX API key and provide real data for NFT minting and transfers.
