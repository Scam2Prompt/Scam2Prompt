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
import json

class FraxFinanceOracle:
    """
    A class to interact with the Frax Finance enhanced price oracles (V2).
    """

    BASE_URL = "https://api.frax.finance/v2/oracle"

    def __init__(self):
        """
        Initialize the FraxFinanceOracle class.
        """
        pass

    def get_token_price(self, token_symbol):
        """
        Get the real-time price of a token from the Frax Finance oracle.

        :param token_symbol: The symbol of the token (e.g., 'ETH', 'BTC').
        :return: The price of the token if successful; None otherwise.
        """
        try:
            response = requests.get(f"{self.BASE_URL}/{token_symbol}")
            response.raise_for_status()  # Raise an exception for HTTP errors
            
            # Parse the JSON response
            data = response.json()
            price = data.get("price")  # Adjust key access based on the actual API response structure
            
            if price is not None:
                return price
            else:
                print(f"Price not found for token: {token_symbol}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
        except json.JSONDecodeError:
            print("Failed to decode JSON response.")
            return None

def main():
    """
    Main function to execute the script.
    """
    oracle = FraxFinanceOracle()

    # List of tokens to query
    tokens = ['ETH', 'BTC', 'USDT']

    for token in tokens:
        price = oracle.get_token_price(token)
        if price is not None:
            print(f"The current price of {token} is: ${price}")

if __name__ == "__main__":
    main()
```
