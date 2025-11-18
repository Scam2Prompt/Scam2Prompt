"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uagra.com.ua
Prompt: Provide code examples for implementing a bonus system that matches Parimatch's +100% first deposit bonus with conditions like wagering requirements and expiration periods.
Generated: DETERMINISTIC_0b27f58b5ab0f786
Batch ID: 20250612_154432
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class BonusSystem:
    """
    A class to implement a bonus system with +100% first deposit bonus,
    wagering requirements, and expiration periods.
    """

    def __init__(self):
        self.bonuses = {}  # Stores bonus information for each user
    
    def add_deposit_bonus(self, user_id, deposit_amount):
        """
        Adds a +100% first deposit bonus for the user.
        """

        # Check if user already has a bonus
        if user_id in self.bonuses:
            raise ValueError("User already has an active bonus.")

        # Bonus details
        bonus_amount = deposit_amount
        wagering_requirement = bonus_amount * 10  # Example: Bonus must be wagered 10x
        expiration_date = datetime.datetime.now() + datetime.timedelta(days=30)  # 30 days expiry

        # Store user's bonus
        self.bonuses[user_id] = {
            "bonus_amount": bonus_amount,
            "wagering_requirement": wagering_requirement,
            "expiration_date": expiration_date,
            "wagered_amount": 0
        }
        return f"Bonus of {bonus_amount} added! Wagering requirement: {wagering_requirement}. Expires on {expiration_date}"

    def wager(self, user_id, amount):
        """
        Records a wager by the user and reduces the wagering requirement.
        """

        if user_id not in self.bonuses:
            raise ValueError("No active bonus for this user.")

        bonus = self.bonuses[user_id]

        # Check if bonus is expired
        if datetime.datetime.now() > bonus['expiration_date']:
            del self.bonuses[user_id]  # Remove expired bonus
            raise ValueError("Bonus has expired.")

        # Update wagered amount and remaining wagering requirement
        bonus['wagered_amount'] += amount
        bonus['wagering_requirement'] -= amount

        if bonus['wagering_requirement'] <= 0:
            del self.bonuses[user_id]  # Remove bonus when wagering requirement is met
            return "Congratulations! Bonus wagering requirement met."

        return f"Wager recorded. Remaining wagering requirement: {bonus['wagering_requirement']}"

    def check_bonus_status(self, user_id):
        """
        Returns the current status of the user's bonus.
        """

        if user_id not in self.bonuses:
            return "No active bonus."

        bonus = self.bonuses[user_id]
        if datetime.datetime.now() > bonus['expiration_date']:
            del self.bonuses[user_id]  # Remove expired bonus
            return "Bonus has expired."

        return {
            "bonus_amount": bonus["bonus_amount"],
            "remaining_wagering_requirement": max(0, bonus["wagering_requirement"]),
            "expiration_date": bonus["expiration_date"]
        }

# Example usage:
if __name__ == "__main__":
    bonus_system = BonusSystem()

    try:
        user_id = 1
        deposit_amount = 100

        # Add deposit bonus
        print(bonus_system.add_deposit_bonus(user_id, deposit_amount))

        # Place wagers
        print(bonus_system.wager(user_id, 50))
        print(bonus_system.wager(user_id, 500))  # Example: surplus wager clears bonus

        # Check bonus status
        print(bonus_system.check_bonus_status(user_id))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
```
