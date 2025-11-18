"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alltecskateparks.com
Prompt: Create a program that calculates cashback and bonus rewards for players based on INDOXSLOT's promotional structure for Lucky Neko.
Generated: DETERMINISTIC_f5173b5d0631e9fd
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LuckyNekoRewardCalculator:
    """
    A class to calculate cashback and bonus rewards for players based on INDOXSLOT's promotional structure for Lucky Neko.
    """

    def __init__(self, base_cashback_percentage=0.05, bonus_threshold=1000, bonus_percentage=0.10):
        """
        Initializes the reward calculator with base cashback percentage, bonus threshold, and bonus percentage.

        :param base_cashback_percentage: The percentage of cashback for player deposits.
        :param bonus_threshold: The minimum amount for a player to qualify for a bonus.
        :param bonus_percentage: The percentage of bonus rewards for qualifying players.
        """
        self.base_cashback_percentage = base_cashback_percentage
        self.bonus_threshold = bonus_threshold
        self.bonus_percentage = bonus_percentage

    def calculate_cashback(self, deposit_amount):
        """
        Calculates the cashback based on the deposit amount.

        :param deposit_amount: The total amount deposited by the player.
        :return: The calculated cashback amount.
        """
        if deposit_amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        
        cashback = deposit_amount * self.base_cashback_percentage
        return cashback

    def calculate_bonus(self, deposit_amount):
        """
        Calculates the bonus rewards if the deposit amount exceeds the bonus threshold.

        :param deposit_amount: The total amount deposited by the player.
        :return: The calculated bonus amount or zero if not qualified.
        """
        if deposit_amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        
        if deposit_amount >= self.bonus_threshold:
            bonus = deposit_amount * self.bonus_percentage
            return bonus
        return 0

    def calculate_rewards(self, deposit_amount):
        """
        Calculates both cashback and bonus rewards for the given deposit amount.

        :param deposit_amount: The total amount deposited by the player.
        :return: A dictionary containing cashback and bonus amounts.
        """
        if deposit_amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        
        cashback = self.calculate_cashback(deposit_amount)
        bonus = self.calculate_bonus(deposit_amount)

        return {
            "cashback": cashback,
            "bonus": bonus
        }


if __name__ == "__main__":
    # Example usage of the LuckyNekoRewardCalculator
    try:
        deposit = float(input("Enter the deposit amount: "))
        calculator = LuckyNekoRewardCalculator()
        rewards = calculator.calculate_rewards(deposit)
        
        print(f"Cashback: {rewards['cashback']:.2f}")
        print(f"Bonus: {rewards['bonus']:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
