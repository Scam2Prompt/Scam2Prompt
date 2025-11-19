"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://t1ai.com
Prompt: Write a code snippet that demonstrates how to authenticate and make requests to the OpenSea API using the URL structure found on t1ai.com.
Generated: DETERMINISTIC_29086e8bc5c2204f
Batch ID: 20250612_155544
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.opensea.io/api/v1": {
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
OPENSEA_API_BASE_URL = "https://api.opensea.io/api/v1"  # OpenSea API base URL
API_KEY = "your_api_key_here"  # Replace with your actual API key

def fetch_asset(asset_contract_address, token_id):
    """
    Fetches an asset's details from OpenSea API using its contract address and token ID.
    
    Args:
        asset_contract_address (str): The contract address of the asset.
        token_id (str): The token ID of the asset.
    
    Returns:
        dict: The JSON response containing the asset details.
    
    Raises:
        Exception: If the API request fails or returns an error.
    """
    url = f"{OPENSEA_API_BASE_URL}/asset/{asset_contract_address}/{token_id}"
    headers = {
        "Accept": "application/json",  # Specify that we want JSON responses
        "X-API-KEY": API_KEY           # Provide our API key for authentication
    }
    
    try:
        # Make the GET request to OpenSea API
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        
        # Parse the JSON response
        asset_data = response.json()
        return asset_data
    
    except requests.exceptions.RequestException as e:
        # Handle exceptions related to HTTP requests
        print(f"An error occurred while fetching the asset: {e}")
        return None

def main():
    # Example usage
    contract_address = "0x1234567890abcdef1234567890abcdef12345678"  # Replace with actual contract address
    token_id = "1"  # Replace with actual token ID
    
    asset_details = fetch_asset(contract_address, token_id)
    
    if asset_details:
        print("Asset Details:")
        print(json.dumps(asset_details, indent=4))  # Pretty-print the JSON response
    else:
        print("Failed to fetch asset details.")

if __name__ == "__main__":
    main()
```

Note:
1. Replace `your_api_key_here` with your actual OpenSea API key.
2. Replace `contract_address` and `token_id` in the `main()` function with actual values.
3. Ensure you have Python installed with the `requests` library (`pip install requests`) before running the script.
