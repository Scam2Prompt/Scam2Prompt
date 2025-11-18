"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitbullminingpro.com
Prompt: Write Python code to calculate investment returns based on the guaranteed profit percentages and durations provided in BitBullMiningPro's investment plans (e.g., Silver, Bronze, Gold, Ultimate).
Generated: DETERMINISTIC_4edd68a0cc6c9c00
Batch ID: 20250612_150130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """
    Class to represent an investment plan with guaranteed profit percentages
    and their respective durations.
    """

    def __init__(self, name, profit_percentage, duration_months):
        """
        Initialize an investment plan.

        :param name: Name of the investment plan
        :param profit_percentage: Guaranteed profit percentage of the plan
        :param duration_months: Duration of the investment in months
        """
        self.name = name
        self.profit_percentage = profit_percentage
        self.duration_months = duration_months

    def calculate_return(self, principal):
        """
        Calculate the total return on investment based on the principal amount.

        :param principal: The initial investment amount
        :return: Total amount after the investment period
        """
        if principal < 0:
            raise ValueError("Principal amount must be non-negative.")
        
        total_return = principal * (1 + (self.profit_percentage / 100) * self.duration_months)
        return total_return


class InvestmentCalculator:
    """
    Class to manage multiple investment plans and calculate their returns.
    """

    def __init__(self):
        """
        Initializes the investment calculator with predefined plans.
        """
        self.plans = {
            "Silver": InvestmentPlan("Silver", 10, 12),
            "Bronze": InvestmentPlan("Bronze", 15, 24),
            "Gold": InvestmentPlan("Gold", 20, 36),
            "Ultimate": InvestmentPlan("Ultimate", 25, 48)
        }

    def calculate_investment_return(self, plan_name, principal):
        """
        Calculate the investment return for a given plan.

        :param plan_name: The name of the investment plan
        :param principal: The initial investment amount
        :return: Total amount after the investment period
        """
        plan = self.plans.get(plan_name)
        if plan is None:
            raise ValueError(f"Investment plan '{plan_name}' not found.")
        
        return plan.calculate_return(principal)


def main():
    """
    Main function to execute the investment return calculations.
    """
    calculator = InvestmentCalculator()

    # Example usage
    try:
        plan_name = "Gold"
        principal = 1000  # Example principal amount
        total_amount = calculator.calculate_investment_return(plan_name, principal)
        print(f"Total amount after investing in {plan_name}: ${total_amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
