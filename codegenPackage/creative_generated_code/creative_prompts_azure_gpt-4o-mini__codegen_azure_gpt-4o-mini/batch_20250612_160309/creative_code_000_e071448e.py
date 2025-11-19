"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sabkafuture.com
Prompt: Generate a Python script that calculates potential returns based on the investment plans offered by Sabka Future, including the MINI, BASIC, and GOLD plans.
Generated: DETERMINISTIC_e071448e997f389e
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# investment_calculator.py

class InvestmentPlan:
    """
    A base class to represent an investment plan.
    """
    def __init__(self, name, principal, rate_of_return, duration):
        """
        Initialize an investment plan.

        :param name: Name of the investment plan
        :param principal: The initial amount invested
        :param rate_of_return: The annual rate of return (as a decimal)
        :param duration: The duration of the investment in years
        """
        self.name = name
        self.principal = principal
        self.rate_of_return = rate_of_return
        self.duration = duration

    def calculate_return(self):
        """
        Calculate the potential return on investment.

        :return: The total value after the duration
        """
        try:
            total_value = self.principal * ((1 + self.rate_of_return) ** self.duration)
            return total_value
        except Exception as e:
            print(f"Error calculating return for {self.name}: {e}")
            return None


class InvestmentCalculator:
    """
    A class to manage multiple investment plans.
    """
    def __init__(self):
        """
        Initialize the investment calculator with an empty list of plans.
        """
        self.plans = []

    def add_plan(self, plan):
        """
        Add an investment plan to the calculator.

        :param plan: An instance of InvestmentPlan
        """
        if isinstance(plan, InvestmentPlan):
            self.plans.append(plan)
        else:
            print("Error: The provided plan is not an instance of InvestmentPlan.")

    def calculate_all_returns(self):
        """
        Calculate returns for all added investment plans.

        :return: A dictionary of plan names and their corresponding returns
        """
        returns = {}
        for plan in self.plans:
            returns[plan.name] = plan.calculate_return()
        return returns


def main():
    """
    Main function to run the investment calculator.
    """
    # Create an instance of the InvestmentCalculator
    calculator = InvestmentCalculator()

    # Define investment plans
    mini_plan = InvestmentPlan(name="MINI", principal=1000, rate_of_return=0.05, duration=1)
    basic_plan = InvestmentPlan(name="BASIC", principal=5000, rate_of_return=0.07, duration=3)
    gold_plan = InvestmentPlan(name="GOLD", principal=20000, rate_of_return=0.10, duration=5)

    # Add plans to the calculator
    calculator.add_plan(mini_plan)
    calculator.add_plan(basic_plan)
    calculator.add_plan(gold_plan)

    # Calculate and display potential returns
    potential_returns = calculator.calculate_all_returns()
    
    print("Potential Returns on Investment Plans:")
    for plan_name, return_value in potential_returns.items():
        if return_value is not None:
            print(f"{plan_name}: ${return_value:.2f}")
        else:
            print(f"{plan_name}: Calculation failed.")


if __name__ == "__main__":
    main()
```
