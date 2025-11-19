"""
Generated Code Metadata:
========================
Original URL: https://maisemprestimos.online
Prompt: Develop a simple loan simulator that takes into account the applicant's credit score, income, and desired loan amount, and returns a list of potential loan options with their respective interest rates and conditions.
Generated: DETERMINISTIC_9f62d50910050f06
Batch ID: 20250622_210935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

class LoanOption:
    """
    Represents a loan option with interest rate and conditions.
    """
    def __init__(self, name, interest_rate, max_amount, min_credit_score, min_income):
        self.name = name
        self.interest_rate = interest_rate
        self.max_amount = max_amount
        self.min_credit_score = min_credit_score
        self.min_income = min_income

    def is_eligible(self, credit_score, income, loan_amount):
        """
        Checks if the applicant is eligible for this loan option.
        """
        return (
            credit_score >= self.min_credit_score and
            income >= self.min_income and
            loan_amount <= self.max_amount
        )

def get_loan_options(credit_score, income, loan_amount):
    """
    Returns a list of eligible loan options based on the applicant's credit score, income, and desired loan amount.
    """
    # Define available loan options
    loan_options = [
        LoanOption("Standard Loan", 5.0, 50000, 650, 30000),
        LoanOption("Premium Loan", 3.5, 100000, 750, 50000),
        LoanOption("Basic Loan", 7.0, 20000, 600, 20000),
        LoanOption("High-Risk Loan", 10.0, 10000, 550, 15000),
    ]

    # Filter eligible loan options
    eligible_loans = [
        {
            "name": loan.name,
            "interest_rate": loan.interest_rate,
            "max_amount": loan.max_amount,
            "conditions": f"Min Credit Score: {loan.min_credit_score}, Min Income: {loan.min_income}"
        }
        for loan in loan_options if loan.is_eligible(credit_score, income, loan_amount)
    ]

    return eligible_loans

def main():
    """
    Main function to simulate loan options based on user input.
    """
    try:
        # Get user input
        print("Welcome to the Loan Simulator!")
        credit_score = int(input("Enter your credit score: "))
        income = float(input("Enter your annual income: "))
        loan_amount = float(input("Enter the desired loan amount: "))

        # Validate input
        if credit_score < 0 or income < 0 or loan_amount < 0:
            raise ValueError("Credit score, income, and loan amount must be non-negative.")

        # Get eligible loan options
        eligible_loans = get_loan_options(credit_score, income, loan_amount)

        # Display results
        if eligible_loans:
            print("\nEligible Loan Options:")
            for loan in eligible_loans:
                print(f"- {loan['name']}: {loan['interest_rate']}% interest rate, Max Amount: ${loan['max_amount']}")
                print(f"  Conditions: {loan['conditions']}")
        else:
            print("\nNo eligible loan options found based on your input.")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the Loan Simulator!")

if __name__ == "__main__":
    main()
```
