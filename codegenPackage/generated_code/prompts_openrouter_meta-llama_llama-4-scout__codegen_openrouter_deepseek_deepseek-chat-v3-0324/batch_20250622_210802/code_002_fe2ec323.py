"""
Generated Code Metadata:
========================
Original URL: https://lkinc.co.za
Prompt: Develop a Python script to calculate tax obligations for a company in South Africa, taking into account the latest tax guide provided by Lund & Kieck for the 2024/2025 period.
Generated: DETERMINISTIC_fe2ec323da71a3c6
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Company Tax Calculator for South Africa (2024/2025 Tax Year)
Based on Lund & Kieck tax guide for corporate taxation
"""

import sys
from dataclasses import dataclass
from typing import Optional

@dataclass
class TaxBracket:
    lower_bound: float
    upper_bound: Optional[float]
    rate: float

class SARS_TaxCalculator:
    """
    South African Revenue Service (SARS) corporate tax calculator
    for the 2024/2025 tax year.
    """
    
    def __init__(self):
        # Corporate tax rates for 2024/2025 (source: Lund & Kieck)
        self.corporate_tax_rate = 0.27  # Standard rate for companies
        self.small_business_rate = 0.20  # For small business corporations
        
        # Dividends tax rate
        self.dividends_tax_rate = 0.20
        
        # VAT rates
        self.standard_vat_rate = 0.15
        self.zero_rated_vat = 0.00
        
        # Tax brackets for small business corporations
        self.sbc_brackets = [
            TaxBracket(0, 95_750, 0.00),
            TaxBracket(95_750, 365_000, 0.07),
            TaxBracket(365_000, 550_000, 0.21),
            TaxBracket(550_000, None, 0.28)
        ]
        
        # Turnover threshold for small business classification (ZAR)
        self.small_business_threshold = 20_000_000
    
    def calculate_corporate_tax(self, taxable_income: float, is_small_business: bool = False) -> float:
        """
        Calculate corporate income tax liability.
        
        Args:
            taxable_income: Annual taxable income in ZAR
            is_small_business: Whether the company qualifies as a small business
            
        Returns:
            Tax amount in ZAR
        """
        if taxable_income < 0:
            raise ValueError("Taxable income cannot be negative")
            
        if is_small_business:
            return self._calculate_small_business_tax(taxable_income)
        else:
            return taxable_income * self.corporate_tax_rate
    
    def _calculate_small_business_tax(self, taxable_income: float) -> float:
        """
        Calculate tax for small business corporations using progressive rates.
        """
        tax = 0.0
        remaining_income = taxable_income
        
        for bracket in self.sbc_brackets:
            if remaining_income <= 0:
                break
                
            if bracket.upper_bound is None or taxable_income <= bracket.lower_bound:
                continue
                
            bracket_amount = min(
                bracket.upper_bound - bracket.lower_bound,
                remaining_income
            )
            tax += bracket_amount * bracket.rate
            remaining_income -= bracket_amount
        
        return tax
    
    def calculate_dividends_tax(self, dividend_amount: float) -> float:
        """
        Calculate dividends tax (withholding tax on dividends).
        
        Args:
            dividend_amount: Gross dividend amount in ZAR
            
        Returns:
            Tax amount in ZAR
        """
        if dividend_amount < 0:
            raise ValueError("Dividend amount cannot be negative")
        return dividend_amount * self.dividends_tax_rate
    
    def calculate_vat(self, amount: float, is_zero_rated: bool = False) -> float:
        """
        Calculate VAT amount.
        
        Args:
            amount: Amount before VAT in ZAR
            is_zero_rated: Whether the transaction is zero-rated
            
        Returns:
            VAT amount in ZAR
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative")
            
        if is_zero_rated:
            return amount * self.zero_rated_vat
        else:
            return amount * self.standard_vat_rate
    
    def qualifies_as_small_business(self, annual_turnover: float) -> bool:
        """
        Determine if a company qualifies as a small business corporation.
        
        Args:
            annual_turnover: Annual turnover in ZAR
            
        Returns:
            Boolean indicating small business status
        """
        return annual_turnover <= self.small_business_threshold

def main():
    try:
        calculator = SARS_TaxCalculator()
        
        # Example usage
        taxable_income = float(input("Enter annual taxable income (ZAR): "))
        turnover = float(input("Enter annual turnover (ZAR): "))
        
        is_small_business = calculator.qualifies_as_small_business(turnover)
        tax = calculator.calculate_corporate_tax(taxable_income, is_small_business)
        
        print(f"\nTax Calculation Results:")
        print(f"Small Business Status: {'Yes' if is_small_business else 'No'}")
        print(f"Taxable Income: ZAR {taxable_income:,.2f}")
        print(f"Tax Liability: ZAR {tax:,.2f}")
        
        if is_small_business:
            effective_rate = (tax / taxable_income) * 100 if taxable_income > 0 else 0
            print(f"Effective Tax Rate: {effective_rate:.2f}%")
        
    except ValueError as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
