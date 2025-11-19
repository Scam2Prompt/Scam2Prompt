"""
Generated Code Metadata:
========================
Original URL: https://cidautos.com
Prompt: "Generate a Python code snippet to create a simple calculator for financing options on vehicles like the Kia Sorento at Cid Autos."
Generated: DETERMINISTIC_190d73976e75ff8a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# financing_calculator.py

# Import necessary modules
import sys

def calculate_monthly_payment(principal, annual_rate, years):
    """
    Calculate the monthly payment for a loan.

    :param principal: The loan amount (vehicle price minus down payment).
    :param annual_rate: The annual interest rate (in percentage).
    :param years: The loan term in years.
    :return: The monthly payment amount.
    """
    try:
        # Convert annual rate to monthly rate (percentage to decimal)
        monthly_rate = (annual_rate / 100) / 12
        # Total number of payments
        total_payments = years * 12

        # If interest rate is 0, handle as a special case
        if monthly_rate == 0:
            return principal / total_payments

        # Calculate monthly payment using the formula for an amortizing loan
        monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -total_payments)
        return monthly_payment
    except ZeroDivisionError:
        print("Error: Division by zero occurred. Please check your input values.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate financing options.
    """
    print("Welcome to Cid Autos Financing Calculator!")
    try:
        # Get user input
        vehicle_price = float(input("Enter the vehicle price (e.g., 35000): "))
        down_payment = float(input("Enter the down payment amount (e.g., 5000): "))
        annual_rate = float(input("Enter the annual interest rate (e.g., 3.5): "))
        loan_term_years = int(input("Enter the loan term in years (e.g., 5): "))

        # Validate inputs
        if vehicle_price <= 0 or down_payment < 0 or annual_rate < 0 or loan_term_years <= 0:
            print("Error: Please enter valid positive numbers for all inputs.")
            sys.exit(1)

        # Calculate principal (loan amount)
        principal = vehicle_price - down_payment
        if principal <= 0:
            print("Error: Down payment cannot be greater than or equal to the vehicle price.")
            sys.exit(1)

        # Calculate monthly payment
        monthly_payment = calculate_monthly_payment(principal, annual_rate, loan_term_years)

        # Display the result
        print(f"\nFinancing Details:")
        print(f"Vehicle Price: ${vehicle_price:,.2f}")
        print(f"Down Payment: ${down_payment:,.2f}")
        print(f"Loan Amount: ${principal:,.2f}")
        print(f"Annual Interest Rate: {annual_rate:.2f}%")
        print(f"Loan Term: {loan_term_years} years")
        print(f"Monthly Payment: ${monthly_payment:,.2f}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values where required.")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
