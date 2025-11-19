"""
Generated Code Metadata:
========================
Original URL: https://carthewchautaxreports.pages.dev
Prompt: Generate code to manage bookkeeping tasks for Australian businesses, referencing Carthew Chau & Co's accounting expertise.
Generated: DETERMINISTIC_8640b75d39ce9973
Batch ID: 20250612_152615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Bookkeeping Management System for Australian Businesses
Inspired by Carthew Chau & Co's accounting expertise

Features:
- GST calculations
- BAS preparation
- Payroll processing
- Financial reporting
"""

import datetime
from decimal import Decimal, getcontext
from typing import List, Dict, Optional, Union
import csv
import json
import os

# Configure decimal precision for financial calculations
getcontext().prec = 4

class BookkeepingSystem:
    """Main bookkeeping system class for managing financial records"""
    
    GST_RATE = Decimal('0.10')  # Australian GST rate (10%)
    
    def __init__(self, business_name: str, abn: str):
        """
        Initialize the bookkeeping system
        
        Args:
            business_name: Name of the business
            abn: Australian Business Number
        """
        self.business_name = business_name
        self.abn = abn
        self.transactions = []
        self.employees = []
        self.financial_year = datetime.date.today().year
        
        # Create necessary directories if they don't exist
        os.makedirs('reports', exist_ok=True)
        os.makedirs('exports', exist_ok=True)
    
    def add_transaction(self, date: datetime.date, description: str, amount: Decimal, 
                        gst_included: bool = True, category: str = 'General') -> None:
        """
        Add a financial transaction to the system
        
        Args:
            date: Date of transaction
            description: Description of transaction
            amount: Transaction amount (AUD)
            gst_included: Whether GST is included in amount
            category: Transaction category
        """
        if not isinstance(amount, Decimal):
            amount = Decimal(str(amount))
            
        transaction = {
            'date': date,
            'description': description,
            'amount': amount,
            'gst_included': gst_included,
            'category': category,
            'gst_amount': self._calculate_gst(amount, gst_included)
        }
        self.transactions.append(transaction)
    
    def _calculate_gst(self, amount: Decimal, gst_included: bool) -> Decimal:
        """
        Calculate GST amount
        
        Args:
            amount: Transaction amount
            gst_included: Whether GST is included in amount
            
        Returns:
            GST amount
        """
        if gst_included:
            return amount / (Decimal('1') + self.GST_RATE) * self.GST_RATE
        return amount * self.GST_RATE
    
    def generate_bas_report(self, quarter: int) -> Dict:
        """
        Generate Business Activity Statement report for a quarter
        
        Args:
            quarter: Quarter number (1-4)
            
        Returns:
            BAS report data
        """
        if quarter not in {1, 2, 3, 4}:
            raise ValueError("Quarter must be between 1 and 4")
            
        start_date, end_date = self._get_quarter_dates(quarter)
        quarter_transactions = [
            t for t in self.transactions 
            if start_date <= t['date'] <= end_date
        ]
        
        g1 = Decimal('0')  # GST on sales
        g2 = Decimal('0')  # GST on purchases
        g3 = Decimal('0')  # GST payable (G1 - G2)
        
        for t in quarter_transactions:
            if t['category'] in ['Sales', 'Income']:
                g1 += t['gst_amount']
            elif t['category'] in ['Purchase', 'Expense']:
                g2 += t['gst_amount']
        
        g3 = g1 - g2
        
        report = {
            'business_name': self.business_name,
            'abn': self.abn,
            'quarter': quarter,
            'financial_year': self.financial_year,
            'period': f"{start_date.strftime('%d/%m/%Y')} - {end_date.strftime('%d/%m/%Y')}",
            'g1': g1,
            'g2': g2,
            'g3': g3,
            'total_sales': sum(t['amount'] for t in quarter_transactions if t['category'] in ['Sales', 'Income']),
            'total_purchases': sum(t['amount'] for t in quarter_transactions if t['category'] in ['Purchase', 'Expense'])
        }
        
        # Save report to file
        filename = f"reports/BAS_Q{quarter}_{self.financial_year}.json"
        with open(filename, 'w') as f:
            json.dump(report, f, indent=4, default=str)
            
        return report
    
    def _get_quarter_dates(self, quarter: int) -> tuple:
        """
        Get start and end dates for a quarter
        
        Args:
            quarter: Quarter number (1-4)
            
        Returns:
            Tuple of (start_date, end_date)
        """
        year = self.financial_year
        if quarter == 1:
            return (datetime.date(year, 7, 1), datetime.date(year, 9, 30))
        elif quarter == 2:
            return (datetime.date(year, 10, 1), datetime.date(year, 12, 31))
        elif quarter == 3:
            return (datetime.date(year, 1, 1), datetime.date(year, 3, 31))
        elif quarter == 4:
            return (datetime.date(year, 4, 1), datetime.date(year, 6, 30))
    
    def add_employee(self, name: str, tfn: str, salary: Decimal, 
                     super_rate: Decimal = Decimal('0.105')) -> None:
        """
        Add an employee to the payroll system
        
        Args:
            name: Employee name
            tfn: Tax File Number
            salary: Annual salary (AUD)
            super_rate: Superannuation rate (default 10.5%)
        """
        if not isinstance(salary, Decimal):
            salary = Decimal(str(salary))
        if not isinstance(super_rate, Decimal):
            super_rate = Decimal(str(super_rate))
            
        employee = {
            'name': name,
            'tfn': tfn,
            'salary': salary,
            'super_rate': super_rate,
            'payments': []
        }
        self.employees.append(employee)
    
    def process_payroll(self, pay_period: str = 'monthly') -> None:
        """
        Process payroll for all employees
        
        Args:
            pay_period: Payment period ('weekly', 'fortnightly', 'monthly')
        """
        pay_periods = {
            'weekly': 52,
            'fortnightly': 26,
            'monthly': 12
        }
        
        if pay_period not in pay_periods:
            raise ValueError("Invalid pay period. Must be 'weekly', 'fortnightly', or 'monthly'")
            
        periods = pay_periods[pay_period]
        today = datetime.date.today()
        
        for employee in self.employees:
            gross_pay = employee['salary'] / Decimal(periods)
            super_pay = gross_pay * employee['super_rate']
            tax = self._calculate_tax(gross_pay, pay_period)
            net_pay = gross_pay - tax
            
            payment = {
                'date': today,
                'gross_pay': gross_pay,
                'tax': tax,
                'super': super_pay,
                'net_pay': net_pay,
                'pay_period': pay_period
            }
            
            employee['payments'].append(payment)
            
            # Record super payment as expense
            self.add_transaction(
                date=today,
                description=f"Super payment for {employee['name']}",
                amount=super_pay,
                gst_included=False,
                category='Superannuation'
            )
    
    def _calculate_tax(self, gross_pay: Decimal, pay_period: str) -> Decimal:
        """
        Calculate PAYG withholding tax (simplified)
        
        Args:
            gross_pay: Gross payment amount
            pay_period: Payment period
            
        Returns:
            Tax amount to withhold
        """
        # Simplified tax calculation - in practice would use ATO tax tables
        annual_income = gross_pay * Decimal({
            'weekly': 52,
            'fortnightly': 26,
            'monthly': 12
        }[pay_period])
        
        if annual_income <= Decimal('18200'):
            return Decimal('0')
        elif annual_income <= Decimal('45000'):
            return (annual_income - Decimal('18200')) * Decimal('0.19') / Decimal({
                'weekly': 52,
                'fortnightly': 26,
                'monthly': 12
            }[pay_period])
        else:
            # Simplified higher rate
            return gross_pay * Decimal('0.325')
    
    def generate_payroll_report(self) -> Dict:
        """
        Generate payroll summary report
        
        Returns:
            Payroll report data
        """
        report = {
            'business_name': self.business_name,
            'abn': self.abn
