"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://digitalwealthtraders.com
Prompt: Create a program to simulate an investment plan with parameters like minimum deposit, duration, and fixed interest rates, as outlined in Digitalwealthtraders' Bronze, Silver, Gold, and Platinum plans.
Generated: DETERMINISTIC_2b72c67896f0f1f9
Batch ID: 20250612_150446
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
    A class to represent an investment plan.

    Attributes:
        name (str): The name of the investment plan.
        min_deposit (float): The minimum deposit required for the plan.
        duration_years (int): The duration of the investment in years.
        interest_rate (float): The fixed interest rate for the plan.
    """

    def __init__(self, name, min_deposit, duration_years, interest_rate):
        """
        Initializes the InvestmentPlan with the given parameters.

        Args:
            name (str): The name of the investment plan.
            min_deposit (float): The minimum deposit required for the plan.
            duration_years (int): The duration of the investment in years.
            interest_rate (float): The fixed interest rate for the plan.
        """
        if min_deposit <= 0 or duration_years <= 0 or interest_rate <= 0:
            raise ValueError("Minimum deposit, duration, and interest rate must be positive values.")

        self.name = name
        self.min_deposit = min_deposit
        self.duration_years = duration_years
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal

    def calculate_final_amount(self, initial_investment):
        """
        Calculates the final amount after the investment duration.

        Args:
            initial_investment (float): The initial investment amount.

        Returns:
            float: The final amount after interest is applied.

        Raises:
            ValueError: If the initial investment is less than the minimum deposit.
        """
        if initial_investment < self.min_deposit:
            raise ValueError(f"Initial investment must be at least {self.min_deposit}.")

        # Calculate the final amount using compound interest formula
        final_amount = initial_investment * (1 + self.interest_rate) ** self.duration_years
        return final_amount


# Define Investment Plans
BRONZE_PLAN = InvestmentPlan("Bronze", 1000.0, 1, 5)
SILVER_PLAN = InvestmentPlan("Silver", 5000.0, 3, 7)
GOLD_PLAN = InvestmentPlan("Gold", 10000.0, 5, 10)
PLATINUM_PLAN = InvestmentPlan("Platinum", 25000.0, 10, 12)

def main():
    """
    Main function to run the investment simulation.
    """
    try:
        # Example usage of investment plans
        initial_investment = 6000.0  # User input for initial investment
        plan = SILVER_PLAN  # Choosing the investment plan

        # Calculate the final amount
        final_amount = plan.calculate_final_amount(initial_investment)

        print(f"Final amount after {plan.duration_years} years in the {plan.name} plan: ${final_amount:.2f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
