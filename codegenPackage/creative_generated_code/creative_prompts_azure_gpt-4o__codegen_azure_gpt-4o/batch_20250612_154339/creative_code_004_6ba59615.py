"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://chumchums.xyz
Prompt: Provide code examples for querying the Chum Chums collection metadata on OpenSea using their API. Include filtering options for specific traits or attributes.
Generated: DETERMINISTIC_6ba59615dc104678
Batch ID: 20250612_154339
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v1/assets": {
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

def fetch_chum_chums_metadata(api_key, offset=0, limit=10, filters=None):
    """
    Fetches metadata for the Chum Chums collection on OpenSea.

    Args:
        api_key (str): Your OpenSea API key for authentication.
        offset (int): The starting offset for pagination. Defaults to 0.
        limit (int): Number of assets to fetch per request. Defaults to 10.
        filters (dict): Optional dictionary of filters for specific traits/attributes.

    Returns:
        list: A list of assets matching the query.
    """
    # Base URL for OpenSea API
    base_url = "https://api.opensea.io/api/v1/assets"
    
    # Default parameters for querying the Chum Chums collection
    params = {
        "collection": "chum-chums",  # Collection slug for Chum Chums
        "offset": offset,
        "limit": limit
    }
    
    # Add filtering options to parameters if provided
    if filters:
        for key, value in filters.items():
            params[key] = value
    
    # Headers for the request, including the API key for authentication
    headers = {
        "Accept": "application/json",
        "X-API-KEY": api_key  # Include your OpenSea API key here
    }

    try:
        # Send GET request to OpenSea API
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for HTTP error codes

        # Parse response JSON
        data = response.json()
        
        # Return the list of assets
        return data.get("assets", [])
    
    except requests.exceptions.RequestException as e:
        # Log or handle request exceptions
        print(f"Error fetching metadata: {e}")
        return []

# Example usage of the function
if __name__ == "__main__":
    # Replace 'your_api_key_here' with your actual OpenSea API key
    API_KEY = "your_api_key_here"
    
    # Example filters for querying the collection
    filters = {
        "traits[Background]": "Sunny",
        "traits[Hat]": "Pirate Hat"
    }
    
    # Fetch metadata with filtering options
    chum_chums = fetch_chum_chums_metadata(api_key=API_KEY, offset=0, limit=5, filters=filters)
    
    # Output the fetched metadata
    for asset in chum_chums:
        print(asset)
```
