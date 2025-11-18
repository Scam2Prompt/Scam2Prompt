"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://supermining.website
Prompt: Provide a Python implementation for calculating affiliate bonuses based on SuperMining's tiered bonus percentages (e.g., 30%, 40%, 50%, 100%) for upgraded plans.
Generated: DETERMINISTIC_8f6602b5a2a783b0
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class AffiliateBonusCalculator:
    """
    A class to calculate affiliate bonuses based on tiered percentages.
    """

    def __init__(self):
        # Define the tiered bonus percentages in a dictionary
        self.tiers = {
            1: 0.30,  # 30%
            2: 0.40,  # 40%
            3: 0.50,  # 50%
            4: 1.00   # 100%
        }

    def calculate_bonus(self, plan_tier, sales_amount):
        """
        Calculate the bonus for a given plan tier and sales amount.

        :param plan_tier: The tier level of the affiliate plan (1-4).
        :param sales_amount: The total sales amount for which the bonus is calculated.
        :return: The calculated bonus amount.
        :raises ValueError: If the plan tier is not in the valid range.
        """

        # Validate the input parameters
        if plan_tier not in self.tiers:
            raise ValueError(f"Invalid plan tier: {plan_tier}. Must be between 1 and 4.")
        
        if sales_amount < 0:
            raise ValueError("Sales amount cannot be negative.")

        # Calculate the bonus based on the tier
        bonus_percentage = self.tiers[plan_tier]
        bonus = sales_amount * bonus_percentage

        return bonus

def main():
    """
    Main function to demonstrate the AffiliateBonusCalculator.
    """
    calculator = AffiliateBonusCalculator()
    
    try:
        # Example usage
        plan_tier = 3  # Example tier
        sales_amount = 1000.00  # Example sales amount

        bonus = calculator.calculate_bonus(plan_tier, sales_amount)
        print(f"The calculated bonus for plan tier {plan_tier} on sales amount ${sales_amount} is: ${bonus:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
