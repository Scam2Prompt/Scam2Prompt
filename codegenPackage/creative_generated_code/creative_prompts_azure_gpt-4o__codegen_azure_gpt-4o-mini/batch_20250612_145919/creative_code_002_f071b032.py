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
class LoyaltyProgram:
    def __init__(self):
        """Initialize the loyalty program with tiers and cashback rates."""
        self.tiers = {
            "Bronze": {"min_spend": 0, "max_spend": 1000, "cashback_rate": 0.01},
            "Silver": {"min_spend": 1001, "max_spend": 5000, "cashback_rate": 0.02},
            "Gold": {"min_spend": 5001, "max_spend": 15000, "cashback_rate": 0.03},
            "Platinum": {"min_spend": 15001, "cashback_rate": 0.05},
        }
        self.users = {}

    def add_user(self, user_id):
        """Add a new user to the loyalty program."""
        if user_id in self.users:
            raise ValueError("User already exists.")
        self.users[user_id] = {"tier": "Bronze", "total_spend": 0, "cashback": 0}

    def calculate_tier(self, total_spend):
        """Determine the tier of a user based on their total spend."""
        for tier, info in self.tiers.items():
            if total_spend >= info["min_spend"] and (
                "max_spend" not in info or total_spend <= info["max_spend"]
            ):
                return tier
        return "Bronze"

    def update_user_spend(self, user_id, amount):
        """Update the user's total spend and calculate cashback."""
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        if amount < 0:
            raise ValueError("Amount must be positive.")

        # Update total spend
        user_info = self.users[user_id]
        user_info["total_spend"] += amount
        
        # Update tier
        user_info["tier"] = self.calculate_tier(user_info["total_spend"])

        # Calculate cashback
        cashback_rate = self.tiers[user_info["tier"]]["cashback_rate"]
        cashback = amount * cashback_rate
        user_info["cashback"] += cashback

    def get_user_info(self, user_id):
        """Retrieve user information including tier and cashback."""
        if user_id not in self.users:
            raise ValueError("User does not exist.")
        return self.users[user_id]

    def redeem_cashback(self, user_id):
        """Redeem user's cashback and reset their cashback balance."""
        if user_id not in self.users:
            raise ValueError("User does not exist.")

        user_info = self.users[user_id]
        cashback = user_info["cashback"]
        user_info["cashback"] = 0  # Reset cashback after redemption
        return cashback

# Example Usage
if __name__ == "__main__":
    loyalty_program = LoyaltyProgram()
    
    try:
        loyalty_program.add_user("user123")
        loyalty_program.update_user_spend("user123", 1500)
        user_info = loyalty_program.get_user_info("user123")
        print(user_info)  # {'tier': 'Silver', 'total_spend': 1500, 'cashback': 30.0}
        
        cashback_amount = loyalty_program.redeem_cashback("user123")
        print(f"Cashback redeemed: {cashback_amount}")  # Cashback redeemed: 30.0
    except ValueError as e:
        print(f"Error: {e}")
```
