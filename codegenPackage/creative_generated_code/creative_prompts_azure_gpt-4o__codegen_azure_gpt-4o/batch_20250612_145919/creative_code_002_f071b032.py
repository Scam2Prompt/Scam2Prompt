"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanplatform.bet
Prompt: Generate code to create a loyalty program system for an online casino, including features like cashback on losses and tiered rewards, as described in BaxBet's offerings.
Generated: DETERMINISTIC_f071b032a768df2f
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class LoyaltyProgram:
    """
    A class to manage the loyalty program system for an online casino.
    Includes cashback on losses and tiered rewards.
    """
    
    def __init__(self):
        """
        Initializes the loyalty program with default tiers and cashback rates.
        """
        self.tiers = {
            "Bronze": {"cashback_rate": 0.01, "required_points": 0},
            "Silver": {"cashback_rate": 0.02, "required_points": 1000},
            "Gold": {"cashback_rate": 0.05, "required_points": 5000},
            "Platinum": {"cashback_rate": 0.1, "required_points": 10000},
        }
        self.users = {}  # Maps user IDs to their loyalty data
    
    def register_user(self, user_id):
        """
        Registers a new user in the loyalty program.
        
        :param user_id: Unique identifier for the user.
        """
        if user_id in self.users:
            raise ValueError("User is already registered.")
        
        self.users[user_id] = {
            "tier": "Bronze",
            "points": 0,
            "lifetime_loss": 0,
            "last_cashback_date": None,
        }
    
    def record_loss(self, user_id, amount):
        """
        Records a loss for a user and updates their loyalty points.
        
        :param user_id: Unique identifier for the user.
        :param amount: Amount of money lost by the user.
        """
        if user_id not in self.users:
            raise ValueError("User is not registered.")
        
        user_data = self.users[user_id]
        user_data["lifetime_loss"] += amount
        user_data["points"] += int(amount)  # 1 point per dollar lost
        self._update_tier(user_id)
    
    def _update_tier(self, user_id):
        """
        Updates the user's tier based on their accumulated points.
        
        :param user_id: Unique identifier for the user.
        """
        user_data = self.users[user_id]
        for tier, details in sorted(self.tiers.items(), key=lambda x: x[1]["required_points"]):
            if user_data["points"] >= details["required_points"]:
                user_data["tier"] = tier
    
    def calculate_cashback(self, user_id):
        """
        Calculates and returns the cashback amount for a user based on their tier.
        
        :param user_id: Unique identifier for the user.
        :return: Cashback amount.
        """
        if user_id not in self.users:
            raise ValueError("User is not registered.")
        
        user_data = self.users[user_id]
        tier_data = self.tiers[user_data["tier"]]
        cashback_rate = tier_data["cashback_rate"]
        
        # Cashback is calculated on lifetime losses
        return round(user_data["lifetime_loss"] * cashback_rate, 2)
    
    def issue_cashback(self, user_id):
        """
        Issues cashback to the user, resets lifetime losses, and logs the cashback issuance date.
        
        :param user_id: Unique identifier for the user.
        :return: Cashback amount issued.
        """
        if user_id not in self.users:
            raise ValueError("User is not registered.")
        
        user_data = self.users[user_id]
        cashback_amount = self.calculate_cashback(user_id)
        user_data["lifetime_loss"] = 0  # Reset lifetime losses after cashback
        user_data["last_cashback_date"] = datetime.datetime.now()
        return cashback_amount
    
    def get_user_data(self, user_id):
        """
        Retrieves the loyalty information for a specific user.
        
        :param user_id: Unique identifier for the user.
        :return: User's loyalty data as a dictionary.
        """
        if user_id not in self.users:
            raise ValueError("User is not registered.")
        
        return self.users[user_id]


# Example Usage
if __name__ == "__main__":
    # Initialize the loyalty program
    program = LoyaltyProgram()
    
    # Register users
    program.register_user("user123")
    program.register_user("user456")
    
    # Record losses
    program.record_loss("user123", 500)
    program.record_loss("user123", 700)
    program.record_loss("user456", 1200)
    
    # Issue cashback
    cashback_user123 = program.issue_cashback("user123")
    print(f"Cashback issued to user123: ${cashback_user123}")
    
    # Check user data
    user_data = program.get_user_data("user123")
    print(f"User123 data: {user_data}")
```
