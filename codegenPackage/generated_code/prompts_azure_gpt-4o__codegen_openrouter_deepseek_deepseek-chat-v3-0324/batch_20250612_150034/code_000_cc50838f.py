"""
Generated Code Metadata:
========================
Original URL: https://jamcards.io
Prompt: Write a script using the OpenSea API to fetch details about the "Heart Full of Love JamCards" NFT collection, including item names, prices, and last sale amounts.
Generated: DETERMINISTIC_cc50838f9e359655
Batch ID: 20250612_150034
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v2": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import json
from datetime import datetime

# OpenSea API configuration
OPENSEA_API_BASE_URL = "https://api.opensea.io/api/v2"
COLLECTION_SLUG = "heart-full-of-love-jamcards"
HEADERS = {
    "accept": "application/json",
    "X-API-KEY": "your-api-key-here"  # Replace with your actual OpenSea API key
}

def fetch_collection_details():
    """
    Fetch basic details about the NFT collection.
    Returns: Dictionary containing collection details or None if error occurs.
    """
    url = f"{OPENSEA_API_BASE_URL}/collections/{COLLECTION_SLUG}"
    
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching collection details: {e}")
        return None

def fetch_nfts(limit=50, next_cursor=None):
    """
    Fetch NFTs from the collection with pagination support.
    Args:
        limit: Number of NFTs to fetch per request (max 200)
        next_cursor: Pagination cursor for next page
    Returns: Dictionary containing NFTs and pagination info or None if error occurs
    """
    url = f"{OPENSEA_API_BASE_URL}/collection/{COLLECTION_SLUG}/nfts"
    params = {
        "limit": limit,
    }
    
    if next_cursor:
        params["next"] = next_cursor
    
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching NFTs: {e}")
        return None

def process_nft_data(nfts):
    """
    Process raw NFT data to extract relevant information.
    Args:
        nfts: List of NFT dictionaries from API response
    Returns: List of processed NFT dictionaries
    """
    processed_nfts = []
    
    for nft in nfts.get('nfts', []):
        processed = {
            'name': nft.get('name', 'Unnamed'),
            'token_id': nft.get('identifier'),
            'image_url': nft.get('image_url'),
            'last_sale': None,
            'current_price': None
        }
        
        # Process last sale if available
        if nft.get('last_sale'):
            last_sale = nft['last_sale']
            processed['last_sale'] = {
                'amount': float(last_sale.get('total_price', 0)),
                'currency': last_sale.get('payment_token', {}).get('symbol', 'ETH'),
                'date': last_sale.get('event_timestamp')
            }
        
        # Process listings if available
        if nft.get('orders'):
            for order in nft['orders']:
                if order.get('order_type') == 'basic' and order.get('side') == 1:  # Sell order
                    processed['current_price'] = {
                        'amount': float(order.get('current_price', 0)),
                        'currency': order.get('payment_token', {}).get('symbol', 'ETH')
                    }
                    break
        
        processed_nfts.append(processed)
    
    return processed_nfts

def save_to_json(data, filename_prefix="nft_data"):
    """
    Save data to a JSON file with timestamp.
    Args:
        data: Data to save
        filename_prefix: Prefix for the filename
    """
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{filename_prefix}_{timestamp}.json"
    
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Data saved to {filename}")
    except IOError as e:
        print(f"Error saving file: {e}")

def main():
    # Fetch collection details
    collection = fetch_collection_details()
    if not collection:
        print("Failed to fetch collection details. Exiting.")
        return
    
    print(f"Fetching NFTs for collection: {collection.get('name')}")
    
    all_nfts = []
    next_cursor = None
    has_more = True
    
    # Fetch all NFTs with pagination
    while has_more:
        response = fetch_nfts(limit=50, next_cursor=next_cursor)
        if not response:
            break
            
        processed = process_nft_data(response)
        all_nfts.extend(processed)
        
        next_cursor = response.get('next')
        has_more = bool(next_cursor)
        print(f"Fetched {len(processed)} NFTs. Total so far: {len(all_nfts)}")
    
    if not all_nfts:
        print("No NFTs found in collection.")
        return
    
    # Save results
    result = {
        'collection': {
            'name': collection.get('name'),
            'description': collection.get('description'),
            'total_supply': collection.get('total_supply'),
            'stats': collection.get('stats')
        },
        'nfts': all_nfts,
        'timestamp': datetime.now().isoformat()
    }
    
    save_to_json(result)
    print(f"Successfully processed {len(all_nfts)} NFTs")

if __name__ == "__main__":
    main()
```
