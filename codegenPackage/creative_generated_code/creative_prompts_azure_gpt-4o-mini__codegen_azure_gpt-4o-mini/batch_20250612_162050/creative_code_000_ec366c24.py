"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tsmwealth.co.za
Prompt: Generate a code snippet for a financial planning tool that incorporates long-term insurance and investment strategies as outlined by TSM Wealth.
Generated: DETERMINISTIC_ec366c24dcf81f9c
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Union

class FinancialPlan:
    """Class to represent a financial plan with insurance and investment strategies."""
    
    def __init__(self, name: str):
        self.name = name
        self.insurance_strategies: List[Dict[str, Union[str, float]]] = []
        self.investment_strategies: List[Dict[str, Union[str, float]]] = []

    def add_insurance_strategy(self, strategy_name: str, coverage_amount: float) -> None:
        """Add an insurance strategy to the financial plan."""
        if coverage_amount <= 0:
            raise ValueError("Coverage amount must be greater than zero.")
        
        self.insurance_strategies.append({
            "strategy_name": strategy_name,
            "coverage_amount": coverage_amount
        })

    def add_investment_strategy(self, strategy_name: str, investment_amount: float) -> None:
        """Add an investment strategy to the financial plan."""
        if investment_amount <= 0:
            raise ValueError("Investment amount must be greater than zero.")
        
        self.investment_strategies.append({
            "strategy_name": strategy_name,
            "investment_amount": investment_amount
        })

    def generate_plan_summary(self) -> Dict[str, Union[str, List[Dict[str, Union[str, float]]]]]:
        """Generate a summary of the financial plan."""
        return {
            "name": self.name,
            "insurance_strategies": self.insurance_strategies,
            "investment_strategies": self.investment_strategies
        }

    def save_plan_to_file(self, filename: str) -> None:
        """Save the financial plan to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_plan_summary(), file, indent=4)
        except IOError as e:
            raise Exception(f"An error occurred while saving the file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        my_financial_plan = FinancialPlan("John Doe's Financial Future")
        my_financial_plan.add_insurance_strategy("Whole Life Insurance", 500000)
        my_financial_plan.add_investment_strategy("Index Fund", 10000)
        
        print("Financial Plan Summary:")
        print(json.dumps(my_financial_plan.generate_plan_summary(), indent=4))

        # Save the financial plan to a file
        my_financial_plan.save_plan_to_file("financial_plan.json")

    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")
```
