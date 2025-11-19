"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradetoearnoptions.com
Prompt: Write a code snippet that calculates potential returns based on the investment plans offered by Tradetoearnoption, specifically for the Gold and Deluxe plans.
Generated: DETERMINISTIC_adf17fbcd577dcaf
Batch ID: 20250612_160413
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
    Class to represent an investment plan and calculate potential returns.
    """
    
    def __init__(self, plan_name, principal_amount, interest_rate, duration_years):
        """
        Initializes the investment plan with the given parameters.

        :param plan_name: Name of the investment plan (e.g., 'Gold', 'Deluxe')
        :param principal_amount: The amount of money invested (float)
        :param interest_rate: The annual interest rate (as a percentage, float)
        :param duration_years: Duration of the investment in years (int)
        """
        self.plan_name = plan_name
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.duration_years = duration_years

    def calculate_returns(self):
        """
        Calculates the potential returns from the investment plan.

        :return: Total amount after the investment duration (float)
        """
        try:
            if self.principal_amount < 0 or self.interest_rate < 0 or self.duration_years < 0:
                raise ValueError("Principal amount, interest rate, and duration must be non-negative.")

            # Calculate the total amount using compound interest formula
            total_amount = self.principal_amount * (1 + (self.interest_rate / 100)) ** self.duration_years
            return total_amount
        
        except Exception as e:
            print(f"Error calculating returns: {e}")
            return None


def main():
    """
    Main function to demonstrate the investment return calculations for Gold and Deluxe plans.
    """
    # Define investment plans with sample parameters
    gold_plan = InvestmentPlan(plan_name="Gold", principal_amount=10000, interest_rate=5, duration_years=10)
    deluxe_plan = InvestmentPlan(plan_name="Deluxe", principal_amount=15000, interest_rate=7, duration_years=10)

    # Calculate and print potential returns for each plan
    plans = [gold_plan, deluxe_plan]
    
    for plan in plans:
        returns = plan.calculate_returns()
        if returns is not None:
            print(f"Total amount after investing in {plan.plan_name} plan: ${returns:.2f}")


if __name__ == "__main__":
    main()
```
