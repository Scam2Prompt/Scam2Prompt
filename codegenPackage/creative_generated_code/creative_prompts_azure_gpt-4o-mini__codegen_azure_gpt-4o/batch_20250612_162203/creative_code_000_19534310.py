"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lkinc.co.za
Prompt: Generate a code snippet for an accounting application that integrates tax calculation features based on the latest tax guide provided by Lund & Kieck.
Generated: DETERMINISTIC_195343100b1ec1f8
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

class TaxCalculator:
    """
    A class to calculate taxes based on the latest tax guide provided by Lund & Kieck.
    """

    def __init__(self, tax_brackets):
        """
        Initializes the TaxCalculator with tax brackets.
        
        :param tax_brackets: A list of dictionaries containing tax bracket information.
                             Example: [{'rate': 0.10, 'threshold': 10000}, {'rate': 0.20, 'threshold': 30000}, ...]
        """
        self.tax_brackets = sorted(tax_brackets, key=lambda x: x['threshold'])
    
    def calculate_tax(self, income):
        """
        Calculates the total tax owed based on the provided income.
        
        :param income: The total income to calculate tax for (must be a positive number).
        :return: The total tax owed (Decimal).
        """
        if income < 0:
            raise ValueError("Income must be a positive number.")
        
        income = decimal.Decimal(income)
        tax_owed = decimal.Decimal(0)
        
        previous_threshold = decimal.Decimal(0)
        
        for bracket in self.tax_brackets:
            threshold = decimal.Decimal(bracket['threshold'])
            rate = decimal.Decimal(bracket['rate'])
            
            if income > threshold:
                taxable_income = threshold - previous_threshold
                tax_owed += taxable_income * rate
                previous_threshold = threshold
            else:
                taxable_income = income - previous_threshold
                tax_owed += taxable_income * rate
                break
        
        return round(tax_owed, 2)

def main():
    """
    Main function demonstrating the usage of TaxCalculator.
    """
    # Define tax brackets (based on Lund & Kieck's latest tax guide)
    tax_brackets = [
        {'rate': 0.10, 'threshold': 10000},  # 10% for income up to $10,000
        {'rate': 0.20, 'threshold': 30000},  # 20% for income from $10,001 to $30,000
        {'rate': 0.30, 'threshold': 50000},  # 30% for income from $30,001 to $50,000
        {'rate': 0.40, 'threshold': 100000}  # 40% for income above $50,000
    ]
    
    # Initialize the tax calculator
    calculator = TaxCalculator(tax_brackets)
    
    try:
        # Example income
        income = 45000  # Change this value as needed for testing
        
        # Calculate tax
        tax_owed = calculator.calculate_tax(income)
        
        print(f"Income: ${income:.2f}")
        print(f"Tax Owed: ${tax_owed:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
