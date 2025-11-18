"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediate-helix.com
Prompt: Write a Python program to calculate the impact of tax-loss harvesting on a portfolio, including scenarios where compound interest might improve returns, as described by Immediate Helix V9.
Generated: DETERMINISTIC_4b78d7f639eaf4b3
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Python Program to Calculate the Impact of Tax-Loss Harvesting on a Portfolio.

This program takes into account:
1. Tax rates for capital gains.
2. Loss harvesting to offset gains.
3. Compound interest on reinvested savings.

Inputs:
- Initial portfolio value.
- Annual rate of return.
- Tax rate on capital gains.
- Years invested.
- Annual loss harvested (if applicable).

Outputs:
- Final portfolio value with tax-loss harvesting.
- Final portfolio value without tax-loss harvesting.

Author: Expert Developer
Date: Immediate Helix V9 Reference
"""

# Import necessary modules
import sys

def calculate_portfolio_growth(initial_value, annual_rate, years):
    """
    Calculates portfolio value based on compound interest formula.
    Args:
        initial_value (float): Initial value of the portfolio.
        annual_rate (float): Annual rate of return (e.g., 0.07 for 7%).
        years (int): Number of years invested.
    Returns:
        float: Portfolio value after the specified years.
    """
    try:
        return initial_value * ((1 + annual_rate) ** years)
    except Exception as e:
        print(f"Error in compound interest calculation: {e}")
        sys.exit(1)


def calculate_tax_loss_harvesting_impact(initial_value, annual_rate, tax_rate, years, annual_loss_harvested):
    """
    Calculates the impact of tax-loss harvesting on portfolio growth.
    Args:
        initial_value (float): Initial value of the portfolio.
        annual_rate (float): Annual rate of return.
        tax_rate (float): Tax rate on capital gains.
        years (int): Number of years invested.
        annual_loss_harvested (float): Annual tax-loss harvested amount.
    Returns:
        dict: Portfolio values with and without tax-loss harvesting.
    """
    try:
        # Portfolio growth without tax-loss harvesting
        portfolio_no_harvest = calculate_portfolio_growth(initial_value, annual_rate, years)
        
        # Portfolio growth with tax-loss harvesting
        tax_savings = annual_loss_harvested * tax_rate * years
        reinvested_tax_savings = calculate_portfolio_growth(tax_savings, annual_rate, years)
        portfolio_with_harvest = portfolio_no_harvest + reinvested_tax_savings
        
        return {
            "Portfolio Without Tax-Loss Harvesting": portfolio_no_harvest,
            "Portfolio With Tax-Loss Harvesting": portfolio_with_harvest
        }
    except Exception as e:
        print(f"Error in tax-loss harvesting calculation: {e}")
        sys.exit(1)


def main():
    """
    Main function to handle user input and program execution.
    """
    try:
        # Request user input for portfolio parameters
        print("Enter portfolio details:")
        initial_value = float(input("Initial Portfolio Value ($): "))
        annual_rate = float(input("Annual Rate of Return (e.g., 0.07 for 7%): "))
        tax_rate = float(input("Tax Rate on Capital Gains (e.g., 0.15 for 15%): "))
        years = int(input("Years Invested: "))
        annual_loss_harvested = float(input("Annual Loss Harvested ($): "))
        
        # Calculate tax-loss harvesting impact
        results = calculate_tax_loss_harvesting_impact(
            initial_value, annual_rate, tax_rate, years, annual_loss_harvested
        )
        
        # Display results
        print("\nPortfolio Growth Summary:")
        for key, value in results.items():
            print(f"{key}: ${value:,.2f}")
    
    except ValueError:
        print("Invalid input. Please enter numeric values for all parameters.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
