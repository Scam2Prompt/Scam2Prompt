"""
Generated Code Metadata:
========================
Original URL: https://summar.com
Prompt: Write a Python code snippet to calculate the benefits of using freight factoring for a small trucking company, considering same-day funding and non-recourse programs.
Generated: DETERMINISTIC_a83d46ee9ce6c9e2
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def calculate_freight_factoring_benefits(invoice_amount, payment_delay_days, factoring_rate, non_recourse_fee=0):
    """
    Calculate the benefits of using freight factoring for a small trucking company.

    Parameters:
        invoice_amount (float): The total amount of the invoice.
        payment_delay_days (int): The number of days the payment is delayed without factoring.
        factoring_rate (float): The percentage fee charged by the factoring company (e.g., 0.03 for 3%).
        non_recourse_fee (float): Additional fee for non-recourse factoring (default is 0).

    Returns:
        dict: A dictionary containing the factoring cost, avoided delay cost, and net benefit.
    """
    try:
        # Validate inputs
        if invoice_amount <= 0 or payment_delay_days < 0 or factoring_rate < 0 or non_recourse_fee < 0:
            raise ValueError("Invalid input values. Ensure all values are positive.")

        # Calculate factoring cost
        factoring_cost = invoice_amount * factoring_rate + non_recourse_fee

        # Assume a daily cost of delay (e.g., lost opportunity cost or interest rate)
        daily_delay_cost = 0.01 * invoice_amount  # Example: 1% of invoice amount per day
        avoided_delay_cost = daily_delay_cost * payment_delay_days

        # Calculate net benefit
        net_benefit = avoided_delay_cost - factoring_cost

        # Return results as a dictionary
        return {
            "factoring_cost": round(factoring_cost, 2),
            "avoided_delay_cost": round(avoided_delay_cost, 2),
            "net_benefit": round(net_benefit, 2),
        }

    except ValueError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"An unexpected error occurred: {str(e)}"}


# Example usage
if __name__ == "__main__":
    # Inputs for the calculation
    invoice_amount = 5000.0  # Example invoice amount in dollars
    payment_delay_days = 30  # Example payment delay in days
    factoring_rate = 0.03    # Example factoring rate (3%)
    non_recourse_fee = 50.0  # Example non-recourse fee in dollars

    # Calculate benefits
    benefits = calculate_freight_factoring_benefits(
        invoice_amount, payment_delay_days, factoring_rate, non_recourse_fee
    )

    # Display results
    if "error" in benefits:
        print(f"Error: {benefits['error']}")
    else:
        print("Freight Factoring Benefits:")
        print(f"Factoring Cost: ${benefits['factoring_cost']}")
        print(f"Avoided Delay Cost: ${benefits['avoided_delay_cost']}")
        print(f"Net Benefit: ${benefits['net_benefit']}")
```
