"""
Generated Code Metadata:
========================
Original URL: https://betpandaofficial.com
Prompt: Generate code to calculate a 100% deposit bonus up to 1 Bitcoin and a 10% cashback on losses, as described in Betpanda's bonus system.
Generated: DETERMINISTIC_a2a29a93107beec0
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class BetpandaBonusSystem:
    """
    A class to calculate deposit bonuses and cashback for Betpanda's bonus system.
    """

    MAX_DEPOSIT_BONUS = 1.0  # Maximum deposit bonus in Bitcoin
    CASHBACK_PERCENTAGE = 0.10  # Cashback percentage on losses

    def __init__(self, deposit_amount: float):
        """
        Initializes the BetpandaBonusSystem with a deposit amount.

        :param deposit_amount: The amount of Bitcoin deposited by the user.
        """
        if deposit_amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.deposit_amount = deposit_amount

    def calculate_deposit_bonus(self) -> float:
        """
        Calculates the deposit bonus based on the deposit amount.

        :return: The deposit bonus in Bitcoin.
        """
        bonus = min(self.deposit_amount, self.MAX_DEPOSIT_BONUS)
        return bonus

    def calculate_cashback(self, losses: float) -> float:
        """
        Calculates the cashback based on the losses incurred.

        :param losses: The total losses incurred by the user.
        :return: The cashback amount in Bitcoin.
        """
        if losses < 0:
            raise ValueError("Losses cannot be negative.")
        cashback = losses * self.CASHBACK_PERCENTAGE
        return cashback

    def summary(self, losses: float) -> dict:
        """
        Provides a summary of the bonuses and cashback.

        :param losses: The total losses incurred by the user.
        :return: A dictionary containing the deposit bonus and cashback.
        """
        deposit_bonus = self.calculate_deposit_bonus()
        cashback = self.calculate_cashback(losses)

        return {
            "Deposit Amount": self.deposit_amount,
            "Deposit Bonus": deposit_bonus,
            "Losses": losses,
            "Cashback": cashback
        }


# Example usage
if __name__ == "__main__":
    try:
        deposit = float(input("Enter your deposit amount in Bitcoin: "))
        losses = float(input("Enter your total losses in Bitcoin: "))

        bonus_system = BetpandaBonusSystem(deposit)
        summary = bonus_system.summary(losses)

        print("\nBonus Summary:")
        for key, value in summary.items():
            print(f"{key}: {value:.4f} BTC")

    except ValueError as e:
        print(f"Error: {e}")
```
