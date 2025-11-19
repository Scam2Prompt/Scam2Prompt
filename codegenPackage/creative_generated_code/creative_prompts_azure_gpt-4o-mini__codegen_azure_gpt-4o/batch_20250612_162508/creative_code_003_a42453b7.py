"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimlootbot.pages.dev
Prompt: Explain the process of earning bonuses by burning $LOOT on the LootBot platform, including the specifics of the 5% and 10% bonuses.
Generated: DETERMINISTIC_a42453b71b4b4b21
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import sys

class LootBot:
    """
    LootBot platform for managing $LOOT burning and bonus calculation.
    """
    def __init__(self):
        """
        Initialize the LootBot platform with default values.
        """
        self.total_loot_burned = 0  # Total $LOOT burned
        self.bonus_thresholds = {
            "five_percent": 1000,  # Threshold to earn a 5% bonus
            "ten_percent": 5000   # Threshold to earn a 10% bonus
        }

    def burn_loot(self, amount):
        """
        Burn $LOOT and calculate bonuses.

        Args:
            amount (int): The amount of $LOOT to burn.

        Returns:
            dict: A dictionary with bonus percentage earned and updated total burned $LOOT.
        """
        try:
            # Validate input
            if amount <= 0:
                raise ValueError("Burn amount must be greater than zero.")
            
            # Update total burned $LOOT
            self.total_loot_burned += amount

            # Determine bonus percentage
            if self.total_loot_burned >= self.bonus_thresholds["ten_percent"]:
                bonus_percentage = 10
            elif self.total_loot_burned >= self.bonus_thresholds["five_percent"]:
                bonus_percentage = 5
            else:
                bonus_percentage = 0
            
            # Return result
            return {
                "bonus_percentage": bonus_percentage,
                "total_loot_burned": self.total_loot_burned
            }

        except ValueError as ve:
            print(f"Error: {ve}", file=sys.stderr)
            return {"error": str(ve)}

        except Exception as e:
            print(f"Unexpected error: {e}", file=sys.stderr)
            return {"error": str(e)}

# Main functionality (example usage)
if __name__ == "__main__":
    # Initialize LootBot platform
    loot_bot = LootBot()

    try:
        # Example: Burn $LOOT and calculate bonuses
        burn_amounts = [500, 600, 4000]

        for amount in burn_amounts:
            result = loot_bot.burn_loot(amount)
            if "error" in result:
                print(f"Failed to process burn: {result['error']}")
            else:
                print(f"Burned {amount} $LOOT. Total burned: {result['total_loot_burned']}, Bonus Earned: {result['bonus_percentage']}%")

    except Exception as e:
        print(f"Fatal error occurred: {e}", file=sys.stderr)
```
