"""
Generated Code Metadata:
========================
Original URL: https://camelot.netlify.app
Prompt: "Generate a Python code snippet to calculate the potential return on investment (ROI) for a fix and flip project using a 100% purchase price and 100% rehab loan from a private money lender like Appak Capital."
Generated: DETERMINISTIC_92a39e6b0d692c07
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
import sys

def calculate_roi(purchase_price, rehab_cost, sale_price, interest_rate, loan_term_months, lender_points):
    """
    Calculate the Return on Investment (ROI) for a fix-and-flip project.

    Parameters:
        purchase_price (float): The purchase price of the property.
        rehab_cost (float): The cost of rehabilitation.
        sale_price (float): The final sale price of the property.
        interest_rate (float): Annual interest rate of the loan (as a percentage).
        loan_term_months (int): Duration of the loan in months.
        lender_points (float): Points charged by the lender (as a percentage of the loan amount).

    Returns:
        float: The ROI as a percentage.
    """
    try:
        # Validate inputs
        if purchase_price <= 0 or rehab_cost < 0 or sale_price <= 0 or interest_rate < 0 or loan_term_months <= 0 or lender_points < 0:
            raise ValueError("All input values must be positive numbers.")

        # Calculate total loan amount (100% purchase price + 100% rehab cost)
        total_loan_amount = purchase_price + rehab_cost

        # Calculate lender points cost
        lender_points_cost = (lender_points / 100) * total_loan_amount

        # Calculate monthly interest rate
        monthly_interest_rate = (interest_rate / 100) / 12

        # Calculate total interest paid over the loan term
        total_interest_paid = total_loan_amount * monthly_interest_rate * loan_term_months

        # Calculate total costs (purchase price, rehab cost, lender points, and interest)
        total_costs = purchase_price + rehab_cost + lender_points_cost + total_interest_paid

        # Calculate profit
        profit = sale_price - total_costs

        # Calculate ROI
        roi = (profit / total_costs) * 100

        return roi

    except ValueError as ve:
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None


# Example usage
if __name__ == "__main__":
    # Input values for the fix-and-flip project
    purchase_price = 200000  # Example purchase price
    rehab_cost = 50000       # Example rehab cost
    sale_price = 300000      # Example sale price
    interest_rate = 10       # Example annual interest rate (in percentage)
    loan_term_months = 6     # Example loan term (in months)
    lender_points = 2        # Example lender points (in percentage)

    # Calculate ROI
    roi = calculate_roi(purchase_price, rehab_cost, sale_price, interest_rate, loan_term_months, lender_points)

    if roi is not None:
        print(f"Potential ROI: {roi:.2f}%")
    else:
        print("Failed to calculate ROI due to input errors or unexpected issues.")
```
