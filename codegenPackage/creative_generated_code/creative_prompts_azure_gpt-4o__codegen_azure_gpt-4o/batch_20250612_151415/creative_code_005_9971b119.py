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
# Loan Eligibility Estimator
# This program estimates loan eligibility based on income and basic criteria.

def calculate_loan_eligibility(income, monthly_expenses, credit_score):
    """
    Function to estimate loan eligibility.
    Args:
        income (float): Monthly income of the individual.
        monthly_expenses (float): Monthly expenses of the individual.
        credit_score (int): Credit score of the individual (300-850 scale).
    Returns:
        dict: Loan eligibility details including maximum loan amount and approval status.
    """
    try:
        # Ensure inputs are valid
        if income <= 0 or monthly_expenses < 0 or not (300 <= credit_score <= 850):
            raise ValueError("Invalid input values. Ensure income > 0, expenses >= 0, and credit_score is between 300 and 850.")

        # Calculate disposable income
        disposable_income = income - monthly_expenses

        # Check if income is sufficient
        if disposable_income <= 1000:
            return {
                "eligible": False,
                "message": "Insufficient disposable income for loan approval."
            }

        # Determine loan eligibility based on credit score and disposable income
        if credit_score >= 750:
            max_loan_amount = disposable_income * 10  # High credit score, 10x disposable income
        elif credit_score >= 650:
            max_loan_amount = disposable_income * 7  # Medium credit score, 7x disposable income
        else:
            max_loan_amount = disposable_income * 4  # Low credit score, 4x disposable income
        
        # Return eligibility details
        return {
            "eligible": True,
            "max_loan_amount": round(max_loan_amount, 2),
            "message": "Loan approved based on your income and credit score."
        }
    except ValueError as ve:
        return {
            "eligible": False,
            "message": str(ve)
        }
    except Exception as e:
        return {
            "eligible": False,
            "message": f"An unexpected error occurred: {str(e)}"
        }

def main():
    """
    Main function to interact with the user and estimate their loan eligibility.
    """
    print("Welcome to the Loan Eligibility Estimator!")
    try:
        # Get user inputs
        income = float(input("Enter your monthly income (in USD): "))
        monthly_expenses = float(input("Enter your monthly expenses (in USD): "))
        credit_score = int(input("Enter your credit score (300-850): "))

        # Calculate loan eligibility
        result = calculate_loan_eligibility(income, monthly_expenses, credit_score)

        # Display the result
        print("\nLoan Eligibility Results:")
        print(f"Eligibility Status: {'Approved' if result['eligible'] else 'Denied'}")
        if result['eligible']:
            print(f"Maximum Loan Amount: ${result['max_loan_amount']}")
        print(f"Message: {result['message']}")
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
