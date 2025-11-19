"""
Generated Code Metadata:
========================
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Generate code to create a promotional system for an online casino that offers bonuses across the first four deposits, similar to the €2,000 welcome bonus structure described on Jackpot Cow Casino's website.
Generated: DETERMINISTIC_2c806e8f04cf5aa1
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class CasinoBonusSystem:
    def __init__(self):
        # Initialize the bonus structure for the first four deposits
        self.bonus_structure = {
            1: (0.50, 2000),  # 50% bonus up to €2000 on the first deposit
            2: (0.25, 1000),  # 25% bonus up to €1000 on the second deposit
            3: (0.20, 500),   # 20% bonus up to €500 on the third deposit
            4: (0.15, 300)    # 15% bonus up to €300 on the fourth deposit
        }

    def calculate_bonus(self, deposit_number, deposit_amount):
        """
        Calculate the bonus for a given deposit number and amount.

        :param deposit_number: The deposit number (1 to 4)
        :param deposit_amount: The amount of the deposit
        :return: The calculated bonus amount
        :raises ValueError: If the deposit number is not between 1 and 4
        """
        if deposit_number < 1 or deposit_number > 4:
            raise ValueError("Deposit number must be between 1 and 4.")

        # Get the bonus percentage and maximum bonus for the deposit number
        bonus_percentage, max_bonus = self.bonus_structure[deposit_number]

        # Calculate the bonus
        bonus = deposit_amount * bonus_percentage

        # Ensure the bonus does not exceed the maximum allowed
        return min(bonus, max_bonus)

    def apply_bonus(self, deposit_number, deposit_amount):
        """
        Apply the bonus to the deposit and return the total amount credited.

        :param deposit_number: The deposit number (1 to 4)
        :param deposit_amount: The amount of the deposit
        :return: The total amount credited to the player's account
        :raises ValueError: If the deposit number is not between 1 and 4
        """
        # Calculate the bonus
        bonus = self.calculate_bonus(deposit_number, deposit_amount)

        # Calculate the total credited amount
        total_credited = deposit_amount + bonus

        return total_credited

# Example usage
if __name__ == "__main__":
    bonus_system = CasinoBonusSystem()

    # Simulate deposits and print the results
    try:
        for deposit_number in range(1, 5):
            deposit_amount = float(input(f"Enter the amount for deposit {deposit_number}: €"))
            total = bonus_system.apply_bonus(deposit_number, deposit_amount)
            print(f"Total credited for deposit {deposit_number}: €{total:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
