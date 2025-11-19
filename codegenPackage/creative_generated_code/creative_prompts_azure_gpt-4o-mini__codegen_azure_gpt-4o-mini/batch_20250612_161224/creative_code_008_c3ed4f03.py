"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstone-finance.pages.dev
Prompt: Write a tutorial on integrating RedStone's zero-latency oracle for a perpetual trading platform.
Generated: DETERMINISTIC_c3ed4f032e6b206e
Batch ID: 20250612_161224
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.redstone.finance/oracle/v1": {
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
import time

class RedstoneOracle:
    """
    A class to interact with RedStone's zero-latency oracle for fetching asset prices.
    """

    BASE_URL = "https://api.redstone.finance/oracle/v1"
    
    def __init__(self, asset_symbol):
        """
        Initializes the RedstoneOracle class with the given asset symbol.

        Args:
            asset_symbol (str): The symbol of the asset to fetch prices for (e.g., 'BTC', 'ETH').
        """
        self.asset_symbol = asset_symbol

    def fetch_price(self):
        """
        Fetches the latest price of the specified asset from RedStone's oracle.

        Returns:
            float: The latest price of the asset.

        Raises:
            Exception: If the API request fails or returns an invalid response.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/price/{self.asset_symbol}")
            response.raise_for_status()  # Raise an error for bad responses
            data = response.json()

            # Check if the response contains the expected data
            if 'price' not in data:
                raise ValueError("Invalid response structure: 'price' key not found.")

            return data['price']
        
        except requests.RequestException as req_err:
            # Handle request errors (e.g., connection errors)
            print(f"Request error: {req_err}")
            raise
        except ValueError as val_err:
            # Handle data parsing errors
            print(f"Data error: {val_err}")
            raise
        except Exception as e:
            # Handle any other exceptions
            print(f"Unexpected error: {e}")
            raise

def main():
    """
    Main function to demonstrate the usage of the RedstoneOracle class.
    It continuously fetches and prints the price of the specified asset.
    """
    asset_symbol = "BTC"  # Example asset; change as needed
    oracle = RedstoneOracle(asset_symbol)

    print(f"Fetching price for {asset_symbol}...")

    try:
        while True:
            price = oracle.fetch_price()
            print(f"The current price of {asset_symbol} is: ${price:.2f}")
            time.sleep(30)  # Wait for 30 seconds before the next fetch

    except KeyboardInterrupt:
        print("Price fetching interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```

This code provides a clean integration with RedStone's zero-latency oracle by fetching asset prices while handling potential errors. To use this code, simply run it in an environment where the `requests` library is available. Adjust the `asset_symbol` in the `main` function for different assets.
