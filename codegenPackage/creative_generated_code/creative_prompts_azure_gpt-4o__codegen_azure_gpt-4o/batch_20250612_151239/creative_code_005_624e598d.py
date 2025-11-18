"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dbm.mu
Prompt: Create a Python function to compare loan options for taxi operators purchasing electric vehicles, using the details provided by the Development Bank of Mauritius.
Generated: DETERMINISTIC_624e598d3acfee1b
Batch ID: 20250612_151239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def compare_loan_options(vehicle_cost, down_payment, loan_term_years, interest_rate_1, interest_rate_2):
    """
    Compare loan options for purchasing electric vehicles based on loan details.

    Args:
        vehicle_cost (float): Total cost of the electric vehicle.
        down_payment (float): Initial payment made upfront.
        loan_term_years (int): Loan repayment period in years.
        interest_rate_1 (float): Interest rate for loan option 1 (as a percentage).
        interest_rate_2 (float): Interest rate for loan option 2 (as a percentage).

    Returns:
        dict: Comparison of total repayment and monthly repayment amounts for both loan options.
    """
    try:
        # Validate input data
        if vehicle_cost <= 0 or down_payment < 0 or loan_term_years <= 0:
            raise ValueError("Invalid input values. Ensure vehicle_cost > 0, down_payment >= 0, and loan_term_years > 0.")
        if interest_rate_1 < 0 or interest_rate_2 < 0:
            raise ValueError("Interest rates must be non-negative.")

        # Calculate loan amount after down payment
        loan_amount = vehicle_cost - down_payment
        if loan_amount <= 0:
            raise ValueError("Down payment must be less than the vehicle cost.")

        # Convert interest rates from percentage to decimal
        interest_rate_1 = interest_rate_1 / 100
        interest_rate_2 = interest_rate_2 / 100

        # Helper function to calculate monthly repayment and total repayment
        def calculate_repayment(loan_amount, annual_rate, term_years):
            monthly_rate = annual_rate / 12
            num_payments = term_years * 12
            # Formula for calculating monthly repayment for fixed-rate loans
            monthly_repayment = loan_amount * (monthly_rate * math.pow(1 + monthly_rate, num_payments)) / \
                                (math.pow(1 + monthly_rate, num_payments) - 1)
            # Total repayment over the loan term
            total_repayment = monthly_repayment * num_payments
            return monthly_repayment, total_repayment

        # Calculate repayments for loan option 1
        monthly_1, total_1 = calculate_repayment(loan_amount, interest_rate_1, loan_term_years)

        # Calculate repayments for loan option 2
        monthly_2, total_2 = calculate_repayment(loan_amount, interest_rate_2, loan_term_years)

        # Return a comparison of loan options
        return {
            "Loan Option 1": {
                "Monthly Repayment": round(monthly_1, 2),
                "Total Repayment": round(total_1, 2)
            },
            "Loan Option 2": {
                "Monthly Repayment": round(monthly_2, 2),
                "Total Repayment": round(total_2, 2)
            }
        }

    except ValueError as e:
        # Handle invalid input values
        return {"error": str(e)}
    except Exception as e:
        # Handle unexpected errors
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage:
if __name__ == "__main__":
    # Example loan details
    vehicle_cost_example = 2000000  # Cost of the electric vehicle in MUR
    down_payment_example = 400000  # Initial payment made upfront in MUR
    loan_term_years_example = 5  # Loan repayment period in years
    interest_rate_1_example = 6.5  # Interest rate for loan option 1 (percentage)
    interest_rate_2_example = 7.5  # Interest rate for loan option 2 (percentage)

    # Comparing loan options
    comparison_result = compare_loan_options(
        vehicle_cost_example,
        down_payment_example,
        loan_term_years_example,
        interest_rate_1_example,
        interest_rate_2_example
    )

    # Print comparison results
    print(comparison_result)
```
