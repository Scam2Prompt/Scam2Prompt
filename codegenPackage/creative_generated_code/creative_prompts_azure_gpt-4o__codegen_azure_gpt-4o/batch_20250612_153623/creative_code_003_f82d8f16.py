"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maisemprestimos.online
Prompt: Develop a Python program that calculates and compares the total cost of different types of loans (personal, consignado, with collateral, and specific financing) based on user input for loan amount, interest rate, and repayment period.
Generated: DETERMINISTIC_f82d8f1693d6e87b
Batch ID: 20250612_153623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Loan Comparison Program
# This program calculates and compares the total cost of different types of loans based on user inputs.

def calculate_total_cost(loan_amount, annual_interest_rate, repayment_years):
    """
    Calculates the total cost of a loan based on the loan amount, annual interest rate, and repayment period.
    Uses the formula for compound interest to compute the total repayment amount.

    Parameters:
        loan_amount (float): The principal amount of the loan.
        annual_interest_rate (float): The annual interest rate as a percentage (e.g., 5.5 for 5.5%).
        repayment_years (int): The repayment period in years.

    Returns:
        float: The total cost of the loan (principal + interest).
    """
    try:
        # Convert annual interest rate to a decimal (e.g., 5.5% -> 0.055)
        interest_rate_decimal = annual_interest_rate / 100
        
        # Calculate the total cost using compound interest formula
        total_cost = loan_amount * (1 + interest_rate_decimal * repayment_years)
        return total_cost
    except Exception as e:
        print(f"Error while calculating loan cost: {e}")
        return None


def get_user_input():
    """
    Prompts the user for loan details including loan amount, annual interest rate, and repayment years.

    Returns:
        tuple: A tuple containing loan amount, annual interest rate, and repayment years.
    """
    try:
        loan_amount = float(input("Enter the loan amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        repayment_years = int(input("Enter the repayment period (in years): "))
        return loan_amount, annual_interest_rate, repayment_years
    except ValueError:
        print("Invalid input. Please enter numeric values for loan amount and interest rate, and an integer for repayment years.")
        return None


def main():
    """
    Main function to calculate and compare different types of loans based on user input.
    """
    print("Welcome to the Loan Comparison Program!")
    
    # Define loan types for comparison
    loan_types = ["Personal Loan", "Consignado Loan", "Collateral Loan", "Specific Financing"]

    # Get user input
    user_input = get_user_input()
    if user_input is None:
        print("Error: Unable to proceed due to invalid input.")
        return

    loan_amount, annual_interest_rate, repayment_years = user_input

    # Calculate and display the total cost for each loan type
    print("\nLoan Cost Comparison:")
    for loan_type in loan_types:
        total_cost = calculate_total_cost(loan_amount, annual_interest_rate, repayment_years)
        if total_cost is not None:
            print(f"{loan_type}: Total Cost = ${total_cost:,.2f}")
        else:
            print(f"{loan_type}: Calculation failed due to an error.")
    
    print("\nThank you for using the Loan Comparison Program!")


# Entry point of the program
if __name__ == "__main__":
    main()
```
