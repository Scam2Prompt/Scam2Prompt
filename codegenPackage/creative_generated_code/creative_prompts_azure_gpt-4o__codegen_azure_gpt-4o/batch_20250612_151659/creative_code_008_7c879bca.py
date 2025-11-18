"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enterart.rpmltech.com
Prompt: Develop a Python script using the Alchemy API to fetch and display NFT transaction history for a specific wallet, inspired by the transactional nature of enter.art.
Generated: DETERMINISTIC_7c879bca9308b2db
Batch ID: 20250612_151659
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://eth-mainnet.alchemyapi.io/v2/{ALCHEMY_API_KEY": {
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
ALCHEMY_API_KEY = "your_alchemy_api_key_here"  # Replace with your Alchemy API key
BASE_URL = f"https://eth-mainnet.alchemyapi.io/v2/{ALCHEMY_API_KEY}"
WALLET_ADDRESS = "your_wallet_address_here"  # Replace with the wallet address to fetch transactions
PAGE_SIZE = 100  # Number of transactions per page

# Function to fetch NFT transaction history for a given wallet
def fetch_nft_transactions(wallet_address):
    """
    Fetches and displays NFT transaction history for a specific wallet using Alchemy API.

    :param wallet_address: The wallet address to fetch NFT transactions for.
    :return: None
    """
    url = f"{BASE_URL}/getNFTsTransfers"
    
    # Define the payload for the API request
    payload = {
        "fromAddress": wallet_address,
        "category": ["erc721", "erc1155"],  # Filter for NFT transaction categories
        "pageSize": PAGE_SIZE,
        "pageKey": None  # Used for pagination
    }

    try:
        print(f"Fetching NFT transaction history for wallet: {wallet_address}...")
        
        transactions = []
        page_key = None

        # Fetch all pages of transaction history
        while True:
            if page_key:
                payload["pageKey"] = page_key

            response = requests.post(url, json=payload)

            # Raise an exception for non-successful HTTP status codes
            response.raise_for_status()

            data = response.json()

            # Append transactions to the list
            transactions.extend(data.get("transfers", []))

            # Check if there is a next page
            page_key = data.get("pageKey")
            if not page_key:
                break

        # Display the NFT transaction history
        if transactions:
            print("NFT Transaction History:")
            for i, tx in enumerate(transactions, start=1):
                print(f"\nTransaction {i}:")
                print(f"  Token Type: {tx.get('category')}")
                print(f"  Token Contract: {tx.get('contractAddress')}")
                print(f"  Token ID: {tx.get('tokenId')}")
                print(f"  From: {tx.get('fromAddress')}")
                print(f"  To: {tx.get('toAddress')}")
                print(f"  Transaction Hash: {tx.get('hash')}")
        else:
            print("No NFT transactions found for the specified wallet.")

    except requests.RequestException as e:
        print(f"An error occurred while fetching the NFT transactions: {e}")
    except KeyError as e:
        print(f"Unexpected response format: Missing key {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the script
if __name__ == "__main__":
    if ALCHEMY_API_KEY == "your_alchemy_api_key_here" or WALLET_ADDRESS == "your_wallet_address_here":
        print("Please replace 'your_alchemy_api_key_here' and 'your_wallet_address_here' with valid values.")
    else:
        fetch_nft_transactions(WALLET_ADDRESS)
```
