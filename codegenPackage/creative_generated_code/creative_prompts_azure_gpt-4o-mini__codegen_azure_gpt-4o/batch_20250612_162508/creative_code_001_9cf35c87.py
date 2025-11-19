"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-mof.web.app
Prompt: How can I retrieve the 24-hour volume and floor prices of NFT collections like Mad Lads and Transdimensional Fox Federation from the NFT-MOF API?
Generated: DETERMINISTIC_9cf35c879e14155f
Batch ID: 20250612_162508
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.nft-mof.com": {
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

def fetch_nft_data(api_url, collection_names):
    """
    Fetch the 24-hour volume and floor prices of NFT collections from the NFT-MOF API.

    Parameters:
        api_url (str): The base URL of the NFT-MOF API.
        collection_names (list): A list of NFT collection names to query.

    Returns:
        dict: A dictionary containing the collection names as keys and their respective
              24-hour volume and floor prices as values.
    """
    nft_data = {}

    for collection in collection_names:
        try:
            # Construct the API endpoint URL for the collection
            endpoint = f"{api_url}/collections/{collection}/stats"
            
            # Send a GET request to the API
            response = requests.get(endpoint)
            
            # Raise an exception for HTTP errors (e.g., 404, 500)
            response.raise_for_status()
            
            # Parse the JSON response
            data = response.json()
            
            # Extract the 24-hour volume and floor price
            volume_24h = data.get("volume_24h", None)
            floor_price = data.get("floor_price", None)
            
            # Ensure both values are available; otherwise, skip the collection
            if volume_24h is not None and floor_price is not None:
                nft_data[collection] = {
                    "volume_24h": volume_24h,
                    "floor_price": floor_price
                }
            else:
                print(f"Warning: Missing data for collection '{collection}'. Skipping.")
        
        except requests.exceptions.RequestException as e:
            # Handle any errors that occur during the request
            print(f"Error: Failed to fetch data for collection '{collection}'. Details: {e}")
    
    return nft_data


# Sample usage
if __name__ == "__main__":
    # Base URL of the NFT-MOF API
    api_base_url = "https://api.nft-mof.com"
    
    # List of NFT collections to query
    collections = ["MadLads", "TransdimensionalFoxFederation"]
    
    # Fetch the NFT data
    results = fetch_nft_data(api_base_url, collections)
    
    # Print the results
    if results:
        print("Fetched NFT data:")
        for collection, stats in results.items():
            print(f"Collection: {collection}")
            print(f"  24-hour Volume: {stats['volume_24h']}")
            print(f"  Floor Price: {stats['floor_price']}")
    else:
        print("No data fetched.")
```
