"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintradeoptions.com
Prompt: Generate code to implement an investment plan selection system for Fintradeoptions, allowing users to choose between Starter, Premium, Advanced, Pro, and Trial plans and calculate returns.
Generated: DETERMINISTIC_77a46430b89c0f01
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class InvestmentPlan:
    """Class representing an investment plan."""
    
    def __init__(self, name, initial_investment, annual_return_rate, duration_years):
        """
        Initializes an investment plan with the given parameters.

        :param name: Name of the investment plan
        :param initial_investment: Initial investment amount
        :param annual_return_rate: Expected annual return rate (as a percentage)
        :param duration_years: Duration of the investment in years
        """
        self.name = name
        self.initial_investment = initial_investment
        self.annual_return_rate = annual_return_rate
        self.duration_years = duration_years

    def calculate_returns(self):
        """
        Calculates the total returns from the investment.

        :return: Total value of the investment after the specified duration
        """
        try:
            total_value = self.initial_investment * (1 + self.annual_return_rate / 100) ** self.duration_years
            return total_value
        except Exception as e:
            print(f"Error calculating returns: {e}")
            return None


class InvestmentPlanSelector:
    """Class to handle selection and management of investment plans."""
    
    def __init__(self):
        """Initializes the investment plan selector with predefined plans."""
        self.plans = {
            "Starter": InvestmentPlan("Starter", initial_investment=1000, annual_return_rate=5, duration_years=5),
            "Premium": InvestmentPlan("Premium", initial_investment=5000, annual_return_rate=7, duration_years=10),
            "Advanced": InvestmentPlan("Advanced", initial_investment=10000, annual_return_rate=10, duration_years=15),
            "Pro": InvestmentPlan("Pro", initial_investment=25000, annual_return_rate=12, duration_years=20),
            "Trial": InvestmentPlan("Trial", initial_investment=0, annual_return_rate=0, duration_years=1)
        }

    def select_plan(self, plan_name):
        """
        Selects an investment plan based on the plan name.

        :param plan_name: The name of the investment plan
        :return: The selected InvestmentPlan object or None if plan not found
        """
        plan = self.plans.get(plan_name)
        if plan:
            return plan
        else:
            print(f"Plan '{plan_name}' not found.")
            return None


def main():
    """Main function to run the investment plan selection system."""
    selector = InvestmentPlanSelector()
    
    print("Available Investment Plans:")
    for name in selector.plans.keys():
        print(name)

    # Example user input (in production, replace with actual user input handling)
    user_input = "Premium"  # This should come from user input in a real application

    selected_plan = selector.select_plan(user_input)
    
    if selected_plan:
        total_returns = selected_plan.calculate_returns()
        if total_returns is not None:
            print(f"Total returns for the {selected_plan.name} plan: ${total_returns:.2f}")


if __name__ == "__main__":
    main()
```
