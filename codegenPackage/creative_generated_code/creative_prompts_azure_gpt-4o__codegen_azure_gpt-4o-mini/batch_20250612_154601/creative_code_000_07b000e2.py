"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://envisiontradezone.com
Prompt: Write Python code to calculate the return rate for day trading, swing trading, and positional trading using the specific percentages provided on Envisiontradezone's platform.
Generated: DETERMINISTIC_07b000e2da36c3e6
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradingReturnCalculator:
    """
    A class to calculate the return rate for different types of trading: 
    day trading, swing trading, and positional trading.
    """

    def __init__(self):
        # Dictionary to hold trading strategies and their respective return percentages
        self.trading_strategies = {
            "day_trading": 0.015,   # Example: 1.5% return
            "swing_trading": 0.05,  # Example: 5% return
            "positional_trading": 0.10  # Example: 10% return
        }

    def calculate_return(self, initial_investment: float, strategy: str) -> float:
        """
        Calculate the return based on the initial investment and trading strategy.

        :param initial_investment: The amount of money invested initially
        :param strategy: The trading strategy to use (day_trading, swing_trading, positional_trading)
        :return: The total return amount after applying the return percentage
        :raises ValueError: If the strategy is not recognized or if the investment is negative
        """

        # Validate the initial investment
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative amount.")

        # Validate the trading strategy
        if strategy not in self.trading_strategies:
            raise ValueError(f"Invalid strategy: {strategy}. Choose from {list(self.trading_strategies.keys())}.")

        # Calculate the return
        return_percentage = self.trading_strategies[strategy]
        total_return = initial_investment * return_percentage

        return total_return

    def display_return(self, initial_investment: float, strategy: str):
        """
        Display the calculated return for the given trading strategy.

        :param initial_investment: The amount of money invested initially
        :param strategy: The trading strategy to use
        """
        try:
            total_return = self.calculate_return(initial_investment, strategy)
            print(f"For an initial investment of ${initial_investment:.2f} in {strategy.replace('_', ' ').title()}, "
                  f"the total return is: ${total_return:.2f}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    # Create an instance of TradingReturnCalculator
    calculator = TradingReturnCalculator()

    # Example usage
    investments = [
        {"amount": 1000, "strategy": "day_trading"},
        {"amount": 1500, "strategy": "swing_trading"},
        {"amount": 2000, "strategy": "positional_trading"},
        {"amount": -500, "strategy": "day_trading"},  # Example of error
        {"amount": 1000, "strategy": "invalid_strategy"}  # Example of error
    ]

    # Calculate and display returns for each investment scenario
    for investment in investments:
        calculator.display_return(investment["amount"], investment["strategy"])
```
