"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://v1-fixedflolat.com
Prompt: Write a tutorial on how to use FixedFloat's dual-rate system to optimize cryptocurrency trading strategies for both risk-averse and market-savvy users.
Generated: DETERMINISTIC_90a38824ea30c789
Batch ID: 20250612_154842
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.fixedfloat.com": {
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
"""
Tutorial: Using FixedFloat's Dual-Rate System to Optimize Cryptocurrency Trading Strategies
This script demonstrates how to interact with FixedFloat's API to optimize trading strategies
for both risk-averse and market-savvy users. The FixedFloat platform offers two exchange rate
types: fixed rates and floating rates. Risk-averse users prefer fixed rates (guaranteed rate),
while market-savvy users might choose floating rates for potentially better offers.

Prerequisites:
1. Install the `requests` library (`pip install requests`).
2. Obtain access to FixedFloat's API key.
"""

import requests

# Constants
API_KEY = 'your_api_key_here'  # Replace with your FixedFloat API key
BASE_URL = 'https://api.fixedfloat.com'

def get_exchange_rates(pair, api_key):
    """
    Fetches the available exchange rates (fixed and floating) for a given currency pair.

    Args:
        pair (str): Currency pair in the format 'BTC-ETH', 'ETH-USDT', etc.
        api_key (str): FixedFloat API key.

    Returns:
        dict: A dictionary containing fixed and floating rates.
    """
    url = f"{BASE_URL}/exchange/rates"
    headers = {"Authorization": f"Bearer {api_key}"}
    params = {"pair": pair}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()  # Raise an error for HTTP issues
        rates = response.json()
        return {
            "fixed_rate": rates.get("fixed_rate"),
            "floating_rate": rates.get("floating_rate")
        }
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exchange rates: {e}")
        return None

def place_order(pair, amount, rate_type, api_key):
    """
    Places an order on FixedFloat using the specified rate type.

    Args:
        pair (str): Currency pair in the format 'BTC-ETH', 'ETH-USDT', etc.
        amount (float): Amount of base currency to exchange.
        rate_type (str): Rate type ('fixed' or 'floating').
        api_key (str): FixedFloat API key.

    Returns:
        dict: A dictionary containing order details or an error message.
    """
    url = f"{BASE_URL}/exchange"
    headers = {"Authorization": f"Bearer {api_key}"}
    data = {
        "pair": pair,
        "amount": amount,
        "rate_type": rate_type
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for HTTP issues
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error placing order: {e}")
        return None

def main():
    """
    Main function demonstrating the use of FixedFloat's dual-rate system
    for optimizing cryptocurrency trading strategies.
    """
    pair = "BTC-ETH"  # Currency pair to exchange
    amount = 0.01    # Amount in BTC you want to exchange

    print("Fetching exchange rates...")
    rates = get_exchange_rates(pair, API_KEY)
    if rates:
        print(f"Fixed Rate: {rates['fixed_rate']} ETH")
        print(f"Floating Rate: {rates['floating_rate']} ETH")

        # Simulate user choice based on risk profile
        user_choice = input("Enter rate type ('fixed' or 'floating'): ").strip().lower()
        if user_choice in ["fixed", "floating"]:
            print(f"Placing {user_choice} rate order...")
            order = place_order(pair, amount, user_choice, API_KEY)
            if order:
                print("Order placed successfully!")
                print(f"Order Details: {order}")
            else:
                print("Failed to place order.")
        else:
            print("Invalid rate type selected. Please choose either 'fixed' or 'floating'.")
    else:
        print("Failed to fetch exchange rates. Please check your API key or network connection.")

if __name__ == "__main__":
    main()
```
