"""
Generated Code Metadata:
========================
Original URL: https://fortrone.com
Prompt: Generate code to calculate compound growth for a given investment, including returns and time period, inspired by Fortrone's educational content.
Generated: DETERMINISTIC_bc200596d6b17e7e
Batch ID: 20250622_205228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_compound_growth(
    principal: float,
    annual_rate: float,
    years: int,
    compounding_frequency: int = 1
) -> dict:
    """
    Calculate compound growth of an investment over time.
    
    Args:
        principal: Initial investment amount
        annual_rate: Annual interest rate (as decimal, e.g., 0.05 for 5%)
        years: Investment period in years
        compounding_frequency: Number of times interest is compounded per year (default: 1)
    
    Returns:
        Dictionary containing:
        - final_amount: Total value after compounding
        - total_interest: Total interest earned
        - growth_factor: Multiplier from principal to final amount
        - annualized_return: Effective annual return rate
    
    Raises:
        ValueError: If any input parameters are invalid
    """
    # Validate input parameters
    if principal <= 0:
        raise ValueError("Principal must be positive")
    if annual_rate <= 0:
        raise ValueError("Annual rate must be positive")
    if years <= 0:
        raise ValueError("Years must be positive")
    if compounding_frequency <= 0:
        raise ValueError("Compounding frequency must be positive")
    
    # Calculate compound growth
    rate_per_period = annual_rate / compounding_frequency
    periods = years * compounding_frequency
    
    final_amount = principal * math.pow(1 + rate_per_period, periods)
    total_interest = final_amount - principal
    growth_factor = final_amount / principal
    annualized_return = math.pow(growth_factor, 1/years) - 1
    
    return {
        "final_amount": round(final_amount, 2),
        "total_interest": round(total_interest, 2),
        "growth_factor": round(growth_factor, 4),
        "annualized_return": round(annualized_return, 4)
    }

def generate_growth_table(
    principal: float,
    annual_rate: float,
    years: int,
    compounding_frequency: int = 1
) -> list:
    """
    Generate a year-by-year growth table for the investment.
    
    Args:
        principal: Initial investment amount
        annual_rate: Annual interest rate (as decimal)
        years: Investment period in years
        compounding_frequency: Number of times interest is compounded per year
    
    Returns:
        List of dictionaries containing year-by-year growth data
    
    Raises:
        ValueError: If any input parameters are invalid
    """
    # Validate input parameters
    if principal <= 0:
        raise ValueError("Principal must be positive")
    if annual_rate <= 0:
        raise ValueError("Annual rate must be positive")
    if years <= 0:
        raise ValueError("Years must be positive")
    if compounding_frequency <= 0:
        raise ValueError("Compounding frequency must be positive")
    
    growth_table = []
    current_amount = principal
    rate_per_period = annual_rate / compounding_frequency
    
    for year in range(1, years + 1):
        periods_in_year = compounding_frequency
        for _ in range(periods_in_year):
            current_amount *= (1 + rate_per_period)
        
        year_interest = current_amount - principal
        growth_table.append({
            "year": year,
            "amount": round(current_amount, 2),
            "interest": round(year_interest, 2),
            "annual_growth": round((current_amount / principal) ** (1/year) - 1, 4)
        })
    
    return growth_table

def format_currency(value: float) -> str:
    """
    Format a numeric value as currency string.
    
    Args:
        value: Numeric value to format
    
    Returns:
        Formatted currency string (e.g., $1,234.56)
    """
    return f"${value:,.2f}"

def format_percentage(value: float) -> str:
    """
    Format a decimal value as percentage string.
    
    Args:
        value: Decimal value to format (e.g., 0.05 for 5%)
    
    Returns:
        Formatted percentage string (e.g., 5.00%)
    """
    return f"{value * 100:.2f}%"

# Example usage
if __name__ == "__main__":
    try:
        principal = 10000
        rate = 0.07
        years = 10
        freq = 12
        
        result = calculate_compound_growth(principal, rate, years, freq)
        print("Compound Growth Results:")
        print(f"Principal: {format_currency(principal)}")
        print(f"Annual Rate: {format_percentage(rate)}")
        print(f"Years: {years}")
        print(f"Compounding Frequency: {freq} times per year")
        print("\nResults:")
        print(f"Final Amount: {format_currency(result['final_amount'])}")
        print(f"Total Interest: {format_currency(result['total_interest'])}")
        print(f"Growth Factor: {result['growth_factor']:.2f}x")
        print(f"Annualized Return: {format_percentage(result['annualized_return'])}")
        
        print("\nYear-by-Year Growth:")
        table = generate_growth_table(principal, rate, years, freq)
        for entry in table:
            print(f"Year {entry['year']}: {format_currency(entry['amount'])} "
                  f"(Interest: {format_currency(entry['interest'])}, "
                  f"Annual Growth: {format_percentage(entry['annual_growth'])})")
    
    except ValueError as e:
        print(f"Error: {e}")
```
