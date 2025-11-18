"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://future-lolex.pages.dev
Prompt: Create a program to model speculative trading scenarios using leverage, based on the LOLEX platform's trading categories.
Generated: DETERMINISTIC_c618fe0287e4d5ec
Batch ID: 20250612_154631
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class TradingScenario:
    """
    A class to model a speculative trading scenario using leverage.
    """

    def __init__(self, initial_investment, leverage, price_per_unit):
        """
        Initialize the trading scenario with the specified parameters.
        
        :param initial_investment: The initial amount of capital to invest.
        :param leverage: The leverage factor (e.g., 2 for 2x leverage).
        :param price_per_unit: The price of the asset per unit.
        """
        self.initial_investment = initial_investment
        self.leverage = leverage
        self.price_per_unit = price_per_unit
        self.total_investment = initial_investment * leverage
        self.units_purchased = self.total_investment / price_per_unit
        self.current_price = price_per_unit

    def simulate_price_change(self, volatility):
        """
        Simulate a price change based on the specified volatility.
        
        :param volatility: The percentage change to simulate (as a decimal).
        :return: New price after the change.
        """
        price_change = self.current_price * random.uniform(-volatility, volatility)
        self.current_price += price_change
        return self.current_price

    def calculate_profit_loss(self):
        """
        Calculate the profit or loss based on the current price.
        
        :return: The profit or loss amount.
        """
        if self.current_price <= 0:
            raise ValueError("Current price must be greater than zero.")
        
        total_value = self.units_purchased * self.current_price
        profit_loss = total_value - self.total_investment
        return profit_loss

    def trading_summary(self):
        """
        Generate a summary of the trading scenario.
        
        :return: A dictionary containing the trading summary.
        """
        summary = {
            'Initial Investment': self.initial_investment,
            'Leverage': self.leverage,
            'Total Investment': self.total_investment,
            'Units Purchased': self.units_purchased,
            'Current Price': self.current_price,
            'Profit/Loss': self.calculate_profit_loss()
        }
        return summary

def main():
    """
    Main function to execute the trading scenario simulation.
    """
    try:
        # Initialize parameters for the trading scenario
        initial_investment = 1000  # User's initial capital
        leverage = 2                 # 2x leverage
        price_per_unit = 50         # Price of the asset
        volatility = 0.1             # 10% price change

        # Create a trading scenario
        trading_scenario = TradingScenario(initial_investment, leverage, price_per_unit)

        # Simulate price changes
        for _ in range(10):  # Simulate 10 price changes
            new_price = trading_scenario.simulate_price_change(volatility)
            print(f"New Price: {new_price:.2f}")

        # Print trading summary
        summary = trading_scenario.trading_summary()
        print("\nTrading Summary:")
        for key, value in summary.items():
            print(f"{key}: {value:.2f}" if isinstance(value, (int, float)) else f"{key}: {value}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
