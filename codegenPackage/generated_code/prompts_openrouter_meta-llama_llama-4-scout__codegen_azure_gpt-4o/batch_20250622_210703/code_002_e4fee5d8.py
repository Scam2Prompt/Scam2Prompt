"""
Generated Code Metadata:
========================
Original URL: https://lenderlibrary.ca
Prompt: "Write a script to calculate mortgage ratios for a property with 1 to 4 rental units using DLC's guidelines."
Generated: DETERMINISTIC_e4fee5d81d8c95c5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys

def calculate_mortgage_ratios(property_value, loan_amount, rental_income, expenses):
    """
    Calculate mortgage ratios for a property with 1 to 4 rental units.

    Args:
        property_value (float): The total value of the property.
        loan_amount (float): The loan amount for the property.
        rental_income (float): Total monthly rental income from all units.
        expenses (float): Total monthly expenses for the property.

    Returns:
        dict: A dictionary containing the Loan-to-Value (LTV) ratio and Debt Service Coverage Ratio (DSCR).
    """
    try:
        # Validate inputs
        if property_value <= 0 or loan_amount <= 0 or rental_income < 0 or expenses < 0:
            raise ValueError("Inputs must be positive numbers. Rental income and expenses can be zero.")

        # Calculate Loan-to-Value (LTV) ratio
        ltv_ratio = (loan_amount / property_value) * 100

        # Calculate Debt Service Coverage Ratio (DSCR)
        if expenses == 0:
            raise ValueError("Expenses cannot be zero when calculating DSCR.")
        dscr = rental_income / expenses

        return {
            "LTV Ratio (%)": round(ltv_ratio, 2),
            "DSCR": round(dscr, 2)
        }

    except ZeroDivisionError:
        print("Error: Division by zero occurred. Please check your inputs.", file=sys.stderr)
        return None
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to interact with the user and calculate mortgage ratios.
    """
    print("Mortgage Ratio Calculator for Properties with 1 to 4 Rental Units")
    print("Please provide the following details:")

    try:
        # Get user inputs
        property_value = float(input("Enter the property value ($): "))
        loan_amount = float(input("Enter the loan amount ($): "))
        rental_income = float(input("Enter the total monthly rental income ($): "))
        expenses = float(input("Enter the total monthly expenses ($): "))

        # Calculate ratios
        ratios = calculate_mortgage_ratios(property_value, loan_amount, rental_income, expenses)

        if ratios:
            print("\nMortgage Ratios:")
            print(f"Loan-to-Value (LTV) Ratio: {ratios['LTV Ratio (%)']}%")
            print(f"Debt Service Coverage Ratio (DSCR): {ratios['DSCR']}")

    except ValueError:
        print("Error: Invalid input. Please enter numeric values.", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
```
