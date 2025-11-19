"""
Generated Code Metadata:
========================
Original URL: https://welforcevestcapital.com
Prompt: Create a Python program to simulate the investment plan selection process on Welforcevest Capital, allowing users to choose plans like Starter, Standard, Advanced, Pro, or Enterprise and calculate the expected profit.
Generated: DETERMINISTIC_806d55a7a5c61f53
Batch ID: 20250612_154609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class InvestmentPlan:
    """Class to represent an investment plan with its details."""
    
    def __init__(self, name, initial_investment, expected_return_rate, duration_years):
        """
        Initialize an investment plan.

        :param name: Name of the investment plan
        :param initial_investment: Initial amount to invest
        :param expected_return_rate: Expected return rate as a percentage
        :param duration_years: Duration of the investment in years
        """
        self.name = name
        self.initial_investment = initial_investment
        self.expected_return_rate = expected_return_rate
        self.duration_years = duration_years

    def calculate_expected_profit(self):
        """
        Calculate the expected profit from the investment plan.

        :return: Expected profit amount
        """
        return self.initial_investment * (self.expected_return_rate / 100) * self.duration_years


class InvestmentSimulator:
    """Class to simulate the investment plan selection process."""

    def __init__(self):
        """Initialize the investment simulator with available plans."""
        self.plans = {
            "Starter": InvestmentPlan("Starter", 1000, 5, 1),
            "Standard": InvestmentPlan("Standard", 5000, 7, 3),
            "Advanced": InvestmentPlan("Advanced", 10000, 10, 5),
            "Pro": InvestmentPlan("Pro", 20000, 12, 7),
            "Enterprise": InvestmentPlan("Enterprise", 50000, 15, 10),
        }

    def display_plans(self):
        """Display available investment plans to the user."""
        print("Available Investment Plans:")
        for plan_name, plan in self.plans.items():
            print(f"{plan_name}: Initial Investment: ${plan.initial_investment}, "
                  f"Expected Return Rate: {plan.expected_return_rate}%, "
                  f"Duration: {plan.duration_years} years")

    def select_plan(self, plan_name):
        """
        Select an investment plan and calculate the expected profit.

        :param plan_name: Name of the investment plan to select
        :return: Expected profit or error message
        """
        plan = self.plans.get(plan_name)
        if plan:
            expected_profit = plan.calculate_expected_profit()
            return f"Expected profit from {plan.name} plan: ${expected_profit:.2f}"
        else:
            return "Error: Invalid investment plan selected."


def main():
    """Main function to run the investment simulator."""
    simulator = InvestmentSimulator()
    
    # Display available plans
    simulator.display_plans()
    
    # User input for plan selection
    user_input = input("Please select an investment plan (Starter, Standard, Advanced, Pro, Enterprise): ")
    
    # Calculate and display expected profit
    result = simulator.select_plan(user_input.strip())
    print(result)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
