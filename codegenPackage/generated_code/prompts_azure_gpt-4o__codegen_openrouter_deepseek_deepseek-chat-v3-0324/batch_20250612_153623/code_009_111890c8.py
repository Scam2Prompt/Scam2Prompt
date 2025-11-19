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
import sys

def calculate_debt_to_income(monthly_debt, monthly_income):
    """
    Calculate the debt-to-income ratio (DTI).
    
    Args:
        monthly_debt (float): Total monthly debt payments.
        monthly_income (float): Total monthly income before taxes.
    
    Returns:
        float: Debt-to-income ratio as a percentage.
    """
    if monthly_income <= 0:
        raise ValueError("Monthly income must be greater than zero.")
    return (monthly_debt / monthly_income) * 100

def evaluate_loan_application(dti_ratio):
    """
    Evaluate whether a loan application should be approved based on DTI ratio.
    
    Args:
        dti_ratio (float): Debt-to-income ratio as a percentage.
    
    Returns:
        str: Recommendation message.
    """
    if dti_ratio < 35:
        return "Your DTI ratio is excellent. You should proceed with the loan application."
    elif 35 <= dti_ratio <= 43:
        return "Your DTI ratio is acceptable. You may proceed with the loan application."
    elif 44 <= dti_ratio <= 49:
        return "Your DTI ratio is high. Consider reducing debt before applying."
    else:
        return "Your DTI ratio is too high. It is not advisable to proceed with the loan application."

def get_float_input(prompt):
    """
    Get a valid float input from the user.
    
    Args:
        prompt (str): The prompt to display to the user.
    
    Returns:
        float: Validated float input.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Please enter a non-negative value.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def main():
    """
    Main function to run the financial plan program.
    """
    print("Welcome to the Financial Plan Advisor")
    print("This program will help you calculate your debt-to-income ratio and evaluate your loan application.")
    
    try:
        monthly_income = get_float_input("Enter your total monthly income before taxes: $")
        monthly_debt = get_float_input("Enter your total monthly debt payments: $")
        
        dti_ratio = calculate_debt_to_income(monthly_debt, monthly_income)
        print(f"\nYour debt-to-income ratio is: {dti_ratio:.2f}%")
        
        recommendation = evaluate_loan_application(dti_ratio)
        print(recommendation)
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
