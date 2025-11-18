"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinofinance.com
Prompt: Write a function to calculate repayment terms for settled case financing, using Rhino Finance's approach of "no repayment if litigation is lost."
Generated: DETERMINISTIC_34bd71c40427d2fc
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_repayment(litigation_won, funding_amount, interest_rate, case_resolution_time, max_repayment_cap):
    """
    Calculate repayment terms for settled case financing using Rhino Finance's approach:
    - No repayment if litigation is lost.
    - If litigation is won, repayment is calculated based on the funding amount, interest rate, 
      and case resolution time, subject to a maximum repayment cap.

    Args:
        litigation_won (bool): True if litigation is won, False otherwise.
        funding_amount (float): The initial amount of funding provided for the case.
        interest_rate (float): Annual interest rate as a percentage (e.g., 12.5 for 12.5%).
        case_resolution_time (float): Time taken to resolve the case in years.
        max_repayment_cap (float): Maximum repayment cap amount.

    Returns:
        float: Calculated repayment amount if litigation is won; 0 if litigation is lost.
    """
    try:
        # Validate inputs
        if funding_amount <= 0:
            raise ValueError("Funding amount must be greater than zero.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if case_resolution_time < 0:
            raise ValueError("Case resolution time cannot be negative.")
        if max_repayment_cap <= 0:
            raise ValueError("Maximum repayment cap must be greater than zero.")

        # If litigation is lost, no repayment is required
        if not litigation_won:
            return 0.0

        # Calculate repayment amount based on compound interest formula
        repayment_amount = funding_amount * (math.pow((1 + interest_rate / 100), case_resolution_time))

        # Apply maximum repayment cap
        repayment_amount = min(repayment_amount, max_repayment_cap)

        return round(repayment_amount, 2)

    except Exception as e:
        # Log and handle unexpected errors
        print(f"Error calculating repayment: {str(e)}")
        raise

# Example usage (remove or comment out this section in production):
if __name__ == "__main__":
    # Case parameters
    litigation_won = True
    funding_amount = 10000.0  # Initial funding amount in USD
    interest_rate = 12.5      # Annual interest rate in percentage
    case_resolution_time = 3  # Time in years
    max_repayment_cap = 20000.0  # Maximum repayment cap in USD

    repayment = calculate_repayment(litigation_won, funding_amount, interest_rate, case_resolution_time, max_repayment_cap)
    print(f"Repayment Amount: ${repayment}")
```
