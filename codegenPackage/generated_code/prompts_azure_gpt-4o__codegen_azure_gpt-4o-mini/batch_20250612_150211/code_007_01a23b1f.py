"""
Generated Code Metadata:
========================
Original URL: https://bitinvestcoin.com
Prompt: Create a Python program to model tailored investment plans for cryptocurrency investors, including options for low-risk entry, accelerated growth, and retirement planning, inspired by BitInvestCoin.
Generated: DETERMINISTIC_01a23b1f3cd49368
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class InvestmentPlan:
    """
    A class to represent an investment plan for cryptocurrency investors.
    """

    def __init__(self, name: str, risk_level: str, expected_return: float, duration_years: int):
        """
        Initializes an InvestmentPlan instance.

        :param name: Name of the investment plan.
        :param risk_level: Risk level of the investment (e.g., low, medium, high).
        :param expected_return: Expected return on investment as a percentage.
        :param duration_years: Duration of the investment in years.
        """
        self.name = name
        self.risk_level = risk_level
        self.expected_return = expected_return
        self.duration_years = duration_years

    def calculate_future_value(self, initial_investment: float) -> float:
        """
        Calculates the future value of the investment.

        :param initial_investment: The initial amount invested.
        :return: The future value of the investment.
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative value.")
        
        future_value = initial_investment * (1 + self.expected_return / 100) ** self.duration_years
        return future_value

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the investment plan to a dictionary.

        :return: A dictionary representation of the investment plan.
        """
        return {
            "name": self.name,
            "risk_level": self.risk_level,
            "expected_return": self.expected_return,
            "duration_years": self.duration_years
        }


class InvestmentPortfolio:
    """
    A class to manage a portfolio of investment plans.
    """

    def __init__(self):
        """
        Initializes an empty investment portfolio.
        """
        self.plans: List[InvestmentPlan] = []

    def add_plan(self, plan: InvestmentPlan):
        """
        Adds an investment plan to the portfolio.

        :param plan: An instance of InvestmentPlan to add.
        """
        self.plans.append(plan)

    def calculate_total_future_value(self, initial_investment: float) -> float:
        """
        Calculates the total future value of all investment plans in the portfolio.

        :param initial_investment: The initial amount invested in each plan.
        :return: The total future value of the portfolio.
        """
        total_value = 0
        for plan in self.plans:
            total_value += plan.calculate_future_value(initial_investment)
        return total_value

    def export_to_json(self, file_path: str):
        """
        Exports the investment portfolio to a JSON file.

        :param file_path: The path to the file where the portfolio will be saved.
        """
        try:
            with open(file_path, 'w') as json_file:
                json.dump([plan.to_dict() for plan in self.plans], json_file, indent=4)
        except IOError as e:
            print(f"Error writing to file {file_path}: {e}")


def main():
    """
    Main function to demonstrate the investment plans and portfolio management.
    """
    # Create investment plans
    low_risk_plan = InvestmentPlan("Low-Risk Entry", "Low", 5.0, 5)
    accelerated_growth_plan = InvestmentPlan("Accelerated Growth", "Medium", 15.0, 10)
    retirement_plan = InvestmentPlan("Retirement Planning", "High", 25.0, 20)

    # Create an investment portfolio and add plans
    portfolio = InvestmentPortfolio()
    portfolio.add_plan(low_risk_plan)
    portfolio.add_plan(accelerated_growth_plan)
    portfolio.add_plan(retirement_plan)

    # Calculate total future value for an initial investment of $10,000
    initial_investment = 10000
    total_future_value = portfolio.calculate_total_future_value(initial_investment)
    print(f"Total future value of the portfolio: ${total_future_value:.2f}")

    # Export portfolio to JSON
    portfolio.export_to_json("investment_portfolio.json")


if __name__ == "__main__":
    main()
```
