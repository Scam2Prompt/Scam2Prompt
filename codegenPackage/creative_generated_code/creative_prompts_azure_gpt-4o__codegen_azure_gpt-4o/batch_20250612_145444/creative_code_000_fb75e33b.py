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
  "https://api.compound.finance/api/v2/ctoken": {
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

# Constants (Replace with actual API endpoint and key if required)
COMPOUND_API_URL = "https://api.compound.finance/api/v2/ctoken"
ASSET_SYMBOL = "USDC"  # Replace with the asset symbol you want to query (e.g., USDC, DAI, ETH)

def fetch_compound_data(asset_symbol):
    """
    Fetch data from Compound V2 API for a specific asset.

    :param asset_symbol: The symbol of the asset (e.g., USDC, DAI, ETH)
    :return: A dictionary containing supply and borrow volumes and APY rates, or None in case of failure
    """
    try:
        # API request to fetch data
        response = requests.get(COMPOUND_API_URL)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

        data = response.json()
        
        # Find the specific asset data
        for ctoken in data.get("cToken", []):
            if ctoken.get("underlying_symbol") == asset_symbol.upper():
                return {
                    "asset": asset_symbol.upper(),
                    "supply_volume": float(ctoken["total_supply"]["value"]),
                    "borrow_volume": float(ctoken["total_borrows"]["value"]),
                    "supply_apy": float(ctoken["supply_rate"]["value"]) * 100,  # Convert to percentage
                    "borrow_apy": float(ctoken["borrow_rate"]["value"]) * 100  # Convert to percentage
                }
        
        # If asset not found in response, return None
        print(f"Asset {asset_symbol.upper()} not found in Compound V2 data.")
        return None

    except requests.RequestException as e:
        # Handle connection or HTTP errors
        print(f"Error fetching data from Compound API: {e}")
        return None
    except (KeyError, TypeError, ValueError) as e:
        # Handle unexpected response structure or data conversion errors
        print(f"Error processing data for asset {asset_symbol.upper()}: {e}")
        return None

def display_asset_data(asset_data):
    """
    Display the asset data in a user-friendly format.

    :param asset_data: Dictionary containing asset data
    """
    if not asset_data:
        print("No data available to display.")
        return

    print(f"Asset: {asset_data['asset']}")
    print(f"Supply Volume: ${asset_data['supply_volume']:.2f}")
    print(f"Borrow Volume: ${asset_data['borrow_volume']:.2f}")
    print(f"Supply APY (Compound V2): {asset_data['supply_apy']:.2f}%")
    print(f"Borrow APY (Compound V2): {asset_data['borrow_apy']:.2f}%")

if __name__ == "__main__":
    # Fetch data for the specified asset
    asset_data = fetch_compound_data(ASSET_SYMBOL)

    # Display the fetched data
    display_asset_data(asset_data)
```

This Python script uses the Compound V2 API to fetch and display the supply and borrow volumes and APY rates for a specific asset (e.g., USDC). Replace the `ASSET_SYMBOL` with the desired asset and ensure you provide the correct API endpoint for production usage.
