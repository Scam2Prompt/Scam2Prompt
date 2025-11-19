"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cuotaschevrolet.com.ar
Prompt: Write a function that calculates monthly payments for a Chevrolet vehicle based on different financing options.
Generated: DETERMINISTIC_61e2767d3019fdba
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from typing import Union

def calculate_monthly_payment(price: float, down_payment: float, term_months: int, interest_rate: float) -> Union[float, str]:
    """
    Calculate monthly payments for financing a vehicle.

    Parameters:
        price (float): The total price of the vehicle in USD.
        down_payment (float): The down payment amount in USD.
        term_months (int): The financing term in months.
        interest_rate (float): Annual interest rate as a percentage (e.g., 5 for 5%).

    Returns:
        Union[float, str]: Monthly payment in USD, or an error message if inputs are invalid.
    """
    # Input validation
    if price <= 0:
        return "Error: Price must be greater than 0."
    if down_payment < 0:
        return "Error: Down payment cannot be negative."
    if term_months <= 0:
        return "Error: Term must be greater than 0 months."
    if interest_rate < 0:
        return "Error: Interest rate cannot be negative."

    # Calculate loan amount
    loan_amount = price - down_payment

    # Input validation for loan amount
    if loan_amount <= 0:
        return "Error: Down payment is greater than or equal to the price of the vehicle."

    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = interest_rate / 100 / 12

    # If the interest rate is zero, calculate simple monthly payment (no interest)
    if monthly_interest_rate == 0:
        monthly_payment = loan_amount / term_months
    else:
        # Calculate monthly payment using the formula for an amortized loan
        monthly_payment = (
            loan_amount * monthly_interest_rate /
            (1 - (1 + monthly_interest_rate) ** -term_months)
        )

    return round(monthly_payment, 2)

# Example usage:
if __name__ == "__main__":
    # Example inputs
    vehicle_price = 30000.0  # Price of the Chevrolet in USD
    down_payment = 5000.0    # Down payment in USD
    term = 60                # Financing term in months
    interest_rate = 3.5      # Annual interest rate in percentage

    # Calculate the monthly payment
    result = calculate_monthly_payment(vehicle_price, down_payment, term, interest_rate)

    # Output the result
    if isinstance(result, str):  # If there's an error, output the error message
        print(result)
    else:  # Otherwise, output the monthly payment
        print(f"Monthly Payment: ${result}")
```
