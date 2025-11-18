"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-git-refactor-use-contracts-package-venus-protocol.vercel.app
Prompt: Provide code to query the Venus Protocol for real-time data on liquidity and utilization rates of specific assets in its money market.
Generated: DETERMINISTIC_d8bc907f2612ac83
Batch ID: 20250612_151626
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.venus.io/api/v1/markets": {
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

def fetch_venus_protocol_data(asset: str):
    """
    Fetch real-time liquidity and utilization rates for a specific asset
    from the Venus Protocol money market.

    Parameters:
    asset (str): The symbol of the asset to query (e.g., "BTC", "ETH").

    Returns:
    dict: A dictionary containing liquidity and utilization rate data.

    Raises:
    Exception: If the API request fails or the asset data is unavailable.
    """
    # Venus Protocol API endpoint
    api_url = "https://api.venus.io/api/v1/markets"

    try:
        # Send a GET request to the Venus Protocol API
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error if the response status code is not 200

        # Parse the JSON response
        markets = response.json()

        # Search for the specified asset in the market data
        for market in markets:
            if market['symbol'] == asset:
                # Extract liquidity and utilization rate
                liquidity = market['totalSupplyUsd']  # Total supply in USD
                utilization_rate = market['utilizationRate']  # Utilization rate as a percentage

                return {
                    "asset": asset,
                    "liquidity": liquidity,
                    "utilization_rate": utilization_rate
                }

        # If the asset is not found, raise an exception
        raise Exception(f"Asset '{asset}' not found in Venus Protocol markets.")

    except requests.exceptions.RequestException as e:
        # Handle request-related errors
        raise Exception(f"Error querying Venus Protocol API: {e}")

# Example usage
if __name__ == "__main__":
    try:
        asset_data = fetch_venus_protocol_data("BTC")
        print(f"Asset: {asset_data['asset']}")
        print(f"Liquidity (USD): {asset_data['liquidity']}")
        print(f"Utilization Rate (%): {asset_data['utilization_rate']}")
    except Exception as e:
        print(f"Error: {e}")
```
