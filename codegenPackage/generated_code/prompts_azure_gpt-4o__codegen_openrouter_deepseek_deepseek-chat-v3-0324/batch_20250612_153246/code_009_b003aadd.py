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
"""
Script to calculate fiscal benefits for property owners renting out their properties.
Based on the "Beneficios Fiscales para Propietarios de Inmuebles en Alquiler" section.

Calculates:
1. Deductible expenses
2. Taxable base reduction
3. Final tax liability
"""

import math
from typing import Dict, Union, Optional

class PropertyRentalTaxCalculator:
    """
    Calculator for fiscal benefits on rental properties.
    
    Attributes:
        rental_income (float): Annual rental income
        property_value (float): Fiscal value of the property
        expenses (Dict[str, float]): Dictionary of deductible expenses
        is_primary_residence (bool): Whether property is primary residence
        owner_age (Optional[int]): Age of property owner (for age-based deductions)
    """
    
    def __init__(
        self,
        rental_income: float,
        property_value: float,
        expenses: Dict[str, float],
        is_primary_residence: bool = False,
        owner_age: Optional[int] = None
    ):
        """
        Initialize calculator with property and owner details.
        
        Args:
            rental_income: Annual rental income in local currency
            property_value: Fiscal value of property in local currency
            expenses: Dictionary of deductible expenses with categories as keys
            is_primary_residence: Whether property is primary residence
            owner_age: Age of property owner (optional)
        """
        self.rental_income = rental_income
        self.property_value = property_value
        self.expenses = expenses
        self.is_primary_residence = is_primary_residence
        self.owner_age = owner_age
        
        # Validate inputs
        if rental_income <= 0:
            raise ValueError("Rental income must be positive")
        if property_value <= 0:
            raise ValueError("Property value must be positive")
        if any(expense < 0 for expense in expenses.values()):
            raise ValueError("Expenses cannot be negative")
        if owner_age is not None and owner_age <= 0:
            raise ValueError("Owner age must be positive if provided")

    def calculate_deductible_expenses(self) -> float:
        """
        Calculate total deductible expenses based on rental regulations.
        
        Returns:
            Total deductible expenses amount
        """
        # Standard deductions (maintenance, taxes, etc.)
        standard_deductions = sum(self.expenses.values())
        
        # Additional deductions for primary residence
        if self.is_primary_residence:
            standard_deductions += self.property_value * 0.02  # 2% of property value
        
        # Cap deductions at 60% of rental income
        max_deduction = self.rental_income * 0.6
        return min(standard_deductions, max_deduction)

    def calculate_taxable_base_reduction(self) -> float:
        """
        Calculate reduction to taxable base based on owner's age.
        
        Returns:
            Amount to reduce taxable base by
        """
        if self.owner_age is None:
            return 0.0
            
        # Age-based reductions
        if self.owner_age >= 65:
            return self.rental_income * 0.4  # 40% reduction
        elif self.owner_age >= 75:
            return self.rental_income * 0.6  # 60% reduction
        return 0.0

    def calculate_taxable_income(self) -> float:
        """
        Calculate final taxable income after all deductions and reductions.
        
        Returns:
            Taxable income amount
        """
        deductible_expenses = self.calculate_deductible_expenses()
        taxable_base = self.rental_income - deductible_expenses
        reduction = self.calculate_taxable_base_reduction()
        return max(0, taxable_base - reduction)

    def calculate_tax_liability(self, tax_rate: float = 0.19) -> float:
        """
        Calculate final tax liability based on taxable income.
        
        Args:
            tax_rate: Applicable tax rate (default 19%)
            
        Returns:
            Tax liability amount
        """
        if not 0 <= tax_rate <= 1:
            raise ValueError("Tax rate must be between 0 and 1")
            
        taxable_income = self.calculate_taxable_income()
        return taxable_income * tax_rate

    def generate_report(self) -> Dict[str, Union[float, Dict[str, float]]]:
        """
        Generate comprehensive report of all calculations.
        
        Returns:
            Dictionary containing all calculation results
        """
        return {
            "rental_income": self.rental_income,
            "property_value": self.property_value,
            "expenses": self.expenses,
            "deductible_expenses": self.calculate_deductible_expenses(),
            "taxable_base_reduction": self.calculate_taxable_base_reduction(),
            "taxable_income": self.calculate_taxable_income(),
            "tax_liability": self.calculate_tax_liability(),
            "is_primary_residence": self.is_primary_residence,
            "owner_age": self.owner_age
        }


# Example usage
if __name__ == "__main__":
    try:
        # Sample property data
        calculator = PropertyRentalTaxCalculator(
            rental_income=24000,  # €2,000/month
            property_value=300000,
            expenses={
                "maintenance": 2000,
                "property_tax": 1200,
                "insurance": 600,
                "utilities": 1800
            },
            is_primary_residence=False,
            owner_age=68
        )
        
        # Generate and print report
        report = calculator.generate_report()
        for key, value in report.items():
            if isinstance(value, dict):
                print(f"{key}:")
                for subkey, subvalue in value.items():
                    print(f"  {subkey}: {subvalue:,.2f}")
            else:
                print(f"{key}: {value:,.2f}" if isinstance(value, (int, float)) else f"{key}: {value}")
                
    except ValueError as e:
        print(f"Error in calculation: {e}")
```
