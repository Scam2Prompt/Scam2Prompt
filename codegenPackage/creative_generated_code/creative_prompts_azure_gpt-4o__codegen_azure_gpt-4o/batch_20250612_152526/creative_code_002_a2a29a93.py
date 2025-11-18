"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betpandaofficial.com
Prompt: Generate code to calculate a 100% deposit bonus up to 1 Bitcoin and a 10% cashback on losses, as described in Betpanda's bonus system.
Generated: DETERMINISTIC_a2a29a93107beec0
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from decimal import Decimal

class BetpandaBonusSystem:
    """
    A class to calculate bonuses and cashback based on Betpanda's bonus system:
    - 100% deposit bonus up to 1 Bitcoin.
    - 10% cashback on losses.
    """
    
    def __init__(self):
        # Define constants for bonus calculations
        self.MAX_BONUS = Decimal('1.0')  # Maximum bonus in Bitcoin
        self.CASHBACK_RATE = Decimal('0.1')  # 10% cashback rate

    def calculate_deposit_bonus(self, deposit_amount: Decimal) -> Decimal:
        """
        Calculate the 100% deposit bonus, capped at 1 Bitcoin.
        
        :param deposit_amount: The amount deposited in Bitcoin.
        :return: The deposit bonus in Bitcoin.
        """
        if deposit_amount <= 0:
            raise ValueError("Deposit amount must be greater than 0")
        # Calculate bonus and apply cap
        bonus = min(deposit_amount, self.MAX_BONUS)
        return bonus

    def calculate_cashback(self, losses: Decimal) -> Decimal:
        """
        Calculate the 10% cashback on losses.
        
        :param losses: The amount lost in Bitcoin.
        :return: The cashback in Bitcoin.
        """
        if losses < 0:
            raise ValueError("Losses cannot be negative")
        cashback = losses * self.CASHBACK_RATE
        return cashback


# Example Usage
if __name__ == "__main__":
    # Create an instance of BetpandaBonusSystem
    bonus_system = BetpandaBonusSystem()

    try:
        # Input deposit amount and losses
        deposit_amount = Decimal('1.5')  # Example deposit in Bitcoin
        losses = Decimal('0.8')         # Example losses in Bitcoin

        # Calculate bonuses and cashback
        deposit_bonus = bonus_system.calculate_deposit_bonus(deposit_amount)
        cashback = bonus_system.calculate_cashback(losses)

        # Output the results
        print(f"Deposit Amount: {deposit_amount} BTC")
        print(f"Deposit Bonus: {deposit_bonus} BTC")
        print(f"Losses: {losses} BTC")
        print(f"Cashback: {cashback} BTC")
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
```
