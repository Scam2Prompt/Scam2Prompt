"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudo-protocol.xyz
Prompt: Generate code to implement Crudo Protocol's loyalty program, where users receive cashback and entries into giveaways based on their investment tier during the presale.
Generated: DETERMINISTIC_d00b4f3c88e81e71
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Setup logging to capture errors and activity
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class LoyaltyProgram:
    """
    Implements the Crudo Protocol's loyalty program.
    Users receive cashback and giveaway entries based on their investment tier.
    """
    def __init__(self):
        # Define investment tiers and their respective benefits
        self.tiers = {
            "Bronze": {"min_investment": 100, "cashback_percentage": 2, "giveaway_entries": 1},
            "Silver": {"min_investment": 500, "cashback_percentage": 5, "giveaway_entries": 3},
            "Gold": {"min_investment": 1000, "cashback_percentage": 10, "giveaway_entries": 5},
            "Platinum": {"min_investment": 5000, "cashback_percentage": 15, "giveaway_entries": 10},
        }

    def calculate_rewards(self, investment_amount):
        """
        Calculate cashback and giveaway entries based on investment amount.

        :param investment_amount: The amount invested by the user.
        :return: A dictionary containing the user's tier, cashback, and giveaway entries.
        """
        try:
            # Determine user tier based on investment amount
            user_tier = None
            for tier, benefits in sorted(self.tiers.items(), key=lambda x: x[1]['min_investment'], reverse=True):
                if investment_amount >= benefits['min_investment']:
                    user_tier = tier
                    cashback = investment_amount * (benefits['cashback_percentage'] / 100)
                    giveaway_entries = benefits['giveaway_entries']
                    return {
                        "tier": user_tier,
                        "investment_amount": investment_amount,
                        "cashback": round(cashback, 2),
                        "giveaway_entries": giveaway_entries,
                    }
            # If no tier matches, user does not qualify for rewards
            return {
                "tier": "None",
                "investment_amount": investment_amount,
                "cashback": 0,
                "giveaway_entries": 0,
            }
        except Exception as e:
            logging.error("Error calculating rewards: %s", str(e))
            return None

    def display_rewards(self, rewards):
        """
        Display the calculated rewards to the user in a readable format.

        :param rewards: A dictionary containing the user's tier, cashback, and giveaway entries.
        """
        try:
            if rewards is None:
                print("Error: Unable to calculate rewards.")
                return
            print(f"\nLoyalty Program Rewards:")
            print(f"  Investment Amount: ${rewards['investment_amount']}")
            print(f"  Tier: {rewards['tier']}")
            print(f"  Cashback: ${rewards['cashback']}")
            print(f"  Giveaway Entries: {rewards['giveaway_entries']}")
        except Exception as e:
            logging.error("Error displaying rewards: %s", str(e))

# Example usage
if __name__ == "__main__":
    program = LoyaltyProgram()
    try:
        # User investment amount (replace with actual user input in production)
        investment = float(input("Enter your investment amount during the presale: "))
        rewards = program.calculate_rewards(investment)
        program.display_rewards(rewards)
    except ValueError:
        logging.error("Invalid input. Please enter a valid numeric investment amount.")
        print("Error: Please enter a valid numeric investment amount.")
```
