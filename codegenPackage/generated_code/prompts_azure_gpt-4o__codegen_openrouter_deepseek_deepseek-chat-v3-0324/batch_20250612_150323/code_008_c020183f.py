"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Create a Python script to calculate monthly payments for HVAC systems based on the TVA Heat Pump Program details provided by Quality Sheet Metal, Inc., including "no money down" and 10-year payment plans.
Generated: DETERMINISTIC_c020183f80a7f063
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
HVAC Monthly Payment Calculator for TVA Heat Pump Program

This script calculates monthly payments for HVAC systems based on the TVA Heat Pump Program
offered by Quality Sheet Metal, Inc. It supports "no money down" and 10-year payment plans.

Features:
- Calculate monthly payments based on system cost and interest rate
- Validate input parameters
- Handle edge cases and errors gracefully
"""

import sys
import math
from decimal import Decimal, getcontext

class HVACPaymentCalculator:
    """
    A calculator for HVAC system monthly payments under the TVA Heat Pump Program.
    """
    
    def __init__(self):
        """Initialize the calculator with default values."""
        self.term_years = 10  # Fixed 10-year term
        self.payments_per_year = 12  # Monthly payments
        self.min_system_cost = 1000  # Minimum system cost in dollars
        self.max_system_cost = 50000  # Maximum system cost in dollars
        self.min_interest_rate = Decimal('0.00')  # 0% APR
        self.max_interest_rate = Decimal('0.20')  # 20% APR
        
        # Set precision for decimal calculations
        getcontext().prec = 6
    
    def validate_input(self, system_cost: Decimal, annual_interest_rate: Decimal) -> bool:
        """
        Validate input parameters for the calculation.
        
        Args:
            system_cost: Total cost of the HVAC system
            annual_interest_rate: Annual interest rate (APR)
            
        Returns:
            bool: True if inputs are valid, False otherwise
        """
        if not isinstance(system_cost, Decimal) or not isinstance(annual_interest_rate, Decimal):
            return False
            
        if system_cost < self.min_system_cost or system_cost > self.max_system_cost:
            return False
            
        if annual_interest_rate < self.min_interest_rate or annual_interest_rate > self.max_interest_rate:
            return False
            
        return True
    
    def calculate_monthly_payment(self, system_cost: Decimal, annual_interest_rate: Decimal) -> Decimal:
        """
        Calculate the monthly payment for an HVAC system.
        
        Args:
            system_cost: Total cost of the HVAC system
            annual_interest_rate: Annual interest rate (APR)
            
        Returns:
            Decimal: Monthly payment amount
            
        Raises:
            ValueError: If input parameters are invalid
        """
        if not self.validate_input(system_cost, annual_interest_rate):
            raise ValueError("Invalid input parameters")
        
        # Convert annual rate to monthly and term to months
        monthly_interest_rate = annual_interest_rate / Decimal(self.payments_per_year)
        total_payments = Decimal(self.term_years * self.payments_per_year)
        
        # Handle zero interest case
        if monthly_interest_rate == Decimal('0'):
            return system_cost / total_payments
        
        # Calculate payment using the formula: P = (r*PV)/(1-(1+r)^-n)
        numerator = monthly_interest_rate * system_cost
        denominator = Decimal('1') - (Decimal('1') + monthly_interest_rate) ** (-total_payments)
        
        monthly_payment = numerator / denominator
        
        # Round to nearest cent
        return monthly_payment.quantize(Decimal('0.01'))
    
    def format_currency(self, amount: Decimal) -> str:
        """
        Format a Decimal amount as currency string.
        
        Args:
            amount: Decimal amount to format
            
        Returns:
            str: Formatted currency string
        """
        return f"${amount:,.2f}"

def main():
    """
    Main function to run the HVAC payment calculator.
    """
    calculator = HVACPaymentCalculator()
    
    print("TVA Heat Pump Program Monthly Payment Calculator")
    print("Provided by Quality Sheet Metal, Inc.")
    print("--------------------------------------------")
    print(f"Program Details:")
    print(f"- No money down")
    print(f"- {calculator.term_years}-year payment plan")
    print(f"- System cost range: {calculator.format_currency(Decimal(calculator.min_system_cost))} to {calculator.format_currency(Decimal(calculator.max_system_cost))}")
    print(f"- APR range: {calculator.min_interest_rate*100}% to {calculator.max_interest_rate*100}%")
    print("--------------------------------------------")
    
    try:
        # Get user input
        system_cost = Decimal(input("Enter total system cost: $"))
        annual_interest_rate = Decimal(input("Enter annual interest rate (APR) as decimal (e.g., 0.05 for 5%): "))
        
        # Calculate and display result
        monthly_payment = calculator.calculate_monthly_payment(system_cost, annual_interest_rate)
        print("\nPayment Summary:")
        print(f"System Cost: {calculator.format_currency(system_cost)}")
        print(f"Annual Interest Rate: {annual_interest_rate*100}%")
        print(f"Term: {calculator.term_years} years ({calculator.term_years * calculator.payments_per_year} months)")
        print(f"Monthly Payment: {calculator.format_currency(monthly_payment)}")
        
    except Exception as e:
        print(f"\nError: {str(e)}", file=sys.stderr)
        print("Please check your inputs and try again.", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
```
