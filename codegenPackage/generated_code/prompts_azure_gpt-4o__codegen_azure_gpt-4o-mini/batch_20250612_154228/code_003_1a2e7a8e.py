"""
Generated Code Metadata:
========================
Original URL: https://betlahze.vip
Prompt: Write a script to calculate cashback rewards for users based on their losses in casino games, as described in BaxBet's loyalty program.
Generated: DETERMINISTIC_1a2e7a8e382eba2a
Batch ID: 20250612_154228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CashbackCalculator:
    """
    A class to calculate cashback rewards based on user losses in casino games.
    """

    def __init__(self, cashback_percentage: float):
        """
        Initializes the CashbackCalculator with a specified cashback percentage.

        :param cashback_percentage: The percentage of losses to be returned as cashback.
        """
        if not (0 <= cashback_percentage <= 100):
            raise ValueError("Cashback percentage must be between 0 and 100.")
        self.cashback_percentage = cashback_percentage / 100  # Convert to decimal

    def calculate_cashback(self, losses: float) -> float:
        """
        Calculates the cashback based on the user's losses.

        :param losses: The total losses incurred by the user.
        :return: The calculated cashback amount.
        """
        if losses < 0:
            raise ValueError("Losses cannot be negative.")
        
        cashback = losses * self.cashback_percentage
        return round(cashback, 2)  # Round to two decimal places for currency format

def main():
    """
    Main function to execute the cashback calculation.
    """
    try:
        # Example usage
        cashback_percentage = 10.0  # Example cashback percentage
        losses = float(input("Enter total losses: "))  # User input for losses

        # Create a CashbackCalculator instance
        calculator = CashbackCalculator(cashback_percentage)

        # Calculate cashback
        cashback = calculator.calculate_cashback(losses)

        # Display the result
        print(f"Your cashback reward is: ${cashback}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
