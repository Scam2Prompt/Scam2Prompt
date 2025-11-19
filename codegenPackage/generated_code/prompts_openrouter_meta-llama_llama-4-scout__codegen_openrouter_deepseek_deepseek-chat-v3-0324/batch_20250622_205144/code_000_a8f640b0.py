"""
Generated Code Metadata:
========================
Original URL: https://ziggyloan.com
Prompt: "Generate a Python script to calculate the total amount payable for a personal loan of $4,300 with an Annual Percentage Rate (APR) of 35.99% and a repayment period of 30 months."
Generated: DETERMINISTIC_a8f640b08b573ba1
Batch ID: 20250622_205144
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_loan_payment(principal, annual_rate, months):
    """
    Calculate the total amount payable for a personal loan.
    
    Args:
        principal (float): The loan amount.
        annual_rate (float): Annual Percentage Rate (APR) as a percentage.
        months (int): Loan term in months.
    
    Returns:
        float: Total amount payable.
    
    Raises:
        ValueError: If any input is invalid (negative or zero values).
    """
    if principal <= 0 or annual_rate <= 0 or months <= 0:
        raise ValueError("All inputs must be positive values")
    
    # Convert APR to monthly rate
    monthly_rate = annual_rate / 100 / 12
    
    # Calculate monthly payment using the formula for fixed-rate loans
    monthly_payment = (principal * monthly_rate) / (1 - (1 + monthly_rate) ** -months)
    
    # Calculate total amount payable
    total_payable = monthly_payment * months
    
    return round(total_payable, 2)

def main():
    try:
        principal = 4300.0
        apr = 35.99
        months = 30
        
        total = calculate_loan_payment(principal, apr, months)
        print(f"Principal: ${principal:,.2f}")
        print(f"APR: {apr}%")
        print(f"Term: {months} months")
        print(f"Total amount payable: ${total:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
