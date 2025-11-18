"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jadobet.org
Prompt: Generate code for implementing a loyalty program in a casino platform, including features like cashback on losses and tier-based rewards, inspired by BaxBet's offerings.
Generated: DETERMINISTIC_e19c31a4c9e7dc00
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoyaltyProgram:
    def __init__(self):
        # Initialize the loyalty program with empty user data
        self.users = {}
        self.tiers = {
            "Bronze": {"min_spent": 0, "cashback_rate": 0.01},
            "Silver": {"min_spent": 1000, "cashback_rate": 0.02},
            "Gold": {"min_spent": 5000, "cashback_rate": 0.03},
            "Platinum": {"min_spent": 10000, "cashback_rate": 0.05},
        }

    def register_user(self, user_id):
        """Register a new user in the loyalty program."""
        if user_id in self.users:
            raise ValueError(f"User {user_id} is already registered.")
        
        self.users[user_id] = {
            "total_spent": 0,
            "cashback_earned": 0,
            "tier": "Bronze"
        }
        print(f"User {user_id} registered successfully.")

    def update_spending(self, user_id, amount):
        """Update the total spending for a user and calculate cashback."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        
        if amount < 0:
            raise ValueError("Amount must be non-negative.")

        # Update total spent
        user_data = self.users[user_id]
        user_data["total_spent"] += amount
        
        # Calculate cashback on losses (amount is assumed to be losses)
        cashback = amount * self.get_cashback_rate(user_data["tier"])
        user_data["cashback_earned"] += cashback
        
        # Print the cashback earned
        print(f"User {user_id} earned ${cashback:.2f} in cashback.")

        # Update tier if necessary
        self.update_tier(user_id)

    def get_cashback_rate(self, tier):
        """Get the cashback rate for a given tier."""
        return self.tiers[tier]["cashback_rate"]

    def update_tier(self, user_id):
        """Update the user's tier based on total spending."""
        total_spent = self.users[user_id]["total_spent"]
        for tier, info in reversed(self.tiers.items()):
            if total_spent >= info["min_spent"]:
                if self.users[user_id]["tier"] != tier:
                    print(f"User {user_id} upgraded to {tier} tier.")
                    self.users[user_id]["tier"] = tier
                return

    def get_user_info(self, user_id):
        """Retrieve the loyalty program information for a user."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} is not registered.")
        
        return self.users[user_id]

# Example usage
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    
    # Register users
    loyalty_program.register_user("user123")
    loyalty_program.register_user("user456")

    # Update spending and check loyalty status
    loyalty_program.update_spending("user123", 1500)
    loyalty_program.update_spending("user123", 4000)

    # Retrieve user info
    user_info = loyalty_program.get_user_info("user123")
    print(user_info)
```
