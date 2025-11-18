"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://origineth.us
Prompt: Write a Python script to simulate a mortgage loan using the parameters provided by Crédit Agricole's "Simulation Prêt Immobilier" tool.
Generated: DETERMINISTIC_2d8734317344fb88
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def simulate_mortgage_loan(principal, annual_interest_rate, loan_term_years):
    """
    Simulate a mortgage loan and calculate monthly payments, total payment, and total interest.

    Args:
        principal (float): The loan amount (in euros).
        annual_interest_rate (float): Annual interest rate (as a percentage, e.g., 3.5 for 3.5%).
        loan_term_years (int): Loan term in years.

    Returns:
        dict: A dictionary containing monthly payment, total payment, and total interest.
    """
    try:
        # Ensure inputs are valid
        if principal <= 0 or annual_interest_rate <= 0 or loan_term_years <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Convert annual interest rate to monthly interest rate (decimal value)
        monthly_interest_rate = (annual_interest_rate / 100) / 12

        # Calculate the total number of payments
        total_payments = loan_term_years * 12

        # Calculate monthly payment using the formula for annuity payments
        monthly_payment = (principal * monthly_interest_rate) / (1 - math.pow(1 + monthly_interest_rate, -total_payments))

        # Calculate total payment over the loan term
        total_payment = monthly_payment * total_payments

        # Calculate total interest paid
        total_interest = total_payment - principal

        # Return results in a dictionary
        return {
            "monthly_payment": round(monthly_payment, 2),
            "total_payment": round(total_payment, 2),
            "total_interest": round(total_interest, 2)
        }

    except ValueError as ve:
        return {"error": str(ve)}

    except Exception as e:
        return {"error": "An unexpected error occurred: " + str(e)}


# Test the simulation with sample inputs
if __name__ == "__main__":
    # Sample inputs
    principal = 200000  # Loan amount in euros
    annual_interest_rate = 3.5  # Annual interest rate in %
    loan_term_years = 25  # Loan term in years

    # Run simulation
    result = simulate_mortgage_loan(principal, annual_interest_rate, loan_term_years)

    # Print results
    if "error" in result:
        print("Error:", result["error"])
    else:
        print("Mortgage Loan Simulation Results:")
        print(f"Monthly Payment: €{result['monthly_payment']}")
        print(f"Total Payment: €{result['total_payment']}")
        print(f"Total Interest: €{result['total_interest']}")
```
