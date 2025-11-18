"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swapspace.vip
Prompt: Generate a script that integrates SwapSpace’s API to track Anyswap (ANY) token price changes and display a real-time price chart.
Generated: DETERMINISTIC_70ac2bedd3dbc408
Batch ID: 20250612_145913
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.swapspace.co/v1/tokens": {
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
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants for the API and the ANY token
API_URL = "https://api.swapspace.co/v1/tokens"
ANY_TOKEN_ID = "anyswap"  # The ID for the Anyswap token
PRICE_HISTORY = []  # List to store price history for plotting

def fetch_any_token_price():
    """Fetch the current price of the Anyswap (ANY) token from SwapSpace's API."""
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raise an error for bad responses
        tokens = response.json()
        
        # Find the ANY token in the response
        for token in tokens:
            if token['id'] == ANY_TOKEN_ID:
                return token['price']

        raise ValueError("ANY token not found in the response.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None
    except ValueError as ve:
        print(ve)
        return None

def update_price_history(frame):
    """Update the price history for the ANY token and plot it."""
    price = fetch_any_token_price()
    if price is not None:
        PRICE_HISTORY.append(price)
        if len(PRICE_HISTORY) > 20:  # Limit to the last 20 prices for better visualization
            PRICE_HISTORY.pop(0)
        
        # Clear the current plot and display the updated prices
        plt.clf()
        plt.plot(PRICE_HISTORY, label='ANY Token Price', color='blue')
        plt.title('Anyswap (ANY) Token Real-Time Price Chart')
        plt.xlabel('Time (updates)')
        plt.ylabel('Price (USD)')
        plt.legend()
        plt.grid()
    else:
        print("Could not update price history.")

def main():
    """Main function to set up the real-time price chart."""
    plt.figure(figsize=(10, 5))
    ani = animation.FuncAnimation(plt.gcf(), update_price_history, interval=10000)  # Update every 10 seconds
    plt.show()

if __name__ == "__main__":
    main()
```
