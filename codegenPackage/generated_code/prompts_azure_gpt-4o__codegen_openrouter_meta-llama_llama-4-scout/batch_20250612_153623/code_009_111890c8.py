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
# financial_plan.py

class FinancialPlan:
    def __init__(self, income, debts=None):
        """
        Initialize a FinancialPlan object.

        Args:
        - income (float): The user's monthly gross income.
        - debts (list of dict, optional): A list of debts with 'name', 'monthly_payment' keys. Defaults to None.
        """
        self.income = income
        self.debts = debts if debts is not None else []

    def calculate_debt_to_income_ratio(self):
        """
        Calculate the debt-to-income ratio.

        Returns:
        - float: The debt-to-income ratio.
        """
        total_monthly_debt = sum(debt['monthly_payment'] for debt in self.debts)
        if self.income == 0:
            raise ValueError("Income cannot be zero")
        return (total_monthly_debt / self.income) * 100

    def should_proceed_with_loan_application(self):
        """
        Suggest whether the user should proceed with a loan application based on the debt-to-income ratio.

        Returns:
        - bool: Whether the user should proceed with a loan application.
        """
        debt_to_income_ratio = self.calculate_debt_to_income_ratio()
        # General guideline: 36% or less is good, 37% to 43% is cautionary, and above 43% is risky
        return debt_to_income_ratio <= 36

    def add_debt(self, name, monthly_payment):
        """
        Add a debt to the financial plan.

        Args:
        - name (str): The name of the debt.
        - monthly_payment (float): The monthly payment of the debt.
        """
        self.debts.append({'name': name, 'monthly_payment': monthly_payment})

    def __str__(self):
        """
        Return a string representation of the financial plan.

        Returns:
        - str: A string representation of the financial plan.
        """
        debts_str = '\n'.join(f"- {debt['name']}: ${debt['monthly_payment']:.2f}" for debt in self.debts)
        return f"Income: ${self.income:.2f}\nDebts:\n{debts_str}\nDebt-to-Income Ratio: {self.calculate_debt_to_income_ratio():.2f}%"


def main():
    try:
        income = float(input("Enter your monthly gross income: $"))
        financial_plan = FinancialPlan(income)

        while True:
            print("\nOptions:")
            print("1. Add debt")
            print("2. Calculate debt-to-income ratio and suggest loan application")
            print("3. Exit")
            option = input("Choose an option: ")

            if option == "1":
                name = input("Enter debt name: ")
                monthly_payment = float(input("Enter monthly payment: $"))
                financial_plan.add_debt(name, monthly_payment)
                print(financial_plan)
            elif option == "2":
                print(financial_plan)
                if financial_plan.should_proceed_with_loan_application():
                    print("Based on your debt-to-income ratio, it is recommended to proceed with the loan application.")
                else:
                    print("Based on your debt-to-income ratio, it is not recommended to proceed with the loan application.")
            elif option == "3":
                break
            else:
                print("Invalid option. Please choose a valid option.")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
