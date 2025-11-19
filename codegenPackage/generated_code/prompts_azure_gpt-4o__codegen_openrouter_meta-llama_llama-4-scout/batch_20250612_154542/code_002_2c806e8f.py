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
# promotional_system.py

class PromotionalSystem:
    def __init__(self, bonus_structure):
        """
        Initialize the promotional system with a bonus structure.

        Args:
            bonus_structure (list): A list of tuples containing the deposit number and the bonus amount.
        """
        self.bonus_structure = bonus_structure

    def calculate_bonus(self, deposit_amount, deposit_number):
        """
        Calculate the bonus for a given deposit amount and deposit number.

        Args:
            deposit_amount (float): The amount of the deposit.
            deposit_number (int): The number of the deposit.

        Returns:
            float: The bonus amount.

        Raises:
            ValueError: If the deposit number is not in the bonus structure.
        """
        for structure in self.bonus_structure:
            if structure[0] == deposit_number:
                # Assuming the bonus is a percentage of the deposit amount
                return deposit_amount * structure[1] / 100
        raise ValueError("Deposit number not found in bonus structure")

    def get_bonus_structure(self):
        """
        Get the bonus structure.

        Returns:
            list: A list of tuples containing the deposit number and the bonus amount.
        """
        return self.bonus_structure


class Casino:
    def __init__(self, promotional_system):
        """
        Initialize the casino with a promotional system.

        Args:
            promotional_system (PromotionalSystem): The promotional system.
        """
        self.promotional_system = promotional_system
        self.deposits = {}

    def make_deposit(self, user_id, deposit_amount, deposit_number):
        """
        Make a deposit and calculate the bonus.

        Args:
            user_id (int): The ID of the user.
            deposit_amount (float): The amount of the deposit.
            deposit_number (int): The number of the deposit.

        Returns:
            dict: A dictionary containing the deposit amount and the bonus amount.

        Raises:
            ValueError: If the deposit number is not in the bonus structure.
        """
        if user_id not in self.deposits:
            self.deposits[user_id] = []

        bonus_amount = self.promotional_system.calculate_bonus(deposit_amount, deposit_number)
        self.deposits[user_id].append({"deposit_amount": deposit_amount, "bonus_amount": bonus_amount, "deposit_number": deposit_number})

        return {"deposit_amount": deposit_amount, "bonus_amount": bonus_amount}

    def get_user_deposits(self, user_id):
        """
        Get the deposits for a user.

        Args:
            user_id (int): The ID of the user.

        Returns:
            list: A list of dictionaries containing the deposit amount, bonus amount, and deposit number.
        """
        return self.deposits.get(user_id, [])


def main():
    # Define the bonus structure for the first four deposits
    bonus_structure = [
        (1, 100),  # 100% bonus for the first deposit up to €2,000
        (2, 50),   # 50% bonus for the second deposit up to €1,000
        (3, 25),   # 25% bonus for the third deposit up to €500
        (4, 10)    # 10% bonus for the fourth deposit up to €200
    ]

    promotional_system = PromotionalSystem(bonus_structure)
    casino = Casino(promotional_system)

    user_id = 1
    deposits = [
        {"deposit_amount": 1000, "deposit_number": 1},
        {"deposit_amount": 500, "deposit_number": 2},
        {"deposit_amount": 200, "deposit_number": 3},
        {"deposit_amount": 100, "deposit_number": 4},
    ]

    for deposit in deposits:
        result = casino.make_deposit(user_id, deposit["deposit_amount"], deposit["deposit_number"])
        print(f"Deposit {deposit['deposit_number']}: {result['deposit_amount']}, Bonus: {result['bonus_amount']}")

    user_deposits = casino.get_user_deposits(user_id)
    print("\nUser Deposits:")
    for deposit in user_deposits:
        print(f"Deposit {deposit['deposit_number']}: {deposit['deposit_amount']}, Bonus: {deposit['bonus_amount']}")


if __name__ == "__main__":
    main()
```
