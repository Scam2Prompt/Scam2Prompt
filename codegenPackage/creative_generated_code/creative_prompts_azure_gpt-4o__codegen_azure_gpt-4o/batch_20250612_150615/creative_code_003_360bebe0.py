"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://panchsheelbank.com
Prompt: Create a script to calculate loan interest rates for housing loans based on the deposit interest rates provided by Panchsheel Mercantile Co-op. Bank Ltd.
Generated: DETERMINISTIC_360bebe03eab9664
Batch ID: 20250612_150615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_loan_interest_rate(deposit_interest_rate):
    """
    Calculate the loan interest rate for housing loans based on the deposit interest rate.
    Panchsheel Mercantile Co-op Bank Ltd. uses the formula:
    Loan Interest Rate = Deposit Interest Rate + 3.5%

    Args:
        deposit_interest_rate (float): The deposit interest rate in percentage.

    Returns:
        float: The calculated loan interest rate in percentage.
    """
    try:
        # Ensure that the deposit interest rate is a valid float
        if deposit_interest_rate < 0:
            raise ValueError("Deposit interest rate cannot be negative.")
        return round(deposit_interest_rate + 3.5, 2)
    except ValueError as e:
        raise ValueError(f"Invalid input for deposit interest rate: {e}")

def main():
    """
    Main function to handle user input and calculate the loan interest rate.
    """
    print("Welcome to Panchsheel Mercantile Co-op Bank Ltd.")
    print("Calculate Loan Interest Rate for Housing Loans\n")

    try:
        # Get user input for deposit interest rate
        deposit_interest_rate_input = input("Enter the deposit interest rate (%) offered by the bank: ").strip()

        # Convert user input to a float
        deposit_interest_rate = float(deposit_interest_rate_input)

        # Calculate loan interest rate
        loan_interest_rate = calculate_loan_interest_rate(deposit_interest_rate)

        # Display the result
        print(f"\nBased on a deposit interest rate of {deposit_interest_rate}%, "
              f"the loan interest rate for housing loans will be {loan_interest_rate}%.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the service.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nProcess interrupted by the user. Exiting...")
        sys.exit(1)
```
