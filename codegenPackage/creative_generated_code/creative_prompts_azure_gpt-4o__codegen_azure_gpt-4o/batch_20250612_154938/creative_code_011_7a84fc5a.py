"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maya-finance.com
Prompt: Create a Python script to calculate the total cost of a loan for Maya Finance, including principal, interest, and any additional fees, based on user input for loan type and duration.
Generated: DETERMINISTIC_7a84fc5ae21ecd8c
Batch ID: 20250612_154938
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def get_user_input(prompt, input_type, validation=None):
    """
    Prompts the user for input, validates, and converts it to the appropriate type.

    Args:
        prompt (str): The message displayed to the user.
        input_type (type): The type to which the input should be converted.
        validation (function, optional): A validation function to check input validity.

    Returns:
        input_type: User-provided and validated input.

    Raises:
        ValueError: If the input is invalid or conversion fails.
    """
    while True:
        try:
            user_input = input(prompt)
            converted_input = input_type(user_input)
            if validation and not validation(converted_input):
                raise ValueError("Input failed validation.")
            return converted_input
        except ValueError as e:
            print(f"Invalid input: {e}")

def calculate_loan_cost(principal, interest_rate, duration, additional_fees):
    """
    Calculates the total cost of a loan.

    Args:
        principal (float): The principal amount of the loan.
        interest_rate (float): The annual interest rate as a percentage (e.g., 5.5 for 5.5%).
        duration (int): The duration of the loan in years.
        additional_fees (float): Any additional fees associated with the loan.

    Returns:
        float: Total cost of the loan.
    """
    interest_cost = principal * (interest_rate / 100) * duration
    total_cost = principal + interest_cost + additional_fees
    return total_cost

def main():
    """
    Main function to calculate loan cost based on user input.
    """
    print("Welcome to Maya Finance Loan Calculator!")

    # Get loan type
    loan_types = {
        "personal": {"max_duration": 5, "fees": 100},
        "home": {"max_duration": 30, "fees": 500},
        "auto": {"max_duration": 7, "fees": 200},
    }

    print("Available loan types: personal, home, auto")
    loan_type = get_user_input(
        "Enter the loan type: ",
        str,
        lambda x: x.lower() in loan_types
    ).lower()

    # Get loan details
    principal = get_user_input(
        "Enter the principal amount of the loan: $",
        float,
        lambda x: x > 0
    )
    interest_rate = get_user_input(
        "Enter the annual interest rate (in %): ",
        float,
        lambda x: x > 0
    )
    duration = get_user_input(
        f"Enter the loan duration (in years, max {loan_types[loan_type]['max_duration']}): ",
        int,
        lambda x: 0 < x <= loan_types[loan_type]['max_duration']
    )

    # Calculate total cost
    additional_fees = loan_types[loan_type]['fees']
    total_cost = calculate_loan_cost(principal, interest_rate, duration, additional_fees)

    # Display results
    print(f"\nLoan Type: {loan_type.capitalize()}")
    print(f"Principal Amount: ${principal:,.2f}")
    print(f"Annual Interest Rate: {interest_rate:.2f}%")
    print(f"Loan Duration: {duration} years")
    print(f"Additional Fees: ${additional_fees:,.2f}")
    print(f"Total Cost of Loan: ${total_cost:,.2f}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCalculation interrupted. Exiting...")
        sys.exit(0)
```
