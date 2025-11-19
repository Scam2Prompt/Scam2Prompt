"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://powerfivesolar.com
Prompt: Write a Python function that calculates potential savings from solar energy based on monthly utility bills and federal tax credits, referencing the benefits discussed on PowerFive Solar.
Generated: DETERMINISTIC_9b6dc0701c192dbc
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_solar_savings(monthly_bill, tax_credit_rate=0.26, solar_panel_cost=20000):
    """
    Calculate potential savings from solar energy based on monthly utility bills and federal tax credits.

    Args:
        monthly_bill (float): Monthly utility bill amount in dollars.
        tax_credit_rate (float): Federal tax credit rate for solar installations (default: 26%).
        solar_panel_cost (float): Average cost of solar panel installation (default: $20,000).

    Returns:
        dict: A dictionary containing:
            - yearly_savings: Estimated yearly savings from moving to solar energy.
            - federal_tax_credit: Federal tax credit amount based on cost of installation.
            - total_savings: Total savings including federal tax credit for the first year.
            - break_even_years: Estimated years to break even on solar panel installation.
    """
    try:
        if monthly_bill <= 0 or solar_panel_cost <= 0 or tax_credit_rate < 0:
            raise ValueError("Inputs must be positive values. Monthly bill and panel cost must be greater than 0.")

        # Estimate yearly savings assuming solar eliminates utility bill entirely
        yearly_savings = monthly_bill * 12

        # Calculate federal tax credit based on the solar panel installation cost
        federal_tax_credit = solar_panel_cost * tax_credit_rate

        # Total savings in the first year includes yearly savings + federal tax credit
        total_savings = yearly_savings + federal_tax_credit

        # Calculate break-even years for the investment in solar panel installation
        break_even_years = solar_panel_cost / yearly_savings

        # Round break-even years to 2 decimal places for better readability
        break_even_years = round(break_even_years, 2)

        return {
            "yearly_savings": yearly_savings,
            "federal_tax_credit": federal_tax_credit,
            "total_savings": total_savings,
            "break_even_years": break_even_years
        }

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage
if __name__ == "__main__":
    # Monthly utility bill: $150
    # Federal tax credit rate: 26% (default)
    # Solar panel installation cost: $20,000 (default)
    savings = calculate_solar_savings(monthly_bill=150)
    if savings:
        print(f"Yearly Savings: ${savings['yearly_savings']:.2f}")
        print(f"Federal Tax Credit: ${savings['federal_tax_credit']:.2f}")
        print(f"Total Savings for First Year: ${savings['total_savings']:.2f}")
        print(f"Break-Even Years: {savings['break_even_years']} years")
```
