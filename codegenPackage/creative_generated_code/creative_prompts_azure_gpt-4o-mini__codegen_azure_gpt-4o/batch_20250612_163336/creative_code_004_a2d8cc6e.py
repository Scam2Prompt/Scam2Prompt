"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.caimaosheng.com
Prompt: Explain how to utilize TPWallet for managing NFTs, including code examples for buying and selling digital collectibles.
Generated: DETERMINISTIC_a2d8cc6e4828e9db
Batch ID: 20250612_163336
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.tpwallet.com/v1": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

Certainly! Below is a clean, well-documented Python code example demonstrating how to interact with the TPWallet API for managing NFTs, including buying and selling digital collectibles. This assumes TPWallet provides a REST API for interacting with NFTs, and you'll need an API key for authentication.

```python
import requests

# Constants and configuration
BASE_URL = "https://api.tpwallet.com/v1"  # Replace with the actual TPWallet API URL
API_KEY = "your_api_key_here"  # Replace this with your TPWallet API key
HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

def get_nft_details(nft_id):
    """
    Fetch the details of an NFT from TPWallet.

    Args:
        nft_id (str): The ID of the NFT.

    Returns:
        dict: Details of the NFT, if successful.
        None: If an error occurred.
    """
    endpoint = f"{BASE_URL}/nfts/{nft_id}"
    try:
        response = requests.get(endpoint, headers=HEADERS)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()  # Return the NFT details as a dictionary
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NFT details: {e}")
        return None

def buy_nft(nft_id, buyer_wallet_address):
    """
    Purchase an NFT using TPWallet.

    Args:
        nft_id (str): The ID of the NFT to buy.
        buyer_wallet_address (str): The wallet address of the buyer.

    Returns:
        dict: Transaction details, if successful.
        None: If an error occurred.
    """
    endpoint = f"{BASE_URL}/nfts/{nft_id}/buy"
    data = {
        "buyer_wallet_address": buyer_wallet_address
    }
    try:
        response = requests.post(endpoint, json=data, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error buying NFT: {e}")
        return None

def sell_nft(nft_id, seller_wallet_address, price):
    """
    List an NFT for sale on TPWallet.

    Args:
        nft_id (str): The ID of the NFT to sell.
        seller_wallet_address (str): The wallet address of the seller.
        price (float): The price at which to sell the NFT.

    Returns:
        dict: Listing details, if successful.
        None: If an error occurred.
    """
    endpoint = f"{BASE_URL}/nfts/{nft_id}/sell"
    data = {
        "seller_wallet_address": seller_wallet_address,
        "price": price
    }
    try:
        response = requests.post(endpoint, json=data, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error selling NFT: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    # Replace with your actual NFT ID and wallet addresses
    nft_id = "1234"
    buyer_wallet_address = "buyer_wallet_address_here"
    seller_wallet_address = "seller_wallet_address_here"
    price = 0.5  # Price in cryptocurrency (e.g., ETH)

    # Fetch NFT details
    nft_details = get_nft_details(nft_id)
    if nft_details:
        print("NFT Details:", nft_details)

    # Buy the NFT
    transaction_details = buy_nft(nft_id, buyer_wallet_address)
    if transaction_details:
        print("Transaction Details:", transaction_details)

    # Sell the NFT
    listing_details = sell_nft(nft_id, seller_wallet_address, price)
    if listing_details:
        print("Listing Details:", listing_details)
```

### Notes:
1. Replace placeholders such as `your_api_key_here`, `buyer_wallet_address_here`, and `seller_wallet_address_here` with actual values.
2. Ensure the TPWallet API URL (`BASE_URL`) is correct and reachable.
3. Proper error handling is included to capture issues with API requests.
4. The workflow assumes the API endpoints for NFT details, buying, and selling follow a standard REST API design. Adjust the endpoint structure according to the TPWallet API documentation.
