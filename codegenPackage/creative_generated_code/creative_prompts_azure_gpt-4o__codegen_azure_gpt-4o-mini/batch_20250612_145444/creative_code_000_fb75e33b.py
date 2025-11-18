"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://compound.morpho.dev
Prompt: Write a script using the CompoundV2 API to query the current supply and borrow volumes for a specific asset and display the APY rates for both P2P and CompoundV2 markets.
Generated: DETERMINISTIC_fb75e33bbccafcbf
Batch ID: 20250612_145444
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.compound.finance/api/v2": {
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

# Constants for API endpoints
COMPOUND_API_BASE_URL = "https://api.compound.finance/api/v2"

def get_asset_data(asset_symbol: str):
    """
    Gets the current supply and borrow volumes for a specific asset 
    and the APY rates for both P2P and CompoundV2 markets.

    :param asset_symbol: The symbol of the asset to query (e.g., 'DAI').
    :return: A dictionary containing supply and borrow volumes and APY rates.
    """
    try:
        # Retrieve the market data for all assets
        markets_response = requests.get(f"{COMPOUND_API_BASE_URL}/markets")
        markets_response.raise_for_status()  # Raise an error for bad responses

        # Parse the JSON response
        markets_data = markets_response.json()['markets']

        # Find the specific market data for the requested asset
        for market in markets_data:
            if market['symbol'] == asset_symbol:
                return {
                    'supply_balance': market['supply_balance'],
                    'borrow_balance': market['borrow_balance'],
                    'supply_apy': market['supply_apy'],
                    'borrow_apy': market['borrow_apy']
                }

        # If the asset is not found, raise an error
        raise ValueError(f"Asset '{asset_symbol}' not found in markets.")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching market data: {e}")
        return None
    except ValueError as ve:
        print(ve)
        return None

def display_asset_data(asset_data):
    """
    Displays the asset data in a readable format.

    :param asset_data: A dictionary containing supply and borrow data and APY rates.
    """
    if asset_data:
        print(f"Supply Balance: {asset_data['supply_balance']}")
        print(f"Borrow Balance: {asset_data['borrow_balance']}")
        print(f"Supply APY: {asset_data['supply_apy']:.2%}")
        print(f"Borrow APY: {asset_data['borrow_apy']:.2%}")
    else:
        print("No data to display.")

if __name__ == "__main__":
    # Example asset to query
    ASSET_SYMBOL = 'DAI'

    # Fetch and display data for the specified asset
    asset_data = get_asset_data(ASSET_SYMBOL)
    display_asset_data(asset_data)
```
