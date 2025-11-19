"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marttrade.org
Prompt: How can I create an investment plan template based on the pricing structure provided by Lucidbrokers Investment?
Generated: DETERMINISTIC_28bfd1f0b428d107
Batch ID: 20250612_135324
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class InvestmentPlan:
    """
    A class to represent an investment plan based on the pricing structure from Lucidbrokers Investment.
    """

    def __init__(self, initial_investment: float, years: int, annual_return_rate: float):
        """
        Initialize the investment plan with the given parameters.

        :param initial_investment: The initial amount of money to invest
        :param years: The duration of the investment in years
        :param annual_return_rate: The expected annual return rate as a percentage
        """
        if initial_investment < 0:
            raise ValueError("Initial investment must be a non-negative number.")
        if years < 0:
            raise ValueError("Years must be a non-negative integer.")
        if annual_return_rate < 0:
            raise ValueError("Annual return rate must be a non-negative percentage.")

        self.initial_investment = initial_investment
        self.years = years
        self.annual_return_rate = annual_return_rate
        self.investments: List[Dict[str, Any]] = []

    def calculate_future_value(self) -> float:
        """
        Calculate the future value of the investment after a specified number of years.

        :return: The future value of the investment
        """
        future_value = self.initial_investment * (1 + self.annual_return_rate / 100) ** self.years
        return future_value

    def generate_investment_plan(self) -> None:
        """
        Generate an investment plan over the years and store it in the investments list.
        """
        for year in range(1, self.years + 1):
            future_value = self.initial_investment * (1 + self.annual_return_rate / 100) ** year
            self.investments.append({
                "year": year,
                "future_value": round(future_value, 2)
            })

    def export_to_json(self, filename: str) -> None:
        """
        Export the investment plan to a JSON file.

        :param filename: The name of the file to save the JSON data
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.investments, json_file, indent=4)
        except IOError as e:
            print(f"An error occurred while writing to file: {e}")

    def get_investment_summary(self) -> Dict[str, float]:
        """
        Get a summary of the investment plan.

        :return: A dictionary with the initial investment, years, annual return rate, and future value
        """
        future_value = self.calculate_future_value()
        return {
            "Initial Investment": self.initial_investment,
            "Years": self.years,
            "Annual Return Rate": self.annual_return_rate,
            "Future Value": round(future_value, 2)
        }


if __name__ == "__main__":
    try:
        # Example usage of the InvestmentPlan class
        investment_plan = InvestmentPlan(initial_investment=10000, years=10, annual_return_rate=5)
        investment_plan.generate_investment_plan()

        # Print investment summary
        summary = investment_plan.get_investment_summary()
        print("Investment Summary:", summary)

        # Export investment plan to JSON
        investment_plan.export_to_json("investment_plan.json")

    except ValueError as e:
        print(f"ValueError: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
