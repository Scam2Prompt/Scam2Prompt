"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://carolinacapitalre.com
Prompt: Generate a script to calculate ROI for mid-size commercial and residential properties, incorporating the investment model strategy used by Carolina Capital.
Generated: DETERMINISTIC_47a9d2000ad22acf
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# roi_calculator.py
# Script to calculate ROI (Return on Investment) for mid-size commercial and residential properties.
# This script incorporates an example investment model strategy.

# Import necessary libraries
import sys

def calculate_roi(property_type, purchase_price, annual_rental_income, annual_expenses):
    """
    Calculate ROI for a property based on the investment model.

    Args:
        property_type (str): Type of property ('commercial' or 'residential').
        purchase_price (float): Total purchase price of the property.
        annual_rental_income (float): Total annual rental income from the property.
        annual_expenses (float): Total annual expenses for the property.

    Returns:
        float: ROI as a percentage.
    """
    try:
        # Validate inputs
        if purchase_price <= 0:
            raise ValueError("Purchase price must be greater than zero.")
        if annual_rental_income < 0 or annual_expenses < 0:
            raise ValueError("Rental income and expenses must be non-negative.")
        if property_type not in ['commercial', 'residential']:
            raise ValueError("Invalid property type. Choose 'commercial' or 'residential'.")

        # Calculate annual net income (income - expenses)
        annual_net_income = annual_rental_income - annual_expenses

        # Apply investment model strategy
        # Example model: ROI for commercial properties is adjusted by a 10% risk factor
        # Residential properties are adjusted by a 5% risk factor
        risk_adjustment_factor = 0.10 if property_type == 'commercial' else 0.05
        adjusted_net_income = annual_net_income * (1 - risk_adjustment_factor)

        # Calculate ROI (Net Income / Purchase Price * 100)
        roi = (adjusted_net_income / purchase_price) * 100

        return roi

    except Exception as e:
        # Handle unexpected errors gracefully
        print(f"Error: {e}")
        sys.exit(1)

def main():
    """
    Main function to gather user input and calculate ROI.
    """
    print("=== ROI Calculator ===")

    try:
        # Gather user input
        property_type = input("Enter property type ('commercial' or 'residential'): ").strip().lower()
        purchase_price = float(input("Enter purchase price of the property: "))
        annual_rental_income = float(input("Enter annual rental income: "))
        annual_expenses = float(input("Enter annual expenses: "))

        # Calculate ROI
        roi = calculate_roi(property_type, purchase_price, annual_rental_income, annual_expenses)

        # Display result
        print(f"ROI for the {property_type} property: {roi:.2f}%")

    except ValueError:
        # Handle invalid input errors
        print("Invalid input. Please ensure all values are correct and try again.")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

This script is ready to run and calculates ROI based on user input. Save it as `roi_calculator.py` and execute it in a Python environment.
