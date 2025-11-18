"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://futuresourcelimited.com
Prompt: Write code to implement a referral bonus system that provides an 8% bonus for referrals, as described in the investment plans on futuresourcelimited.com.
Generated: DETERMINISTIC_473608ff624c7c21
Batch ID: 20250612_150316
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

class ReferralBonusSystem:
    """
    Referral Bonus System to calculate referral bonuses based on an 8% rate.
    """

    def __init__(self, bonus_rate=0.08):
        """
        Initialize the ReferralBonusSystem with a given bonus rate.
        :param bonus_rate: Percentage rate for referral bonus (default: 8%).
        """
        self.bonus_rate = decimal.Decimal(str(bonus_rate))

    def calculate_bonus(self, investment_amount):
        """
        Calculate referral bonus based on the investment amount.
        :param investment_amount: Investment amount in decimal or float.
        :return: Computed bonus as a decimal.
        """
        try:
            investment_amount = decimal.Decimal(str(investment_amount))
            if investment_amount <= 0:
                raise ValueError("Investment amount must be greater than zero.")
            
            # Calculate the referral bonus
            bonus = investment_amount * self.bonus_rate
            return bonus
        except (ValueError, decimal.InvalidOperation) as error:
            raise ValueError(f"Invalid investment amount: {error}")

    def display_bonus(self, investment_amount):
        """
        Display the referral bonus based on the provided investment amount.
        :param investment_amount: Investment amount in decimal or float.
        """
        try:
            bonus = self.calculate_bonus(investment_amount)
            print(f"Investment Amount: ${investment_amount:.2f}")
            print(f"Referral Bonus (8%): ${bonus:.2f}")
        except ValueError as error:
            print(f"Error: {error}")


# Usage example
if __name__ == "__main__":
    referral_system = ReferralBonusSystem()

    try:
        # Example investment amounts
        investments = [500, 1000, -200, "abc"]
        
        for investment in investments:
            print("------")
            referral_system.display_bonus(investment)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
