"""
Generated Code Metadata:
========================
Original URL: https://uventures.com.sg
Prompt: "Write a code snippet to calculate corporate tax in Singapore using a given set of financial data and incorporating tax planning strategies."
Generated: DETERMINISTIC_d664281db5337d11
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Corporate Tax Calculator for Singapore with Tax Planning Strategies
"""

class SingaporeCorporateTaxCalculator:
    """
    A class to calculate corporate tax liability in Singapore based on financial data
    and apply tax planning strategies to optimize tax payable.
    """
    
    def __init__(self):
        """
        Initialize tax rates and thresholds as per Singapore tax laws (2023).
        """
        # Singapore has a flat corporate tax rate with partial exemptions
        self.base_tax_rate = 0.17  # 17% flat rate
        
        # Partial tax exemption thresholds
        self.first_10k_exemption = 0.75  # 75% exemption on first 10k
        self.next_190k_exemption = 0.50  # 50% exemption on next 190k
        self.exemption_cap = 200000  # Cap for partial exemptions
        
        # Tax rebates (if any announced for the year)
        self.tax_rebate_rate = 0.0  # Default to 0, can be updated if rebate announced
        self.tax_rebate_cap = 0  # Default to 0
        
        # Capital allowances rates
        self.capital_allowance_rate = 0.0  # To be set based on asset type
        
    def calculate_taxable_income(self, financial_data):
        """
        Calculate taxable income after accounting for deductions and capital allowances.
        
        Args:
            financial_data (dict): Dictionary containing financial data
                - 'revenue': Total revenue
                - 'expenses': Allowable business expenses
                - 'capital_expenditure': Capital expenditure for the year
                - 'capital_allowance_type': Type of capital allowance to claim
        
        Returns:
            float: Taxable income after deductions
        """
        try:
            revenue = financial_data.get('revenue', 0)
            expenses = financial_data.get('expenses', 0)
            capital_expenditure = financial_data.get('capital_expenditure', 0)
            
            # Calculate capital allowance based on type
            allowance_type = financial_data.get('capital_allowance_type', 'straight_line')
            if allowance_type == 'straight_line':
                self.capital_allowance_rate = 0.2  # 20% straight line
            elif allowance_type == 'accelerated':
                self.capital_allowance_rate = 0.5  # 50% accelerated
            
            capital_allowance = capital_expenditure * self.capital_allowance_rate
            
            taxable_income = revenue - expenses - capital_allowance
            return max(0, taxable_income)  # Ensure non-negative
            
        except Exception as e:
            raise ValueError(f"Error calculating taxable income: {str(e)}")
    
    def apply_partial_exemptions(self, taxable_income):
        """
        Apply Singapore's partial tax exemptions to taxable income.
        
        Args:
            taxable_income (float): The taxable income before exemptions
            
        Returns:
            float: Taxable income after applying partial exemptions
        """
        try:
            if taxable_income <= 0:
                return 0
                
            # Calculate exempt amounts
            first_10k = min(10000, taxable_income)
            remaining_income = max(0, taxable_income - 10000)
            next_190k = min(190000, remaining_income)
            
            exempt_amount = (first_10k * self.first_10k_exemption) + \
                          (next_190k * self.next_190k_exemption)
            
            # Total exemption cannot exceed cap
            exempt_amount = min(exempt_amount, self.exemption_cap)
            
            return max(0, taxable_income - exempt_amount)
            
        except Exception as e:
            raise ValueError(f"Error applying partial exemptions: {str(e)}")
    
    def apply_tax_rebate(self, tax_payable):
        """
        Apply any announced tax rebate to the tax payable amount.
        
        Args:
            tax_payable (float): The tax amount before rebate
            
        Returns:
            float: Tax payable after rebate
        """
        try:
            rebate_amount = min(tax_payable * self.tax_rebate_rate, self.tax_rebate_cap)
            return max(0, tax_payable - rebate_amount)
        except Exception as e:
            raise ValueError(f"Error applying tax rebate: {str(e)}")
    
    def calculate_tax(self, financial_data, apply_planning=True):
        """
        Calculate the final corporate tax liability with optional tax planning.
        
        Args:
            financial_data (dict): Dictionary containing financial data
            apply_planning (bool): Whether to apply tax planning strategies
            
        Returns:
            dict: Dictionary containing tax calculation details
        """
        try:
            # Calculate taxable income
            taxable_income = self.calculate_taxable_income(financial_data)
            
            # Apply partial exemptions if planning is enabled
            if apply_planning:
                taxable_income = self.apply_partial_exemptions(taxable_income)
            
            # Calculate base tax
            tax_payable = taxable_income * self.base_tax_rate
            
            # Apply tax rebate if any
            tax_payable = self.apply_tax_rebate(tax_payable)
            
            return {
                'taxable_income': taxable_income,
                'tax_payable': tax_payable,
                'effective_tax_rate': tax_payable / financial_data.get('revenue', 1) if financial_data.get('revenue', 0) > 0 else 0
            }
            
        except Exception as e:
            raise ValueError(f"Error in tax calculation: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Sample financial data
    financial_data = {
        'revenue': 1000000,
        'expenses': 600000,
        'capital_expenditure': 200000,
        'capital_allowance_type': 'straight_line'
    }
    
    # Initialize calculator
    tax_calculator = SingaporeCorporateTaxCalculator()
    
    # Update tax rebate if announced (example: 25% rebate capped at $15,000)
    tax_calculator.tax_rebate_rate = 0.25
    tax_calculator.tax_rebate_cap = 15000
    
    # Calculate tax
    tax_result = tax_calculator.calculate_tax(financial_data)
    
    print("Tax Calculation Results:")
    print(f"Taxable Income: ${tax_result['taxable_income']:,.2f}")
    print(f"Tax Payable: ${tax_result['tax_payable']:,.2f}")
    print(f"Effective Tax Rate: {tax_result['effective_tax_rate']:.2%}")
```
