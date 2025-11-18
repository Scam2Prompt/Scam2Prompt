"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lenderlibrary.ca
Prompt: Write a Python script that calculates mortgage ratios for 1 to 4 rental units based on guidelines provided by Dominion Lending's "Biblio-Hypothécaire" portal. Include options for variable-to-fixed mortgage conversion.
Generated: DETERMINISTIC_57f6b6a73a8039e6
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_mortgage_ratios(principal, interest_rate, term_years, rental_income, num_units):
    """
    Calculate mortgage ratios based on Dominion Lending's guidelines.
    Args:
        principal (float): The loan principal amount in dollars.
        interest_rate (float): The annual interest rate as a percentage.
        term_years (int): The loan term in years.
        rental_income (float): Monthly rental income for the property.
        num_units (int): Number of rental units (1 to 4).

    Returns:
        dict: A dictionary containing mortgage-related calculations.
    """
    if num_units not in [1, 2, 3, 4]:
        raise ValueError("Number of rental units must be between 1 and 4.")

    if principal <= 0 or interest_rate <= 0 or term_years <= 0 or rental_income <= 0:
        raise ValueError("Principal, interest rate, term years, and rental income must be positive.")

    # Convert annual interest rate to monthly rate
    monthly_rate = (interest_rate / 100) / 12

    # Total number of payments over the loan term
    total_payments = term_years * 12

    # Calculate monthly mortgage payment using the formula for fixed-rate loans
    monthly_payment = (principal * monthly_rate * (1 + monthly_rate)**total_payments) / ((1 + monthly_rate)**total_payments - 1)

    # Calculate mortgage ratios
    income_ratio = rental_income / monthly_payment
    unit_ratio = monthly_payment / num_units

    return {
        "monthly_payment": round(monthly_payment, 2),
        "income_ratio": round(income_ratio, 2),
        "unit_ratio": round(unit_ratio, 2),
    }


def variable_to_fixed(principal, variable_rate, fixed_rate, term_years):
    """
    Convert a variable-rate mortgage to a fixed-rate mortgage and calculate monthly payments.
    Args:
        principal (float): The loan principal amount in dollars.
        variable_rate (float): The current variable interest rate as a percentage.
        fixed_rate (float): The desired fixed interest rate as a percentage.
        term_years (int): The loan term in years.

    Returns:
        dict: A dictionary containing comparison of monthly payments for variable and fixed rates.
    """
    if principal <= 0 or variable_rate <= 0 or fixed_rate <= 0 or term_years <= 0:
        raise ValueError("Principal, interest rates, and term years must be positive.")

    # Convert annual interest rates to monthly rates
    variable_monthly_rate = (variable_rate / 100) / 12
    fixed_monthly_rate = (fixed_rate / 100) / 12

    # Total number of payments over the loan term
    total_payments = term_years * 12

    # Calculate monthly payments for both variable and fixed rates
    variable_monthly_payment = (principal * variable_monthly_rate * (1 + variable_monthly_rate)**total_payments) / ((1 + variable_monthly_rate)**total_payments - 1)
    fixed_monthly_payment = (principal * fixed_monthly_rate * (1 + fixed_monthly_rate)**total_payments) / ((1 + fixed_monthly_rate)**total_payments - 1)

    return {
        "variable_monthly_payment": round(variable_monthly_payment, 2),
        "fixed_monthly_payment": round(fixed_monthly_payment, 2),
    }


def main():
    """
    Main function to accept user input and perform mortgage calculations.
    """
    try:
        print("Welcome to the Mortgage Calculator")
        principal = float(input("Enter the loan principal amount (in dollars): "))
        interest_rate = float(input("Enter the annual interest rate (as a percentage): "))
        term_years = int(input("Enter the loan term (in years): "))
        rental_income = float(input("Enter the monthly rental income (in dollars): "))
        num_units = int(input("Enter the number of rental units (1 to 4): "))
        
        # Calculate mortgage ratios
        ratios = calculate_mortgage_ratios(principal, interest_rate, term_years, rental_income, num_units)
        print("\nMortgage Ratios:")
        print(f"Monthly Payment: ${ratios['monthly_payment']}")
        print(f"Income Ratio: {ratios['income_ratio']}")
        print(f"Unit Ratio: ${ratios['unit_ratio']} per unit")

        # Option for variable-to-fixed mortgage conversion
        convert_choice = input("\nDo you want to calculate variable-to-fixed mortgage payments? (yes/no): ").strip().lower()
        if convert_choice == "yes":
            variable_rate = float(input("Enter the current variable interest rate (as a percentage): "))
            fixed_rate = float(input("Enter the desired fixed interest rate (as a percentage): "))
            comparison = variable_to_fixed(principal, variable_rate, fixed_rate, term_years)
            print("\nVariable-to-Fixed Mortgage Comparison:")
            print(f"Variable Monthly Payment: ${comparison['variable_monthly_payment']}")
            print(f"Fixed Monthly Payment: ${comparison['fixed_monthly_payment']}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        sys.exit(1)
```
