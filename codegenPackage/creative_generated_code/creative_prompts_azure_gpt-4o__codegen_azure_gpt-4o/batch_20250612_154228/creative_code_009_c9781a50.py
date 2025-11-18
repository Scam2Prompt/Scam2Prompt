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
import logging

# Configure logging for error tracking
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class CashbackCalculator:
    """
    A class to calculate cashback rewards based on user losses.
    """

    def __init__(self, cashback_percentage):
        """
        Initializes the cashback calculator.

        :param cashback_percentage: Percentage of losses to be returned as cashback (e.g., 10 for 10%).
        """
        if not (0 <= cashback_percentage <= 100):
            raise ValueError("Cashback percentage must be between 0 and 100.")
        self.cashback_percentage = cashback_percentage

    def calculate_cashback(self, losses):
        """
        Calculates the cashback based on user losses.

        :param losses: The amount of losses incurred by the user.
        :return: The cashback reward.
        """
        try:
            if losses < 0:
                raise ValueError("Losses cannot be negative.")
            # Calculate cashback based on the percentage
            cashback = (losses * self.cashback_percentage) / 100
            return round(cashback, 2)
        except TypeError:
            logging.error("Invalid type for losses. Expected a numeric value.", exc_info=True)
            raise ValueError("Losses must be a numeric value.")

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with a 10% cashback rate
        cashback_calculator = CashbackCalculator(cashback_percentage=10)

        # Example user losses
        user_losses = float(input("Enter the user's losses: "))

        # Calculate the cashback reward
        cashback_reward = cashback_calculator.calculate_cashback(user_losses)

        print(f"Cashback reward: ${cashback_reward}")
    except ValueError as e:
        logging.error(f"Error: {e}")
        print(f"Error: {e}")
    except Exception as e:
        logging.error("An unexpected error occurred.", exc_info=True)
        print("An unexpected error occurred. Please try again.")
```
