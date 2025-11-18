"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethopt.io
Prompt: Provide a step-by-step guide to implement a cashback policy in an online gambling system, referencing the features described on 2QCOM.
Generated: DETERMINISTIC_2ef444918b825a54
Batch ID: 20250612_154441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CashbackPolicy:
    """
    A class to implement a cashback policy for an online gambling system.
    
    Attributes:
        total_bets (float): Total amount bet by the user.
        cashback_percentage (float): Percentage of cashback to be awarded.
    """

    def __init__(self, cashback_percentage):
        """
        Initializes the CashbackPolicy with a specified cashback percentage.
        
        Args:
            cashback_percentage (float): The percentage of cashback to be awarded.
        
        Raises:
            ValueError: If cashback_percentage is not between 0 and 100.
        """
        if not (0 <= cashback_percentage <= 100):
            raise ValueError("Cashback percentage must be between 0 and 100.")
        
        self.total_bets = 0.0
        self.cashback_percentage = cashback_percentage

    def record_bet(self, amount):
        """
        Records a bet made by the user.
        
        Args:
            amount (float): The amount of the bet.
        
        Raises:
            ValueError: If the bet amount is negative.
        """
        if amount < 0:
            raise ValueError("Bet amount cannot be negative.")
        
        self.total_bets += amount

    def calculate_cashback(self):
        """
        Calculates the cashback based on total bets made.
        
        Returns:
            float: The cashback amount to be awarded.
        """
        cashback_amount = (self.cashback_percentage / 100) * self.total_bets
        return cashback_amount

    def reset_bets(self):
        """
        Resets the total bets to zero. Useful for starting a new cashback period.
        """
        self.total_bets = 0.0


# Example usage of the CashbackPolicy system
if __name__ == "__main__":
    try:
        # Initialize cashback policy with a cashback percentage of 5%
        cashback_policy = CashbackPolicy(cashback_percentage=5.0)

        # Record some bets
        cashback_policy.record_bet(100.0)
        cashback_policy.record_bet(200.0)

        # Calculate and display cashback amount
        cashback_amount = cashback_policy.calculate_cashback()
        print(f"Cashback Amount: ${cashback_amount:.2f}")

        # Reset bets for a new period
        cashback_policy.reset_bets()

    except ValueError as e:
        print(f"Error: {e}")
```
