"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Create a Python script to calculate monthly payments for HVAC systems based on the TVA Heat Pump Program details provided by Quality Sheet Metal, Inc., including "no money down" and 10-year payment plans.
Generated: DETERMINISTIC_c020183f80a7f063
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

def calculate_monthly_payment(cost, annual_interest_rate, years):
    """
    Calculate the monthly payment for an HVAC system using the formula for 
    fixed monthly payments on loans.

    Parameters:
    - cost (float): Total cost of the HVAC system in dollars.
    - annual_interest_rate (float): Annual interest rate as a percentage (e.g., 6.0 for 6%).
    - years (int): Loan term in years.

    Returns:
    - float: Monthly payment amount in dollars.
    """
    try:
        # Convert annual interest rate to monthly interest rate (decimal form)
        monthly_interest_rate = annual_interest_rate / 100 / 12

        # Total number of monthly payments
        total_months = years * 12

        # If the interest rate is 0, return simple division of cost by months
        if monthly_interest_rate == 0:
            return cost / total_months

        # Formula for calculating monthly payment (amortization formula)
        monthly_payment = (
            cost 
            * monthly_interest_rate 
            * math.pow(1 + monthly_interest_rate, total_months)
        ) / (math.pow(1 + monthly_interest_rate, total_months) - 1)

        return monthly_payment
    
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while calculating monthly payment: {e}")
        return None


def main():
    """
    Main function to prompt user input and calculate HVAC monthly payments.
    """
    print("Welcome to the HVAC Monthly Payment Calculator based on TVA Heat Pump Program!")

    try:
        # Prompt user for inputs
        cost = float(input("Enter the total cost of the HVAC system (in dollars): "))
        annual_interest_rate = float(input("Enter the annual interest rate (e.g., 6 for 6%): "))
        years = int(input("Enter the loan term in years (e.g., 10): "))
        
        # Validate inputs
        if cost <= 0 or annual_interest_rate < 0 or years <= 0:
            print("Invalid input. Please ensure the cost is positive, interest rate is non-negative, and years are positive.")
            return

        # Calculate monthly payment
        monthly_payment = calculate_monthly_payment(cost, annual_interest_rate, years)

        # Display the result
        if monthly_payment is not None:
            print(f"\nFor a system costing ${cost:.2f} with an interest rate of {annual_interest_rate:.2f}% over {years} years:")
            print(f"Your estimated monthly payment is: ${monthly_payment:.2f}")
        else:
            print("Failed to calculate monthly payment due to an error.")
    
    except ValueError:
        # Handle invalid input (e.g., non-numeric values)
        print("Invalid input. Please enter numeric values for cost, interest rate, and years.")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
