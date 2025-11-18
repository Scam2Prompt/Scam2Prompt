"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elitesignaltrade.net
Prompt: Develop a program to calculate profits from market rallies and declines for Bitcoin, Ethereum, and Ripple, leveraging the 100X leverage feature offered by Elite Signal Trade.
Generated: DETERMINISTIC_003fd4f9f5ce3b61
Batch ID: 20250612_150417
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.coingecko.com/api/v3/simple/price": {
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

class CryptoProfitCalculator:
    def __init__(self):
        """
        Initialize the profit calculator with constants for leverage and supported cryptocurrencies.
        """
        self.leverage = 100  # 100X leverage
        self.supported_cryptocurrencies = ['Bitcoin', 'Ethereum', 'Ripple']
        self.api_url = 'https://api.coingecko.com/api/v3/simple/price'  # Public API for cryptocurrency prices

    def fetch_crypto_prices(self):
        """
        Fetches the current prices for Bitcoin, Ethereum, and Ripple using the CoinGecko API.
        Returns a dictionary of prices.
        """
        try:
            # Prepare the API query for the required cryptocurrencies
            params = {
                'ids': ','.join([crypto.lower() for crypto in self.supported_cryptocurrencies]),
                'vs_currencies': 'usd'
            }
            response = requests.get(self.api_url, params=params)
            response.raise_for_status()  # Raise an error if the request failed

            # Parse the response JSON
            data = response.json()
            return {
                'Bitcoin': data.get('bitcoin', {}).get('usd'),
                'Ethereum': data.get('ethereum', {}).get('usd'),
                'Ripple': data.get('ripple', {}).get('usd')
            }

        except requests.RequestException as e:
            raise RuntimeError(f"Failed to fetch cryptocurrency prices: {e}")

    def calculate_profit(self, crypto, entry_price, exit_price, investment):
        """
        Calculate the profit or loss for a given cryptocurrency trade.
        :param crypto: The name of the cryptocurrency (e.g., 'Bitcoin', 'Ethereum', 'Ripple')
        :param entry_price: The price at which the cryptocurrency was bought
        :param exit_price: The price at which the cryptocurrency was sold
        :param investment: The amount invested in the trade
        :return: The calculated profit or loss
        """
        if crypto not in self.supported_cryptocurrencies:
            raise ValueError(f"{crypto} is not a supported cryptocurrency.")

        if entry_price <= 0 or exit_price <= 0 or investment <= 0:
            raise ValueError("Entry price, exit price, and investment must all be greater than zero.")

        # Calculate the price movement percentage
        price_movement_percentage = ((exit_price - entry_price) / entry_price) * 100

        # Account for 100X leverage
        leveraged_movement_percentage = price_movement_percentage * self.leverage

        # Calculate profit or loss
        profit_or_loss = (leveraged_movement_percentage / 100) * investment

        return profit_or_loss

    def display_results(self, crypto, entry_price, exit_price, investment):
        """
        Display the trade results in a user-friendly format.
        """
        try:
            profit = self.calculate_profit(crypto, entry_price, exit_price, investment)
            print(f"Trade Results for {crypto}:")
            print(f"  Entry Price: ${entry_price:.2f}")
            print(f"  Exit Price:  ${exit_price:.2f}")
            print(f"  Investment:  ${investment:.2f}")
            print(f"  Profit/Loss: ${profit:.2f}")
            print("-" * 30)
        except ValueError as e:
            print(f"Error: {e}")
        except RuntimeError as e:
            print(f"Runtime Error: {e}")


if __name__ == "__main__":
    # Create an instance of the calculator
    calculator = CryptoProfitCalculator()

    print("Fetching current cryptocurrency prices...")
    try:
        crypto_prices = calculator.fetch_crypto_prices()

        # Display fetched prices
        for crypto, price in crypto_prices.items():
            if price:
                print(f"{crypto}: ${price:.2f}")
            else:
                print(f"Could not fetch price for {crypto}.")
        print("-" * 30)

        # Example trade: Bitcoin trade with 100X leverage
        entry_price = 20000  # Example entry price
        exit_price = 22000   # Example exit price
        investment = 100     # Example investment amount
        calculator.display_results("Bitcoin", entry_price, exit_price, investment)

        # Example trade: Ethereum
        entry_price = 1500
        exit_price = 1800
        investment = 200
        calculator.display_results("Ethereum", entry_price, exit_price, investment)

    except RuntimeError as e:
        print(f"Error: {e}")
```
