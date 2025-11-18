"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rand-samp-934.pages.dev
Prompt: Write a Python script to retrieve live charts for SHIB, LEASH, and BONE tokens using data from CoinGecko or Etherscan.
Generated: DETERMINISTIC_a2d2dabc61bf3a54
Batch ID: 20250612_151219
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

# Creative Generated Code:
# ========================

```python
import requests
import matplotlib.pyplot as plt
import datetime
import time

# Constants for the CoinGecko API
COINGECKO_API_URL = "https://api.coingecko.com/api/v3"
TOKENS = {
    "SHIB": {"id": "shiba-inu"},
    "LEASH": {"id": "leash"},
    "BONE": {"id": "bone-shiba-swap"}
}

def fetch_token_price(token_id):
    """
    Fetch the current price of a token from the CoinGecko API.
    
    :param token_id: The CoinGecko ID of the token
    :return: Current price of the token or None if the request fails
    """
    try:
        response = requests.get(f"{COINGECKO_API_URL}/simple/price?ids={token_id}&vs_currencies=usd")
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()
        return data[token_id]["usd"]
    except (requests.RequestException, KeyError) as e:
        print(f"Error fetching price for {token_id}: {e}")
        return None

def plot_live_prices():
    """
    Continuously fetch and plot the live prices for SHIB, LEASH, and BONE tokens.
    """
    plt.ion()  # Enable interactive mode
    fig, ax = plt.subplots()
    ax.set_title("Live Token Prices")
    ax.set_xlabel("Time")
    ax.set_ylabel("Price in USD")
    
    timestamps = []
    prices = {token: [] for token in TOKENS.keys()}

    try:
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            timestamps.append(current_time)

            for token, info in TOKENS.items():
                price = fetch_token_price(info["id"])
                if price is not None:
                    prices[token].append(price)
                    print(f"Current {token} price: ${price}")

            # Clear and re-plot the data
            ax.clear()
            for token, price_list in prices.items():
                ax.plot(timestamps, price_list, label=token)

            ax.set_title("Live Token Prices")
            ax.set_xlabel("Time")
            ax.set_ylabel("Price in USD")
            ax.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()

            plt.pause(60)  # Pause for 60 seconds before the next fetch
    except KeyboardInterrupt:
        print("Live plotting stopped by user.")
    finally:
        plt.ioff()  # Disable interactive mode
        plt.show()  # Show the final plot

if __name__ == "__main__":
    plot_live_prices()
```

This code retrieves live price data for SHIB, LEASH, and BONE tokens using the CoinGecko API and plots it in real-time using Matplotlib. It handles potential errors during the API request and provides a clean user interface.
