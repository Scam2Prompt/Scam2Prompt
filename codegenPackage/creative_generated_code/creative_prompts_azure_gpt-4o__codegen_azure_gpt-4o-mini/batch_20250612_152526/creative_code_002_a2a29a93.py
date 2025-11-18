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
class BetpandaBonusCalculator:
    """
    A class to calculate Betpanda's bonus system which includes a 100% deposit bonus up to 1 Bitcoin
    and a 10% cashback on losses.

    Attributes:
        deposit (float): The amount deposited in Bitcoin.
        losses (float): The amount of losses in Bitcoin.
    """

    MAX_BONUS = 1.0  # Maximum bonus in Bitcoin
    CASHBACK_RATE = 0.10  # Cashback rate (10%)

    def __init__(self, deposit: float, losses: float):
        """
        Initializes the BetpandaBonusCalculator with deposit and losses.

        Args:
            deposit (float): The amount deposited in Bitcoin.
            losses (float): The amount of losses in Bitcoin.
        """
        self.deposit = deposit
        self.losses = losses

    def calculate_deposit_bonus(self) -> float:
        """
        Calculates the 100% deposit bonus based on the deposited amount.

        Returns:
            float: The amount of bonus received (in Bitcoin).
        """
        # Ensure deposit is non-negative
        if self.deposit < 0:
            raise ValueError("Deposit amount cannot be negative.")
        
        # Calculate the bonus as either double the deposit or the maximum bonus
        bonus = min(self.deposit * 2, self.MAX_BONUS)
        return bonus

    def calculate_cashback(self) -> float:
        """
        Calculates the cashback based on the losses.

        Returns:
            float: The amount of cashback received (in Bitcoin).
        """
        # Ensure losses are non-negative
        if self.losses < 0:
            raise ValueError("Losses amount cannot be negative.")
        
        cashback = self.losses * self.CASHBACK_RATE
        return cashback

    def calculate_total_bonus(self) -> float:
        """
        Calculates the total bonus which includes the deposit bonus and cashback.

        Returns:
            float: The total bonus amount (in Bitcoin).
        """
        deposit_bonus = self.calculate_deposit_bonus()
        cashback = self.calculate_cashback()
        total_bonus = deposit_bonus + cashback
        return total_bonus


# Example usage
if __name__ == "__main__":
    try:
        deposit_amount = float(input("Enter deposit amount in Bitcoin: "))
        loss_amount = float(input("Enter loss amount in Bitcoin: "))

        bonus_calculator = BetpandaBonusCalculator(deposit_amount, loss_amount)
        total_bonus = bonus_calculator.calculate_total_bonus()

        print(f"Total Bonus: {total_bonus:.4f} Bitcoin")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
