"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airbox-dao.web.app
Prompt: Create a script to search for collections and creators on the Solana network, as highlighted in the Airbox DAO content.
Generated: DETERMINISTIC_9273b908f0eb22a5
Batch ID: 20250612_150557
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.solscan.io": {
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
BASE_URL = "https://api.solscan.io"  # Solana blockchain explorer API
API_KEY = "your_api_key_here"        # Replace with your Solscan API key

# Function to search for collections
def search_collections(keyword):
    """
    Search for collections on the Solana network using a keyword.
    
    Args:
        keyword (str): Search term for the collection.
        
    Returns:
        list: List of matching collections or an empty list if none found.
    """
    try:
        url = f"{BASE_URL}/nft/collections"
        headers = {"accept": "application/json", "token": API_KEY}
        params = {"search": keyword}
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        data = response.json()
        return data.get("data", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching collections: {e}")
        return []

# Function to search for creators
def search_creators(keyword):
    """
    Search for creators on the Solana network using a keyword.
    
    Args:
        keyword (str): Search term for the creator.
        
    Returns:
        list: List of matching creators or an empty list if none found.
    """
    try:
        url = f"{BASE_URL}/nft/creators"
        headers = {"accept": "application/json", "token": API_KEY}
        params = {"search": keyword}
        
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        data = response.json()
        return data.get("data", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching creators: {e}")
        return []

# Main function for demonstration
if __name__ == "__main__":
    # Input keywords
    collection_keyword = input("Enter keyword to search for collections: ").strip()
    creator_keyword = input("Enter keyword to search for creators: ").strip()

    # Search collections
    print("\n--- Searching Collections ---")
    collections = search_collections(collection_keyword)
    if collections:
        for idx, collection in enumerate(collections, start=1):
            print(f"{idx}. {collection.get('name')} (ID: {collection.get('id')})")
    else:
        print("No collections found.")

    # Search creators
    print("\n--- Searching Creators ---")
    creators = search_creators(creator_keyword)
    if creators:
        for idx, creator in enumerate(creators, start=1):
            print(f"{idx}. {creator.get('name')} (Address: {creator.get('address')})")
    else:
        print("No creators found.")
```

### Notes:
- Replace `your_api_key_here` with your actual API key for the Solscan API.
- Ensure the Solscan API is accessible and has the appropriate endpoints for `/nft/collections` and `/nft/creators`. Adjust the endpoints if necessary.
- Install the `requests` library if not already installed by running `pip install requests`.
