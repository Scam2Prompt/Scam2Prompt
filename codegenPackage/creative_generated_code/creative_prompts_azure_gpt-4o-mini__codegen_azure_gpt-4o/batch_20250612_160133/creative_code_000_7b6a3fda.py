"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clhwgw.cn
Prompt: Generate a Python script that utilizes the OKX API to fetch the latest trading prices for BTC, ETH, and USDT.
Generated: DETERMINISTIC_7b6a3fda2199bd5a
Batch ID: 20250612_160133
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://www.okx.com": {
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
OKX_API_BASE_URL = "https://www.okx.com"
TICKER_API_ENDPOINT = "/api/v5/market/ticker"
ASSETS = ["BTC-USDT", "ETH-USDT", "USDT-USDT"]  # Trading pairs to fetch prices for

def fetch_latest_prices(assets):
    """
    Fetch the latest trading prices for the specified assets from OKX.

    Args:
        assets (list): List of asset trading pairs.

    Returns:
        dict: A dictionary containing asset trading pairs as keys and their latest prices as values.
    """
    prices = {}
    for asset in assets:
        url = f"{OKX_API_BASE_URL}{TICKER_API_ENDPOINT}"
        params = {"instId": asset}  # Instrument ID for the trading pair
        try:
            # Make a GET request to the OKX API
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)
            
            # Parse the JSON response
            data = response.json()
            if "data" in data and len(data["data"]) > 0:
                # Extract the latest price for the trading pair
                prices[asset] = float(data["data"][0]["last"])
            else:
                prices[asset] = None  # No data available for the asset
        except requests.RequestException as e:
            # Log the error and set the price to None for the asset
            print(f"Error fetching data for {asset}: {e}")
            prices[asset] = None
    return prices

def main():
    """
    Main function to fetch and display the latest trading prices for BTC, ETH, and USDT.
    """
    print("Fetching latest trading prices...")
    prices = fetch_latest_prices(ASSETS)
    print("Latest Prices:")
    for asset, price in prices.items():
        if price is not None:
            print(f"{asset}: ${price:.2f}")
        else:
            print(f"{asset}: Price data unavailable")

if __name__ == "__main__":
    main()
```
