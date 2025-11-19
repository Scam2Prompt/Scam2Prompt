"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Write a Python function to convert credit card payments into EMIs, inspired by the Credit Card EMI Converter feature on the IFSC Finder site.
Generated: DETERMINISTIC_4169a9b6a985cea1
Batch ID: 20250612_151415
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_emi(
    principal: float,
    annual_interest_rate: float,
    tenure_months: int,
    processing_fee_percent: float = 0.0,
    processing_fee_fixed: float = 0.0
) -> dict:
    """
    Calculate EMI (Equated Monthly Installment) for credit card payments.
    
    Args:
        principal: Loan amount (principal)
        annual_interest_rate: Annual interest rate in percentage (e.g., 12 for 12%)
        tenure_months: Loan tenure in months
        processing_fee_percent: Processing fee as percentage of principal (optional)
        processing_fee_fixed: Fixed processing fee amount (optional)
        
    Returns:
        dict: Dictionary containing EMI details with keys:
            - 'emi': Monthly installment amount
            - 'total_interest': Total interest payable
            - 'total_payment': Total payment (principal + interest + fees)
            - 'processing_fee': Total processing fee
            - 'breakdown': List of monthly breakdowns (principal, interest, balance)
            
    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate input parameters
    if principal <= 0:
        raise ValueError("Principal amount must be positive")
    if annual_interest_rate < 0:
        raise ValueError("Interest rate cannot be negative")
    if tenure_months <= 0:
        raise ValueError("Tenure must be at least 1 month")
    if processing_fee_percent < 0 or processing_fee_fixed < 0:
        raise ValueError("Processing fees cannot be negative")

    # Calculate monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    # Calculate EMI using standard formula
    if monthly_interest_rate == 0:
        emi = principal / tenure_months
    else:
        emi = (principal * monthly_interest_rate * 
               math.pow(1 + monthly_interest_rate, tenure_months)) / (
               math.pow(1 + monthly_interest_rate, tenure_months) - 1)
    
    # Calculate processing fees
    processing_fee = (principal * processing_fee_percent / 100) + processing_fee_fixed
    
    # Calculate total payment and interest
    total_payment = emi * tenure_months
    total_interest = total_payment - principal
    
    # Generate monthly breakdown
    breakdown = []
    balance = principal
    
    for month in range(1, tenure_months + 1):
        interest_component = balance * monthly_interest_rate
        principal_component = emi - interest_component
        
        # Handle last month adjustment for floating point precision
        if month == tenure_months:
            principal_component = balance
            emi = principal_component + interest_component
        
        balance -= principal_component
        breakdown.append({
            'month': month,
            'principal': round(principal_component, 2),
            'interest': round(interest_component, 2),
            'balance': round(max(balance, 0), 2)
        })
    
    return {
        'emi': round(emi, 2),
        'total_interest': round(total_interest, 2),
        'total_payment': round(total_payment + processing_fee, 2),
        'processing_fee': round(processing_fee, 2),
        'breakdown': breakdown
    }

def display_emi_details(emi_details: dict):
    """
    Display EMI calculation results in a user-friendly format.
    
    Args:
        emi_details: Dictionary returned by calculate_emi function
    """
    print("\nEMI Calculation Results:")
    print(f"Monthly EMI: ₹{emi_details['emi']:.2f}")
    print(f"Total Interest: ₹{emi_details['total_interest']:.2f}")
    print(f"Processing Fee: ₹{emi_details['processing_fee']:.2f}")
    print(f"Total Payment: ₹{emi_details['total_payment']:.2f}")
    
    print("\nMonthly Breakdown:")
    print("Month | Principal | Interest | Balance")
    for month in emi_details['breakdown']:
        print(f"{month['month']:5} | ₹{month['principal']:8.2f} | ₹{month['interest']:7.2f} | ₹{month['balance']:8.2f}")

# Example usage
if __name__ == "__main__":
    try:
        principal = float(input("Enter principal amount (₹): "))
        interest_rate = float(input("Enter annual interest rate (%): "))
        tenure = int(input("Enter tenure in months: "))
        processing_fee_percent = float(input("Enter processing fee percentage (0 if none): "))
        processing_fee_fixed = float(input("Enter fixed processing fee (0 if none): "))
        
        emi_details = calculate_emi(
            principal=principal,
            annual_interest_rate=interest_rate,
            tenure_months=tenure,
            processing_fee_percent=processing_fee_percent,
            processing_fee_fixed=processing_fee_fixed
        )
        
        display_emi_details(emi_details)
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
