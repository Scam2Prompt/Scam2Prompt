"""
Generated Code Metadata:
========================
Original URL: https://www.aulacontable.com
Prompt: Create a Python script to simulate the calculation of income tax for individuals, based on the "Impuesto a la renta persona natural" course from AulaContable.
Generated: DETERMINISTIC_dc5f3cb704ecce9e
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Income Tax Calculator for Individuals (Natural Persons) based on Ecuadorian tax laws.

This script calculates the income tax for individuals based on the progressive tax brackets
defined by the Ecuadorian tax authority (SRI). It considers deductions for dependents and
other allowable expenses as per the tax regulations.

Tax brackets and rates are based on the latest available information from AulaContable.
"""

class IncomeTaxCalculator:
    """
    A class to calculate income tax for natural persons in Ecuador.
    
    Attributes:
        tax_brackets (list): List of tuples representing tax brackets and rates.
        dependent_deduction (float): Fixed deduction amount per dependent.
        base_fraction (float): Base fraction for tax calculation.
    """
    
    def __init__(self):
        """Initialize the tax calculator with current tax brackets and rates."""
        self.tax_brackets = [
            (0, 11902, 0, 0),
            (11902, 15159, 0.05, 596),
            (15159, 19682, 0.10, 750),
            (19682, 26031, 0.12, 1092),
            (26031, 34255, 0.15, 1794),
            (34255, 45407, 0.20, 2883),
            (45407, 60407, 0.25, 4320),
            (60407, 80605, 0.30, 6300),
            (80605, 107201, 0.35, 9000),
            (107201, float('inf'), 0.37, 12600)
        ]
        self.dependent_deduction = 1750  # USD per dependent
        self.base_fraction = 0.5  # 50% of income considered for tax calculation
    
    def calculate_taxable_income(self, gross_income, num_dependents=0, other_deductions=0):
        """
        Calculate the taxable income after applying deductions.
        
        Args:
            gross_income (float): Total annual income before deductions.
            num_dependents (int): Number of dependents (default 0).
            other_deductions (float): Other allowable deductions (default 0).
            
        Returns:
            float: Taxable income after deductions.
        """
        try:
            if gross_income < 0:
                raise ValueError("Gross income cannot be negative")
            if num_dependents < 0:
                raise ValueError("Number of dependents cannot be negative")
            if other_deductions < 0:
                raise ValueError("Other deductions cannot be negative")
                
            dependent_deductions = num_dependents * self.dependent_deduction
            taxable_income = (gross_income * self.base_fraction) - dependent_deductions - other_deductions
            return max(0, taxable_income)  # Taxable income can't be negative
        except (TypeError, ValueError) as e:
            print(f"Error calculating taxable income: {e}")
            return 0
    
    def calculate_tax(self, taxable_income):
        """
        Calculate the tax amount based on taxable income and tax brackets.
        
        Args:
            taxable_income (float): The taxable income after deductions.
            
        Returns:
            float: The calculated tax amount.
        """
        try:
            if taxable_income < 0:
                raise ValueError("Taxable income cannot be negative")
                
            tax = 0
            for bracket in self.tax_brackets:
                lower, upper, rate, base_tax = bracket
                if taxable_income > lower:
                    bracket_amount = min(taxable_income, upper) - lower
                    tax += bracket_amount * rate
                else:
                    break
            
            # Apply the base tax from the highest applicable bracket
            for bracket in reversed(self.tax_brackets):
                if taxable_income > bracket[0]:
                    tax += bracket[3]
                    break
            
            return tax
        except (TypeError, ValueError) as e:
            print(f"Error calculating tax: {e}")
            return 0
    
    def calculate_net_income(self, gross_income, num_dependents=0, other_deductions=0):
        """
        Calculate the net income after tax deductions.
        
        Args:
            gross_income (float): Total annual income before deductions.
            num_dependents (int): Number of dependents (default 0).
            other_deductions (float): Other allowable deductions (default 0).
            
        Returns:
            float: Net income after tax.
        """
        try:
            taxable_income = self.calculate_taxable_income(gross_income, num_dependents, other_deductions)
            tax = self.calculate_tax(taxable_income)
            return gross_income - tax
        except Exception as e:
            print(f"Error calculating net income: {e}")
            return 0


def main():
    """Main function to demonstrate the tax calculator."""
    calculator = IncomeTaxCalculator()
    
    print("Ecuadorian Income Tax Calculator for Natural Persons")
    print("---------------------------------------------------")
    
    try:
        gross_income = float(input("Enter your annual gross income (USD): "))
        num_dependents = int(input("Enter number of dependents: "))
        other_deductions = float(input("Enter other allowable deductions (USD): "))
        
        taxable_income = calculator.calculate_taxable_income(gross_income, num_dependents, other_deductions)
        tax = calculator.calculate_tax(taxable_income)
        net_income = calculator.calculate_net_income(gross_income, num_dependents, other_deductions)
        
        print("\nTax Calculation Results:")
        print(f"Taxable Income: ${taxable_income:,.2f}")
        print(f"Income Tax: ${tax:,.2f}")
        print(f"Net Income: ${net_income:,.2f}")
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
