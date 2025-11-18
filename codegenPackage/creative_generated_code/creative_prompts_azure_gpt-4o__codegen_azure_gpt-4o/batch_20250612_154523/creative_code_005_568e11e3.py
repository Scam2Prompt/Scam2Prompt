"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galxe.de.com
Prompt: Write code to implement a promotional system for an online betting platform, including welcome bonuses and weekly cashback, similar to 123B's promotions.
Generated: DETERMINISTIC_568e11e3bdfe6400
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class PromotionSystem:
    """
    Class to manage promotional system for an online betting platform.
    Includes welcome bonuses and weekly cashback.
    """
    def __init__(self):
        # Maintain user data with promotions state
        self.users = {}

    def register_user(self, user_id):
        """
        Registers a new user and assigns the welcome bonus.
        
        :param user_id: Unique identifier for the user
        """
        if user_id in self.users:
            raise ValueError("User already registered.")
        
        # Initialize user data
        self.users[user_id] = {
            "balance": 0.0,
            "cashback_eligibility": False,
            "last_cashback_date": None,
        }
        
        # Grant welcome bonus
        welcome_bonus = 100.0  # Example: $100 as a welcome bonus
        self.users[user_id]["balance"] += welcome_bonus
        print(f"Welcome bonus of ${welcome_bonus} granted to user {user_id}.")

    def record_bet(self, user_id, bet_amount, win_amount):
        """
        Records a bet for the user.
        
        :param user_id: Unique identifier for the user
        :param bet_amount: Amount bet by the user
        :param win_amount: Amount won by the user (if any)
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        if bet_amount <= 0:
            raise ValueError("Bet amount must be positive.")
        
        # Update the user's balance
        self.users[user_id]["balance"] = self.users[user_id]["balance"] - bet_amount + win_amount
        
        # Mark user eligible for cashback
        self.users[user_id]["cashback_eligibility"] = True

    def process_weekly_cashback(self):
        """
        Processes the weekly cashback for eligible users.
        """
        current_date = datetime.datetime.now().date()

        for user_id, data in self.users.items():
            # Check cashback eligibility and if one week has passed since last cashback
            if data["cashback_eligibility"] and (
                data["last_cashback_date"] is None or 
                (current_date - data["last_cashback_date"]).days >= 7
            ):
                # Example cashback calculation: 10% of losses
                cashback_amount = max(0, -data["balance"] * 0.10)
                data["balance"] += cashback_amount
                data["last_cashback_date"] = current_date
                print(f"Weekly cashback of ${cashback_amount:.2f} granted to user {user_id}.")
                
                # Reset eligibility after processing cashback
                data["cashback_eligibility"] = False

    def get_user_balance(self, user_id):
        """
        Retrieves the current balance of the user.
        
        :param user_id: Unique identifier for the user
        :return: Current balance of the user
        """
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        return self.users[user_id]["balance"]

# Example usage
if __name__ == "__main__":
    system = PromotionSystem()
    
    try:
        # Register users
        system.register_user("user123")
        system.register_user("user456")
        
        # Record bets
        system.record_bet("user123", bet_amount=50.0, win_amount=0.0)
        system.record_bet("user456", bet_amount=30.0, win_amount=20.0)
        
        # Process weekly cashback
        system.process_weekly_cashback()
        
        # Get user balances
        print(f"User123 balance: ${system.get_user_balance('user123'):.2f}")
        print(f"User456 balance: ${system.get_user_balance('user456'):.2f}")
    except Exception as e:
        print(f"Error: {e}")
```
