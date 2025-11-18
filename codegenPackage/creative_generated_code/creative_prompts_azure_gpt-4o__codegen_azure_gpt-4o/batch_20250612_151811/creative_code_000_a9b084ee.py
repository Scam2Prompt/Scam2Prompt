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

def validate_user_details(name, age, email):
    """
    Validates the user's details.
    Args:
        name (str): User's name.
        age (int): User's age.
        email (str): User's email address.
    Returns:
        bool: True if all validations pass, False otherwise.
    """
    # Validate name: Must not be empty and contain only alphabets
    if not name or not name.isalpha():
        print("Invalid name. Name must only contain alphabets.")
        return False
    
    # Validate age: Must be between 18 and 65
    if not (18 <= age <= 65):
        print("Invalid age. Age must be between 18 and 65.")
        return False
    
    # Validate email: Must be a valid email format
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        print("Invalid email. Please provide a valid email address.")
        return False
    
    return True


def validate_loan_amount(amount):
    """
    Validates the loan amount.
    Args:
        amount (float): Requested loan amount.
    Returns:
        bool: True if validation passes, False otherwise.
    """
    # Loan amount must be within a permissible range
    if not (1000 <= amount <= 50000):
        print("Invalid loan amount. Must be between $1,000 and $50,000.")
        return False
    return True


def check_credit_score(credit_score):
    """
    Simulates a credit score check.
    Args:
        credit_score (int): User's credit score.
    Returns:
        bool: True if credit score is above the threshold, False otherwise.
    """
    # Minimum credit score required is 600
    return credit_score >= 600


def approve_loan(name, age, email, loan_amount, credit_score):
    """
    Simulates the loan approval process.
    Args:
        name (str): User's name.
        age (int): User's age.
        email (str): User's email address.
        loan_amount (float): Requested loan amount.
        credit_score (int): User's credit score.
    Returns:
        str: Approval status message.
    """
    if not validate_user_details(name, age, email):
        return "Loan approval failed due to invalid user details."

    if not validate_loan_amount(loan_amount):
        return "Loan approval failed due to invalid loan amount."

    if not check_credit_score(credit_score):
        return "Loan approval failed due to low credit score."

    return f"Loan approved for {name}. Amount: ${loan_amount:.2f}"


def main():
    """
    Entry point for the loan approval system.
    """
    print("Welcome to the Loan Approval System!")
    
    try:
        # Get user input
        name = input("Enter your full name: ").strip()
        age = int(input("Enter your age: ").strip())
        email = input("Enter your email address: ").strip()
        loan_amount = float(input("Enter the loan amount you are requesting: ").strip())
        credit_score = int(input("Enter your credit score: ").strip())
        
        # Process loan approval
        result = approve_loan(name, age, email, loan_amount, credit_score)
        print(result)
    except ValueError:
        print("Invalid input. Please ensure all fields are entered correctly.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
