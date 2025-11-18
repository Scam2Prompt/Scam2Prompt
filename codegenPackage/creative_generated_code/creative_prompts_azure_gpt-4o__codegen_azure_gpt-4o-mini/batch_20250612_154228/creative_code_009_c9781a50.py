"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betbax.net
Prompt: Write a Python script to calculate cashback rewards based on user losses, similar to the cashback system described on BaxBet.
Generated: DETERMINISTIC_c9781a50c9997491
Batch ID: 20250612_154228
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
    A class to calculate cashback rewards based on user losses.

    Attributes
    ----------
    loss_threshold : float
        The minimum loss required to earn cashback.
    cashback_percentage : float
        The percentage of cashback to be awarded on losses.

    Methods
    -------
    calculate_cashback(loss_amount):
        Calculates and returns the cashback amount based on user losses.
    """

    def __init__(self, loss_threshold: float, cashback_percentage: float):
        """
        Initializes the CashbackCalculator with a specific loss threshold and cashback percentage.

        Parameters
        ----------
        loss_threshold : float
            The minimum loss to qualify for cashback.
        cashback_percentage : float
            The percentage of cashback to be applied.
        """
        if loss_threshold < 0 or cashback_percentage < 0:
            raise ValueError("loss_threshold and cashback_percentage must be non-negative.")
        
        self.loss_threshold = loss_threshold
        self.cashback_percentage = cashback_percentage / 100  # Convert percentage to decimal

    def calculate_cashback(self, loss_amount: float) -> float:
        """
        Calculates cashback based on the user's loss amount.

        Parameters
        ----------
        loss_amount : float
            The total amount of user losses.

        Returns
        -------
        float
            The calculated cashback amount, or 0 if the loss is below the threshold.
        """
        if loss_amount < 0:
            raise ValueError("Loss amount cannot be negative.")

        if loss_amount < self.loss_threshold:
            return 0.0  # No cashback if losses are below the threshold

        cashback = loss_amount * self.cashback_percentage
        return cashback


def main():
    """
    Main function to demonstrate cashback calculation.
    It handles user input and displays the calculated cashback.
    """
    try:
        # Set cashback parameters
        loss_threshold = 100.0  # Minimum loss to qualify for cashback
        cashback_percentage = 5.0  # Cashback percentage

        # Create a CashbackCalculator instance
        calculator = CashbackCalculator(loss_threshold, cashback_percentage)

        # Get loss amount from user
        loss_amount = float(input("Enter your total losses: "))

        # Calculate and display cashback
        cashback = calculator.calculate_cashback(loss_amount)
        print(f"Your cashback amount is: ${cashback:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
