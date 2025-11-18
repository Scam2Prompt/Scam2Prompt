"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vatanbet.info
Prompt: Generate code for a loyalty program system that calculates cashback on losses for users, inspired by BaxBet's cashback feature.
Generated: DETERMINISTIC_fba5bd14293ffd0c
Batch ID: 20250612_145919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Loyalty Program System - Cashback Feature

This script calculates cashback on losses for users based on a loyalty program. 
It supports customizable cashback rates based on user tiers and includes error handling.
"""

class LoyaltyProgram:
    def __init__(self):
        """
        Initialize the loyalty program with predefined tiers and cashback rates.
        Each tier specifies a cashback percentage.
        """
        self.tier_cashback_rates = {
            "bronze": 0.05,  # 5% cashback for bronze tier
            "silver": 0.10,  # 10% cashback for silver tier
            "gold": 0.15,    # 15% cashback for gold tier
            "platinum": 0.20 # 20% cashback for platinum tier
        }

    def calculate_cashback(self, user_losses, user_tier):
        """
        Calculate cashback based on user losses and user tier.

        Parameters:
        user_losses (float): The total amount of losses the user incurred.
        user_tier (str): The loyalty tier of the user.

        Returns:
        float: The cashback amount.
        """
        # Validate input data
        if not isinstance(user_losses, (int, float)) or user_losses < 0:
            raise ValueError("user_losses must be a non-negative number.")
        
        if user_tier not in self.tier_cashback_rates:
            raise ValueError(f"Invalid user tier. Accepted tiers: {', '.join(self.tier_cashback_rates.keys())}")
        
        # Calculate cashback
        cashback_rate = self.tier_cashback_rates[user_tier]
        cashback_amount = user_losses * cashback_rate
        
        return round(cashback_amount, 2)  # Round to 2 decimal places for monetary values


# Example usage
if __name__ == "__main__":
    # Create an instance of the loyalty program
    loyalty_program = LoyaltyProgram()

    try:
        # Sample user data
        user_losses = 1000.00  # User lost $1000
        user_tier = "gold"     # User is in the gold tier

        # Calculate cashback
        cashback = loyalty_program.calculate_cashback(user_losses, user_tier)

        print(f"User Tier: {user_tier}")
        print(f"Total Losses: ${user_losses}")
        print(f"Cashback Earned: ${cashback}")

    except ValueError as e:
        # Handle errors gracefully
        print(f"Error: {e}")
```
