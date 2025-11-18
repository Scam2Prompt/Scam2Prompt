"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinexchainltd.com
Prompt: Write code to calculate leverage up to 1:100 for professional traders, as offered by Coinex Chain Trading Company Ltd.
Generated: DETERMINISTIC_508268eb03311d6d
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LeverageCalculator:
    """
    A class to calculate leverage for professional traders.

    Attributes:
        max_leverage (float): The maximum allowable leverage ratio.
    """

    def __init__(self, max_leverage=100.0):
        """
        Initializes the LeverageCalculator with a specified max leverage.

        Args:
            max_leverage (float): Maximum leverage ratio (default is 100.0).
        """
        if max_leverage <= 0:
            raise ValueError("Max leverage must be greater than 0.")
        self.max_leverage = max_leverage

    def calculate_leverage(self, equity, margin):
        """
        Calculate the leverage based on equity and margin.

        Args:
            equity (float): The total equity of the trader.
            margin (float): The margin used for trading.

        Returns:
            float: The calculated leverage.

        Raises:
            ValueError: If equity <= 0 or margin <= 0, or if margin exceeds equity.
        """
        if equity <= 0:
            raise ValueError("Equity must be greater than 0.")
        if margin <= 0:
            raise ValueError("Margin must be greater than 0.")
        if margin > equity:
            raise ValueError("Margin cannot exceed equity.")

        leverage = equity / margin
        if leverage > self.max_leverage:
            raise ValueError(f"Leverage cannot exceed the maximum limit of {self.max_leverage}.")

        return leverage


def main():
    """
    Main function to demonstrate leverage calculation.
    """
    try:
        equity = float(input("Enter your total equity: "))  # User input for total equity
        margin = float(input("Enter your margin used for trading: "))  # User input for margin
        
        # Create an instance of LeverageCalculator
        calculator = LeverageCalculator()
        
        # Calculate leverage
        leverage = calculator.calculate_leverage(equity, margin)
        
        print(f"Your calculated leverage is: {leverage:.2f}:1")

    except ValueError as e:
        print(f"Error: {e}")  # Handle invalid input

if __name__ == "__main__":
    main()
```
