"""
Generated Code Metadata:
========================
Original URL: https://mixer-novostei.ru
Prompt: Generate a code example that demonstrates how to track the performance of investments on Ribbon Finance using their token RBN.
Generated: DETERMINISTIC_0807c61108f0564b
Batch ID: 20250612_161317
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```python
import requests
import time
from datetime import datetime

# Constants
RBN_TOKEN_ADDRESS = "0x6123b0049f904d730db3c36a31167d9d4121fa6b"  # Ribbon Finance Token (RBN) address
COINGECKO_API_URL = "https://api.coingecko.com/api/v3"
UPDATE_INTERVAL = 60  # Time interval (in seconds) to fetch data

def fetch_rbn_price():
    """
    Fetch the current price of RBN token in USD from CoinGecko API.
    Returns:
        float: Current price of RBN in USD.
    """
    try:
        response = requests.get(f"{COINGECKO_API_URL}/simple/token_price/ethereum", params={
            "contract_addresses": RBN_TOKEN_ADDRESS,
            "vs_currencies": "usd"
        })
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        return data[RBN_TOKEN_ADDRESS]["usd"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching RBN price: {e}")
        return None
    except KeyError:
        print("Unexpected response format from CoinGecko API.")
        return None

def track_investment_performance(initial_investment, initial_price):
    """
    Track the performance of an investment in RBN token.
    Args:
        initial_investment (float): Initial amount invested in USD.
        initial_price (float): Initial price of RBN token in USD.
    """
    try:
        # Calculate the initial number of tokens purchased
        initial_tokens = initial_investment / initial_price
        print(f"Initial Investment: ${initial_investment:.2f}")
        print(f"Initial RBN Price: ${initial_price:.2f}")
        print(f"Initial Tokens Purchased: {initial_tokens:.6f}\n")

        while True:
            current_price = fetch_rbn_price()
            if current_price is not None:
                # Calculate the current value of the investment
                current_value = initial_tokens * current_price
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Current RBN Price: ${current_price:.2f}")
                print(f"Current Investment Value: ${current_value:.2f}\n")
            else:
                print("Unable to fetch current price. Retrying...\n")
            
            time.sleep(UPDATE_INTERVAL)  # Wait for the next update
    except KeyboardInterrupt:
        print("Tracking stopped by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    try:
        # Fetch the initial price of RBN token
        initial_price = fetch_rbn_price()
        if initial_price is None:
            print("Failed to fetch initial RBN price. Exiting...")
        else:
            # Start tracking investment performance
            initial_investment = 1000.0  # Example: $1000 initial investment
            track_investment_performance(initial_investment, initial_price)
    except Exception as e:
        print(f"An error occurred during initialization: {e}")
```
