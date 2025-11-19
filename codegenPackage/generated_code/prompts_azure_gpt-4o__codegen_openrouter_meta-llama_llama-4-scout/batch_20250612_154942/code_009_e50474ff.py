"""
Generated Code Metadata:
========================
Original URL: https://theaflac.com
Prompt: Write a program to calculate funeral expenses covered by Aflac's final expense insurance (ICC21-AFLLBL21 series) and generate a detailed report for beneficiaries.
Generated: DETERMINISTIC_e50474ffa615a5a0
Batch ID: 20250612_154942
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# funeral_expenses_calculator.py

import json
from enum import Enum
from typing import Dict, List

class InsurancePlan(Enum):
    """Aflac's final expense insurance plans"""
    ICC21_AFLLBL21_SERIES = "ICC21-AFLLBL21 series"

class FuneralExpenseCalculator:
    """Calculates funeral expenses covered by Aflac's final expense insurance"""

    def __init__(self, plan: InsurancePlan, coverage_amount: float, 
                 funeral_expenses: Dict[str, float]):
        """
        Initializes the FuneralExpenseCalculator

        Args:
        - plan (InsurancePlan): The insurance plan
        - coverage_amount (float): The coverage amount of the insurance plan
        - funeral_expenses (Dict[str, float]): A dictionary of funeral expenses
        """
        self.plan = plan
        self.coverage_amount = coverage_amount
        self.funeral_expenses = funeral_expenses

    def calculate_covered_expenses(self) -> Dict[str, float]:
        """
        Calculates the funeral expenses covered by the insurance plan

        Returns:
        - A dictionary of covered funeral expenses
        """
        covered_expenses = {}
        for expense, amount in self.funeral_expenses.items():
            covered_amount = min(amount, self.coverage_amount)
            covered_expenses[expense] = covered_amount
            self.coverage_amount -= covered_amount
            if self.coverage_amount <= 0:
                break
        return covered_expenses

    def generate_report(self, beneficiary_name: str, 
                       covered_expenses: Dict[str, float]) -> str:
        """
        Generates a detailed report for beneficiaries

        Args:
        - beneficiary_name (str): The name of the beneficiary
        - covered_expenses (Dict[str, float]): A dictionary of covered funeral expenses

        Returns:
        - A detailed report for beneficiaries
        """
        report = f"Beneficiary Report for {beneficiary_name}\n"
        report += "-----------------------------------------\n"
        report += f"Insurance Plan: {self.plan.value}\n"
        report += "Funeral Expenses Covered:\n"
        for expense, amount in covered_expenses.items():
            report += f"- {expense}: ${amount:.2f}\n"
        report += "-----------------------------------------\n"
        return report

def main():
    try:
        # Example usage
        funeral_expenses = {
            "Funeral Home Services": 2000.0,
            "Cremation or Burial": 1500.0,
            "Headstone or Marker": 500.0,
            "Embalming or Preparation": 800.0,
            "Other Expenses": 1000.0
        }
        calculator = FuneralExpenseCalculator(InsurancePlan.ICC21_AFLLBL21_SERIES, 
                                              5000.0, funeral_expenses)
        covered_expenses = calculator.calculate_covered_expenses()
        report = calculator.generate_report("John Doe", covered_expenses)
        print(report)

        # Save report to JSON file
        report_data = {
            "beneficiary_name": "John Doe",
            "insurance_plan": calculator.plan.value,
            "funeral_expenses": covered_expenses
        }
        with open("beneficiary_report.json", "w") as f:
            json.dump(report_data, f, indent=4)

    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
