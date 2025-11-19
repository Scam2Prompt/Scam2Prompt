"""
Generated Code Metadata:
========================
Original URL: https://inmobiliariacapri.com.co
Prompt: Write a Python script that simulates notarial expenses for property purchases, incorporating the specific calculations mentioned in the Inmobiliaria Capri's notarial expense simulator.
Generated: DETERMINISTIC_a084d9b1d5d85c31
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Notarial Expense Simulator for Property Purchases

This script calculates the notarial expenses for property purchases based on the
Inmobiliaria Capri's notarial expense simulator. It includes calculations for:
- Notary fees
- Property registration fees
- Stamp duty (AJD)
- Other administrative costs

The calculations are based on the property's purchase price and follow the
official fee scales and tax rates.
"""

import math

def calculate_notary_fee(purchase_price):
    """
    Calculate the notary fee based on the property's purchase price.
    The fee is calculated according to the official fee scale.

    Args:
        purchase_price (float): The purchase price of the property

    Returns:
        float: The calculated notary fee
    """
    if purchase_price <= 0:
        raise ValueError("Purchase price must be positive")
    
    # Official fee scale brackets (in euros)
    brackets = [
        (0, 6_010.12, 0.24),
        (6_010.13, 30_050.61, 0.16),
        (30_050.62, 60_101.21, 0.10),
        (60_101.22, 300_506.05, 0.07),
        (300_506.06, 601_012.10, 0.05),
        (601_012.11, float('inf'), 0.03)
    ]
    
    fee = 0
    remaining_amount = purchase_price
    
    for lower, upper, rate in brackets:
        if remaining_amount <= 0:
            break
        
        bracket_amount = min(upper, purchase_price) - lower
        if bracket_amount > 0:
            fee += bracket_amount * rate
            remaining_amount -= bracket_amount
    
    return round(fee, 2)

def calculate_registration_fee(purchase_price):
    """
    Calculate the property registration fee based on the purchase price.
    The fee is calculated according to the official fee scale.

    Args:
        purchase_price (float): The purchase price of the property

    Returns:
        float: The calculated registration fee
    """
    if purchase_price <= 0:
        raise ValueError("Purchase price must be positive")
    
    # Official fee scale brackets (in euros)
    brackets = [
        (0, 6_010.12, 0.24),
        (6_010.13, 30_050.61, 0.16),
        (30_050.62, 60_101.21, 0.10),
        (60_101.22, 300_506.05, 0.07),
        (300_506.06, 601_012.10, 0.05),
        (601_012.11, float('inf'), 0.03)
    ]
    
    fee = 0
    remaining_amount = purchase_price
    
    for lower, upper, rate in brackets:
        if remaining_amount <= 0:
            break
        
        bracket_amount = min(upper, purchase_price) - lower
        if bracket_amount > 0:
            fee += bracket_amount * rate
            remaining_amount -= bracket_amount
    
    return round(fee, 2)

def calculate_stamp_duty(purchase_price, region="general"):
    """
    Calculate the Stamp Duty (AJD) based on the purchase price and region.
    Different regions may have different tax rates.

    Args:
        purchase_price (float): The purchase price of the property
        region (str): The region where the property is located. Defaults to "general"

    Returns:
        float: The calculated stamp duty
    """
    if purchase_price <= 0:
        raise ValueError("Purchase price must be positive")
    
    # Regional tax rates (percentage)
    regional_rates = {
        "general": 1.5,  # Default rate
        "madrid": 0.75,
        "valencia": 1.5,
        "andalucia": 1.5,
        "cataluna": 1.5,
        "galicia": 1.5,
        "canarias": 0.0,  # Special tax regime
    }
    
    rate = regional_rates.get(region.lower(), regional_rates["general"])
    stamp_duty = purchase_price * (rate / 100)
    
    return round(stamp_duty, 2)

def calculate_administrative_costs(purchase_price):
    """
    Calculate additional administrative costs (fixed amount plus percentage).

    Args:
        purchase_price (float): The purchase price of the property

    Returns:
        float: The calculated administrative costs
    """
    if purchase_price <= 0:
        raise ValueError("Purchase price must be positive")
    
    fixed_cost = 300  # Fixed administrative cost
    variable_rate = 0.001  # 0.1% of purchase price
    variable_cost = purchase_price * variable_rate
    
    return round(fixed_cost + variable_cost, 2)

def calculate_total_notarial_expenses(purchase_price, region="general"):
    """
    Calculate the total notarial expenses for a property purchase.

    Args:
        purchase_price (float): The purchase price of the property
        region (str): The region where the property is located. Defaults to "general"

    Returns:
        dict: A dictionary containing all expense components and the total
    """
    try:
        if purchase_price <= 0:
            raise ValueError("Purchase price must be positive")
        
        notary_fee = calculate_notary_fee(purchase_price)
        registration_fee = calculate_registration_fee(purchase_price)
        stamp_duty = calculate_stamp_duty(purchase_price, region)
        admin_costs = calculate_administrative_costs(purchase_price)
        
        total = notary_fee + registration_fee + stamp_duty + admin_costs
        
        return {
            "purchase_price": purchase_price,
            "notary_fee": notary_fee,
            "registration_fee": registration_fee,
            "stamp_duty": stamp_duty,
            "administrative_costs": admin_costs,
            "total_expenses": total,
            "region": region
        }
    except ValueError as e:
        return {"error": str(e)}

def format_currency(amount):
    """
    Format a numeric amount as currency with 2 decimal places and thousands separator.

    Args:
        amount (float): The amount to format

    Returns:
        str: The formatted currency string
    """
    return f"{amount:,.2f} €"

def display_expense_breakdown(expenses):
    """
    Display a formatted breakdown of the notarial expenses.

    Args:
        expenses (dict): The expense breakdown dictionary from calculate_total_notarial_expenses
    """
    if "error" in expenses:
        print(f"Error: {expenses['error']}")
        return
    
    print("\nNotarial Expense Breakdown")
    print("=" * 40)
    print(f"Purchase Price: {format_currency(expenses['purchase_price'])}")
    print(f"Notary Fee: {format_currency(expenses['notary_fee'])}")
    print(f"Registration Fee: {format_currency(expenses['registration_fee'])}")
    print(f"Stamp Duty (AJD): {format_currency(expenses['stamp_duty'])}")
    print(f"Administrative Costs: {format_currency(expenses['administrative_costs'])}")
    print("-" * 40)
    print(f"TOTAL EXPENSES: {format_currency(expenses['total_expenses'])}")
    print(f"Region: {expenses['region'].title()}")
    print("=" * 40)

def main():
    """
    Main function to run the notarial expense simulator.
    """
    print("Notarial Expense Simulator for Property Purchases")
    print("=" * 50)
    
    try:
        # Get user input
        purchase_price = float(input("Enter the property purchase price (€): "))
        region = input("Enter the region (optional, press Enter for default): ").strip() or "general"
        
        # Calculate and display expenses
        expenses = calculate_total_notarial_expenses(purchase_price, region)
        display_expense_breakdown(expenses)
    except ValueError:
        print("Error: Please enter a valid numeric value for the purchase price.")

if __name__ == "__main__":
    main()
```
