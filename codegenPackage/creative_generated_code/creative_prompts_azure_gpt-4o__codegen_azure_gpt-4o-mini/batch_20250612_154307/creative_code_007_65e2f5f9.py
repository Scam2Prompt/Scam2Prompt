"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinrush.bet
Prompt: Write code to implement a bonus purchase system for casino games, allowing players to buy benefits like free spins or multipliers using cryptocurrency.
Generated: DETERMINISTIC_65e2f5f97a0f535c
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from decimal import Decimal, InvalidOperation

class BonusPurchaseSystem:
    """A system for managing bonus purchases in a casino using cryptocurrency."""

    def __init__(self):
        """Initializes the bonus purchase system with an empty inventory of bonuses."""
        self.bonuses = {
            "free_spin": {"price": Decimal('0.001'), "description": "1 Free Spin"},
            "multiplier_2x": {"price": Decimal('0.002'), "description": "2x Multiplier for 10 spins"},
            "multiplier_3x": {"price": Decimal('0.003'), "description": "3x Multiplier for 10 spins"}
        }
        self.user_wallets = {}

    def create_user_wallet(self, user_id):
        """Creates a wallet for a user if it doesn't already exist."""
        if user_id in self.user_wallets:
            raise ValueError(f"Wallet for user {user_id} already exists.")
        self.user_wallets[user_id] = Decimal('0.0')

    def add_funds(self, user_id, amount):
        """Adds funds to a user's wallet."""
        self._validate_user(user_id)
        amount_decimal = self._convert_to_decimal(amount)
        self.user_wallets[user_id] += amount_decimal

    def purchase_bonus(self, user_id, bonus_type):
        """Allows a user to purchase a bonus if they have enough funds."""
        self._validate_user(user_id)
        if bonus_type not in self.bonuses:
            raise ValueError(f"Bonus type '{bonus_type}' is not available.")
        
        bonus_price = self.bonuses[bonus_type]["price"]
        if self.user_wallets[user_id] < bonus_price:
            raise ValueError("Insufficient funds to purchase this bonus.")

        # Deduct the bonus price from the user's wallet
        self.user_wallets[user_id] -= bonus_price
        return f"Bonus '{bonus_type}' purchased successfully!"

    def _validate_user(self, user_id):
        """Checks whether a user has a wallet."""
        if user_id not in self.user_wallets:
            raise ValueError(f"No wallet found for user {user_id}. Please create one first.")

    def _convert_to_decimal(self, value):
        """Converts an input value to a Decimal type."""
        try:
            return Decimal(value)
        except InvalidOperation:
            raise ValueError(f"Invalid amount: {value}")

    def get_balance(self, user_id):
        """Returns the current balance of a user's wallet."""
        self._validate_user(user_id)
        return self.user_wallets[user_id]

    def get_available_bonuses(self):
        """Returns a list of available bonuses with their prices and descriptions."""
        return json.dumps(self.bonuses, indent=4)

# Example usage
if __name__ == "__main__":
    bonus_system = BonusPurchaseSystem()
    
    # Creating a user wallet
    user_id = 'player1'
    bonus_system.create_user_wallet(user_id)
    
    # Adding funds to the user's wallet
    bonus_system.add_funds(user_id, '0.005')
    
    # Checking balance
    print(f"User balance: {bonus_system.get_balance(user_id)}")
    
    # Purchasing a bonus
    try:
        print(bonus_system.purchase_bonus(user_id, 'free_spin'))
    except ValueError as e:
        print(e)

    # Checking remaining balance
    print(f"User balance after purchase: {bonus_system.get_balance(user_id)}")

    # Display available bonuses
    print("Available bonuses:")
    print(bonus_system.get_available_bonuses())
```
