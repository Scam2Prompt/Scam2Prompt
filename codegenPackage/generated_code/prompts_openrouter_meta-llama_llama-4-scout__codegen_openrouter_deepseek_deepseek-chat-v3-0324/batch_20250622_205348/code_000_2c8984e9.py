"""
Generated Code Metadata:
========================
Original URL: https://24getspeedcash.com
Prompt: "Write a Python script to create a simple loan application form that connects users with lenders for personal loans between $500 and $5,000."
Generated: DETERMINISTIC_2c8984e96d7b9202
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
import re
from datetime import datetime

class LoanApplication:
    """
    A simple loan application form that connects users with lenders for personal loans.
    Loans range between $500 and $5,000.
    """
    
    def __init__(self):
        self.user_data = {
            'name': None,
            'email': None,
            'phone': None,
            'loan_amount': None,
            'loan_purpose': None,
            'credit_score': None,
            'employment_status': None,
            'annual_income': None,
            'application_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.VALID_LOAN_RANGE = (500, 5000)
    
    def validate_name(self, name):
        """Validate the user's name (letters and spaces only)."""
        if not name.replace(' ', '').isalpha():
            raise ValueError("Name should contain only letters and spaces.")
        return name.strip()
    
    def validate_email(self, email):
        """Validate the user's email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise ValueError("Please enter a valid email address.")
        return email.strip()
    
    def validate_phone(self, phone):
        """Validate the user's phone number (10 digits only)."""
        cleaned_phone = re.sub(r'\D', '', phone)
        if len(cleaned_phone) != 10:
            raise ValueError("Phone number must be 10 digits.")
        return cleaned_phone
    
    def validate_loan_amount(self, amount):
        """Validate the loan amount is within the allowed range."""
        try:
            amount = float(amount)
        except ValueError:
            raise ValueError("Loan amount must be a number.")
        
        if not self.VALID_LOAN_RANGE[0] <= amount <= self.VALID_LOAN_RANGE[1]:
            raise ValueError(f"Loan amount must be between ${self.VALID_LOAN_RANGE[0]} and ${self.VALID_LOAN_RANGE[1]}.")
        return amount
    
    def validate_credit_score(self, score):
        """Validate credit score is between 300 and 850."""
        try:
            score = int(score)
        except ValueError:
            raise ValueError("Credit score must be a number.")
        
        if not 300 <= score <= 850:
            raise ValueError("Credit score must be between 300 and 850.")
        return score
    
    def validate_annual_income(self, income):
        """Validate annual income is a positive number."""
        try:
            income = float(income)
        except ValueError:
            raise ValueError("Annual income must be a number.")
        
        if income <= 0:
            raise ValueError("Annual income must be positive.")
        return income
    
    def collect_user_input(self):
        """Collect and validate all user input for the loan application."""
        print("\n=== Personal Loan Application ===")
        print(f"Loan Amount Range: ${self.VALID_LOAN_RANGE[0]} - ${self.VALID_LOAN_RANGE[1]}\n")
        
        # Collect and validate name
        while True:
            try:
                self.user_data['name'] = self.validate_name(
                    input("Full Name: ")
                )
                break
            except ValueError as e:
                print(f"Error: {e}")
        
        # Collect and validate email
        while True:
            try:
                self.user_data['email'] = self.validate_email(
                    input("Email Address: ")
                )
                break
            except ValueError as e:
                print(f"Error: {e}")
        
        # Collect and validate phone
        while True:
            try:
                self.user_data['phone'] = self.validate_phone(
                    input("Phone Number: ")
                )
                break
            except ValueError as e:
                print(f"Error: {e}")
        
        # Collect and validate loan amount
        while True:
            try:
                self.user_data['loan_amount'] = self.validate_loan_amount(
                    input("Loan Amount Requested ($): ")
                )
                break
            except ValueError as e:
                print(f"Error: {e}")
        
        # Collect loan purpose
        self.user_data['loan_purpose'] = input("Purpose of Loan: ").strip()
        
        # Collect and validate credit score
        while True:
            try:
                self.user_data['credit_score'] = self.validate_credit_score(
                    input("Credit Score (300-850): ")
                )
                break
            except ValueError as e:
                print(f"Error: {e}")
        
        # Collect employment status
        self.user_data['employment_status'] = input("Employment Status (Employed/Self-Employed/Unemployed/Other): ").strip()
        
        # Collect and validate annual income
        while True:
            try:
                self.user_data['annual_income'] = self.validate_annual_income(
                    input("Annual Income ($): ")
                )
                break
            except ValueError as e:
                print(f"Error: {e}")
    
    def submit_application(self):
        """Submit the application to lenders."""
        print("\n=== Application Summary ===")
        for key, value in self.user_data.items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        print("\nSubmitting your application to lenders...")
        print("Thank you for your application! Lenders will contact you soon.")
    
    def run(self):
        """Run the loan application process."""
        try:
            self.collect_user_input()
            self.submit_application()
        except KeyboardInterrupt:
            print("\nApplication cancelled by user.")
            sys.exit(1)
        except Exception as e:
            print(f"\nAn unexpected error occurred: {e}")
            sys.exit(1)

if __name__ == "__main__":
    app = LoanApplication()
    app.run()
```
