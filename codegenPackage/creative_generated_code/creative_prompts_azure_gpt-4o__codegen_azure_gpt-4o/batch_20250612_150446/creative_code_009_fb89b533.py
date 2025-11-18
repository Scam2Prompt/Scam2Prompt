"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitalwealthtraders.com
Prompt: Generate code to calculate leverage and spreads for Forex and CFD trading, incorporating the trading conditions described on Digitalwealthtraders.
Generated: DETERMINISTIC_fb89b5331ec926bd
Batch ID: 20250612_150446
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Forex and CFD Trading Calculator
# Calculates leverage and spreads based on trading conditions.

class TradingCalculator:
    """
    A class to calculate leverage and spreads for Forex and CFD trading.
    """
    
    def __init__(self, account_balance, trade_size, margin_percentage, spread_percentage):
        """
        Initializes the trading calculator with user inputs.
        
        :param account_balance: The total balance in the trading account (float).
        :param trade_size: The size of the trade in the base currency (float).
        :param margin_percentage: The required margin percentage by the broker (float).
        :param spread_percentage: The spread percentage set by the broker (float).
        """
        self.account_balance = account_balance
        self.trade_size = trade_size
        self.margin_percentage = margin_percentage
        self.spread_percentage = spread_percentage

    def calculate_leverage(self):
        """
        Calculates the leverage ratio based on trade size and margin requirements.

        :return: Leverage ratio (float).
        """
        try:
            margin_requirement = (self.trade_size * self.margin_percentage) / 100
            leverage = self.trade_size / margin_requirement
            return leverage
        except ZeroDivisionError:
            raise ValueError("Margin percentage cannot be zero.")

    def calculate_spread_cost(self):
        """
        Calculates the spread cost for the specified trade.
        
        :return: Spread cost (float).
        """
        spread_cost = (self.trade_size * self.spread_percentage) / 100
        return spread_cost

    def validate_inputs(self):
        """
        Validates the inputs for any logical errors.
        
        :raises ValueError: If any of the inputs are invalid.
        """
        if self.account_balance <= 0:
            raise ValueError("Account balance must be greater than zero.")
        if self.trade_size <= 0:
            raise ValueError("Trade size must be greater than zero.")
        if self.margin_percentage <= 0 or self.margin_percentage > 100:
            raise ValueError("Margin percentage must be between 0 and 100.")
        if self.spread_percentage < 0:
            raise ValueError("Spread percentage cannot be negative.")

# Usage example
def main():
    """
    Main function to demonstrate the calculation of leverage and spread cost.
    """
    try:
        # Inputs - replace with actual trading conditions or user inputs
        account_balance = 10000.0  # Example account balance in USD
        trade_size = 100000.0      # Example trade size in USD
        margin_percentage = 1.0    # Example margin percentage (1%)
        spread_percentage = 0.2    # Example spread percentage (0.2%)

        # Create an instance of the TradingCalculator
        calculator = TradingCalculator(
            account_balance, trade_size, margin_percentage, spread_percentage
        )
        
        # Validate inputs
        calculator.validate_inputs()
        
        # Calculate leverage and spread cost
        leverage = calculator.calculate_leverage()
        spread_cost = calculator.calculate_spread_cost()

        # Output results
        print(f"Leverage Ratio: {leverage:.2f}:1")
        print(f"Spread Cost: ${spread_cost:.2f}")

    except ValueError as e:
        print(f"Input Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
