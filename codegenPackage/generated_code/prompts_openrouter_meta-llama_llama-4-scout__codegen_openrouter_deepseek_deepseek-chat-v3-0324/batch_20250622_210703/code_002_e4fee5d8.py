"""
Generated Code Metadata:
========================
Original URL: https://lenderlibrary.ca
Prompt: "Write a script to calculate mortgage ratios for a property with 1 to 4 rental units using DLC's guidelines."
Generated: DETERMINISTIC_e4fee5d81d8c95c5
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
"""
Mortgage Ratio Calculator for Properties with 1-4 Rental Units (DLC Guidelines)

This script calculates key mortgage ratios (GDS, TDS) for rental properties based on DLC's guidelines.
"""

import sys
from typing import Dict, Tuple, Optional

def calculate_mortgage_ratios(
    property_price: float,
    down_payment: float,
    annual_interest_rate: float,
    amortization_period: int,
    annual_property_taxes: float,
    annual_heating_costs: float,
    condo_fees: float = 0.0,
    other_housing_costs: float = 0.0,
    gross_annual_income: float = 0.0,
    annual_other_debt_payments: float = 0.0,
    num_units: int = 1,
    monthly_rent_per_unit: Optional[Dict[int, float]] = None
) -> Tuple[float, float, float, float]:
    """
    Calculate mortgage ratios (GDS, TDS) for rental properties.

    Args:
        property_price: Total purchase price of the property
        down_payment: Down payment amount
        annual_interest_rate: Annual mortgage interest rate (as decimal)
        amortization_period: Amortization period in years
        annual_property_taxes: Annual property taxes
        annual_heating_costs: Annual heating costs
        condo_fees: Monthly condo fees (if applicable)
        other_housing_costs: Other monthly housing costs
        gross_annual_income: Borrower's gross annual income
        annual_other_debt_payments: Annual payments for other debts
        num_units: Number of rental units (1-4)
        monthly_rent_per_unit: Dictionary of monthly rents per unit (key: unit number, value: rent)

    Returns:
        Tuple containing:
        - Monthly mortgage payment
        - Gross Debt Service ratio (GDS)
        - Total Debt Service ratio (TDS)
        - Rental income offset percentage
    """
    if num_units < 1 or num_units > 4:
        raise ValueError("Number of units must be between 1 and 4")
    
    if monthly_rent_per_unit is None:
        monthly_rent_per_unit = {i: 0.0 for i in range(1, num_units + 1)}
    
    # Calculate mortgage details
    principal = property_price - down_payment
    monthly_interest_rate = annual_interest_rate / 12
    total_payments = amortization_period * 12
    
    if principal <= 0:
        raise ValueError("Principal amount must be positive")
    
    # Calculate monthly mortgage payment
    if monthly_interest_rate == 0:
        monthly_mortgage = principal / total_payments
    else:
        monthly_mortgage = principal * (
            monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments
        ) / ((1 + monthly_interest_rate) ** total_payments - 1)
    
    # Calculate total monthly housing costs
    monthly_property_taxes = annual_property_taxes / 12
    monthly_heating = annual_heating_costs / 12
    monthly_other_debt = annual_other_debt_payments / 12
    
    total_monthly_housing_costs = (
        monthly_mortgage
        + monthly_property_taxes
        + monthly_heating
        + condo_fees
        + other_housing_costs
    )
    
    # Calculate rental income offset (DLC guidelines: 50% of rental income)
    total_monthly_rent = sum(monthly_rent_per_unit.values())
    rental_offset = total_monthly_rent * 0.5
    
    # Calculate adjusted housing costs
    adjusted_housing_costs = max(0, total_monthly_housing_costs - rental_offset)
    
    # Calculate ratios
    monthly_income = gross_annual_income / 12 if gross_annual_income else 0
    
    gds_ratio = (
        (adjusted_housing_costs / monthly_income) * 100
    ) if monthly_income else 0
    
    total_debt = adjusted_housing_costs + monthly_other_debt
    tds_ratio = (
        (total_debt / monthly_income) * 100
    ) if monthly_income else 0
    
    rental_offset_percentage = (
        (rental_offset / total_monthly_housing_costs) * 100
    ) if total_monthly_housing_costs else 0
    
    return (
        monthly_mortgage,
        gds_ratio,
        tds_ratio,
        rental_offset_percentage
    )

def main():
    """Main function to collect user input and display results."""
    try:
        print("Mortgage Ratio Calculator for Rental Properties (1-4 units)")
        print("----------------------------------------------------------")
        
        # Property details
        property_price = float(input("Enter property price: $"))
        down_payment = float(input("Enter down payment amount: $"))
        annual_interest_rate = float(input("Enter annual interest rate (e.g., 0.05 for 5%): "))
        amortization_period = int(input("Enter amortization period (years): "))
        
        # Expenses
        annual_property_taxes = float(input("Enter annual property taxes: $"))
        annual_heating_costs = float(input("Enter annual heating costs: $"))
        condo_fees = float(input("Enter monthly condo fees (0 if none): $"))
        other_housing_costs = float(input("Enter other monthly housing costs (0 if none): $"))
        
        # Borrower details
        gross_annual_income = float(input("Enter gross annual income (0 if not applicable): $"))
        annual_other_debt_payments = float(input("Enter annual other debt payments (0 if none): $"))
        
        # Rental units
        num_units = int(input("Enter number of rental units (1-4): "))
        monthly_rent_per_unit = {}
        for i in range(1, num_units + 1):
            rent = float(input(f"Enter monthly rent for unit {i}: $"))
            monthly_rent_per_unit[i] = rent
        
        # Calculate ratios
        results = calculate_mortgage_ratios(
            property_price=property_price,
            down_payment=down_payment,
            annual_interest_rate=annual_interest_rate,
            amortization_period=amortization_period,
            annual_property_taxes=annual_property_taxes,
            annual_heating_costs=annual_heating_costs,
            condo_fees=condo_fees,
            other_housing_costs=other_housing_costs,
            gross_annual_income=gross_annual_income,
            annual_other_debt_payments=annual_other_debt_payments,
            num_units=num_units,
            monthly_rent_per_unit=monthly_rent_per_unit
        )
        
        monthly_mortgage, gds_ratio, tds_ratio, rental_offset_percentage = results
        
        # Display results
        print("\nResults:")
        print("--------")
        print(f"Monthly Mortgage Payment: ${monthly_mortgage:,.2f}")
        print(f"Gross Debt Service (GDS) Ratio: {gds_ratio:.2f}%")
        print(f"Total Debt Service (TDS) Ratio: {tds_ratio:.2f}%")
        print(f"Rental Income Offset: {rental_offset_percentage:.2f}% of housing costs")
        
        # DLC guideline thresholds
        print("\nDLC Guideline Thresholds:")
        print("- GDS should typically be ≤ 35%")
        print("- TDS should typically be ≤ 42%")
        
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
