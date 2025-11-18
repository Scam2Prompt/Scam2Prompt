"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Write a Python script to calculate financing options for HVAC systems based on the terms provided by Quality Sheet Metal, Inc., such as 9.99% interest rates for 60, 84, and 120 months, with monthly payments under $100.
Generated: DETERMINISTIC_256065ce8d9279b3
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_monthly_payment(principal, interest_rate, months):
    """
    Calculate the monthly payment for a loan using the formula for fixed-rate amortizing loans.

    Args:
        principal (float): The amount borrowed (loan principal).
        interest_rate (float): Annual interest rate (e.g., 9.99% should be passed as 0.0999).
        months (int): Loan tenure in months.

    Returns:
        float: Monthly payment amount.
    """
    # Convert annual interest rate to monthly interest rate
    monthly_rate = interest_rate / 12
    
    try:
        # Avoid division by zero
        if monthly_rate == 0:
            return principal / months
        
        # Fixed-rate loan formula
        payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
        return payment
    except ZeroDivisionError:
        print("Error: Division by zero occurred in the payment calculation.")
        return None


def recommend_financing_options(principal):
    """
    Recommend financing options for HVAC systems based on interest rate and term limits.

    Args:
        principal (float): The total cost of the HVAC system.

    Returns:
        dict: Recommended financing terms with monthly payment details.
    """
    # Financing terms provided by Quality Sheet Metal, Inc.
    INTEREST_RATE = 0.0999  # 9.99% annual interest rate
    TERMS = [60, 84, 120]  # Loan terms in months
    MAX_MONTHLY_PAYMENT = 100  # Maximum allowed monthly payment
    
    recommendations = {}
    for term in TERMS:
        monthly_payment = calculate_monthly_payment(principal, INTEREST_RATE, term)
        if monthly_payment and monthly_payment <= MAX_MONTHLY_PAYMENT:
            recommendations[term] = round(monthly_payment, 2)
    
    return recommendations


def main():
    """
    Main function to execute the financing calculation and display the results.
    """
    print("Welcome to HVAC Financing Options Calculator")
    
    try:
        # Input validation for principal amount
        principal = float(input("Enter the total cost of the HVAC system: $"))
        if principal <= 0:
            print("Error: Principal amount must be greater than zero.")
            return
        
        # Generate financing recommendations
        recommendations = recommend_financing_options(principal)
        
        if recommendations:
            print("\nRecommended Financing Options:")
            for term, monthly_payment in recommendations.items():
                print(f"  {term} months: ${monthly_payment}/month")
        else:
            print("\nNo financing options available with monthly payments under $100.")
    except ValueError:
        print("Error: Invalid input. Please enter a valid numeric value for the principal amount.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
