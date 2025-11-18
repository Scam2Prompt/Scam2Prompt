"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dominguezparra.com
Prompt: Create a script to calculate the fiscal benefits for property owners renting out their properties, as described in the "Beneficios Fiscales para Propietarios de Inmuebles en Alquiler" section of the Dominguez Parra website.
Generated: DETERMINISTIC_b003aadd2883dc7a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate fiscal benefits for property owners renting out their properties.
This script is based on typical tax benefit calculations and should be updated to reflect
the specific rules outlined in the "Beneficios Fiscales para Propietarios de Inmuebles en Alquiler"
section of the Dominguez Parra website.
"""

import logging

# Set up logging for debugging and error handling
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FiscalBenefitsCalculator:
    """
    A class to calculate fiscal benefits for property owners renting out their properties.
    """
    
    def __init__(self, rental_income, deductible_expenses, tax_rate, additional_discount_rate=0):
        """
        Initialize the calculator with rental income, expenses, and applicable tax rates.

        Args:
            rental_income (float): Total income generated from renting the property.
            deductible_expenses (float): Total deductible expenses associated with the property.
            tax_rate (float): Applicable tax rate as a percentage (e.g., 20 for 20%).
            additional_discount_rate (float, optional): Additional discount rate for fiscal calculations. Default: 0.
        """
        if rental_income < 0 or deductible_expenses < 0 or tax_rate < 0:
            raise ValueError("Rental income, deductible expenses, and tax rate must be non-negative.")
        
        self.rental_income = rental_income
        self.deductible_expenses = deductible_expenses
        self.tax_rate = tax_rate / 100  # Convert percentage to decimal for calculation
        self.additional_discount_rate = additional_discount_rate / 100  # Convert percentage to decimal

    def calculate_taxable_income(self):
        """
        Calculate taxable income after deducting expenses.

        Returns:
            float: Taxable income.
        """
        taxable_income = max(0, self.rental_income - self.deductible_expenses)
        logging.info(f"Calculated taxable income: {taxable_income}")
        return taxable_income

    def calculate_tax_due(self):
        """
        Calculate tax due based on taxable income and tax rate.

        Returns:
            float: Tax amount due.
        """
        taxable_income = self.calculate_taxable_income()
        tax_due = taxable_income * self.tax_rate
        logging.info(f"Calculated tax due: {tax_due}")
        return tax_due

    def calculate_fiscal_benefits(self):
        """
        Calculate fiscal benefits considering additional discounts.

        Returns:
            float: Total fiscal benefits.
        """
        tax_due = self.calculate_tax_due()
        discount = tax_due * self.additional_discount_rate
        fiscal_benefits = tax_due - discount
        logging.info(f"Calculated fiscal benefits: {fiscal_benefits}")
        return fiscal_benefits


# Main script execution
def main():
    try:
        # Example property data (these values should be provided by the user or a database)
        rental_income = float(input("Enter the total rental income (in EUR): "))
        deductible_expenses = float(input("Enter the total deductible expenses (in EUR): "))
        tax_rate = float(input("Enter the applicable tax rate (as a percentage): "))
        additional_discount_rate = float(input("Enter any additional discount rate (as a percentage, optional): ") or 0)

        # Create an instance of the calculator
        calculator = FiscalBenefitsCalculator(rental_income, deductible_expenses, tax_rate, additional_discount_rate)
        
        # Perform calculations
        taxable_income = calculator.calculate_taxable_income()
        tax_due = calculator.calculate_tax_due()
        fiscal_benefits = calculator.calculate_fiscal_benefits()

        # Display results
        print(f"\nResults:")
        print(f"Taxable Income: €{taxable_income:.2f}")
        print(f"Tax Due: €{tax_due:.2f}")
        print(f"Fiscal Benefits: €{fiscal_benefits:.2f}")

    except ValueError as ve:
        logging.error(f"Input Error: {ve}")
        print(f"Error: {ve}")
    except Exception as e:
        logging.error(f"Unexpected Error: {e}")
        print(f"An unexpected error occurred: {e}")


# Entry point of the script
if __name__ == "__main__":
    main()
```
