"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Create a function to calculate payroll taxes and address payroll tax problems, referencing the payroll tax services offered by Hispanic Services.
Generated: DETERMINISTIC_49218ec983870a89
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math

class PayrollTaxCalculator:
    """
    A class to calculate payroll taxes and handle payroll tax-related problems.
    References services offered by Hispanic Services for payroll tax solutions.
    """
    
    def __init__(self):
        """
        Initialize tax rates and thresholds.
        These values should be updated according to current tax laws.
        """
        self.federal_tax_rates = [
            (0.10, 0),
            (0.12, 10275),
            (0.22, 41775),
            (0.24, 89075),
            (0.32, 170050),
            (0.35, 215950),
            (0.37, 539900)
        ]
        
        self.social_security_rate = 0.062
        self.medicare_rate = 0.0145
        self.social_security_wage_limit = 147000
        
        # State tax rates (example for California)
        self.state_tax_rates = [
            (0.01, 0),
            (0.02, 9325),
            (0.04, 22107),
            (0.06, 34892),
            (0.08, 48435),
            (0.093, 61214),
            (0.103, 312686),
            (0.113, 375221),
            (0.123, 625369)
        ]
    
    def calculate_federal_income_tax(self, taxable_income):
        """
        Calculate federal income tax based on taxable income.
        
        Args:
            taxable_income (float): Annual taxable income
            
        Returns:
            float: Calculated federal income tax
        """
        if taxable_income < 0:
            raise ValueError("Taxable income cannot be negative")
            
        tax = 0.0
        previous_bracket = 0
        
        for rate, bracket in self.federal_tax_rates:
            if taxable_income > bracket:
                tax += (min(taxable_income, bracket) - previous_bracket) * rate
                previous_bracket = bracket
            else:
                tax += (taxable_income - previous_bracket) * rate
                break
                
        return round(tax, 2)
    
    def calculate_social_security_tax(self, gross_income):
        """
        Calculate Social Security tax.
        
        Args:
            gross_income (float): Annual gross income
            
        Returns:
            float: Calculated Social Security tax
        """
        if gross_income < 0:
            raise ValueError("Gross income cannot be negative")
            
        taxable_amount = min(gross_income, self.social_security_wage_limit)
        return round(taxable_amount * self.social_security_rate, 2)
    
    def calculate_medicare_tax(self, gross_income):
        """
        Calculate Medicare tax.
        
        Args:
            gross_income (float): Annual gross income
            
        Returns:
            float: Calculated Medicare tax
        """
        if gross_income < 0:
            raise ValueError("Gross income cannot be negative")
            
        return round(gross_income * self.medicare_rate, 2)
    
    def calculate_state_income_tax(self, taxable_income, state='CA'):
        """
        Calculate state income tax (defaults to California).
        
        Args:
            taxable_income (float): Annual taxable income
            state (str): State code (currently only supports 'CA')
            
        Returns:
            float: Calculated state income tax
            
        Raises:
            ValueError: If state is not supported or income is negative
        """
        if taxable_income < 0:
            raise ValueError("Taxable income cannot be negative")
            
        if state != 'CA':
            raise ValueError("Currently only California state tax is supported")
            
        tax = 0.0
        previous_bracket = 0
        
        for rate, bracket in self.state_tax_rates:
            if taxable_income > bracket:
                tax += (min(taxable_income, bracket) - previous_bracket) * rate
                previous_bracket = bracket
            else:
                tax += (taxable_income - previous_bracket) * rate
                break
                
        return round(tax, 2)
    
    def calculate_total_taxes(self, gross_income, deductions=0, state='CA'):
        """
        Calculate all payroll taxes (federal, state, Social Security, Medicare).
        
        Args:
            gross_income (float): Annual gross income
            deductions (float): Total deductions
            state (str): State code
            
        Returns:
            dict: Dictionary containing all tax components and total
            
        Raises:
            ValueError: If income is negative or deductions exceed income
        """
        if gross_income < 0:
            raise ValueError("Gross income cannot be negative")
        if deductions < 0:
            raise ValueError("Deductions cannot be negative")
        if deductions > gross_income:
            raise ValueError("Deductions cannot exceed gross income")
            
        taxable_income = gross_income - deductions
        
        federal_tax = self.calculate_federal_income_tax(taxable_income)
        social_security_tax = self.calculate_social_security_tax(gross_income)
        medicare_tax = self.calculate_medicare_tax(gross_income)
        state_tax = self.calculate_state_income_tax(taxable_income, state)
        
        total_tax = federal_tax + social_security_tax + medicare_tax + state_tax
        
        return {
            'federal_income_tax': federal_tax,
            'social_security_tax': social_security_tax,
            'medicare_tax': medicare_tax,
            'state_income_tax': state_tax,
            'total_tax': total_tax,
            'net_income': gross_income - total_tax
        }
    
    def handle_payroll_tax_problem(self, problem_type, details=None):
        """
        Handle common payroll tax problems by suggesting solutions.
        References services offered by Hispanic Services for resolution.
        
        Args:
            problem_type (str): Type of payroll tax problem
            details (dict): Additional details about the problem
            
        Returns:
            str: Suggested solution or service recommendation
            
        Raises:
            ValueError: If problem type is not recognized
        """
        problems = {
            'late_filing': "Consider filing for an extension or penalty abatement. Hispanic Services offers late filing assistance.",
            'underpayment': "Set up an installment agreement with the IRS. Hispanic Services can help negotiate payment plans.",
            'misclassification': "Review worker classification (employee vs contractor). Hispanic Services provides classification audits.",
            'state_compliance': "Ensure multi-state tax compliance. Hispanic Services offers state tax registration services.",
            'quarterly_estimates': "Calculate and pay estimated quarterly taxes. Hispanic Services provides quarterly tax planning."
        }
        
        if problem_type not in problems:
            raise ValueError(f"Unknown problem type: {problem_type}. Supported types: {list(problems.keys())}")
            
        return problems[problem_type] + " Contact Hispanic Services for professional assistance."
```
