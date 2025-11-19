"""
Generated Code Metadata:
========================
Original URL: https://tsmwealth.co.za
Prompt: Write Python code to calculate long-term investment growth using compound interest, incorporating user-defined parameters for initial investment, annual contribution, interest rate, and time horizon, as described in TSM Wealth's investment services.
Generated: DETERMINISTIC_bce40e5af4a7a7c1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from typing import Union, Optional

def calculate_investment_growth(
    initial_investment: Union[int, float],
    annual_contribution: Union[int, float],
    annual_interest_rate: float,
    years: int,
    contribution_frequency: Optional[str] = "yearly"
) -> dict:
    """
    Calculate the future value of an investment with compound interest and regular contributions.

    Args:
        initial_investment: Initial amount invested (positive number)
        annual_contribution: Amount added to investment each year (positive number)
        annual_interest_rate: Annual interest rate as a decimal (e.g., 0.05 for 5%)
        years: Investment time horizon in years (positive integer)
        contribution_frequency: When contributions are made ("yearly", "monthly", "quarterly")

    Returns:
        Dictionary containing:
        - 'future_value': Final investment value
        - 'total_contributions': Total amount contributed over time
        - 'interest_earned': Total interest earned
        - 'growth_data': Year-by-year growth data

    Raises:
        ValueError: If any input parameter is invalid
    """
    # Validate input parameters
    if initial_investment < 0:
        raise ValueError("Initial investment must be non-negative")
    if annual_contribution < 0:
        raise ValueError("Annual contribution must be non-negative")
    if annual_interest_rate < 0:
        raise ValueError("Annual interest rate must be non-negative")
    if years <= 0:
        raise ValueError("Investment horizon must be at least 1 year")
    
    # Determine contribution periods per year
    freq_map = {
        "yearly": 1,
        "quarterly": 4,
        "monthly": 12
    }
    if contribution_frequency not in freq_map:
        raise ValueError("Invalid contribution frequency. Must be 'yearly', 'quarterly', or 'monthly'")
    
    periods_per_year = freq_map[contribution_frequency]
    periodic_contribution = annual_contribution / periods_per_year
    periodic_rate = annual_interest_rate / periods_per_year
    total_periods = years * periods_per_year

    # Calculate future value using compound interest formula with regular contributions
    future_value = initial_investment * (1 + periodic_rate) ** total_periods
    if periodic_rate > 0:
        future_value += periodic_contribution * (((1 + periodic_rate) ** total_periods - 1) / periodic_rate)
    else:
        future_value += periodic_contribution * total_periods

    # Calculate totals and prepare growth data
    total_contributions = initial_investment + annual_contribution * years
    interest_earned = future_value - total_contributions

    # Generate year-by-year growth data
    growth_data = []
    current_value = initial_investment
    for year in range(1, years + 1):
        for period in range(periods_per_year):
            current_value = current_value * (1 + periodic_rate) + periodic_contribution
        growth_data.append({
            "year": year,
            "value": round(current_value, 2),
            "contributions": initial_investment + annual_contribution * year,
            "interest": round(current_value - (initial_investment + annual_contribution * year), 2)
        })

    return {
        "future_value": round(future_value, 2),
        "total_contributions": round(total_contributions, 2),
        "interest_earned": round(interest_earned, 2),
        "growth_data": growth_data
    }

def get_user_input() -> dict:
    """Collect and validate user input for investment parameters."""
    try:
        initial_investment = float(input("Enter initial investment amount: $"))
        annual_contribution = float(input("Enter annual contribution amount: $"))
        annual_interest_rate = float(input("Enter annual interest rate (e.g., 5 for 5%): ")) / 100
        years = int(input("Enter investment time horizon (years): "))
        contribution_frequency = input("Enter contribution frequency (yearly/quarterly/monthly): ").lower()
        
        return {
            "initial_investment": initial_investment,
            "annual_contribution": annual_contribution,
            "annual_interest_rate": annual_interest_rate,
            "years": years,
            "contribution_frequency": contribution_frequency
        }
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

def display_results(results: dict) -> None:
    """Display the investment growth results in a user-friendly format."""
    print("\nInvestment Growth Projection")
    print("---------------------------")
    print(f"Future Value: ${results['future_value']:,.2f}")
    print(f"Total Contributions: ${results['total_contributions']:,.2f}")
    print(f"Interest Earned: ${results['interest_earned']:,.2f}")
    
    print("\nYear-by-Year Growth:")
    print("Year | Value       | Contributions | Interest Earned")
    print("-----|-------------|---------------|----------------")
    for year_data in results['growth_data']:
        print(f"{year_data['year']:4} | ${year_data['value']:10,.2f} | ${year_data['contributions']:12,.2f} | ${year_data['interest']:14,.2f}")

def main():
    """Main function to execute the investment growth calculator."""
    print("TSM Wealth Investment Growth Calculator")
    print("--------------------------------------\n")
    
    user_input = get_user_input()
    
    try:
        results = calculate_investment_growth(
            initial_investment=user_input["initial_investment"],
            annual_contribution=user_input["annual_contribution"],
            annual_interest_rate=user_input["annual_interest_rate"],
            years=user_input["years"],
            contribution_frequency=user_input["contribution_frequency"]
        )
        display_results(results)
    except ValueError as e:
        print(f"Error in calculation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
