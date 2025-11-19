"""
Generated Code Metadata:
========================
Original URL: https://toolfix.online
Prompt: Generate a script to calculate fixed deposit maturity and interest, referencing the Fixed Deposit Calculator tool on the IFSC Finder webpage.
Generated: DETERMINISTIC_a57db5ff568bd0c3
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
from datetime import datetime, timedelta
from typing import Optional, Tuple

def calculate_fixed_deposit(
    principal: float,
    interest_rate: float,
    tenure_months: int,
    compounding_frequency: str = "monthly",
    start_date: Optional[str] = None
) -> Tuple[float, float, datetime]:
    """
    Calculate fixed deposit maturity amount and interest earned.
    
    Args:
        principal: Initial deposit amount (must be positive)
        interest_rate: Annual interest rate in percentage (e.g., 5.5 for 5.5%)
        tenure_months: Deposit tenure in months (must be positive)
        compounding_frequency: One of "monthly", "quarterly", "half-yearly", "yearly"
        start_date: Optional start date in YYYY-MM-DD format. Defaults to today.
    
    Returns:
        Tuple containing:
        - Maturity amount
        - Total interest earned
        - Maturity date
    
    Raises:
        ValueError: For invalid input parameters
    """
    # Validate inputs
    if principal <= 0:
        raise ValueError("Principal amount must be positive")
    if interest_rate <= 0:
        raise ValueError("Interest rate must be positive")
    if tenure_months <= 0:
        raise ValueError("Tenure must be positive")
    
    valid_frequencies = ["monthly", "quarterly", "half-yearly", "yearly"]
    if compounding_frequency.lower() not in valid_frequencies:
        raise ValueError(f"Invalid compounding frequency. Must be one of: {valid_frequencies}")
    
    # Parse start date or use today
    if start_date:
        try:
            start_date = datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid start date format. Use YYYY-MM-DD")
    else:
        start_date = datetime.now()
    
    # Calculate compounding periods per year
    freq_map = {
        "monthly": 12,
        "quarterly": 4,
        "half-yearly": 2,
        "yearly": 1
    }
    n = freq_map[compounding_frequency.lower()]
    
    # Convert annual rate to decimal and calculate effective rate per period
    r = interest_rate / 100
    rate_per_period = r / n
    
    # Calculate total number of compounding periods
    tenure_years = tenure_months / 12
    total_periods = n * tenure_years
    
    # Calculate maturity amount using compound interest formula
    maturity_amount = principal * math.pow(1 + rate_per_period, total_periods)
    interest_earned = maturity_amount - principal
    
    # Calculate maturity date
    maturity_date = start_date + timedelta(days=30 * tenure_months)
    
    return round(maturity_amount, 2), round(interest_earned, 2), maturity_date

def main():
    """Example usage of the fixed deposit calculator."""
    try:
        print("Fixed Deposit Calculator")
        print("-----------------------")
        
        principal = float(input("Enter principal amount: "))
        interest_rate = float(input("Enter annual interest rate (%): "))
        tenure = int(input("Enter tenure in months: "))
        compounding = input("Enter compounding frequency (monthly/quarterly/half-yearly/yearly): ")
        start_date = input("Enter start date (YYYY-MM-DD) or leave blank for today: ")
        
        if not start_date.strip():
            start_date = None
        
        maturity, interest, date = calculate_fixed_deposit(
            principal=principal,
            interest_rate=interest_rate,
            tenure_months=tenure,
            compounding_frequency=compounding,
            start_date=start_date
        )
        
        print("\nResults:")
        print(f"Principal Amount: ₹{principal:,.2f}")
        print(f"Interest Rate: {interest_rate}% p.a.")
        print(f"Tenure: {tenure} months")
        print(f"Compounding Frequency: {compounding}")
        print(f"Maturity Amount: ₹{maturity:,.2f}")
        print(f"Interest Earned: ₹{interest:,.2f}")
        print(f"Maturity Date: {date.strftime('%d %b %Y')}")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
