"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Create a program that estimates loan eligibility based on income, similar to the Loan Eligibility Estimator tool mentioned on the IFSC Finder website.
Generated: DETERMINISTIC_9971b119ac284c41
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoanEligibilityEstimator:
    """
    A class to estimate loan eligibility based on the user's income and 
    other factors such as monthly expenses and credit score.
    """

    def __init__(self, monthly_income, monthly_expenses, credit_score):
        """
        Initializes the LoanEligibilityEstimator with the user's details.

        Parameters:
        monthly_income (float): The user's monthly income.
        monthly_expenses (float): The user's monthly expenses.
        credit_score (int): The user's credit score (0-850).
        """
        self.monthly_income = monthly_income
        self.monthly_expenses = monthly_expenses
        self.credit_score = credit_score

    def _validate_inputs(self):
        """
        Validates the input values to ensure they are within acceptable ranges.

        Raises:
        ValueError: If any input value is invalid.
        """
        if self.monthly_income < 0:
            raise ValueError("Monthly income must be a non-negative value.")
        if self.monthly_expenses < 0:
            raise ValueError("Monthly expenses must be a non-negative value.")
        if not (0 <= self.credit_score <= 850):
            raise ValueError("Credit score must be between 0 and 850.")

    def estimate_loan_amount(self):
        """
        Estimates the loan amount based on income, expenses and credit score.

        Returns:
        float: Estimated loan amount in dollars.
        """
        self._validate_inputs()
        
        # Calculate disposable income
        disposable_income = self.monthly_income - self.monthly_expenses
        
        # Base loan amount estimate based on disposable income
        if disposable_income <= 0:
            return 0.0  # No loan eligibility if there are no disposable funds
        
        # Maximum loan estimation logic
        base_loan_amount = disposable_income * 12 * 5  # 5 years worth of disposable income
        
        # Adjust based on credit score
        if self.credit_score < 600:
            loan_factor = 0.5  # Lower factor for low credit score
        elif self.credit_score < 700:
            loan_factor = 0.75  # Moderate factor for average credit score
        else:
            loan_factor = 1.0  # Full base amount for good credit score

        estimated_loan = base_loan_amount * loan_factor
        return round(estimated_loan, 2)  # Round to 2 decimal places

def main():
    """
    Main function to run the loan eligibility estimator.
    """
    try:
        # Example user input
        monthly_income = float(input("Enter your monthly income: "))
        monthly_expenses = float(input("Enter your monthly expenses: "))
        credit_score = int(input("Enter your credit score (0-850): "))

        estimator = LoanEligibilityEstimator(monthly_income, monthly_expenses, credit_score)
        estimated_loan_amount = estimator.estimate_loan_amount()

        print(f"Your estimated loan eligibility is: ${estimated_loan_amount}")
    
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
