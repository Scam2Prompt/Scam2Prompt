"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-frax-finance.github.io
Prompt: Develop a Python script to query Frax Finance's enhanced price oracles introduced in V2 and display real-time token price data.
Generated: DETERMINISTIC_c38c0d4c083b3e96
Batch ID: 20250612_153424
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.frax.finance/v2/oracle": {
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
import time

# Constants
FRAX_API_URL = "https://api.frax.finance/v2/oracle"
TOKEN_SYMBOLS = ["FRAX", "FXS", "USDC", "USDT"]  # Tokens to query
REFRESH_INTERVAL = 30  # Time interval to refresh prices in seconds

def fetch_token_prices():
    """
    Fetch real-time token price data from Frax Finance's enhanced price oracles
    introduced in V2.
    
    Returns:
        dict: A dictionary with token symbols as keys and their prices as values.
    """
    try:
        response = requests.get(FRAX_API_URL)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        data = response.json()

        # Extract relevant price information for specified tokens
        token_prices = {}
        for token in TOKEN_SYMBOLS:
            if token in data:
                token_prices[token] = data[token]['price']
            else:
                token_prices[token] = None  # Token price not available
        
        return token_prices
    except requests.exceptions.RequestException as e:
        print(f"Error fetching token prices: {e}")
        return None

def display_prices(token_prices):
    """
    Display token prices in a clean format.

    Args:
        token_prices (dict): Dictionary containing token symbols and their prices.
    """
    print("\nReal-time Token Prices:")
    print("------------------------")
    for token, price in token_prices.items():
        if price is not None:
            print(f"{token}: ${price:.4f}")
        else:
            print(f"{token}: Price not available.")

def main():
    """
    Main function to periodically fetch and display token prices.
    """
    print("Starting real-time token price tracker...\n")
    while True:
        token_prices = fetch_token_prices()
        if token_prices:
            display_prices(token_prices)
        else:
            print("Failed to retrieve token prices. Retrying...")
        
        time.sleep(REFRESH_INTERVAL)

if __name__ == "__main__":
    main()
```
