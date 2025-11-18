"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://holdstation-revshare.pages.dev
Prompt: Develop a program to calculate position size, fees, and liquidation price for BTCUSD trades using Holdstation's trading formulas.
Generated: DETERMINISTIC_86e589c725631df1
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class TradingCalculator:
    """
    A class to calculate position size, fees, and liquidation price for BTCUSD trades
    using Holdstation's trading formulas.
    """

    def __init__(self, leverage: float, entry_price: float, balance: float):
        """
        Initializes the calculator with basic parameters.
        :param leverage: Leverage used for the trade, e.g., 10 for 10x leverage.
        :param entry_price: Entry price of BTC in USD.
        :param balance: Account balance in USD.
        """
        self.leverage = leverage
        self.entry_price = entry_price
        self.balance = balance

    def calculate_position_size(self) -> float:
        """
        Calculate the position size based on leverage and account balance.
        Formula: Position Size = Balance * Leverage
        :return: Position size in USD.
        """
        return self.balance * self.leverage

    def calculate_fees(self, position_size: float, fee_rate: float = 0.001) -> float:
        """
        Calculate the fees based on position size and fee rate.
        Formula: Fees = Position Size * Fee Rate
        :param position_size: Position size in USD.
        :param fee_rate: Fee rate, default is 0.1% (0.001).
        :return: Fees in USD.
        """
        if fee_rate < 0 or fee_rate > 1:
            raise ValueError("Fee rate must be between 0 and 1.")
        return position_size * fee_rate

    def calculate_liquidation_price(self, direction: str) -> float:
        """
        Calculate the liquidation price based on entry price and leverage.
        Formula for long: Liquidation Price = Entry Price * (1 - 1 / Leverage)
        Formula for short: Liquidation Price = Entry Price * (1 + 1 / Leverage)
        :param direction: 'long' for long positions, 'short' for short positions.
        :return: Liquidation price in USD.
        """
        if direction not in ["long", "short"]:
            raise ValueError("Direction must be either 'long' or 'short'.")
        
        if direction == "long":
            return self.entry_price * (1 - 1 / self.leverage)
        else:  # direction == "short"
            return self.entry_price * (1 + 1 / self.leverage)

def main():
    """
    Main function to run the trading calculator.
    """
    try:
        # User inputs
        balance = float(input("Enter your account balance (USD): "))
        leverage = float(input("Enter the leverage (e.g., 10 for 10x): "))
        entry_price = float(input("Enter the entry price of BTC (USD): "))
        direction = input("Enter the trade direction ('long' or 'short'): ").lower()

        # Initialize the trading calculator
        calculator = TradingCalculator(leverage, entry_price, balance)

        # Perform calculations
        position_size = calculator.calculate_position_size()
        fees = calculator.calculate_fees(position_size)
        liquidation_price = calculator.calculate_liquidation_price(direction)

        # Output results
        print("\n=== Trade Calculation Results ===")
        print(f"Position Size: ${position_size:.2f} USD")
        print(f"Fees: ${fees:.2f} USD")
        print(f"Liquidation Price: ${liquidation_price:.2f} USD")
        print("=================================")

    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
