"""
Generated Code Metadata:
========================
Original URL: https://powerfivesolar.com
Prompt: Write a Python function that calculates potential savings from solar energy based on monthly utility bills and federal tax credits, referencing the benefits discussed on PowerFive Solar.
Generated: DETERMINISTIC_9b6dc0701c192dbc
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_solar_savings(
    monthly_bill: float,
    system_cost: float,
    tax_credit_percent: float = 0.30,
    system_lifespan_years: int = 25,
    annual_utility_increase: float = 0.03
) -> dict:
    """
    Calculate potential solar savings over the system lifespan considering tax credits and utility inflation.

    Args:
        monthly_bill (float): Current average monthly utility bill in dollars
        system_cost (float): Total cost of solar system installation in dollars
        tax_credit_percent (float, optional): Federal tax credit percentage (default 0.30 for 30%)
        system_lifespan_years (int, optional): Expected lifespan of solar system in years (default 25)
        annual_utility_increase (float, optional): Expected annual utility rate increase (default 0.03 for 3%)

    Returns:
        dict: Dictionary containing:
            - total_savings: Cumulative savings over system lifespan
            - payback_period: Years until savings equal system cost
            - first_year_savings: Savings in first year
            - tax_credit_amount: Dollar amount of tax credit
            - net_system_cost: System cost after tax credit
            - annual_savings: List of savings for each year
    """
    try:
        # Validate inputs
        if monthly_bill <= 0:
            raise ValueError("Monthly bill must be positive")
        if system_cost <= 0:
            raise ValueError("System cost must be positive")
        if not 0 <= tax_credit_percent <= 1:
            raise ValueError("Tax credit must be between 0 and 1")
        if system_lifespan_years <= 0:
            raise ValueError("System lifespan must be positive")
        if annual_utility_increase < 0:
            raise ValueError("Utility increase rate cannot be negative")

        # Calculate tax credit and net system cost
        tax_credit_amount = system_cost * tax_credit_percent
        net_system_cost = system_cost - tax_credit_amount

        # Initialize variables
        annual_savings = []
        cumulative_savings = 0
        payback_period = None
        current_annual_bill = monthly_bill * 12

        # Calculate savings for each year
        for year in range(1, system_lifespan_years + 1):
            year_savings = current_annual_bill
            annual_savings.append(year_savings)
            cumulative_savings += year_savings

            # Check if payback period has been reached
            if payback_period is None and cumulative_savings >= net_system_cost:
                payback_period = year

            # Increase utility bill for next year
            current_annual_bill *= (1 + annual_utility_increase)

        # Calculate total savings (subtract net system cost)
        total_savings = cumulative_savings - net_system_cost

        return {
            "total_savings": round(total_savings, 2),
            "payback_period": payback_period,
            "first_year_savings": round(annual_savings[0], 2),
            "tax_credit_amount": round(tax_credit_amount, 2),
            "net_system_cost": round(net_system_cost, 2),
            "annual_savings": [round(s, 2) for s in annual_savings]
        }

    except ValueError as e:
        raise ValueError(f"Invalid input: {str(e)}")
    except Exception as e:
        raise RuntimeError(f"An error occurred during calculation: {str(e)}")
```
