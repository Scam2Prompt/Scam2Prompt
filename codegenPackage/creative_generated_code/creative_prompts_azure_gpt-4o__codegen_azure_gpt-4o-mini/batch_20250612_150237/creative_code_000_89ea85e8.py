"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ecobrokercapital.com
Prompt: Write Python code to calculate Bitcoin value in USD using a real-time Bitcoin price API, similar to the Bitcoin calculator described on Eco Broker Capital's website.
Generated: DETERMINISTIC_89ea85e8b2054858
Batch ID: 20250612_150237
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coindesk.com/v1/bpi/currentprice/BTC.json": {
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

class BitcoinValueCalculator:
    """
    A class to calculate the current value of Bitcoin in USD using a real-time price API.
    """

    def __init__(self, api_url: str):
        """
        Initializes the BitcoinValueCalculator with the provided API URL.
        
        :param api_url: URL of the API that provides Bitcoin price data.
        """
        self.api_url = api_url

    def fetch_bitcoin_price(self) -> float:
        """
        Fetches the current Bitcoin price in USD from the API.
        
        :return: The current Bitcoin price in USD.
        :raises RuntimeError: If the API request fails or returns an unexpected result.
        """
        try:
            response = requests.get(self.api_url)
            response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)
            data = response.json()
            
            # Assuming the API returns a JSON object containing 'price' key.
            price = data.get('price')
            if price is None:
                raise ValueError("Price not found in the API response.")
            return float(price)
        
        except requests.RequestException as e:
            raise RuntimeError(f"API request failed: {e}")
        except ValueError as e:
            raise RuntimeError(f"Error parsing API response: {e}")

    def calculate_value_in_usd(self, bitcoin_amount: float) -> float:
        """
        Calculates the value of a given amount of Bitcoin in USD.
        
        :param bitcoin_amount: The amount of Bitcoin to convert to USD.
        :return: The equivalent value in USD.
        :raises ValueError: If the bitcoin_amount is negative.
        """
        if bitcoin_amount < 0:
            raise ValueError("Amount of Bitcoin cannot be negative.")
        
        bitcoin_price = self.fetch_bitcoin_price()
        return bitcoin_amount * bitcoin_price

def main():
    """
    Main function to execute the Bitcoin value calculation.
    """
    # Replace with the actual API URL that provides Bitcoin price data
    api_url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    calculator = BitcoinValueCalculator(api_url)

    try:
        bitcoin_amount = float(input("Enter the amount of Bitcoin: "))
        value_in_usd = calculator.calculate_value_in_usd(bitcoin_amount)
        print(f"The value of {bitcoin_amount} BTC in USD is: ${value_in_usd:.2f}")
    except ValueError as e:
        print(f"Input error: {e}")
    except RuntimeError as e:
        print(f"Runtime error: {e}")

if __name__ == "__main__":
    main()
```
