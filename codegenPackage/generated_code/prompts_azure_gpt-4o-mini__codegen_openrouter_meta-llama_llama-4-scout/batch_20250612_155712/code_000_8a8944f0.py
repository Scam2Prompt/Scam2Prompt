"""
Generated Code Metadata:
========================
Original URL: https://rhinofinance.com
Prompt: Generate a Python script to calculate the estimated fees for a settlement loan based on the terms provided by Rhino Finance.
Generated: DETERMINISTIC_8a8944f05801ab36
Batch ID: 20250612_155712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Rhino Finance Settlement Loan Fee Calculator

Calculates the estimated fees for a settlement loan based on the terms provided by Rhino Finance.

Author: [Your Name]
Date: [Today's Date]
"""

def calculate_settlement_loan_fees(principal, interest_rate, loan_term, fee_percentage):
    """
    Calculates the estimated fees for a settlement loan.

    Args:
        principal (float): The initial loan amount.
        interest_rate (float): The annual interest rate as a decimal.
        loan_term (int): The loan term in years.
        fee_percentage (float): The fee percentage as a decimal.

    Returns:
        dict: A dictionary containing the estimated fees.
    """
    try:
        # Calculate the total interest paid over the loan term
        total_interest = principal * interest_rate * loan_term

        # Calculate the total amount paid
        total_amount_paid = principal + total_interest

        # Calculate the estimated fees
        estimated_fees = total_amount_paid * fee_percentage

        # Return the estimated fees as a dictionary
        return {
            "total_interest": round(total_interest, 2),
            "total_amount_paid": round(total_amount_paid, 2),
            "estimated_fees": round(estimated_fees, 2)
        }

    except TypeError as e:
        print(f"Invalid input type: {e}")
        return None

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    # Example usage
    principal = 10000.0  # Initial loan amount
    interest_rate = 0.06  # Annual interest rate (6%)
    loan_term = 5  # Loan term in years
    fee_percentage = 0.05  # Fee percentage (5%)

    estimated_fees = calculate_settlement_loan_fees(principal, interest_rate, loan_term, fee_percentage)

    if estimated_fees:
        print("Estimated Fees:")
        print(f"Total Interest: ${estimated_fees['total_interest']}")
        print(f"Total Amount Paid: ${estimated_fees['total_amount_paid']}")
        print(f"Estimated Fees: ${estimated_fees['estimated_fees']}")


if __name__ == "__main__":
    main()
```
