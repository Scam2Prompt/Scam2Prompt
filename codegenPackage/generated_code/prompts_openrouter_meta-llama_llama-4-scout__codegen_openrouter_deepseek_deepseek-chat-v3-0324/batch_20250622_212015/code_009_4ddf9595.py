"""
Generated Code Metadata:
========================
Original URL: https://generalearnings.com
Prompt: Write a code snippet to implement a taxation system for an investment firm like General Earnings, which helps fund public works and services.
Generated: DETERMINISTIC_4ddf959579cb8b73
Batch ID: 20250622_212015
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class TaxationSystem:
    """
    A taxation system for an investment firm to calculate taxes based on investment income.
    Taxes fund public works and services.
    """
    
    def __init__(self, tax_rates=None):
        """
        Initialize the taxation system with default or custom tax rates.
        
        Args:
            tax_rates (dict): Dictionary mapping income brackets to tax rates.
                             Example: {50000: 0.15, 100000: 0.20, float('inf'): 0.30}
        """
        self.tax_rates = tax_rates or {
            50000: 0.15,
            100000: 0.20,
            float('inf'): 0.30
        }
    
    def calculate_tax(self, income):
        """
        Calculate the tax owed based on income using progressive tax brackets.
        
        Args:
            income (float): The investment income to be taxed.
            
        Returns:
            float: The total tax amount owed.
            
        Raises:
            ValueError: If income is negative.
        """
        if income < 0:
            raise ValueError("Income cannot be negative.")
        
        tax_owed = 0.0
        previous_bracket = 0
        
        for bracket, rate in sorted(self.tax_rates.items()):
            if income <= previous_bracket:
                break
            taxable_amount = min(income - previous_bracket, bracket - previous_bracket)
            tax_owed += taxable_amount * rate
            previous_bracket = bracket
            
        return tax_owed
    
    def calculate_effective_tax_rate(self, income):
        """
        Calculate the effective tax rate (total tax / total income).
        
        Args:
            income (float): The investment income.
            
        Returns:
            float: The effective tax rate as a decimal.
            
        Raises:
            ValueError: If income is zero or negative.
        """
        if income <= 0:
            raise ValueError("Income must be positive.")
            
        tax = self.calculate_tax(income)
        return tax / income


class PublicWorksFunding:
    """
    Manages allocation of tax revenue to public works and services.
    """
    
    def __init__(self, allocation_ratios=None):
        """
        Initialize with default or custom allocation ratios.
        
        Args:
            allocation_ratios (dict): Dictionary mapping categories to allocation percentages.
                                     Example: {'education': 0.4, 'infrastructure': 0.3, 'healthcare': 0.3}
        """
        self.allocation_ratios = allocation_ratios or {
            'education': 0.4,
            'infrastructure': 0.3,
            'healthcare': 0.2,
            'other': 0.1
        }
    
    def allocate_funds(self, tax_revenue):
        """
        Allocate tax revenue to different public works categories based on predefined ratios.
        
        Args:
            tax_revenue (float): Total tax revenue to allocate.
            
        Returns:
            dict: Dictionary showing allocated amounts per category.
            
        Raises:
            ValueError: If tax_revenue is negative.
        """
        if tax_revenue < 0:
            raise ValueError("Tax revenue cannot be negative.")
            
        allocations = {}
        for category, ratio in self.allocation_ratios.items():
            allocations[category] = tax_revenue * ratio
            
        return allocations


# Example usage
if __name__ == "__main__":
    # Initialize taxation system
    tax_system = TaxationSystem()
    
    # Calculate tax for an investment income
    income = 120000
    try:
        tax = tax_system.calculate_tax(income)
        print(f"Tax owed on ${income:,.2f}: ${tax:,.2f}")
        
        # Calculate effective tax rate
        effective_rate = tax_system.calculate_effective_tax_rate(income)
        print(f"Effective tax rate: {effective_rate:.1%}")
        
        # Allocate funds to public works
        funding = PublicWorksFunding()
        allocations = funding.allocate_funds(tax)
        print("\nFunds allocated to public works:")
        for category, amount in allocations.items():
            print(f"{category.capitalize()}: ${amount:,.2f}")
            
    except ValueError as e:
        print(f"Error: {e}")
```
