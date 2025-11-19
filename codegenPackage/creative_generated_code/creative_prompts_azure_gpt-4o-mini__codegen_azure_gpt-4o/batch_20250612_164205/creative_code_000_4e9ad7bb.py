"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fin-flix.me
Prompt: Generate a code snippet that simulates an online application form for a credit service, including fields for customer number, date of birth, and desired loan amount.
Generated: DETERMINISTIC_4e9ad7bb8fed17fd
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
from datetime import datetime

def validate_customer_number(customer_number):
    """Validate customer number to ensure it is alphanumeric and 6-12 characters long."""
    if not re.match(r'^[a-zA-Z0-9]{6,12}$', customer_number):
        raise ValueError("Customer number must be alphanumeric and 6-12 characters long.")
    return True

def validate_date_of_birth(date_of_birth):
    """Validate date of birth to ensure it follows YYYY-MM-DD format and is a valid date."""
    try:
        dob = datetime.strptime(date_of_birth, '%Y-%m-%d')
        if dob > datetime.now():
            raise ValueError("Date of birth cannot be in the future.")
    except ValueError:
        raise ValueError("Invalid date of birth format. Use YYYY-MM-DD.")
    return True

def validate_loan_amount(loan_amount):
    """Validate loan amount to ensure it is a positive number."""
    try:
        amount = float(loan_amount)
        if amount <= 0:
            raise ValueError("Loan amount must be a positive number.")
    except ValueError:
        raise ValueError("Invalid loan amount. Please enter a numeric value.")
    return True

def collect_application_form():
    """Simulate an online application form for a credit service."""
    try:
        print("Welcome to the Credit Service Application Form!")
        
        # Collect customer number
        customer_number = input("Enter your customer number (alphanumeric, 6-12 characters): ").strip()
        validate_customer_number(customer_number)
        
        # Collect date of birth
        date_of_birth = input("Enter your date of birth (YYYY-MM-DD): ").strip()
        validate_date_of_birth(date_of_birth)
        
        # Collect desired loan amount
        loan_amount = input("Enter your desired loan amount (positive number): ").strip()
        validate_loan_amount(loan_amount)

        # Application form is valid
        print("\nApplication successfully submitted!")
        print(f"Customer Number: {customer_number}")
        print(f"Date of Birth: {date_of_birth}")
        print(f"Desired Loan Amount: ${loan_amount}")

    except ValueError as e:
        print(f"Error: {e}")

# Entry point for the script
if __name__ == "__main__":
    collect_application_form()
```
