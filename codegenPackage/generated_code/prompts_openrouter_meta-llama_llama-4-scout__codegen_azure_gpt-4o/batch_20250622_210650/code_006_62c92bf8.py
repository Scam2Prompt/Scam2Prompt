"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Create a code example to generate a comprehensive financial plan, including retirement savings, education funding, and wealth building, based on TSM Wealth's finance services.
Generated: DETERMINISTIC_62c92bf833b62923
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class FinancialPlan:
    """
    A class to generate a comprehensive financial plan including:
    - Retirement savings
    - Education funding
    - Wealth building
    """

    def __init__(self, annual_income, current_savings, retirement_age, current_age, education_expenses, wealth_goal):
        """
        Initialize the financial plan with user inputs.

        :param annual_income: Annual income of the individual (float)
        :param current_savings: Current savings of the individual (float)
        :param retirement_age: Age at which the individual plans to retire (int)
        :param current_age: Current age of the individual (int)
        :param education_expenses: Estimated education expenses (float)
        :param wealth_goal: Target wealth goal (float)
        """
        self.annual_income = annual_income
        self.current_savings = current_savings
        self.retirement_age = retirement_age
        self.current_age = current_age
        self.education_expenses = education_expenses
        self.wealth_goal = wealth_goal

    def calculate_retirement_savings(self):
        """
        Calculate the required retirement savings based on annual income and years until retirement.

        :return: Required retirement savings (float)
        """
        years_until_retirement = self.retirement_age - self.current_age
        if years_until_retirement <= 0:
            raise ValueError("Retirement age must be greater than current age.")
        
        # Assuming 80% of annual income is needed per year for retirement
        annual_retirement_expense = self.annual_income * 0.8
        # Assuming retirement lasts for 20 years
        retirement_duration = 20
        required_retirement_savings = annual_retirement_expense * retirement_duration

        return required_retirement_savings

    def calculate_education_funding(self):
        """
        Calculate the required education funding.

        :return: Required education funding (float)
        """
        # Assuming education expenses are provided directly
        return self.education_expenses

    def calculate_wealth_building(self):
        """
        Calculate the annual savings required to achieve the wealth goal.

        :return: Annual savings required for wealth building (float)
        """
        years_to_goal = self.retirement_age - self.current_age
        if years_to_goal <= 0:
            raise ValueError("Wealth building goal must be achievable before retirement.")
        
        # Using compound interest formula to calculate annual savings required
        # Assuming an annual return rate of 5% (0.05)
        annual_return_rate = 0.05
        future_value_factor = (math.pow(1 + annual_return_rate, years_to_goal) - 1) / annual_return_rate
        annual_savings_required = self.wealth_goal / future_value_factor

        return annual_savings_required

    def generate_plan(self):
        """
        Generate the comprehensive financial plan.

        :return: Dictionary containing the financial plan details
        """
        try:
            retirement_savings = self.calculate_retirement_savings()
            education_funding = self.calculate_education_funding()
            wealth_building = self.calculate_wealth_building()

            return {
                "Retirement Savings": retirement_savings,
                "Education Funding": education_funding,
                "Annual Wealth Building Savings": wealth_building
            }
        except ValueError as e:
            return {"Error": str(e)}
        except Exception as e:
            return {"Error": f"An unexpected error occurred: {str(e)}"}


# Example usage
if __name__ == "__main__":
    # User inputs
    annual_income = 75000.0
    current_savings = 20000.0
    retirement_age = 65
    current_age = 30
    education_expenses = 50000.0
    wealth_goal = 1000000.0

    # Create financial plan instance
    financial_plan = FinancialPlan(
        annual_income=annual_income,
        current_savings=current_savings,
        retirement_age=retirement_age,
        current_age=current_age,
        education_expenses=education_expenses,
        wealth_goal=wealth_goal
    )

    # Generate and display the financial plan
    plan = financial_plan.generate_plan()
    for key, value in plan.items():
        print(f"{key}: ${value:,.2f}" if isinstance(value, float) else f"{key}: {value}")
```
