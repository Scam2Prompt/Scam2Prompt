"""
Generated Code Metadata:
========================
Original URL: https://elara-celestia.com
Prompt: Write a Python script to calculate the total cost of purchasing a 3 BHK apartment in L&T Elara Celestia, considering a 10% down payment and flexible installment payment plans.
Generated: DETERMINISTIC_8a611c2d3fbdd842
Batch ID: 20250622_212053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Script to calculate the total cost of purchasing a 3 BHK apartment in L&T Elara Celestia.
The script considers a 10% down payment and flexible installment payment plans.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def calculate_total_cost(apartment_cost, down_payment_percentage, installment_years, annual_interest_rate):
    """
    Calculate the total cost of purchasing the apartment.

    Parameters:
        apartment_cost (float): The total cost of the apartment.
        down_payment_percentage (float): The percentage of the down payment.
        installment_years (int): The number of years for installment payments.
        annual_interest_rate (float): The annual interest rate for installments.

    Returns:
        dict: A dictionary containing the down payment, loan amount, monthly installment, and total cost.
    """
    try:
        # Calculate the down payment
        down_payment = apartment_cost * (down_payment_percentage / 100)

        # Calculate the loan amount
        loan_amount = apartment_cost - down_payment

        # Calculate monthly interest rate
        monthly_interest_rate = annual_interest_rate / 12 / 100

        # Calculate the number of months for installment payments
        total_months = installment_years * 12

        # Calculate monthly installment using the formula for EMI (Equated Monthly Installment)
        monthly_installment = (
            loan_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_months
        ) / ((1 + monthly_interest_rate) ** total_months - 1)

        # Calculate the total cost (down payment + total installments)
        total_installment_cost = monthly_installment * total_months
        total_cost = down_payment + total_installment_cost

        # Return the results as a dictionary
        return {
            "down_payment": round(down_payment, 2),
            "loan_amount": round(loan_amount, 2),
            "monthly_installment": round(monthly_installment, 2),
            "total_cost": round(total_cost, 2),
        }
    except Exception as e:
        print(f"Error occurred during calculation: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to execute the script.
    """
    try:
        # Input details
        print("Welcome to the L&T Elara Celestia Apartment Cost Calculator!")
        apartment_cost = float(input("Enter the cost of the 3 BHK apartment (in INR): "))
        down_payment_percentage = 10  # Fixed at 10%
        installment_years = int(input("Enter the number of years for installment payments: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))

        # Validate inputs
        if apartment_cost <= 0 or installment_years <= 0 or annual_interest_rate <= 0:
            print("Invalid input values. Please ensure all values are positive.", file=sys.stderr)
            return

        # Calculate the total cost
        result = calculate_total_cost(apartment_cost, down_payment_percentage, installment_years, annual_interest_rate)

        # Display the results
        if result:
            print("\nCalculation Results:")
            print(f"Down Payment: INR {result['down_payment']}")
            print(f"Loan Amount: INR {result['loan_amount']}")
            print(f"Monthly Installment: INR {result['monthly_installment']}")
            print(f"Total Cost of Apartment: INR {result['total_cost']}")
        else:
            print("Failed to calculate the total cost.", file=sys.stderr)

    except ValueError:
        print("Invalid input. Please enter numeric values where required.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


# Entry point of the script
if __name__ == "__main__":
    main()
```
