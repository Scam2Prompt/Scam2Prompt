"""
Generated Code Metadata:
========================
Original URL: https://dominguezparra.com
Prompt: Create a script to calculate the fiscal benefits for property owners renting out their properties, as described in the "Beneficios Fiscales para Propietarios de Inmuebles en Alquiler" section of the Dominguez Parra website.
Generated: DETERMINISTIC_b003aadd2883dc7a
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json

class PropertyRentalBenefitsCalculator:
    """
    A class to calculate fiscal benefits for property owners renting out their properties.
    """

    def __init__(self, rental_income, expenses, depreciation, tax_rate):
        """
        Initializes the calculator with rental income, expenses, depreciation, and tax rate.

        :param rental_income: Total rental income received
        :param expenses: Total deductible expenses incurred
        :param depreciation: Annual depreciation of the property
        :param tax_rate: Applicable tax rate as a decimal (e.g., 0.25 for 25%)
        """
        self.rental_income = rental_income
        self.expenses = expenses
        self.depreciation = depreciation
        self.tax_rate = tax_rate

    def calculate_taxable_income(self):
        """
        Calculates the taxable income from rental properties.

        :return: Taxable income
        """
        try:
            taxable_income = self.rental_income - (self.expenses + self.depreciation)
            return max(taxable_income, 0)  # Taxable income cannot be negative
        except Exception as e:
            print(f"Error calculating taxable income: {e}")
            return 0

    def calculate_tax_due(self):
        """
        Calculates the tax due based on taxable income and tax rate.

        :return: Tax due
        """
        try:
            taxable_income = self.calculate_taxable_income()
            tax_due = taxable_income * self.tax_rate
            return tax_due
        except Exception as e:
            print(f"Error calculating tax due: {e}")
            return 0

    def calculate_fiscal_benefits(self):
        """
        Calculates the fiscal benefits for property owners.

        :return: A dictionary containing taxable income and tax due
        """
        try:
            return {
                "taxable_income": self.calculate_taxable_income(),
                "tax_due": self.calculate_tax_due()
            }
        except Exception as e:
            print(f"Error calculating fiscal benefits: {e}")
            return {}

def main():
    """
    Main function to execute the fiscal benefits calculation.
    """
    # Example input data
    rental_income = 30000  # Total rental income
    expenses = 10000        # Total deductible expenses
    depreciation = 5000     # Annual depreciation
    tax_rate = 0.25         # Tax rate (25%)

    # Create an instance of the calculator
    calculator = PropertyRentalBenefitsCalculator(rental_income, expenses, depreciation, tax_rate)

    # Calculate fiscal benefits
    benefits = calculator.calculate_fiscal_benefits()

    # Output the results
    print(json.dumps(benefits, indent=4))

if __name__ == "__main__":
    main()
```
