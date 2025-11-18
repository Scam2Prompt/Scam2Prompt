"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swaplab.io
Prompt: Generate a script to calculate deposit limits for a cryptocurrency exchange based on reserves, as described in SWAPLAB's FAQ section.
Generated: DETERMINISTIC_b13428d2ba391593
Batch ID: 20250612_151906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json

class CryptoExchange:
    """
    Class to calculate deposit limits for a cryptocurrency exchange based on reserves.
    """

    def __init__(self, reserves):
        """
        Initialize the exchange with cryptocurrency reserves.

        :param reserves: Dictionary containing cryptocurrency reserves in the format:
                         {"BTC": 10.0, "ETH": 50.0, "LTC": 100.0}.
        """
        if not isinstance(reserves, dict):
            raise ValueError("Reserves should be a dictionary.")
        self.reserves = reserves

    def calculate_deposit_limit(self, currency):
        """
        Calculate the deposit limit for a given cryptocurrency based on reserves.

        :param currency: The cryptocurrency symbol (e.g., "BTC", "ETH").
        :return: The deposit limit for the given cryptocurrency.
        :raises ValueError: If the currency is not found in the reserves.
        """
        if currency not in self.reserves:
            raise ValueError(f"Currency {currency} is not supported.")
        
        # Example calculation of deposit limit: 10% of the reserve
        deposit_limit = self.reserves[currency] * 0.1
        return deposit_limit

    def update_reserves(self, currency, amount):
        """
        Update the reserves for a specific cryptocurrency.

        :param currency: The cryptocurrency symbol (e.g., "BTC", "ETH").
        :param amount: The amount to add to the reserves.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        if currency not in self.reserves:
            raise ValueError(f"Currency {currency} is not supported.")
        
        self.reserves[currency] += amount

    def get_reserves(self):
        """
        Get the current reserves as a dictionary.

        :return: The current reserves.
        """
        return self.reserves


if __name__ == "__main__":
    # Example usage
    try:
        # Initialize reserves
        initial_reserves = {"BTC": 10.0, "ETH": 50.0, "LTC": 100.0}
        exchange = CryptoExchange(initial_reserves)

        # Display current reserves
        print("Current Reserves:", json.dumps(exchange.get_reserves(), indent=4))

        # Calculate deposit limit for BTC
        btc_limit = exchange.calculate_deposit_limit("BTC")
        print(f"BTC Deposit Limit: {btc_limit}")

        # Update reserves for ETH
        exchange.update_reserves("ETH", 10.0)
        print("Updated Reserves:", json.dumps(exchange.get_reserves(), indent=4))

    except ValueError as e:
        print("Error:", e)
```
