"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://daddytate-reward.pages.dev
Prompt: Write a Python script that interacts with the DexScreener API to track the price of $DADDY.
Generated: DETERMINISTIC_5286dd91f447b714
Batch ID: 20250612_155752
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.dexscreener.com/latest/dex/tokens/": {
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

# Define constants for the DexScreener API and the token to track
DEXSCREENER_API_URL = 'https://api.dexscreener.com/latest/dex/tokens/'
TOKEN_ADDRESS = '0xYourTokenAddressHere'  # Replace with the actual token address for $DADDY

def fetch_price(token_address):
    """
    Fetch the current price of the given token from the DexScreener API.

    Args:
        token_address (str): The address of the token to check.

    Returns:
        float: The current price of the token in USD.

    Raises:
        ValueError: If the API response does not contain price data.
        requests.RequestException: If the API call fails.
    """
    response = requests.get(f"{DEXSCREENER_API_URL}{token_address}")

    # Raise an exception for HTTP errors
    response.raise_for_status()

    # Parse the JSON response
    data = response.json()

    # Check if the price data is available
    if 'pairs' in data and len(data['pairs']) > 0:
        price = data['pairs'][0]['priceUsd']
        return float(price)

    raise ValueError("Price data not available in the response")

def main():
    """
    Main function to track the price of the $DADDY token continuously.
    """
    while True:
        try:
            price = fetch_price(TOKEN_ADDRESS)
            print(f"The current price of $DADDY is: ${price:.2f}")
        except ValueError as ve:
            print(f"ValueError: {ve}")
        except requests.RequestException as req_err:
            print(f"RequestException: {req_err}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        # Wait for a specified duration before checking the price again
        time.sleep(60)  # Check price every 60 seconds

if __name__ == "__main__":
    main()
```

Make sure to replace `0xYourTokenAddressHere` with the actual token address for `$DADDY` before running the script.
