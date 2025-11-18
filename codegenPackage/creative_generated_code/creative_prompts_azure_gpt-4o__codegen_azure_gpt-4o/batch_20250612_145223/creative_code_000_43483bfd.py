"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tymebak-loan-application.blogspot.com
Prompt: Write Python code to simulate a loan application process for TymeBank, including input validation for user details and loan amount.
Generated: DETERMINISTIC_43483bfd3a21c4f3
Batch ID: 20250612_145223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re

def validate_name(name):
    """
    Validates if the name contains only alphabetic characters and spaces.
    """
    return bool(re.match(r"^[A-Za-z\s]+$", name))

def validate_age(age):
    """
    Validates if the age is a valid integer and within acceptable limits.
    """
    return age.isdigit() and 18 <= int(age) <= 75

def validate_loan_amount(amount):
    """
    Validates if the loan amount is a valid numeric value and within a reasonable range.
    """
    try:
        amount_float = float(amount)
        return 1000 <= amount_float <= 1000000
    except ValueError:
        return False

def loan_application():
    """
    Main function to handle the loan application process.
    """
    print("Welcome to TymeBank Loan Application Portal!")
    print("Please provide the required details to proceed with your loan application.\n")

    # Get and validate user's full name
    while True:
        full_name = input("Enter your full name: ").strip()
        if validate_name(full_name):
            break
        print("Invalid name. Please enter a valid name containing only letters and spaces.\n")

    # Get and validate user's age
    while True:
        age = input("Enter your age: ").strip()
        if validate_age(age):
            age = int(age)
            break
        print("Invalid age. Age must be a number between 18 and 75.\n")

    # Get and validate the desired loan amount
    while True:
        loan_amount = input("Enter the loan amount you wish to apply for (between 1,000 and 1,000,000): ").strip()
        if validate_loan_amount(loan_amount):
            loan_amount = float(loan_amount)
            break
        print("Invalid loan amount. Please enter a numeric value between 1,000 and 1,000,000.\n")

    # Get user confirmation
    print("\nPlease confirm your details:")
    print(f"Full Name: {full_name}")
    print(f"Age: {age}")
    print(f"Loan Amount: {loan_amount:.2f}")
    confirmation = input("Is the above information correct? (yes/no): ").strip().lower()

    if confirmation == 'yes':
        print("\nThank you for applying, your loan application is being processed!")
    else:
        print("\nApplication canceled. Please restart the process if needed.")

# Entry point for the loan application script
if __name__ == "__main__":
    try:
        loan_application()
    except Exception as e:
        print(f"An error occurred during the application process: {e}")
```
