"""
Generated Code Metadata:
========================
Original URL: https://maisemprestimos.online
Prompt: Develop a Python program that helps users create a financial plan, including calculating their debt-to-income ratio and suggesting whether they should proceed with a loan application based on the guidelines provided in the guide.
Generated: DETERMINISTIC_111890c8e59150ee
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class FinancialPlan:
    """
    A class to represent a financial plan for an individual.
    It includes methods to calculate debt-to-income ratio and
    evaluate loan application eligibility.
    """

    def __init__(self, monthly_income, monthly_debts):
        """
        Initializes the FinancialPlan with monthly income and debts.

        :param monthly_income: float, the total monthly income of the user
        :param monthly_debts: float, the total monthly debt payments of the user
        """
        self.monthly_income = monthly_income
        self.monthly_debts = monthly_debts

    def calculate_debt_to_income_ratio(self):
        """
        Calculates the debt-to-income (DTI) ratio.

        :return: float, the DTI ratio as a percentage
        :raises ValueError: if monthly_income is zero or negative
        """
        if self.monthly_income <= 0:
            raise ValueError("Monthly income must be greater than zero.")

        dti_ratio = (self.monthly_debts / self.monthly_income) * 100
        return dti_ratio

    def evaluate_loan_application(self):
        """
        Evaluates whether the user should proceed with a loan application
        based on the DTI ratio.

        :return: str, recommendation on loan application
        """
        try:
            dti_ratio = self.calculate_debt_to_income_ratio()
            if dti_ratio < 36:
                return "You are in a good position to apply for a loan."
            elif 36 <= dti_ratio < 43:
                return "You may proceed with caution; consider your other financial obligations."
            else:
                return "It is advisable to improve your financial situation before applying for a loan."
        except ValueError as e:
            return str(e)

def main():
    """
    Main function to run the financial planning program.
    It collects user input and provides financial advice.
    """
    try:
        # Collect user input for monthly income and debts
        monthly_income = float(input("Enter your monthly income: "))
        monthly_debts = float(input("Enter your total monthly debts: "))

        # Create a FinancialPlan instance
        financial_plan = FinancialPlan(monthly_income, monthly_debts)

        # Calculate DTI and evaluate loan application
        dti_ratio = financial_plan.calculate_debt_to_income_ratio()
        recommendation = financial_plan.evaluate_loan_application()

        # Display results
        print(f"Your Debt-to-Income Ratio is: {dti_ratio:.2f}%")
        print(recommendation)

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
