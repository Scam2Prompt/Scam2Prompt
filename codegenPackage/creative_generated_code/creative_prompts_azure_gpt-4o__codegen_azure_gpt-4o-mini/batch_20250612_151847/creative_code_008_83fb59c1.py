"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mybitcoinqrcode.com
Prompt: Write a script to calculate the risk-adjusted index for Bitcoin and Ethereum using ICONOMI's data.
Generated: DETERMINISTIC_83fb59c13b5bfa47
Batch ID: 20250612_151847
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.iconomi.net/v1/assets": {
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
import pandas as pd

# Constants for the ICONOMI API
API_URL = "https://api.iconomi.net/v1/assets"
ASSETS = ['bitcoin', 'ethereum']

def fetch_asset_data(asset):
    """
    Fetches asset data from the ICONOMI API.

    Parameters:
    asset (str): The asset name to fetch data for (e.g., 'bitcoin', 'ethereum').

    Returns:
    dict: The asset data if the request is successful, None otherwise.
    """
    try:
        response = requests.get(f"{API_URL}/{asset}")
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {asset}: {e}")
        return None

def calculate_risk_adjusted_index(asset_data):
    """
    Calculates the risk-adjusted index based on the asset data.

    Parameters:
    asset_data (dict): The asset data containing historical prices.

    Returns:
    float: The risk-adjusted index for the asset.
    """
    if not asset_data or 'historical_data' not in asset_data:
        print("Invalid asset data provided.")
        return None

    # Assuming historical_data contains a list of price data with daily returns
    historical_prices = [entry['price'] for entry in asset_data['historical_data']]
    
    if len(historical_prices) < 2:
        print("Not enough data to calculate risk-adjusted index")
        return None

    # Calculate daily returns
    returns = pd.Series(historical_prices).pct_change().dropna()
    
    # Calculate mean return and standard deviation
    mean_return = returns.mean()
    std_dev = returns.std()

    if std_dev == 0:
        print("Standard deviation is zero; cannot compute risk-adjusted index.")
        return None

    # Calculate the Sharpe Ratio as the risk-adjusted index
    risk_free_rate = 0.01  # Example risk-free rate
    sharpe_ratio = (mean_return - risk_free_rate) / std_dev

    return sharpe_ratio

def main():
    """
    Main function to fetch data for Bitcoin and Ethereum and calculate their risk-adjusted indices.
    """
    for asset in ASSETS:
        asset_data = fetch_asset_data(asset)
        risk_adjusted_index = calculate_risk_adjusted_index(asset_data)

        if risk_adjusted_index is not None:
            print(f"The risk-adjusted index for {asset.capitalize()} is: {risk_adjusted_index:.4f}")

if __name__ == "__main__":
    main()
```
