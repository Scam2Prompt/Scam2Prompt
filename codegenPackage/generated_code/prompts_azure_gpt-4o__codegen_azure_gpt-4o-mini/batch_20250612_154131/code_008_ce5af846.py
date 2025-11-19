"""
Generated Code Metadata:
========================
Original URL: https://unstaked-token.world
Prompt: Develop a tool to simulate the number of $UNSD tokens a user will receive based on their investment amount in various cryptocurrencies (e.g., ETH, BNB, USDT).
Generated: DETERMINISTIC_ce5af84630d36068
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class TokenSimulator:
    def __init__(self, conversion_rates):
        """
        Initialize the TokenSimulator with conversion rates for various cryptocurrencies to UNSD tokens.
        
        :param conversion_rates: A dictionary containing conversion rates for each cryptocurrency.
        """
        self.conversion_rates = conversion_rates

    def calculate_unsd_tokens(self, investment_amount, crypto_type):
        """
        Calculate the number of UNSD tokens a user will receive based on their investment amount and cryptocurrency type.
        
        :param investment_amount: The amount of cryptocurrency the user is investing.
        :param crypto_type: The type of cryptocurrency (e.g., 'ETH', 'BNB', 'USDT').
        :return: The number of UNSD tokens received.
        :raises ValueError: If the cryptocurrency type is not supported or investment amount is negative.
        """
        if investment_amount < 0:
            raise ValueError("Investment amount must be non-negative.")
        
        if crypto_type not in self.conversion_rates:
            raise ValueError(f"Unsupported cryptocurrency type: {crypto_type}. Supported types: {list(self.conversion_rates.keys())}")

        # Calculate the number of UNSD tokens based on the investment amount and conversion rate
        unsd_tokens = investment_amount * self.conversion_rates[crypto_type]
        return unsd_tokens

def main():
    # Example conversion rates for demonstration purposes
    conversion_rates = {
        'ETH': 100,   # 1 ETH = 100 UNSD tokens
        'BNB': 50,    # 1 BNB = 50 UNSD tokens
        'USDT': 1      # 1 USDT = 1 UNSD token
    }

    # Create an instance of the TokenSimulator
    simulator = TokenSimulator(conversion_rates)

    # User input for investment amount and cryptocurrency type
    try:
        investment_amount = float(input("Enter your investment amount: "))
        crypto_type = input("Enter the cryptocurrency type (ETH, BNB, USDT): ").strip().upper()

        # Calculate the number of UNSD tokens
        unsd_tokens = simulator.calculate_unsd_tokens(investment_amount, crypto_type)
        print(f"You will receive {unsd_tokens} UNSD tokens for your investment of {investment_amount} {crypto_type}.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
