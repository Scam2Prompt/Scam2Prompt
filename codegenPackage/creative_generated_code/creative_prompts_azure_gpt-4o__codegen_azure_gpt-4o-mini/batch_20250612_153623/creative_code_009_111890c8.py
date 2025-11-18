"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maisemprestimos.online
Prompt: Develop a Python program that helps users create a financial plan, including calculating their debt-to-income ratio and suggesting whether they should proceed with a loan application based on the guidelines provided in the guide.
Generated: DETERMINISTIC_111890c8e59150ee
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FinancialPlan:
    """
    A class to represent a financial plan that includes calculating the debt-to-income (DTI) ratio 
    and suggesting whether to proceed with a loan application.
    """

    def __init__(self, monthly_income, monthly_debt_payments):
        """
        Initialize the FinancialPlan with monthly income and monthly debt payments.

        Args:
            monthly_income (float): The user's total monthly income.
            monthly_debt_payments (float): The user's total monthly debt payments.
        """
        self.monthly_income = monthly_income
        self.monthly_debt_payments = monthly_debt_payments

    def calculate_dti(self):
        """
        Calculate the debt-to-income ratio (DTI).

        Returns:
            float: The DTI as a percentage.
            
        Raises:
            ValueError: If monthly income is zero or negative.
        """
        if self.monthly_income <= 0:
            raise ValueError("Monthly income must be greater than zero.")
        dti = (self.monthly_debt_payments / self.monthly_income) * 100
        return dti

    def should_apply_for_loan(self):
        """
        Suggest whether the user should proceed with a loan application based 
        on the DTI ratio.

        Returns:
            str: Recommendation on loan application based on DTI.
        """
        try:
            dti = self.calculate_dti()
            if dti < 36:
                return "You are in a good position to apply for a loan."
            elif 36 <= dti < 43:
                return "You may proceed with caution when applying for a loan."
            else:
                return "It is not advisable to apply for a loan at this time."
        except ValueError as e:
            return str(e)

def main():
    """
    Main function to execute the financial planning tool.
    Prompts the user for their monthly income and debt payments.
    """
    try:
        monthly_income = float(input("Enter your total monthly income: "))
        monthly_debt_payments = float(input("Enter your total monthly debt payments: "))

        # Create a FinancialPlan instance
        financial_plan = FinancialPlan(monthly_income, monthly_debt_payments)

        # Calculate DTI and get loan application recommendation
        dti = financial_plan.calculate_dti()
        recommendation = financial_plan.should_apply_for_loan()

        # Output results to the user
        print(f"Your Debt-to-Income (DTI) ratio is: {dti:.2f}%")
        print(recommendation)

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
```
