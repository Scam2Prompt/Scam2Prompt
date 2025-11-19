"""
Generated Code Metadata:
========================
Original URL: https://tomatoclub.xyz
Prompt: Write a Python script that calculates the actual interest from DeFi yield rates, considering the nuances of APY as discussed in the article.
Generated: DETERMINISTIC_63ac86ff1cb36fc3
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Union

def calculate_actual_interest(
    principal: float, 
    nominal_apy: float, 
    compounding_periods: int = 365, 
    years: int = 1
) -> float:
    """
    Calculate the actual interest earned based on DeFi APY and compounding frequency.

    APY (Annual Percentage Yield) takes compounding into account, so this function
    converts APY to APR (Annual Percentage Rate) and then calculates actual interest.

    Args:
        principal: Initial investment amount.
        nominal_apy: The APY as a percentage (e.g., 5 for 5% APY).
        compounding_periods: Number of compounding periods per year. Default 365 (daily).
        years: Investment period in years. Default 1.

    Returns:
        The actual interest earned over the period.

    Raises:
        ValueError: If any of the inputs are invalid (non-positive values).
    """
    if principal <= 0 or nominal_apy <= 0 or compounding_periods <= 0 or years <= 0:
        raise ValueError("All input values must be positive numbers.")
    
    # Convert APY from percentage to decimal
    apy_decimal = nominal_apy / 100.0
    
    # Calculate APR from APY
    # Formula: APR = n * ((1 + APY)^(1/n) - 1)
    apr = compounding_periods * (math.pow(1 + apy_decimal, 1.0 / compounding_periods) - 1)
    
    # Calculate the actual interest with compound formula
    # Formula: A = P * (1 + APR/n)^(n*t)
    amount = principal * math.pow(1 + apr / compounding_periods, compounding_periods * years)
    
    actual_interest = amount - principal
    return actual_interest

def main():
    try:
        # Example usage
        principal = float(input("Enter principal amount: "))
        apy = float(input("Enter APY (%): "))
        periods = int(input("Enter compounding periods per year (default 365): ") or 365)
        years = int(input("Enter investment period in years (default 1): ") or 1)
        
        interest = calculate_actual_interest(principal, apy, periods, years)
        print(f"\nActual interest earned: ${interest:,.2f}")
        print(f"Total amount after {years} year(s): ${principal + interest:,.2f}")
    
    except ValueError as e:
        print(f"Error: {e}. Please enter valid positive numbers.")

if __name__ == "__main__":
    main()
```
