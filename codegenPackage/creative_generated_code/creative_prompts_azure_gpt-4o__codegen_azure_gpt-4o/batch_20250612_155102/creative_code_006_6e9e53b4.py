"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abstractdog.testnet.nfts2.me
Prompt: Generate code to list all NFTs minted on the Abstract Testnet blockchain and filter them by price using the NFTs2Me API.
Generated: DETERMINISTIC_6e9e53b4b8da7a97
Batch ID: 20250612_155102
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nfts2me.com/v1": {
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

# Constants
API_BASE_URL = "https://api.nfts2me.com/v1"
API_KEY = "your_api_key_here"  # Replace with your actual API key
CHAIN = "abstract-testnet"  # Blockchain network

def get_nfts_minted(chain):
    """
    Fetches all NFTs minted on the specified chain using the NFTs2Me API.

    Args:
        chain (str): Blockchain identifier (e.g., "abstract-testnet").

    Returns:
        list: A list of NFT objects.
    """
    url = f"{API_BASE_URL}/nfts"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    params = {
        "chain": chain
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4XX or 5XX)
        return response.json().get("nfts", [])  # Extract NFTs from the response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NFTs: {e}")
        return []

def filter_nfts_by_price(nfts, max_price):
    """
    Filters NFTs based on a maximum price.

    Args:
        nfts (list): List of NFT objects.
        max_price (float): Maximum price threshold.

    Returns:
        list: A list of NFT objects that meet the price criteria.
    """
    filtered_nfts = []
    for nft in nfts:
        try:
            price = float(nft.get("price", 0))  # Safely parse price to float
            if price <= max_price:
                filtered_nfts.append(nft)
        except ValueError:
            print(f"Error parsing price for NFT: {nft.get('id')}")
    return filtered_nfts

def main():
    """
    Main function to list and filter NFTs minted on Abstract Testnet.
    """
    # Step 1: Fetch all NFTs minted on the Abstract Testnet
    nfts = get_nfts_minted(CHAIN)
    if not nfts:
        print("No NFTs found.")
        return

    print(f"Total NFTs fetched: {len(nfts)}")

    # Step 2: Filter NFTs by price
    max_price = 10.0  # Example: Filter NFTs with price <= 10.0
    affordable_nfts = filter_nfts_by_price(nfts, max_price)

    print(f"NFTs filtered by price <= {max_price}: {len(affordable_nfts)}")
    for nft in affordable_nfts:
        print(f"ID: {nft.get('id')}, Name: {nft.get('name')}, Price: {nft.get('price')}")

if __name__ == "__main__":
    main()
```

### Notes:
- Replace `"your_api_key_here"` with your actual API key from NFTs2Me.
- Ensure the `nfts2me` API documentation is consulted for any further required parameters or endpoints.
- Install the `requests` library if not already available (`pip install requests`).
