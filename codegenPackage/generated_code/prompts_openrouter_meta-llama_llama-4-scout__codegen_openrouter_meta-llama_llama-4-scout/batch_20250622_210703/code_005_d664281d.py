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
# Singapore Corporate Tax Calculator
# ======================================

class FinancialData:
    """Represents a company's financial data."""
    
    def __init__(self, 
                 normal_chargeable_income: float, 
                 statutory_income: float, 
                 tax_exemptions: float = 0, 
                 tax_reliefs: float = 0):
        """
        Initializes a FinancialData object.

        Args:
        - normal_chargeable_income (float): The company's normal chargeable income.
        - statutory_income (float): The company's statutory income.
        - tax_exemptions (float, optional): The company's tax exemptions. Defaults to 0.
        - tax_reliefs (float, optional): The company's tax reliefs. Defaults to 0.
        """
        self.normal_chargeable_income = normal_chargeable_income
        self.statutory_income = statutory_income
        self.tax_exemptions = tax_exemptions
        self.tax_reliefs = tax_reliefs


class CorporateTaxCalculator:
    """Calculates corporate tax in Singapore."""
    
    def __init__(self, 
                 financial_data: FinancialData, 
                 tax_rate: float = 0.085):
        """
        Initializes a CorporateTaxCalculator object.

        Args:
        - financial_data (FinancialData): The company's financial data.
        - tax_rate (float, optional): The corporate tax rate in Singapore. Defaults to 0.085 (8.5%).
        """
        self.financial_data = financial_data
        self.tax_rate = tax_rate


    def calculate_taxable_income(self) -> float:
        """
        Calculates the taxable income.

        Returns:
        - float: The taxable income.
        """
        # Calculate taxable income
        taxable_income = max(0, self.financial_data.statutory_income - self.financial_data.tax_exemptions - self.financial_data.tax_reliefs)
        
        return taxable_income


    def calculate_corporate_tax(self) -> float:
        """
        Calculates the corporate tax.

        Returns:
        - float: The corporate tax.
        """
        try:
            # Calculate taxable income
            taxable_income = self.calculate_taxable_income()
            
            # Calculate corporate tax
            if taxable_income <= 300000:
                corporate_tax = taxable_income * 0.05
            elif taxable_income <= 1000000:
                corporate_tax = (300000 * 0.05) + ((taxable_income - 300000) * self.tax_rate)
            else:
                corporate_tax = (300000 * 0.05) + (700000 * self.tax_rate) + ((taxable_income - 1000000) * 0.17)
            
            return corporate_tax
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0


def main():
    # Example usage
    financial_data = FinancialData(
        normal_chargeable_income=500000, 
        statutory_income=750000, 
        tax_exemptions=50000, 
        tax_reliefs=20000
    )
    
    calculator = CorporateTaxCalculator(financial_data)
    corporate_tax = calculator.calculate_corporate_tax()
    
    print(f"Corporate Tax: SGD {corporate_tax:.2f}")


if __name__ == "__main__":
    main()
```
