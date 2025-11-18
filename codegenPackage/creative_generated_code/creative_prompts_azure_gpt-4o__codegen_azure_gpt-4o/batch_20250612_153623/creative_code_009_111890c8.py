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
# financial_plan.py

# Import necessary modules
import sys

def calculate_debt_to_income_ratio(total_monthly_debt, monthly_income):
    """
    Calculate the debt-to-income (DTI) ratio.
    
    :param total_monthly_debt: Total monthly debt payments (float)
    :param monthly_income: Monthly income (float)
    :return: Debt-to-Income ratio as a percentage (float)
    """
    try:
        # Ensure inputs are positive numbers
        if total_monthly_debt < 0 or monthly_income <= 0:
            raise ValueError("Debt and income must be positive numbers.")
        
        # Calculate DTI ratio
        dti_ratio = (total_monthly_debt / monthly_income) * 100
        return round(dti_ratio, 2)
    except ZeroDivisionError:
        print("Monthly income cannot be zero.")
        sys.exit(1)

def suggest_loan_application(dti_ratio):
    """
    Suggest whether the user should proceed with a loan application.
    
    Guidelines:
    - If DTI ratio is below 36%, it is considered good.
    - If DTI ratio is between 36% and 43%, proceed with caution.
    - If DTI ratio is above 43%, avoid applying for a loan.
    
    :param dti_ratio: Debt-to-Income ratio (float)
    :return: Suggestion message (str)
    """
    if dti_ratio < 36:
        return "Your DTI ratio is good. You can proceed with a loan application."
    elif 36 <= dti_ratio <= 43:
        return "Your DTI ratio suggests caution. Evaluate your financial situation carefully before applying."
    else:
        return "Your DTI ratio is high. Avoid applying for a loan to prevent financial stress."

def main():
    """
    Main function to interact with the user and provide financial planning insights.
    """
    print("Welcome to the Financial Planning Tool!")
    
    try:
        # Get user input
        total_monthly_debt = float(input("Enter your total monthly debt payments (e.g., 1200.50): "))
        monthly_income = float(input("Enter your monthly income (e.g., 4500.75): "))
        
        # Calculate DTI ratio
        dti_ratio = calculate_debt_to_income_ratio(total_monthly_debt, monthly_income)
        
        # Display results to the user
        print(f"Your Debt-to-Income (DTI) ratio is: {dti_ratio}%")
        suggestion = suggest_loan_application(dti_ratio)
        print(suggestion)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
