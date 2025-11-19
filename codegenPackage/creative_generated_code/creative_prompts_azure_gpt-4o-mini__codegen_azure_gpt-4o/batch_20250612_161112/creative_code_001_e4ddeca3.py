"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://discoverwrap.pages.dev
Prompt: Write a Python script that retrieves and displays the floor prices of popular NFTs like Bored Ape Yacht Club and Pudgy Penguins from the SearchDapps API.
Generated: DETERMINISTIC_e4ddeca388e562eb
Batch ID: 20250612_161112
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.searchdapps.com": {
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

def get_nft_floor_price(api_url: str, collection_name: str) -> float:
    """
    Retrieves the floor price for the specified NFT collection using the SearchDapps API.
    
    Args:
        api_url (str): Base URL for the SearchDapps API.
        collection_name (str): Name of the NFT collection to fetch the floor price.

    Returns:
        float: The floor price of the NFT collection, or None if not found.
    """
    try:
        # Make the API request to fetch NFT data
        response = requests.get(f"{api_url}/collections/{collection_name}")
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Parse response JSON
        data = response.json()
        
        # Extract and return the floor price
        floor_price = data.get('floor_price')
        if floor_price is None:
            print(f"Warning: Floor price not found for collection '{collection_name}'.")
            return None
        return floor_price
    
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error: Failed to fetch data for '{collection_name}'. Details: {e}")
    except ValueError:
        # Handle JSON parsing errors
        print("Error: Unable to parse the response JSON.")
    return None


def main():
    """
    Main function to retrieve and display floor prices for popular NFT collections.
    """
    # Base API URL for SearchDapps
    API_URL = "https://api.searchdapps.com"
    
    # List of popular NFT collections
    nft_collections = [
        "bored-ape-yacht-club",
        "pudgy-penguins"
    ]
    
    # Fetch and display floor prices for each collection
    for collection in nft_collections:
        print(f"Fetching floor price for '{collection}'...")
        floor_price = get_nft_floor_price(API_URL, collection)
        if floor_price is not None:
            print(f"The floor price for '{collection}' is: {floor_price} ETH")
        else:
            print(f"Unable to retrieve floor price for '{collection}'.")

if __name__ == "__main__":
    main()
```
