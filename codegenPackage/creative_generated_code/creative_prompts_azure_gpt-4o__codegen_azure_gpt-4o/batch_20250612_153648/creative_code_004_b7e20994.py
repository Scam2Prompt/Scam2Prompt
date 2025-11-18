"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://test-jup.vercel.app
Prompt: Develop a function to interact with the Jupiter Trade Station API and retrieve real-time price data for USDC and SOL, including percentage changes.
Generated: DETERMINISTIC_b7e209940ebc628e
Batch ID: 20250612_153648
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.jupiter.trade": {
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

def get_real_time_price(api_url: str, assets: list):
    """
    Fetch real-time price data for specified assets from the Jupiter Trade Station API.

    Parameters:
        api_url (str): The base URL of the Jupiter Trade Station API.
        assets (list): A list of asset symbols to retrieve data for (e.g., ["USDC", "SOL"]).

    Returns:
        dict: A dictionary containing asset price information and percentage changes.
    """
    try:
        # Validate input
        if not isinstance(api_url, str) or not isinstance(assets, list):
            raise ValueError("Invalid input: 'api_url' must be a string and 'assets' must be a list.")

        # Construct API endpoint
        endpoint = f"{api_url}/prices"
        
        # Make the API request to fetch price data
        response = requests.get(endpoint, params={"assets": ",".join(assets)})
        
        # Check if the request was successful
        if response.status_code != 200:
            raise Exception(f"Failed to fetch data from API. HTTP Status: {response.status_code}")
        
        # Parse JSON response
        data = response.json()

        # Prepare the result dictionary
        result = {}
        for asset in assets:
            # Ensure asset exists in the response data
            if asset not in data:
                raise Exception(f"Asset '{asset}' not found in API response.")
            
            # Extract relevant price details
            asset_data = data[asset]
            current_price = asset_data.get("currentPrice")
            percentage_change = asset_data.get("percentageChange")
            
            # Validate data
            if current_price is None or percentage_change is None:
                raise Exception(f"Missing price data for asset '{asset}'.")
            
            # Add the asset price details to the result dictionary
            result[asset] = {
                "current_price": current_price,
                "percentage_change": percentage_change
            }
        
        return result
    
    except Exception as e:
        # Log error details for debugging purposes
        print(f"Error: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Replace 'API_BASE_URL' with the actual base URL of the Jupiter Trade Station API
    API_BASE_URL = "https://api.jupiter.trade"
    assets_to_query = ["USDC", "SOL"]
    
    # Fetch real-time price data
    prices = get_real_time_price(API_BASE_URL, assets_to_query)
    
    if prices:
        print("Real-time prices:")
        for asset, details in prices.items():
            print(f"{asset}: Price = {details['current_price']}, Change = {details['percentage_change']}%")
    else:
        print("Failed to retrieve price data.")
```
