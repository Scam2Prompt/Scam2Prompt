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
# debt_repayment.py

from typing import List, Dict

class DebtRepaymentPlan:
    """
    A library function to calculate the optimal debt repayment plan for individuals
    based on various repayment strategies.
    """

    def __init__(self, debts: List[Dict[str, float]], monthly_income: float):
        """
        Initializes the DebtRepaymentPlan instance.

        Args:
            debts: List of dictionaries containing debt information.
                   Each dictionary must have:
                       - 'name': Name of the debt (e.g., credit card, loan).
                       - 'balance': Remaining balance on the debt.
                       - 'interest_rate': Annual interest rate of the debt (as a percentage).
            monthly_income: Monthly income available for debt repayment.
        """
        self.debts = debts
        self.monthly_income = monthly_income

    def calculate_optimal_plan(self, strategy: str = "avalanche") -> List[Dict[str, float]]:
        """
        Calculates the optimal debt repayment plan based on the chosen strategy.

        Args:
            strategy: The repayment strategy to use. Options are:
                      - "avalanche": Pay off debts with the highest interest rate first.
                      - "snowball": Pay off debts with the smallest balance first.

        Returns:
            A list of dictionaries representing the repayment plan for each debt.
            Each dictionary contains:
                - 'name': Name of the debt.
                - 'total_paid': Total amount paid to clear the debt.
                - 'months_to_pay': Number of months taken to pay off the debt.
        """
        if strategy not in {"avalanche", "snowball"}:
            raise ValueError("Invalid strategy. Please choose either 'avalanche' or 'snowball'.")

        # Sort debts based on chosen strategy
        if strategy == "avalanche":
            sorted_debts = sorted(self.debts, key=lambda d: -d["interest_rate"])
        elif strategy == "snowball":
            sorted_debts = sorted(self.debts, key=lambda d: d["balance"])

        repayment_plan = []
        remaining_income = self.monthly_income

        for debt in sorted_debts:
            name = debt["name"]
            balance = debt["balance"]
            monthly_interest_rate = debt["interest_rate"] / 12 / 100
            months_to_pay = 0
            total_paid = 0

            # Calculate repayment period and total payment for each debt
            while balance > 0:
                interest = balance * monthly_interest_rate
                payment = min(remaining_income, balance + interest)
                balance -= payment - interest
                total_paid += payment
                months_to_pay += 1

            repayment_plan.append({
                "name": name,
                "total_paid": round(total_paid, 2),
                "months_to_pay": months_to_pay
            })

        return repayment_plan


# Example Usage:
if __name__ == "__main__":
    # Example debts
    debts = [
        {"name": "Credit Card A", "balance": 5000, "interest_rate": 18},
        {"name": "Car Loan", "balance": 15000, "interest_rate": 5},
        {"name": "Student Loan", "balance": 25000, "interest_rate": 3.5},
    ]

    monthly_income = 2000

    # Create DebtRepaymentPlan instance
    plan_calculator = DebtRepaymentPlan(debts, monthly_income)

    # Calculate repayment plan using Avalanche strategy
    avalanche_plan = plan_calculator.calculate_optimal_plan(strategy="avalanche")
    print("Avalanche Strategy Plan:", avalanche_plan)

    # Calculate repayment plan using Snowball strategy
    snowball_plan = plan_calculator.calculate_optimal_plan(strategy="snowball")
    print("Snowball Strategy Plan:", snowball_plan)
```
