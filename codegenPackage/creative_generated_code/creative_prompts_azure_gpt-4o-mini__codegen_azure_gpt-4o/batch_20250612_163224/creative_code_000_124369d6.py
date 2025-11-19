"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astoricrypto.com
Prompt: Write a Python script that implements a profit-based fee structure for a cryptocurrency trading group, similar to the model described on AstoriCrypto, where members pay 10% of their profits after doubling their portfolio.
Generated: DETERMINISTIC_124369d69aa3dcf8
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to track application flow and errors
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TradingGroupFeeStructure:
    """
    Class to calculate fees for a cryptocurrency trading group based on profit.
    Members pay 10% of their profits, but only after doubling their portfolio.
    """

    def __init__(self, initial_balance):
        """
        Initialize the fee structure with the user's initial balance.
        
        :param initial_balance: (float) The portfolio balance when the user joined.
        """
        if initial_balance <= 0:
            raise ValueError("Initial balance must be greater than 0.")
        self.initial_balance = initial_balance
        self.highest_balance = initial_balance  # Tracks the highest recorded balance

    def calculate_fees(self, current_balance):
        """
        Calculate the fee owed based on the current portfolio balance.
        
        :param current_balance: (float) The current balance of the user's portfolio.
        :return: (float) The fee to be paid, or 0 if no fee is owed.
        """
        if current_balance < 0:
            raise ValueError("Current balance cannot be negative.")

        # Update the highest balance if the current balance exceeds it
        if current_balance > self.highest_balance:
            self.highest_balance = current_balance

        # Check if the portfolio has doubled
        doubled_balance = 2 * self.initial_balance
        if current_balance > doubled_balance:
            # Calculate profits above the doubled threshold
            profit_above_doubled = current_balance - doubled_balance

            # Calculate a 10% fee on the profit above the doubled balance
            fee = 0.10 * profit_above_doubled
            return round(fee, 2)  # Round to 2 decimal places for clarity
        else:
            return 0.0  # No fee owed if portfolio hasn't doubled


def main():
    """
    Main function to demonstrate the TradingGroupFeeStructure functionality.
    """
    try:
        # Example: Initialize the trading group fee structure with a starting balance
        initial_balance = float(input("Enter your initial portfolio balance: "))
        trading_group = TradingGroupFeeStructure(initial_balance)

        while True:
            # Prompt the user for their current portfolio balance
            current_balance = float(input("Enter your current portfolio balance (or -1 to exit): "))
            if current_balance == -1:
                logging.info("Exiting the program...")
                break

            # Calculate fees
            fee = trading_group.calculate_fees(current_balance)

            # Display the result
            if fee > 0:
                print(f"Fee owed based on your profits: ${fee}")
            else:
                print("No fee owed at this time. Keep trading!")

    except ValueError as ve:
        logging.error(f"Input error: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
