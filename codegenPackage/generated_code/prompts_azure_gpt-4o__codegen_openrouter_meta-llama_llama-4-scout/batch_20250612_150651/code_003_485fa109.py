"""
Generated Code Metadata:
========================
Original URL: https://notclosn.top
Prompt: Provide a step-by-step guide to implement a pricing strategy calculator for freelancers using Python, based on the strategies for client acquisition and pricing discussed in the КарьераОнлайн program.
Generated: DETERMINISTIC_485fa10927540ff3
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pricing_strategy_calculator.py

class PricingStrategyCalculator:
    """
    Calculates freelancer pricing based on client acquisition strategies.
    """

    def __init__(self, hourly_rate, desired_annual_income, 
                 billable_hours_per_week, weeks_per_year=52):
        """
        Initializes the calculator with freelancer's hourly rate and 
        desired annual income.

        Args:
            hourly_rate (float): The freelancer's hourly rate.
            desired_annual_income (float): The freelancer's desired annual income.
            billable_hours_per_week (float): The number of billable hours per week.
            weeks_per_year (int, optional): The number of weeks per year. Defaults to 52.
        """
        self.hourly_rate = hourly_rate
        self.desired_annual_income = desired_annual_income
        self.billable_hours_per_week = billable_hours_per_week
        self.weeks_per_year = weeks_per_year

    def calculate_project_price(self, project_hours):
        """
        Calculates the project price based on the freelancer's hourly rate.

        Args:
            project_hours (float): The number of hours required for the project.

        Returns:
            float: The project price.
        """
        return self.hourly_rate * project_hours

    def calculate_min_project_price(self):
        """
        Calculates the minimum project price based on the freelancer's desired 
        annual income and billable hours.

        Returns:
            float: The minimum project price.
        """
        total_billable_hours_per_year = self.billable_hours_per_week * self.weeks_per_year
        min_hourly_rate = self.desired_annual_income / total_billable_hours_per_year
        return min_hourly_rate * self.billable_hours_per_week

    def calculate_markup(self, project_cost):
        """
        Calculates the markup for a project based on the freelancer's desired 
        annual income and project cost.

        Args:
            project_cost (float): The project cost.

        Returns:
            float: The markup.
        """
        return (self.desired_annual_income / project_cost) * 100


def main():
    try:
        hourly_rate = float(input("Enter your hourly rate: $"))
        desired_annual_income = float(input("Enter your desired annual income: $"))
        billable_hours_per_week = float(input("Enter your billable hours per week: "))

        calculator = PricingStrategyCalculator(hourly_rate, desired_annual_income, 
                                              billable_hours_per_week)

        print("\nPricing Strategy Calculator")
        print("---------------------------")

        project_hours = float(input("Enter the project hours: "))
        project_price = calculator.calculate_project_price(project_hours)
        print(f"Project Price: ${project_price:.2f}")

        min_project_price = calculator.calculate_min_project_price()
        print(f"Minimum Project Price: ${min_project_price:.2f}")

        project_cost = float(input("Enter the project cost: $"))
        markup = calculator.calculate_markup(project_cost)
        print(f"Markup: {markup:.2f}%")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
```
