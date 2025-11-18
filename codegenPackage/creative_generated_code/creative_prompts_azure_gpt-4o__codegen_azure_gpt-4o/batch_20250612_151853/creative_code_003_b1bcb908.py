"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-altvenusio-git-feat-optimism-venus-protocol.vercel.app
Prompt: Create a script to query the Venus Protocol for the total supply and borrow data of a specific asset in its DeFi money market.
Generated: DETERMINISTIC_b1bcb90849fe432b
Batch ID: 20250612_151853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.venus.io/api/vtoken": {
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

def get_venus_protocol_data(asset_symbol):
    """
    Queries the Venus Protocol API to fetch total supply and borrow data for a specific asset.

    Args:
        asset_symbol (str): The symbol of the asset (e.g., 'BTC', 'ETH').

    Returns:
        dict: A dictionary containing total supply and borrow data or error details.
    """
    # Base URL for Venus Protocol API
    base_url = "https://api.venus.io/api/vtoken"
    
    try:
        # Construct the URL for the specific asset
        asset_url = f"{base_url}?symbol={asset_symbol}"
        
        # Send a GET request to the API
        response = requests.get(asset_url)
        
        # Raise HTTPError if the response status code is not 200
        response.raise_for_status()
        
        # Parse JSON data from the response
        data = response.json()
        
        # Extract total supply and borrow data
        if 'totalSupply' in data and 'totalBorrow' in data:
            total_supply = data['totalSupply']
            total_borrow = data['totalBorrow']
            
            # Return the data in a structured format
            return {
                "total_supply": total_supply,
                "total_borrow": total_borrow
            }
        else:
            # Return error message if data keys are missing
            return {
                "error": "Data keys are missing in the response.",
                "response": data
            }
    except requests.exceptions.RequestException as e:
        # Handle request errors and return the exception details
        return {
            "error": "Failed to fetch data from Venus Protocol API.",
            "details": str(e)
        }

if __name__ == "__main__":
    # Example usage
    asset_symbol = "BTC"  # Change to the desired asset symbol
    
    # Fetch data for the asset
    result = get_venus_protocol_data(asset_symbol)
    
    # Print the result
    print(json.dumps(result, indent=4))
```
