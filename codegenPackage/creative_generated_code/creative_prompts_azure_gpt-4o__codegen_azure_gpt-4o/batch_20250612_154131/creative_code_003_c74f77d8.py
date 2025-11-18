"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arkventure.net
Prompt: Write a script to model the impact of ARK Venture Fund's single 2.75% management fee compared to a traditional "2 and 20" fee structure over a 5-year investment period.
Generated: DETERMINISTIC_c74f77d80c4130bf
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to model the impact of ARK Venture Fund's single 2.75% management fee 
# compared to a traditional "2 and 20" fee structure over a 5-year investment period.

# Import necessary libraries
import numpy as np

def calculate_ark_fee(initial_investment, annual_return, years, management_fee_rate):
    """
    Calculate the final portfolio value under ARK Venture Fund's 2.75% management fee structure.

    Args:
        initial_investment (float): The initial amount invested.
        annual_return (float): The annual return rate (as a decimal, e.g., 0.10 for 10%).
        years (int): Number of years to project.
        management_fee_rate (float): Annual management fee rate (as a decimal, e.g., 0.0275 for 2.75%).

    Returns:
        float: Final portfolio value after applying ARK Venture Fund's fee structure.
    """
    portfolio_value = initial_investment
    for _ in range(years):
        gross_growth = portfolio_value * (1 + annual_return)
        management_fee = portfolio_value * management_fee_rate
        portfolio_value = gross_growth - management_fee
    return portfolio_value


def calculate_traditional_fee(initial_investment, annual_return, years, management_fee_rate, performance_fee_rate):
    """
    Calculate the final portfolio value under a traditional "2 and 20" fee structure.

    Args:
        initial_investment (float): The initial amount invested.
        annual_return (float): The annual return rate (as a decimal, e.g., 0.10 for 10%).
        years (int): Number of years to project.
        management_fee_rate (float): Annual management fee rate (as a decimal, e.g., 0.02 for 2%).
        performance_fee_rate (float): Performance fee rate (as a decimal, e.g., 0.20 for 20%).

    Returns:
        float: Final portfolio value after applying the traditional "2 and 20" fee structure.
    """
    portfolio_value = initial_investment
    for _ in range(years):
        gross_growth = portfolio_value * (1 + annual_return)
        management_fee = portfolio_value * management_fee_rate
        performance_fee = (gross_growth - portfolio_value) * performance_fee_rate
        portfolio_value = gross_growth - management_fee - performance_fee
    return portfolio_value


def main():
    """
    Main function to compare ARK Venture Fund's fee structure with a traditional "2 and 20" fee structure.
    """
    # Parameters
    initial_investment = 1000000  # $1,000,000 initial investment
    annual_return = 0.10  # 10% annual return
    years = 5  # 5-year investment period
    ark_management_fee_rate = 0.0275  # 2.75% management fee for ARK Venture Fund
    traditional_management_fee_rate = 0.02  # 2% management fee for traditional structure
    traditional_performance_fee_rate = 0.20  # 20% performance fee for traditional structure

    # Calculations
    ark_final_value = calculate_ark_fee(
        initial_investment, annual_return, years, ark_management_fee_rate
    )
    traditional_final_value = calculate_traditional_fee(
        initial_investment, annual_return, years, traditional_management_fee_rate, traditional_performance_fee_rate
    )

    # Output results
    print("Investment Comparison Over 5 Years:")
    print(f"Initial Investment: ${initial_investment:,.2f}")
    print(f"ARK Venture Fund Final Value (2.75% management fee): ${ark_final_value:,.2f}")
    print(f"Traditional '2 and 20' Final Value: ${traditional_final_value:,.2f}")
    print(f"Difference (ARK vs. Traditional): ${ark_final_value - traditional_final_value:,.2f}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
