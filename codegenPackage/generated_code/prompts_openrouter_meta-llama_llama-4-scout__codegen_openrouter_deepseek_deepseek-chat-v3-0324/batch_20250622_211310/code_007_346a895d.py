"""
Generated Code Metadata:
========================
Original URL: https://immediate-evex.org
Prompt: Develop a basic investment calculator using a programming language like Python that takes into account factors like inflation rate and investment horizon.
Generated: DETERMINISTIC_346a895d99e7d794
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

def calculate_future_value(
    principal: float,
    annual_return: float,
    inflation_rate: float,
    years: int,
    contribution: float = 0,
    contribution_frequency: str = 'yearly'
) -> float:
    """
    Calculate the future value of an investment considering inflation and regular contributions.
    
    Args:
        principal: Initial investment amount
        annual_return: Expected annual return rate (as decimal, e.g., 0.07 for 7%)
        inflation_rate: Expected annual inflation rate (as decimal)
        years: Investment horizon in years
        contribution: Regular contribution amount (default 0)
        contribution_frequency: 'yearly', 'monthly', or 'quarterly' (default 'yearly')
    
    Returns:
        Future value of investment in today's dollars (inflation-adjusted)
    
    Raises:
        ValueError: If invalid input parameters are provided
    """
    # Validate input parameters
    if principal < 0:
        raise ValueError("Principal must be non-negative")
    if years < 0:
        raise ValueError("Investment horizon must be non-negative")
    if contribution < 0:
        raise ValueError("Contribution must be non-negative")
    if contribution_frequency not in ['yearly', 'monthly', 'quarterly']:
        raise ValueError("Invalid contribution frequency")
    
    # Calculate real return rate (adjusted for inflation)
    real_return = (1 + annual_return) / (1 + inflation_rate) - 1
    
    # Determine number of contributions per year
    if contribution_frequency == 'yearly':
        periods_per_year = 1
    elif contribution_frequency == 'quarterly':
        periods_per_year = 4
    else:  # monthly
        periods_per_year = 12
    
    # Calculate future value
    total_periods = years * periods_per_year
    periodic_rate = real_return / periods_per_year
    
    # Future value of principal
    fv_principal = principal * (1 + periodic_rate) ** total_periods
    
    # Future value of contributions (if any)
    if contribution > 0:
        fv_contributions = contribution * ((1 + periodic_rate) ** total_periods - 1) / periodic_rate
    else:
        fv_contributions = 0
    
    return fv_principal + fv_contributions

def get_user_input() -> tuple:
    """
    Get user input for investment calculation with validation.
    
    Returns:
        Tuple of (principal, annual_return, inflation_rate, years, contribution, frequency)
    """
    while True:
        try:
            principal = float(input("Enter initial investment amount: $"))
            annual_return = float(input("Enter expected annual return rate (e.g., 7 for 7%): ")) / 100
            inflation_rate = float(input("Enter expected annual inflation rate (e.g., 2.5 for 2.5%): ")) / 100
            years = int(input("Enter investment horizon in years: "))
            contribution = float(input("Enter regular contribution amount (0 for none): $"))
            
            if contribution > 0:
                frequency = input("Enter contribution frequency (yearly/monthly/quarterly): ").lower()
            else:
                frequency = 'yearly'
            
            return (principal, annual_return, inflation_rate, years, contribution, frequency)
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.\n")

def main():
    """
    Main function to run the investment calculator.
    """
    print("Investment Calculator")
    print("---------------------\n")
    
    try:
        principal, annual_return, inflation_rate, years, contribution, frequency = get_user_input()
        
        future_value = calculate_future_value(
            principal=principal,
            annual_return=annual_return,
            inflation_rate=inflation_rate,
            years=years,
            contribution=contribution,
            contribution_frequency=frequency
        )
        
        print("\nInvestment Results:")
        print(f"Initial Investment: ${principal:,.2f}")
        if contribution > 0:
            print(f"Regular Contributions: ${contribution:,.2f} {frequency}")
        print(f"Investment Horizon: {years} years")
        print(f"Expected Annual Return: {annual_return*100:.2f}%")
        print(f"Expected Inflation Rate: {inflation_rate*100:.2f}%")
        print(f"\nFuture Value (in today's dollars): ${future_value:,.2f}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Please check your inputs and try again.")

if __name__ == "__main__":
    main()
```
