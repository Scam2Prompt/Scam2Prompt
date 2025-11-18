"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jadobet.org
Prompt: Generate a Python script to calculate cashback rewards for casino players based on their losses, similar to the cashback feature described on BaxBet.
Generated: DETERMINISTIC_593c03d9f75f07c5
Batch ID: 20250612_154344
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
    A class to calculate cashback rewards for casino players based on their losses.
    """

    def __init__(self, cashback_percentage: float):
        """
        Initializes the CashbackCalculator with a specified cashback percentage.

        Args:
            cashback_percentage (float): The percentage of cashback to be given based on losses.
        """
        if cashback_percentage < 0 or cashback_percentage > 100:
            raise ValueError("Cashback percentage must be between 0 and 100.")
        self.cashback_percentage = cashback_percentage / 100  # Convert percentage to decimal

    def calculate_cashback(self, losses: float) -> float:
        """
        Calculates the cashback based on the losses incurred by the player.

        Args:
            losses (float): The total losses incurred by the player.

        Returns:
            float: The calculated cashback amount.

        Raises:
            ValueError: If losses is negative.
        """
        if losses < 0:
            raise ValueError("Losses must be non-negative.")

        cashback = losses * self.cashback_percentage
        return round(cashback, 2)  # Round to 2 decimal places for currency format


def main():
    """
    Main function to demonstrate the cashback calculation.
    """
    try:
        # Example cashback percentage
        cashback_percentage = 10.0  # 10% cashback
        calculator = CashbackCalculator(cashback_percentage)

        # Example losses
        losses = float(input("Enter the total losses incurred by the player: "))

        # Calculate cashback
        cashback = calculator.calculate_cashback(losses)
        print(f"Cashback amount: ${cashback}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
