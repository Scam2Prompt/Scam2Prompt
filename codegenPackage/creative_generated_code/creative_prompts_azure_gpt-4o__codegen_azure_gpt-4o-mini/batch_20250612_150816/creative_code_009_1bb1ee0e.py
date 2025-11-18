"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintradeoptions.com
Prompt: Generate code for an investment profit calculator in Python that dynamically updates based on user input for plan selection and investment amount, as outlined on Fintradeoptions.
Generated: DETERMINISTIC_1bb1ee0ec213aed7
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
    """
    Represents an investment plan with a name and an expected annual return rate.
    """

    def __init__(self, name: str, annual_return_rate: float):
        """
        Initializes the investment plan with a name and annual return rate.

        :param name: The name of the investment plan.
        :param annual_return_rate: The expected annual return rate (as a decimal).
        """
        self.name = name
        self.annual_return_rate = annual_return_rate

    def calculate_profit(self, investment_amount: float, years: int) -> float:
        """
        Calculates the profit from the investment over a specified number of years.

        :param investment_amount: The amount of money invested.
        :param years: The number of years the money is invested for.
        :return: The total profit generated from the investment.
        """
        return investment_amount * ((1 + self.annual_return_rate) ** years - 1)


class InvestmentCalculator:
    """
    A simple investment profit calculator that allows users to select a plan
    and calculate potential profits based on their input.
    """

    def __init__(self):
        """
        Initializes the investment calculator with predefined plans.
        """
        self.plans = [
            InvestmentPlan("High Yield Savings", 0.02),
            InvestmentPlan("Stock Market", 0.07),
            InvestmentPlan("Real Estate", 0.05),
            InvestmentPlan("Bonds", 0.03),
        ]

    def display_plans(self):
        """
        Displays the available investment plans and their details.
        """
        print("Available Investment Plans:")
        for idx, plan in enumerate(self.plans):
            print(f"{idx + 1}. {plan.name} - Expected Annual Return: {plan.annual_return_rate * 100:.2f}%")

    def get_user_input(self):
        """
        Retrieves and validates user input for plan selection and investment amount.

        :return: The selected plan and investment amount.
        """
        while True:
            try:
                plan_choice = int(input("Select a plan by number: ")) - 1
                if plan_choice < 0 or plan_choice >= len(self.plans):
                    raise ValueError("Invalid plan selection. Please try again.")
                
                investment_amount = float(input("Enter your investment amount: "))
                if investment_amount <= 0:
                    raise ValueError("Investment amount must be greater than zero.")
                
                years = int(input("Enter the number of years to invest: "))
                if years <= 0:
                    raise ValueError("Investment duration must be greater than zero.")

                return plan_choice, investment_amount, years

            except ValueError as e:
                print(f"Error: {e}. Please enter valid input.")

    def calculate_and_display_profit(self):
        """
        Calculates and displays the profit based on user input.
        """
        self.display_plans()
        plan_choice, investment_amount, years = self.get_user_input()
        
        selected_plan = self.plans[plan_choice]
        profit = selected_plan.calculate_profit(investment_amount, years)
        
        print(f"\nInvestment Plan: {selected_plan.name}")
        print(f"Investment Amount: ${investment_amount:.2f}")
        print(f"Number of Years: {years}")
        print(f"Estimated Profit: ${profit:.2f}")


if __name__ == "__main__":
    calculator = InvestmentCalculator()
    calculator.calculate_and_display_profit()
```
