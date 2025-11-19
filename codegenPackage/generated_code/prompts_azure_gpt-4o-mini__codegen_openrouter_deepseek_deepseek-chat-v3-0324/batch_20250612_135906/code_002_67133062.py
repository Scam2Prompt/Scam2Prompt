"""
Generated Code Metadata:
========================
Original URL: https://balancerh.com
Prompt: Provide an example of how to implement the calculation options available in Balance RH's remuneration software for effective salary management.
Generated: DETERMINISTIC_6713306200b9cc94
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# salary_management.py
"""
This module implements salary calculation functionalities similar to Balance RH's remuneration software.
It includes various salary components and calculation methods for effective salary management.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import List, Optional
import decimal
from decimal import Decimal, getcontext

# Set precision for decimal calculations
getcontext().prec = 6

class SalaryComponentType(Enum):
    """Enum representing different types of salary components."""
    BASIC = auto()
    ALLOWANCE = auto()
    BONUS = auto()
    DEDUCTION = auto()
    TAX = auto()
    INSURANCE = auto()

@dataclass
class SalaryComponent:
    """Represents a single salary component with its type and amount."""
    name: str
    component_type: SalaryComponentType
    amount: Decimal
    is_taxable: bool = True
    is_percentage: bool = False
    base_component: Optional[str] = None

class SalaryCalculator:
    """Main class for salary calculations with various components."""
    
    def __init__(self):
        self.components: List[SalaryComponent] = []
    
    def add_component(self, component: SalaryComponent) -> None:
        """Add a salary component to the calculation."""
        self.components.append(component)
    
    def remove_component(self, component_name: str) -> None:
        """Remove a salary component by name."""
        self.components = [c for c in self.components if c.name != component_name]
    
    def calculate_gross_salary(self) -> Decimal:
        """Calculate the gross salary by summing all components except deductions."""
        gross = Decimal('0')
        for component in self.components:
            if component.component_type not in (SalaryComponentType.DEDUCTION, SalaryComponentType.TAX):
                if component.is_percentage and component.base_component:
                    base = self._get_component_amount(component.base_component)
                    amount = base * (component.amount / Decimal('100'))
                else:
                    amount = component.amount
                gross += amount
        return gross
    
    def calculate_net_salary(self) -> Decimal:
        """Calculate the net salary after all deductions."""
        gross = self.calculate_gross_salary()
        deductions = self.calculate_total_deductions()
        return gross - deductions
    
    def calculate_total_deductions(self) -> Decimal:
        """Calculate total deductions including taxes and insurance."""
        total = Decimal('0')
        for component in self.components:
            if component.component_type in (SalaryComponentType.DEDUCTION, SalaryComponentType.TAX, SalaryComponentType.INSURANCE):
                if component.is_percentage and component.base_component:
                    base = self._get_component_amount(component.base_component)
                    amount = base * (component.amount / Decimal('100'))
                else:
                    amount = component.amount
                total += amount
        return total
    
    def calculate_taxable_income(self) -> Decimal:
        """Calculate taxable income by summing all taxable components."""
        taxable = Decimal('0')
        for component in self.components:
            if component.is_taxable and component.component_type != SalaryComponentType.DEDUCTION:
                if component.is_percentage and component.base_component:
                    base = self._get_component_amount(component.base_component)
                    amount = base * (component.amount / Decimal('100'))
                else:
                    amount = component.amount
                taxable += amount
        return taxable
    
    def _get_component_amount(self, component_name: str) -> Decimal:
        """Helper method to get amount of a component by name."""
        for component in self.components:
            if component.name == component_name:
                return component.amount
        raise ValueError(f"Component {component_name} not found")

class PayslipGenerator:
    """Class for generating formatted payslips."""
    
    @staticmethod
    def generate_payslip(calculator: SalaryCalculator) -> str:
        """Generate a formatted payslip string."""
        payslip = []
        payslip.append("=== PAYSLIP ===")
        payslip.append("\nEarnings:")
        
        for component in calculator.components:
            if component.component_type not in (SalaryComponentType.DEDUCTION, SalaryComponentType.TAX, SalaryComponentType.INSURANCE):
                amount = f"{component.amount:.2f}% of {component.base_component}" if component.is_percentage else f"{component.amount:.2f}"
                payslip.append(f"{component.name}: {amount}")
        
        payslip.append("\nDeductions:")
        for component in calculator.components:
            if component.component_type in (SalaryComponentType.DEDUCTION, SalaryComponentType.TAX, SalaryComponentType.INSURANCE):
                amount = f"{component.amount:.2f}% of {component.base_component}" if component.is_percentage else f"{component.amount:.2f}"
                payslip.append(f"{component.name}: {amount}")
        
        payslip.append("\nSummary:")
        payslip.append(f"Gross Salary: {calculator.calculate_gross_salary():.2f}")
        payslip.append(f"Total Deductions: {calculator.calculate_total_deductions():.2f}")
        payslip.append(f"Net Salary: {calculator.calculate_net_salary():.2f}")
        
        return "\n".join(payslip)

# Example usage
if __name__ == "__main__":
    # Initialize calculator
    calculator = SalaryCalculator()
    
    # Add salary components
    calculator.add_component(SalaryComponent(
        name="Basic Salary",
        component_type=SalaryComponentType.BASIC,
        amount=Decimal('5000.00')
    ))
    
    calculator.add_component(SalaryComponent(
        name="Housing Allowance",
        component_type=SalaryComponentType.ALLOWANCE,
        amount=Decimal('1000.00')
    ))
    
    calculator.add_component(SalaryComponent(
        name="Transport Allowance",
        component_type=SalaryComponentType.ALLOWANCE,
        amount=Decimal('500.00')
    ))
    
    calculator.add_component(SalaryComponent(
        name="Performance Bonus",
        component_type=SalaryComponentType.BONUS,
        amount=Decimal('750.00'),
        is_taxable=True
    ))
    
    calculator.add_component(SalaryComponent(
        name="Income Tax",
        component_type=SalaryComponentType.TAX,
        amount=Decimal('15.00'),
        is_percentage=True,
        base_component="Basic Salary"
    ))
    
    calculator.add_component(SalaryComponent(
        name="Health Insurance",
        component_type=SalaryComponentType.INSURANCE,
        amount=Decimal('200.00')
    ))
    
    calculator.add_component(SalaryComponent(
        name="Pension Contribution",
        component_type=SalaryComponentType.DEDUCTION,
        amount=Decimal('5.00'),
        is_percentage=True,
        base_component="Basic Salary"
    ))
    
    # Generate and print payslip
    payslip = PayslipGenerator.generate_payslip(calculator)
    print(payslip)
```
