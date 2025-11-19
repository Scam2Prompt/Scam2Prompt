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
def calculate_solar_savings(monthly_bill, tax_credit_percent, solar_installation_cost):
    """
    Calculate potential savings from solar energy based on monthly utility bills 
    and federal tax credits.

    Parameters:
    monthly_bill (float): The average monthly utility bill in dollars.
    tax_credit_percent (float): The percentage of tax credit available for solar installation.
    solar_installation_cost (float): The total cost of the solar installation in dollars.

    Returns:
    dict: A dictionary containing potential annual savings, total tax credit, 
          and net installation cost after tax credit.
    """

    # Validate input parameters
    if monthly_bill < 0:
        raise ValueError("Monthly bill must be a non-negative value.")
    if not (0 <= tax_credit_percent <= 100):
        raise ValueError("Tax credit percentage must be between 0 and 100.")
    if solar_installation_cost < 0:
        raise ValueError("Solar installation cost must be a non-negative value.")
    
    # Calculate annual utility bill
    annual_bill = monthly_bill * 12
    
    # Calculate potential annual savings assuming solar energy replaces utility bill
    potential_annual_savings = annual_bill

    # Calculate total tax credit based on the solar installation cost
    total_tax_credit = (tax_credit_percent / 100) * solar_installation_cost

    # Calculate net installation cost after applying the tax credit
    net_installation_cost = solar_installation_cost - total_tax_credit

    # Create a result dictionary
    savings_info = {
        "Potential Annual Savings": potential_annual_savings,
        "Total Tax Credit": total_tax_credit,
        "Net Installation Cost": net_installation_cost
    }

    return savings_info


# Example usage (uncomment the following lines to test the function):
# savings = calculate_solar_savings(monthly_bill=150, tax_credit_percent=26, solar_installation_cost=20000)
# print(savings)
```
