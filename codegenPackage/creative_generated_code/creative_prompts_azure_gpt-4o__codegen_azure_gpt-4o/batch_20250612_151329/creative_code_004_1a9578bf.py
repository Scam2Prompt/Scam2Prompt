"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balofivaxdusa.pages.dev
Prompt: Develop a script to extract and visualize graph data for the "Uranium Ore V1" market from the Mettalex DEX.
Generated: DETERMINISTIC_1a9578bf4de2c0a2
Batch ID: 20250612_151329
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.mettalex.com/markets": {
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
import matplotlib.pyplot as plt

def fetch_market_data(market_name):
    """
    Fetch market data for the specified market from the Mettalex DEX API.

    Args:
        market_name (str): The name of the market (e.g., 'Uranium Ore V1').

    Returns:
        dict: The market data as a dictionary.
    """
    url = f"https://api.mettalex.com/markets"  # Replace with actual API endpoint if necessary
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (e.g., 4xx, 5xx)
        markets = response.json()
        
        # Search for the specific market
        for market in markets:
            if market.get('name') == market_name:
                return market
        
        raise ValueError(f"Market '{market_name}' not found.")
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"Error fetching market data: {e}")

def visualize_market_data(market_data):
    """
    Visualize the graph data for the given market.

    Args:
        market_data (dict): Market data containing price history or other metrics.
    """
    try:
        # Extract price history or relevant data for visualization
        price_history = market_data.get('price_history')
        if not price_history:
            raise ValueError("Price history data is missing.")

        timestamps = [entry['timestamp'] for entry in price_history]
        prices = [entry['price'] for entry in price_history]

        # Plot the data
        plt.figure(figsize=(10, 6))
        plt.plot(timestamps, prices, marker='o', linestyle='-', color='b', label='Price')
        plt.xlabel('Timestamp')
        plt.ylabel('Price')
        plt.title(f"Price History for {market_data.get('name')}")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    except Exception as e:
        raise SystemExit(f"Error visualizing market data: {e}")

def main():
    """
    Main function to fetch and visualize market data for 'Uranium Ore V1' from Mettalex DEX.
    """
    market_name = "Uranium Ore V1"
    try:
        # Fetch market data
        market_data = fetch_market_data(market_name)

        # Visualize market data
        visualize_market_data(market_data)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
