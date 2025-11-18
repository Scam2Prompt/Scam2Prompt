"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betlahze.vip
Prompt: Write a script to calculate cashback rewards for users based on their losses in casino games, as described in BaxBet's loyalty program.
Generated: DETERMINISTIC_1a2e7a8e382eba2a
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
    A class to calculate cashback rewards based on losses in casino games.
    The cashback percentage is determined based on the loss amount according to BaxBet's loyalty program.
    """

    def __init__(self, cashback_tiers):
        """
        Initialize the CashbackCalculator with defined cashback tiers.

        Args:
            cashback_tiers (dict): A dictionary that maps loss thresholds to cashback percentages.
        """
        self.cashback_tiers = cashback_tiers

    def calculate_cashback(self, losses):
        """
        Calculate the cashback amount based on the losses incurred.

        Args:
            losses (float): The total losses incurred by the user.

        Returns:
            float: The calculated cashback amount.
        """
        if losses < 0:
            raise ValueError("Losses cannot be negative.")

        cashback_rate = self.get_cashback_rate(losses)
        cashback_amount = losses * cashback_rate
        return round(cashback_amount, 2)

    def get_cashback_rate(self, losses):
        """
        Get the cashback rate based on the specified loss amount.

        Args:
            losses (float): The total losses incurred by the user.

        Returns:
            float: The applicable cashback rate.
        """
        for threshold, rate in sorted(self.cashback_tiers.items(), reverse=True):
            if losses >= threshold:
                return rate
        return 0.0  # No cashback for losses below the minimum threshold

def main():
    # Define cashback tiers (loss threshold: cashback percentage)
    cashback_tiers = {
        1000: 0.15,  # 15% cashback for losses of $1000 or more
        500: 0.10,   # 10% cashback for losses of $500 or more
        0: 0.05      # 5% cashback for any losses
    }

    # Create an instance of CashbackCalculator
    calculator = CashbackCalculator(cashback_tiers)

    # Example user losses
    user_losses = 1200  # Example input

    try:
        cashback = calculator.calculate_cashback(user_losses)
        print(f"Cashback for losses of ${user_losses}: ${cashback}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
