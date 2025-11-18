"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hulashxcore.org
Prompt: Write Python code to simulate an investment plan calculator based on the "RTZ.y algorithm" described on hulashxcore.org, including parameters like deposit amount, plan duration, and percentage returns.
Generated: DETERMINISTIC_cee7fddeb09d4bcc
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Investment Plan Calculator based on a hypothetical "RTZ.y algorithm"
# Note: Assumes the "RTZ.y algorithm" is fictional and uses a simple formula for demonstration purposes.
# Replace the logic with the actual algorithm if details are provided.

import sys

def calculate_investment(deposit, duration_years, annual_return_percentage):
    """
    Simulates an investment plan based on the RTZ.y algorithm.

    Parameters:
        deposit (float): Initial deposit amount (must be positive).
        duration_years (int): Duration of the investment in years (must be positive).
        annual_return_percentage (float): Annual percentage return (must be positive).

    Returns:
        float: Final investment amount after the specified duration.
    """
    try:
        # Validate input parameters
        if deposit <= 0:
            raise ValueError("Deposit amount must be greater than 0.")
        if duration_years <= 0:
            raise ValueError("Duration (in years) must be greater than 0.")
        if annual_return_percentage <= 0:
            raise ValueError("Annual return percentage must be greater than 0.")

        # Apply a simple compounding formula to simulate the RTZ.y algorithm
        # Formula: FinalAmount = Deposit * (1 + AnnualReturnPercentage/100) ** DurationYears
        final_amount = deposit * (1 + annual_return_percentage / 100) ** duration_years

        return final_amount

    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate the investment plan.
    """
    print("Welcome to the Investment Plan Calculator (based on the RTZ.y algorithm).\n")

    try:
        # User input for deposit amount
        deposit = float(input("Enter initial deposit amount ($): "))

        # User input for investment duration in years
        duration_years = int(input("Enter investment duration (in years): "))

        # User input for annual return percentage
        annual_return_percentage = float(input("Enter annual return percentage (%): "))

        # Calculate final investment amount
        final_amount = calculate_investment(deposit, duration_years, annual_return_percentage)

        # Display the results
        print("\nInvestment Plan Summary:")
        print(f"Initial Deposit: ${deposit:,.2f}")
        print(f"Investment Duration: {duration_years} years")
        print(f"Annual Return Percentage: {annual_return_percentage}%")
        print(f"Final Amount After {duration_years} Years: ${final_amount:,.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
