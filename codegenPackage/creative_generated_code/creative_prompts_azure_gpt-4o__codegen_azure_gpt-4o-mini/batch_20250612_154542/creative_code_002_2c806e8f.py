"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Generate code to create a promotional system for an online casino that offers bonuses across the first four deposits, similar to the €2,000 welcome bonus structure described on Jackpot Cow Casino's website.
Generated: DETERMINISTIC_2c806e8f04cf5aa1
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class CasinoBonusSystem:
    """
    A class to represent a promotional system for an online casino that
    manages bonuses for the first four deposits.
    """

    def __init__(self):
        """
        Initializes the CasinoBonusSystem with a bonus structure.
        """
        self.bonus_structure = {
            1: (0.100, 2000),  # 1st deposit: 100% up to €2000
            2: (0.075, 1500),  # 2nd deposit: 75% up to €1500
            3: (0.050, 1000),  # 3rd deposit: 50% up to €1000
            4: (0.025, 500)    # 4th deposit: 25% up to €500
        }
        self.user_balances = {}

    def add_user(self, user_id):
        """
        Adds a user to the system with an initial balance of 0.

        :param user_id: Unique identifier for the user.
        """
        if user_id not in self.user_balances:
            self.user_balances[user_id] = {
                'balance': 0,
                'deposits': 0,
                'bonuses_received': 0
            }
        else:
            raise ValueError("User already exists.")

    def deposit(self, user_id, amount):
        """
        Processes a deposit for a user and applies any applicable bonuses.

        :param user_id: Unique identifier for the user.
        :param amount: The amount to be deposited.
        :raises ValueError: If the user does not exist or amount is invalid.
        """
        if user_id not in self.user_balances:
            raise ValueError("User does not exist.")

        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        user_data = self.user_balances[user_id]

        # Check if the user is eligible for a bonus
        user_data['deposits'] += 1
        bonus = self.calculate_bonus(user_data['deposits'], amount)

        # Update balance
        user_data['balance'] += amount + bonus
        user_data['bonuses_received'] += bonus

    def calculate_bonus(self, deposit_number, amount):
        """
        Calculates the bonus based on the deposit number and amount.

        :param deposit_number: The current deposit number.
        :param amount: The amount deposited.
        :return: The calculated bonus amount.
        """
        if deposit_number in self.bonus_structure:
            bonus_percent, max_bonus = self.bonus_structure[deposit_number]
            bonus = amount * bonus_percent
            return min(bonus, max_bonus)
        return 0

    def get_user_balance(self, user_id):
        """
        Retrieves the user's current balance and bonuses.

        :param user_id: Unique identifier for the user.
        :return: A dictionary containing the user's balance and bonuses.
        :raises ValueError: If the user does not exist.
        """
        if user_id not in self.user_balances:
            raise ValueError("User does not exist.")
        
        return self.user_balances[user_id]

# Example usage
if __name__ == "__main__":
    casino = CasinoBonusSystem()
    casino.add_user('user123')
    
    try:
        casino.deposit('user123', 1000)  # 1st deposit
        casino.deposit('user123', 2000)  # 2nd deposit
        balance_info = casino.get_user_balance('user123')
        print(balance_info)
    except ValueError as e:
        print(f"Error: {e}")
```
