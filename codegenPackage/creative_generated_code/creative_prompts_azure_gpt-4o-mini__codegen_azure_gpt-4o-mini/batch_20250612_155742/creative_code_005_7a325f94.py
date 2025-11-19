"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fun-virtuals-agent.pages.dev
Prompt: Provide an example of a bonding market cap calculation for a new coin on Fun Virtuals.
Generated: DETERMINISTIC_7a325f94813ddec1
Batch ID: 20250612_155742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class BondingMarketCapCalculator:
    """
    A class to calculate the bonding market cap for a new coin on Fun Virtuals.
    """

    def __init__(self, total_supply, price_per_coin):
        """
        Initializes the BondingMarketCapCalculator with the total supply and price per coin.
        
        :param total_supply: Total number of coins available
        :param price_per_coin: Current price per coin
        """
        self.total_supply = total_supply
        self.price_per_coin = price_per_coin

    def calculate_bonding_market_cap(self):
        """
        Calculates the bonding market cap based on total supply and price per coin.
        
        :return: The bonding market cap
        :raises ValueError: If total supply or price per coin is non-positive
        """
        if self.total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if self.price_per_coin <= 0:
            raise ValueError("Price per coin must be greater than zero.")

        # Calculate the bonding market cap
        market_cap = self.total_supply * self.price_per_coin
        return market_cap

if __name__ == "__main__":
    try:
        # Example input for the new coin on Fun Virtuals
        total_supply = 1000000  # Total coins available
        price_per_coin = 10.5    # Price per coin in currency

        # Create an instance of the calculator
        calculator = BondingMarketCapCalculator(total_supply, price_per_coin)

        # Calculate and print the bonding market cap
        bonding_market_cap = calculator.calculate_bonding_market_cap()
        print(f"The bonding market cap is: ${bonding_market_cap:,.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
