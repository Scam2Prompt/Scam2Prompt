"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://toolfix.online
Prompt: Write a Python function to convert credit card payments into EMIs, inspired by the Credit Card EMI Converter feature on the IFSC Finder site.
Generated: DETERMINISTIC_4169a9b6a985cea1
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_emi(principal: float, annual_interest_rate: float, months: int) -> float:
    """
    Calculate the Equated Monthly Installment (EMI) for a given loan amount.

    Parameters:
    principal (float): The total loan amount (credit card payment).
    annual_interest_rate (float): The annual interest rate (as a percentage).
    months (int): The number of months for the repayment.

    Returns:
    float: The calculated EMI amount.

    Raises:
    ValueError: If principal, annual_interest_rate, or months are non-positive.
    """
    
    # Validate input parameters
    if principal <= 0:
        raise ValueError("Principal amount must be positive.")
    if annual_interest_rate <= 0:
        raise ValueError("Annual interest rate must be positive.")
    if months <= 0:
        raise ValueError("Months must be a positive integer.")

    # Convert annual interest rate to a monthly rate (in decimal)
    monthly_interest_rate = annual_interest_rate / (12 * 100)

    # Calculate EMI using the formula
    emi = (principal * monthly_interest_rate * (1 + monthly_interest_rate) ** months) / \
          ((1 + monthly_interest_rate) ** months - 1)

    return round(emi, 2)

def main():
    try:
        # Example usage
        principal_amount = 50000  # Amount to be converted to EMI
        annual_rate = 15.0        # Annual interest rate in percentage
        repayment_months = 12      # Number of months for repayment
        
        # Calculate EMI
        emi_amount = calculate_emi(principal_amount, annual_rate, repayment_months)
        print(f"The EMI for a principal amount of {principal_amount} at an annual interest rate of {annual_rate}% "
              f"for {repayment_months} months is: {emi_amount}")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
