"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://invistribe.com
Prompt: Develop a Python program to calculate potential earnings based on the Fortunity reward tiers (Bronze, Silver, Gold) and simulate the growth of income over time.
Generated: DETERMINISTIC_162771cb25bcce89
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Fortunity:
    """
    A class to calculate potential earnings based on Fortunity reward tiers.
    """

    # Reward tiers with their respective multipliers
    REWARD_TIERS = {
        'Bronze': 1.0,
        'Silver': 1.5,
        'Gold': 2.0
    }

    def __init__(self, base_earning, tier, years):
        """
        Initialize the Fortunity class with base earning, tier, and number of years.

        :param base_earning: Initial earning amount (float)
        :param tier: Reward tier (str), should be one of 'Bronze', 'Silver', 'Gold'
        :param years: Number of years to simulate growth (int)
        """
        self.base_earning = base_earning
        self.tier = tier
        self.years = years
        
        if tier not in self.REWARD_TIERS:
            raise ValueError("Tier must be one of the following: Bronze, Silver, Gold.")

    def calculate_potential_earnings(self):
        """
        Calculate potential earnings after a specified number of years.

        :return: Total earnings (float) after the specified years
        """
        multiplier = self.REWARD_TIERS[self.tier]
        total_earnings = self.base_earning * multiplier * (1 + 0.05) ** self.years  # Assuming a 5% growth rate
        return total_earnings

    def display_earnings(self):
        """
        Display the potential earnings based on the tier.
        """
        try:
            total_earnings = self.calculate_potential_earnings()
            print(f"Base Earning: ${self.base_earning:.2f}")
            print(f"Tier: {self.tier}")
            print(f"Years: {self.years}")
            print(f"Potential Earnings after {self.years} years: ${total_earnings:.2f}")
        except Exception as e:
            print(f"An error occurred: {e}", file=sys.stderr)

def main():
    """
    Main function to execute the earnings calculation.
    """
    # Example parameters (these could come from user input or other sources)
    base_earning = 1000.0  # Initial earning amount
    tier = 'Gold'          # Reward tier
    years = 5              # Number of years to simulate growth

    try:
        # Create a Fortunity instance
        fortunity = Fortunity(base_earning, tier, years)
        # Display the earnings
        fortunity.display_earnings()
    except ValueError as ve:
        print(ve, file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
