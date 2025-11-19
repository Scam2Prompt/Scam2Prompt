"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://24getspeedcash.com
Prompt: Write a Python script that simulates the loan application process, including form submission and lender response, inspired by the features of 24GetSpeedCash.com.
Generated: DETERMINISTIC_7e30ab9cae6452da
Batch ID: 20250612_135804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Constants
MIN_LOAN_AMOUNT = 100
MAX_LOAN_AMOUNT = 5000
MIN_CREDIT_SCORE = 300
MAX_CREDIT_SCORE = 850

# Function to validate form inputs
def validate_inputs(name, age, loan_amount, credit_score):
    """
    Validates the loan application inputs.
    :param name: Applicant's name (string)
    :param age: Applicant's age (integer, must be >= 18)
    :param loan_amount: Requested loan amount (integer, within predefined limits)
    :param credit_score: Applicant's credit score (integer, within predefined limits)
    :return: Boolean indicating if the inputs are valid
    """
    if not name or age < 18:
        return False, "Invalid name or age. Applicant must be at least 18 years old."
    if loan_amount < MIN_LOAN_AMOUNT or loan_amount > MAX_LOAN_AMOUNT:
        return False, f"Loan amount must be between ${MIN_LOAN_AMOUNT} and ${MAX_LOAN_AMOUNT}."
    if credit_score < MIN_CREDIT_SCORE or credit_score > MAX_CREDIT_SCORE:
        return False, f"Credit score must be between {MIN_CREDIT_SCORE} and {MAX_CREDIT_SCORE}."
    return True, "Inputs are valid."

# Function to simulate lender response
def lender_response(loan_amount, credit_score):
    """
    Simulates the lender's response based on the loan amount and credit score.
    :param loan_amount: Requested loan amount (integer)
    :param credit_score: Applicant's credit score (integer)
    :return: String indicating approval or denial
    """
    if credit_score >= 700:  # High credit score, automatic approval
        return f"Loan approved for ${loan_amount} at the best interest rate!"
    elif 600 <= credit_score < 700:  # Moderate credit score, conditional approval
        return f"Loan conditionally approved for ${loan_amount}. Additional verification required."
    else:  # Low credit score, denial
        return "Loan denied due to low credit score."

# Main application function
def loan_application():
    """
    Simulates the loan application process, including form submission and lender response.
    """
    print("Welcome to the Loan Application Portal!")
    
    # Collect applicant details
    name = input("Enter your full name: ").strip()
    try:
        age = int(input("Enter your age: "))
        loan_amount = int(input(f"Enter the loan amount (between ${MIN_LOAN_AMOUNT} and ${MAX_LOAN_AMOUNT}): "))
        credit_score = int(input(f"Enter your credit score (between {MIN_CREDIT_SCORE} and {MAX_CREDIT_SCORE}): "))
    except ValueError:
        print("Error: Invalid input. Please enter numerical values for age, loan amount, and credit score.")
        return
    
    # Validate inputs
    is_valid, validation_message = validate_inputs(name, age, loan_amount, credit_score)
    if not is_valid:
        print(f"Error: {validation_message}")
        return
    
    print("\nForm submitted successfully!")
    print(f"Applicant: {name}")
    print(f"Age: {age}")
    print(f"Requested Loan Amount: ${loan_amount}")
    print(f"Credit Score: {credit_score}")
    
    # Simulate lender response
    response = lender_response(loan_amount, credit_score)
    print("\nLender Response:")
    print(response)

# Entry point of the script
if __name__ == "__main__":
    try:
        loan_application()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
