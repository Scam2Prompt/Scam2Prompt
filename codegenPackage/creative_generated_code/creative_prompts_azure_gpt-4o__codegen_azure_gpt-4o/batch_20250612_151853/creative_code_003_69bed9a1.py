"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-altvenusio-git-feat-optimism-subgraph-venus-protocol.vercel.app
Prompt: Provide an example of how to use the Venus Protocol's API to calculate borrowing limits based on collateralized assets.
Generated: DETERMINISTIC_69bed9a123eeffb0
Batch ID: 20250612_151853
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.venus.io/api/v1": {
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
API_BASE_URL = "https://api.venus.io/api/v1"
COLLATERAL_FACTOR_DECIMALS = 18  # Venus Protocol uses 18 decimals for calculations

def fetch_markets():
    """
    Fetches all available markets from the Venus Protocol API.

    Returns:
        list: List of markets with their details.
    """
    try:
        response = requests.get(f"{API_BASE_URL}/markets")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching markets: {e}")
        return []


def calculate_borrow_limit(collateral_assets, markets_data):
    """
    Calculates the borrowing limit based on provided collateralized assets.

    Args:
        collateral_assets (list): List of dictionaries containing asset symbol and amount.
                                  Example: [{"symbol": "vBTC", "amount": 0.1}, {"symbol": "vETH", "amount": 2}]
        markets_data (list): List of market data fetched from Venus Protocol API.

    Returns:
        float: The calculated borrow limit in USD.
    """
    borrow_limit = 0.0

    for asset in collateral_assets:
        symbol = asset["symbol"]
        amount = asset["amount"]

        # Find the market data for the given asset symbol
        market = next((m for m in markets_data if m["symbol"] == symbol), None)
        if not market:
            print(f"Market data for {symbol} not found. Skipping...")
            continue

        # Extract required data from market details
        collateral_factor = float(market["collateralFactor"]) / (10 ** COLLATERAL_FACTOR_DECIMALS)
        price_in_usd = float(market["priceUSD"])

        # Calculate contribution to the borrow limit
        asset_borrow_limit = amount * price_in_usd * collateral_factor
        borrow_limit += asset_borrow_limit

    return borrow_limit


if __name__ == "__main__":
    # Example collateralized assets
    collateral_assets = [
        {"symbol": "vBTC", "amount": 0.1},  # 0.1 vBTC
        {"symbol": "vETH", "amount": 2}    # 2 vETH
    ]

    # Fetch markets data from Venus Protocol API
    markets_data = fetch_markets()
    if not markets_data:
        print("Failed to fetch markets data. Exiting...")
        exit(1)

    # Calculate borrow limit
    borrow_limit = calculate_borrow_limit(collateral_assets, markets_data)
    print(f"Borrow Limit: ${borrow_limit:.2f} USD")
```

This code is designed to be production-ready, includes error handling, comments, and adheres to best practices.
