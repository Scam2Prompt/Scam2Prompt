"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://welforcevestcapital.com
Prompt: Create a Python program to simulate the investment plan selection process on Welforcevest Capital, allowing users to choose plans like Starter, Standard, Advanced, Pro, or Enterprise and calculate the expected profit.
Generated: DETERMINISTIC_806d55a7a5c61f53
Batch ID: 20250612_154609
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

    def __init__(self, name, initial_investment, annual_return_rate, investment_duration):
        """
        Initialize an investment plan.

        :param name: str - Name of the investment plan
        :param initial_investment: float - Initial amount to invest
        :param annual_return_rate: float - Expected annual return rate (as a decimal)
        :param investment_duration: int - Duration of the investment in years
        """
        self.name = name
        self.initial_investment = initial_investment
        self.annual_return_rate = annual_return_rate
        self.investment_duration = investment_duration

    def calculate_profit(self):
        """Calculate the expected profit from the investment."""
        final_amount = self.initial_investment * (1 + self.annual_return_rate) ** self.investment_duration
        profit = final_amount - self.initial_investment
        return profit


class InvestmentSelector:
    """Class for selecting and managing investment plans."""

    def __init__(self):
        """Initialize the investment selector with predefined plans."""
        self.plans = {
            "Starter": InvestmentPlan("Starter", 1000, 0.05, 5),
            "Standard": InvestmentPlan("Standard", 5000, 0.07, 7),
            "Advanced": InvestmentPlan("Advanced", 10000, 0.1, 10),
            "Pro": InvestmentPlan("Pro", 25000, 0.12, 15),
            "Enterprise": InvestmentPlan("Enterprise", 50000, 0.15, 20)
        }

    def display_plans(self):
        """Display available investment plans."""
        print("Available Investment Plans:")
        for plan_name, plan in self.plans.items():
            print(f"- {plan_name}: Initial Investment: ${plan.initial_investment}, "
                  f"Expected Annual Return Rate: {plan.annual_return_rate * 100}%, "
                  f"Duration: {plan.investment_duration} years")

    def select_plan(self, plan_name):
        """
        Select an investment plan by name.

        :param plan_name: str - The name of the investment plan to select
        :return: InvestmentPlan - The selected investment plan
        :raises ValueError: If the plan name is not found
        """
        try:
            return self.plans[plan_name]
        except KeyError:
            raise ValueError(f"Investment plan '{plan_name}' does not exist.")

    def simulate_investment(self, plan_name):
        """
        Simulate the investment based on the selected plan.

        :param plan_name: str - The name of the investment plan to simulate
        """
        try:
            plan = self.select_plan(plan_name)
            profit = plan.calculate_profit()
            print(f"\nInvestment Plan: {plan.name}")
            print(f"Expected Profit: ${profit:.2f}")
        except ValueError as e:
            print(e)


def main():
    """Main function to run the investment simulator."""
    selector = InvestmentSelector()

    # Display available plans
    selector.display_plans()

    # Get user input for plan selection
    user_choice = input("\nEnter the name of the investment plan you'd like to simulate: ")
    selector.simulate_investment(user_choice)


if __name__ == "__main__":
    main()
```
