"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cashb90.org
Prompt: Create a function that calculates cashback rewards for users based on their betting activity, inspired by the loyalty program at BaxBet.
Generated: DETERMINISTIC_f86f87debe3b1796
Batch ID: 20250612_155855
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CashbackCalculator:
    """
    A class to calculate cashback rewards based on betting activity.
    """

    def __init__(self, cashback_percentage):
        """
        Initializes the CashbackCalculator with a specified cashback percentage.

        Parameters:
        cashback_percentage (float): The percentage of cashback to be awarded on total bets.
        """
        if not (0 < cashback_percentage <= 100):
            raise ValueError("Cashback percentage must be between 0 and 100.")
        self.cashback_percentage = cashback_percentage / 100  # Convert percentage to decimal

    def calculate_cashback(self, total_bet_amount):
        """
        Calculate the cashback based on the total betting amount.

        Parameters:
        total_bet_amount (float): The total amount of bets placed by the user.

        Returns:
        float: The amount of cashback earned.
        """
        if total_bet_amount < 0:
            raise ValueError("Total bet amount cannot be negative.")
        
        cashback = total_bet_amount * self.cashback_percentage
        return round(cashback, 2)  # Round to two decimal places for currency representation

# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the cashback calculator with a 5% cashback rate
        calculator = CashbackCalculator(cashback_percentage=5)

        # Example total bet amount
        total_bets = 1000.00  # Total bets placed by the user

        # Calculate cashback
        cashback_amount = calculator.calculate_cashback(total_bet_amount=total_bets)
        print(f"Cashback earned: ${cashback_amount}")  # Output the cashback amount

    except ValueError as e:
        print(f"Error: {e}")
```
