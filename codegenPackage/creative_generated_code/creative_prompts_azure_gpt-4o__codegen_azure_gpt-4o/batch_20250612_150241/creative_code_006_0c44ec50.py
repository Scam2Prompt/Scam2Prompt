"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://federalfirstcapitalunion.com
Prompt: Develop a program to track savings account growth over time, referencing Federal First Capital Union's personal savings account offerings.
Generated: DETERMINISTIC_0c44ec50c95692ef
Batch ID: 20250612_150241
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program to track savings account growth over time.
This program calculates savings account balance growth based on an annual interest rate with monthly compounding.
It is designed for use with Federal First Capital Union's personal savings account offerings.
"""

# Import necessary library
import sys

def calculate_savings_growth(principal, annual_rate, months, monthly_deposit=0):
    """
    Function to calculate savings account growth over time.
    
    Args:
        principal (float): Initial deposit amount in the savings account.
        annual_rate (float): Annual interest rate as a percentage (e.g., 2.5 for 2.5%).
        months (int): Number of months to calculate growth over.
        monthly_deposit (float): Optional monthly deposit added to the account.
        
    Returns:
        float: Final savings account balance after the specified period.
    """
    try:
        # Validate input arguments
        if principal < 0 or annual_rate < 0 or months < 0 or monthly_deposit < 0:
            raise ValueError("All input values must be non-negative.")
        
        # Convert annual interest rate to a monthly interest rate
        monthly_rate = annual_rate / 100 / 12
        
        balance = principal
        for month in range(1, months + 1):
            # Apply interest for the month
            balance += balance * monthly_rate
            
            # Add monthly deposit, if any
            balance += monthly_deposit
            
        return balance
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

# Main function to interact with the user
def main():
    """
    Main function to run the savings account growth tracking program.
    """
    print("Welcome to Federal First Capital Union's Savings Tracker!")
    
    try:
        # Get user input for savings account parameters
        principal = float(input("Enter the initial deposit amount ($): "))
        annual_rate = float(input("Enter the annual interest rate (%) (e.g., 2.5): "))
        months = int(input("Enter the number of months to track growth (e.g., 24): "))
        monthly_deposit = float(input("Enter optional monthly deposit amount ($), or enter 0 if none: "))
        
        # Validate inputs
        if principal < 0 or annual_rate < 0 or months < 0 or monthly_deposit < 0:
            raise ValueError("All inputs must be non-negative.")
        
        # Calculate savings growth
        final_balance = calculate_savings_growth(principal, annual_rate, months, monthly_deposit)
        
        if final_balance is not None:
            print(f"\nAfter {months} months, your savings account balance will be: ${final_balance:.2f}")
        else:
            print("Unable to calculate savings due to invalid inputs.")
    
    except ValueError as e:
        print(f"Invalid input: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

# Entry point of the program
if __name__ == "__main__":
    main()
```
