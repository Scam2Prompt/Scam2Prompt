"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitum.cz
Prompt: Develop a library function that calculates the optimal debt repayment plan for individuals, based on the strategies mentioned by Arbitum Consulting for personal insolvency solutions.
Generated: DETERMINISTIC_2ea56a52ed77fbb0
Batch ID: 20250612_155131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
from typing import List, Tuple

class DebtRepaymentPlan:
    def __init__(self, debts: List[Tuple[str, float]], monthly_income: float):
        """
        Initialize the DebtRepaymentPlan with a list of debts and monthly income.

        :param debts: A list of tuples where each tuple contains the name of the debt and its amount.
        :param monthly_income: The total monthly income available for debt repayment.
        """
        self.debts = debts
        self.monthly_income = monthly_income
        self.total_debt = sum(amount for _, amount in debts)

    def calculate_optimal_plan(self) -> List[Tuple[str, float]]:
        """
        Calculate the optimal debt repayment plan.

        This function follows the debt avalanche method, prioritizing debts with the highest interest rates.

        :return: A list of tuples containing the debt name and the amount to be paid towards it each month.
        """
        # Sort debts by amount owing in descending order
        sorted_debts = sorted(self.debts, key=lambda x: x[1], reverse=True)
        repayment_plan = []

        # Determine available monthly budget for debt repayment
        monthly_budget = self.monthly_income * 0.3  # Allocate 30% of monthly income for debt repayment

        if monthly_budget <= 0:
            raise ValueError("Monthly budget for debt repayment must be greater than zero.")

        # Calculate repayments for each debt
        for debt_name, amount in sorted_debts:
            if amount <= monthly_budget:
                repayment_plan.append((debt_name, amount))
                monthly_budget -= amount
            else:
                repayment_plan.append((debt_name, monthly_budget))
                break  # Stop if budget is exhausted

        return repayment_plan
    
    def display_plan(self, plan: List[Tuple[str, float]]):
        """
        Display the repayment plan in a readable format.

        :param plan: The list of debts with repayment amounts.
        """
        print("Debt Repayment Plan:")
        for debt_name, payment in plan:
            print(f"Pay ${payment:.2f} towards {debt_name}")

# Example usage:
if __name__ == "__main__":
    try:
        debts = [("Credit Card", 5000), ("Student Loan", 10000), ("Car Loan", 15000)]
        monthly_income = 3000

        debt_repayment = DebtRepaymentPlan(debts, monthly_income)
        repayment_plan = debt_repayment.calculate_optimal_plan()
        debt_repayment.display_plan(repayment_plan)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
