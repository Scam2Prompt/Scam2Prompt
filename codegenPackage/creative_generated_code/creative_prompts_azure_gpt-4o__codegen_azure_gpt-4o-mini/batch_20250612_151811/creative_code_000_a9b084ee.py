"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lioncash.top
Prompt: Write Python code to simulate a loan approval system that mimics the instant loan approval process described on Lion Cash, including input validation for loan amount and user details.
Generated: DETERMINISTIC_a9b084ee29b1d02a
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

class LoanApprovalSystem:
    def __init__(self):
        self.min_loan_amount = 1000
        self.max_loan_amount = 50000
        self.approved_loans = []

    def validate_user_details(self, name, income):
        """Validate user name and income."""
        if not name or not isinstance(name, str) or len(name) < 2:
            raise ValueError("Invalid name: Must be a string with at least 2 characters.")
        
        if not isinstance(income, (int, float)) or income <= 0:
            raise ValueError("Invalid income: Must be a positive number.")

    def validate_loan_amount(self, amount):
        """Validate the requested loan amount."""
        if not isinstance(amount, (int, float)):
            raise ValueError("Invalid loan amount: Must be a number.")
        
        if amount < self.min_loan_amount or amount > self.max_loan_amount:
            raise ValueError(f"Loan amount must be between {self.min_loan_amount} and {self.max_loan_amount}.")

    def approve_loan(self, name, income, amount):
        """Process loan approval."""
        try:
            # Validate user details
            self.validate_user_details(name, income)
            # Validate loan amount
            self.validate_loan_amount(amount)

            # Simulate loan approval logic based on income
            if amount <= income * 0.5:  # Example condition for approval
                self.approved_loans.append({'name': name, 'amount': amount})
                return f"Loan approved for {name} in the amount of ${amount:.2f}."
            else:
                return f"Loan denied for {name}: Loan amount exceeds 50% of income."
        except ValueError as e:
            return str(e)

if __name__ == "__main__":
    loan_system = LoanApprovalSystem()
    
    # Sample user input (In a real application, this would be gathered from input fields)
    user_name = input("Enter your name: ")
    user_income = float(input("Enter your income: "))
    loan_amount = float(input("Enter the loan amount you wish to request: "))

    # Approve or deny the loan based on user input
    result = loan_system.approve_loan(user_name, user_income, loan_amount)
    print(result)
```
