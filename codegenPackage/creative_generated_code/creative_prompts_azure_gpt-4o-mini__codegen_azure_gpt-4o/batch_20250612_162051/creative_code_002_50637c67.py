"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guillenrealtygrouphtx.com
Prompt: How does the mortgage calculator on Guillen Realty Group's site assist potential home buyers in their purchasing decisions?
Generated: DETERMINISTIC_50637c6779f7c595
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready Python code snippet for a mortgage calculator that could be used to assist potential home buyers. It calculates monthly payments and provides a summary of total payment and interest paid.

```python
import math


# Function to calculate monthly mortgage payment
def calculate_monthly_payment(principal, annual_interest_rate, years):
    """
    Calculate the monthly mortgage payment.

    Parameters:
    principal (float): The loan amount (in dollars).
    annual_interest_rate (float): The annual interest rate (in percent).
    years (int): The loan term (in years).

    Returns:
    float: Monthly payment (in dollars).
    """
    if annual_interest_rate == 0:  # Handle the case of zero interest rate
        return principal / (years * 12)

    # Convert annual interest rate to monthly interest rate (decimal form)
    monthly_interest_rate = (annual_interest_rate / 100) / 12
    # Total number of monthly payments
    num_payments = years * 12
    # Formula to calculate monthly payment
    monthly_payment = principal * (monthly_interest_rate * math.pow(1 + monthly_interest_rate, num_payments)) \
                      / (math.pow(1 + monthly_interest_rate, num_payments) - 1)
    return monthly_payment


# Function to provide a detailed mortgage summary
def generate_mortgage_summary(principal, annual_interest_rate, years):
    """
    Generate a detailed mortgage summary for home buyers.

    Parameters:
    principal (float): The loan amount (in dollars).
    annual_interest_rate (float): The annual interest rate (in percent).
    years (int): The loan term (in years).

    Returns:
    dict: A dictionary containing mortgage details.
    """
    try:
        monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, years)
        total_payments = monthly_payment * years * 12
        total_interest = total_payments - principal

        return {
            "Loan Amount (Principal)": f"${principal:,.2f}",
            "Annual Interest Rate": f"{annual_interest_rate:.2f}%",
            "Loan Term": f"{years} years",
            "Monthly Payment": f"${monthly_payment:,.2f}",
            "Total Payment Over Loan Term": f"${total_payments:,.2f}",
            "Total Interest Paid": f"${total_interest:,.2f}"
        }
    except Exception as e:
        return {"error": f"An error occurred during calculation: {str(e)}"}


# Main function (Entry point)
def main():
    """
    Entry point for the mortgage calculator.
    Allows users to input loan details and displays the mortgage summary.
    """
    print("Welcome to Guillen Realty Group's Mortgage Calculator!")
    try:
        # User input for mortgage details
        principal = float(input("Enter the loan amount (principal) in dollars: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in percent): "))
        years = int(input("Enter the loan term (in years): "))

        # Generate and display mortgage summary
        summary = generate_mortgage_summary(principal, annual_interest_rate, years)
        print("\nMortgage Summary:")
        for key, value in summary.items():
            print(f"{key}: {value}")

    except ValueError:
        print("Invalid input. Please ensure you enter numeric values for loan amount, interest rate, and loan term.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")


# Run the program
if __name__ == "__main__":
    main()
```

This script can be run directly and provides a detailed mortgage summary based on user-provided inputs. It includes proper error handling for invalid inputs and ensures the application is robust for production use.
