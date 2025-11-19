"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Generate a code snippet for a financial planning tool that incorporates long-term insurance and investment strategies as outlined by TSM Wealth.
Generated: DETERMINISTIC_ec366c24dcf81f9c
Batch ID: 20250612_162050
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

class FinancialPlanningTool:
    def __init__(self):
        """Initialize the financial planning tool with default strategies."""
        self.insurance_strategies = []
        self.investment_strategies = []

    def add_insurance_strategy(self, strategy: Dict[str, Any]) -> None:
        """
        Add a long-term insurance strategy to the tool.

        Args:
            strategy (Dict[str, Any]): A dictionary containing insurance strategy details.
        """
        self.insurance_strategies.append(strategy)

    def add_investment_strategy(self, strategy: Dict[str, Any]) -> None:
        """
        Add an investment strategy to the tool.

        Args:
            strategy (Dict[str, Any]): A dictionary containing investment strategy details.
        """
        self.investment_strategies.append(strategy)

    def generate_plan(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Generate a comprehensive financial plan.

        Returns:
            Dict[str, List[Dict[str, Any]]]: A dictionary containing insurance and investment strategies.
        """
        return {
            "insurance_strategies": self.insurance_strategies,
            "investment_strategies": self.investment_strategies
        }

    def save_plan_to_file(self, filename: str) -> None:
        """
        Save the financial plan to a JSON file.

        Args:
            filename (str): The name of the file to save the plan to.

        Raises:
            IOError: If there is an error writing to the file.
        """
        plan = self.generate_plan()
        try:
            with open(filename, 'w') as file:
                json.dump(plan, file, indent=4)
        except IOError as e:
            print(f"Error saving plan to file: {e}")

# Example usage
if __name__ == "__main__":
    tool = FinancialPlanningTool()

    # Adding long-term insurance strategies
    tool.add_insurance_strategy({
        "type": "Life Insurance",
        "coverage_amount": 500000,
        "term": "30 years"
    })

    # Adding investment strategies
    tool.add_investment_strategy({
        "type": "Retirement Fund",
        "monthly_contribution": 500,
        "expected_return": 0.07
    })

    # Generate and save the financial plan
    tool.save_plan_to_file("financial_plan.json")
```
