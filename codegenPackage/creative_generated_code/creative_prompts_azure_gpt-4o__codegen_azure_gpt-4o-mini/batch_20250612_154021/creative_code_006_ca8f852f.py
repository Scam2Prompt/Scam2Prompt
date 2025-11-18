"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aterdex.com
Prompt: Develop a function to calculate leverage and margin requirements for a trade on Aster DEX's Simple Mode.
Generated: DETERMINISTIC_ca8f852fa4f5bae5
Batch ID: 20250612_154021
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TradeCalculator:
    """
    A class to calculate leverage and margin requirements for trading on Aster DEX's Simple Mode.
    """

    def __init__(self, trade_amount: float, leverage: float):
        """
        Initializes the TradeCalculator with the specified trade amount and leverage.

        :param trade_amount: The total amount of the trade in the base currency.
        :param leverage: The leverage ratio to be used for the trade.
        """
        if trade_amount <= 0:
            raise ValueError("Trade amount must be greater than zero.")
        if leverage <= 0:
            raise ValueError("Leverage must be greater than zero.")
        
        self.trade_amount = trade_amount
        self.leverage = leverage

    def calculate_margin(self) -> float:
        """
        Calculates the margin required for the trade.

        :return: The margin required in the base currency.
        """
        margin = self.trade_amount / self.leverage
        return margin

    def calculate_leverage(self) -> float:
        """
        Calculates the leverage based on the trade and margin.

        :return: The leverage ratio.
        """
        if self.trade_amount == 0:
            return 0.0
        leverage = self.trade_amount / self.calculate_margin()
        return leverage

    def display_trade_info(self) -> None:
        """
        Displays the trade information including trade amount, leverage, and margin required.
        """
        margin_required = self.calculate_margin()
        print(f"Trade Amount: {self.trade_amount} (Base Currency)")
        print(f"Leverage: {self.leverage}")
        print(f"Margin Required: {margin_required:.2f} (Base Currency)")

# Example usage
if __name__ == "__main__":
    try:
        trade_amount = 1000.0  # Example trade amount
        leverage = 10.0        # Example leverage

        # Create an instance of the TradeCalculator
        calculator = TradeCalculator(trade_amount, leverage)

        # Display trade information
        calculator.display_trade_info()

    except ValueError as e:
        print(f"Error: {e}")
```
