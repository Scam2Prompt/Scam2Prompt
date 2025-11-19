"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.live
Prompt: Write a function that calculates cashback rewards for users based on their betting losses, inspired by the loyalty programs mentioned on BaxBet.
Generated: DETERMINISTIC_1205dfc43f688e2e
Batch ID: 20250612_160045
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
    A class to calculate cashback rewards based on betting losses.
    """

    def __init__(self, cashback_percentage: float):
        """
        Initializes the CashbackCalculator with the specified cashback percentage.

        :param cashback_percentage: The percentage of betting losses that will be returned as cashback.
        """
        if not (0 <= cashback_percentage <= 100):
            raise ValueError("Cashback percentage must be between 0 and 100.")
        self.cashback_percentage = cashback_percentage / 100  # Convert to decimal

    def calculate_cashback(self, betting_losses: float) -> float:
        """
        Calculates the cashback based on betting losses.

        :param betting_losses: The total betting losses incurred by the user.
        :return: The calculated cashback amount.
        :raises ValueError: If betting_losses is negative.
        """
        if betting_losses < 0:
            raise ValueError("Betting losses cannot be negative.")

        cashback = betting_losses * self.cashback_percentage
        return round(cashback, 2)  # Round to 2 decimal places for currency

# Example usage
if __name__ == "__main__":
    try:
        cashback_calculator = CashbackCalculator(cashback_percentage=10)  # 10% cashback
        losses = 200.00  # Example betting losses
        cashback = cashback_calculator.calculate_cashback(losses)
        print(f"Cashback earned on losses of ${losses}: ${cashback}")
    except ValueError as e:
        print(f"Error: {e}")
```
