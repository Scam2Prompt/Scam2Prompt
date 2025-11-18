"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Create a program that calculates monthly loan EMI based on principal, interest rate, and loan tenure, similar to the EMI Calculator tool provided on the IFSC Finder website.
Generated: DETERMINISTIC_8d17fe10c5447177
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# EMI Calculator Program to calculate monthly loan EMI (Equated Monthly Installment)

def calculate_emi(principal, annual_interest_rate, loan_tenure_years):
    """
    Function to calculate monthly EMI for a loan.
    
    Parameters:
    principal (float): The loan amount.
    annual_interest_rate (float): Annual interest rate (in percentage).
    loan_tenure_years (int): Loan tenure in years.

    Returns:
    float: Calculated EMI amount.
    """
    try:
        # Validate input
        if principal <= 0 or annual_interest_rate <= 0 or loan_tenure_years <= 0:
            raise ValueError("Principal, interest rate, and loan tenure must be positive numbers.")

        # Convert annual interest rate to monthly rate (percentage to decimal)
        monthly_interest_rate = annual_interest_rate / (12 * 100)
        
        # Convert loan tenure from years to months
        loan_tenure_months = loan_tenure_years * 12
        
        # Formula to calculate EMI: EMI = P * r * (1 + r)^n / [(1 + r)^n - 1]
        numerator = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** loan_tenure_months
        denominator = (1 + monthly_interest_rate) ** loan_tenure_months - 1
        
        emi = numerator / denominator
        
        return round(emi, 2)  # Return EMI rounded to two decimal places
    
    except ZeroDivisionError:
        # Handle division by zero if the interest rate results in invalid calculations
        raise ValueError("Invalid calculation: Division by zero occurred.")
    except Exception as e:
        # Handle any other exceptions
        raise ValueError(f"An error occurred: {str(e)}")


def main():
    """
    Main function to interact with the user and calculate EMI.
    """
    print("Loan EMI Calculator")
    print("-------------------")
    
    try:
        # Take user inputs
        principal = float(input("Enter loan amount (principal): "))
        annual_interest_rate = float(input("Enter annual interest rate (in %): "))
        loan_tenure_years = int(input("Enter loan tenure (in years): "))

        # Calculate EMI
        emi = calculate_emi(principal, annual_interest_rate, loan_tenure_years)
        
        # Display result
        print(f"\nMonthly EMI: {emi}")
    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    # Entry point of the program
    main()
```
