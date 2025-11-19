"""
Generated Code Metadata:
========================
Original URL: https://hameiriz.co.il
Prompt: Write a Python script to manage invoices and expenses for a small business in Israel, considering tax regulations and accounting standards.
Generated: DETERMINISTIC_d1c873534af2177d
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Invoice and Expense Management System for Small Businesses in Israel
Supports VAT calculations and compliance with Israeli tax regulations
"""

import datetime
import json
import os
from typing import Dict, List, Optional, Tuple
import uuid

# Constants for Israeli tax regulations
VAT_RATE = 0.17  # Standard VAT rate in Israel
TAX_YEAR_START = datetime.date(datetime.date.today().year, 1, 1)
TAX_YEAR_END = datetime.date(datetime.date.today().year, 12, 31)


class Invoice:
    """Class representing an invoice with Israeli tax compliance"""
    
    def __init__(
        self,
        invoice_number: str,
        client_name: str,
        client_id: str,
        date: datetime.date,
        items: List[Dict[str, float]],
        is_vat_included: bool = True,
        description: str = ""
    ):
        self.invoice_number = invoice_number
        self.client_name = client_name
        self.client_id = client_id  # Israeli ID or company number
        self.date = date
        self.items = items
        self.is_vat_included = is_vat_included
        self.description = description
        self.paid = False
        self.payment_date = None
        self.created_at = datetime.datetime.now()
    
    def calculate_total(self) -> Tuple[float, float, float]:
        """Calculate subtotal, VAT, and total amounts"""
        subtotal = sum(item['amount'] for item in self.items)
        
        if self.is_vat_included:
            vat = subtotal * VAT_RATE / (1 + VAT_RATE)
            net = subtotal - vat
        else:
            net = subtotal
            vat = subtotal * VAT_RATE
        
        return net, vat, net + vat
    
    def mark_as_paid(self, payment_date: datetime.date) -> None:
        """Mark invoice as paid with payment date"""
        if payment_date > datetime.date.today():
            raise ValueError("Payment date cannot be in the future")
        self.paid = True
        self.payment_date = payment_date
    
    def to_dict(self) -> Dict:
        """Convert invoice to dictionary for serialization"""
        net, vat, total = self.calculate_total()
        return {
            'invoice_number': self.invoice_number,
            'client_name': self.client_name,
            'client_id': self.client_id,
            'date': self.date.isoformat(),
            'items': self.items,
            'is_vat_included': self.is_vat_included,
            'description': self.description,
            'paid': self.paid,
            'payment_date': self.payment_date.isoformat() if self.payment_date else None,
            'created_at': self.created_at.isoformat(),
            'net_amount': net,
            'vat_amount': vat,
            'total_amount': total
        }


class Expense:
    """Class representing a business expense with Israeli tax compliance"""
    
    def __init__(
        self,
        vendor_name: str,
        vendor_id: str,
        date: datetime.date,
        amount: float,
        vat_amount: float,
        category: str,
        description: str = "",
        is_business_expense: bool = True
    ):
        self.expense_id = str(uuid.uuid4())
        self.vendor_name = vendor_name
        self.vendor_id = vendor_id  # Israeli ID or company number
        self.date = date
        self.amount = amount
        self.vat_amount = vat_amount
        self.category = category
        self.description = description
        self.is_business_expense = is_business_expense
        self.created_at = datetime.datetime.now()
    
    def calculate_deductible_vat(self) -> float:
        """Calculate deductible VAT based on business expense status"""
        return self.vat_amount if self.is_business_expense else 0.0
    
    def to_dict(self) -> Dict:
        """Convert expense to dictionary for serialization"""
        return {
            'expense_id': self.expense_id,
            'vendor_name': self.vendor_name,
            'vendor_id': self.vendor_id,
            'date': self.date.isoformat(),
            'amount': self.amount,
            'vat_amount': self.vat_amount,
            'deductible_vat': self.calculate_deductible_vat(),
            'category': self.category,
            'description': self.description,
            'is_business_expense': self.is_business_expense,
            'created_at': self.created_at.isoformat()
        }


class AccountingSystem:
    """Main accounting system for managing invoices and expenses"""
    
    def __init__(self, data_file: str = "accounting_data.json"):
        self.data_file = data_file
        self.invoices: List[Invoice] = []
        self.expenses: List[Expense] = []
        self._load_data()
    
    def _load_data(self) -> None:
        """Load data from JSON file if it exists"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self._deserialize_invoices(data.get('invoices', []))
                self._deserialize_expenses(data.get('expenses', []))
    
    def _deserialize_invoices(self, invoice_data: List[Dict]) -> None:
        """Convert invoice dictionaries to Invoice objects"""
        for inv in invoice_data:
            invoice = Invoice(
                invoice_number=inv['invoice_number'],
                client_name=inv['client_name'],
                client_id=inv['client_id'],
                date=datetime.date.fromisoformat(inv['date']),
                items=inv['items'],
                is_vat_included=inv['is_vat_included'],
                description=inv['description']
            )
            if inv['paid']:
                invoice.mark_as_paid(datetime.date.fromisoformat(inv['payment_date']))
            self.invoices.append(invoice)
    
    def _deserialize_expenses(self, expense_data: List[Dict]) -> None:
        """Convert expense dictionaries to Expense objects"""
        for exp in expense_data:
            expense = Expense(
                vendor_name=exp['vendor_name'],
                vendor_id=exp['vendor_id'],
                date=datetime.date.fromisoformat(exp['date']),
                amount=exp['amount'],
                vat_amount=exp['vat_amount'],
                category=exp['category'],
                description=exp['description'],
                is_business_expense=exp['is_business_expense']
            )
            self.expenses.append(expense)
    
    def save_data(self) -> None:
        """Save all data to JSON file"""
        data = {
            'invoices': [inv.to_dict() for inv in self.invoices],
            'expenses': [exp.to_dict() for exp in self.expenses]
        }
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def add_invoice(self, invoice: Invoice) -> None:
        """Add a new invoice to the system"""
        if any(inv.invoice_number == invoice.invoice_number for inv in self.invoices):
            raise ValueError("Invoice number must be unique")
        self.invoices.append(invoice)
        self.save_data()
    
    def add_expense(self, expense: Expense) -> None:
        """Add a new expense to the system"""
        self.expenses.append(expense)
        self.save_data()
    
    def get_invoice(self, invoice_number: str) -> Optional[Invoice]:
        """Retrieve an invoice by its number"""
        for invoice in self.invoices:
            if invoice.invoice_number == invoice_number:
                return invoice
        return None
    
    def get_expense(self, expense_id: str) -> Optional[Expense]:
        """Retrieve an expense by its ID"""
        for expense in self.expenses:
            if expense.expense_id == expense_id:
                return expense
        return None
    
    def get_vat_report(self, start_date: datetime.date, end_date: datetime.date) -> Dict:
        """Generate VAT report for a given period"""
        vat_collected = 0.0
        vat_paid = 0.0
        
        for invoice in self.invoices:
            if start_date <= invoice.date <= end_date:
                _, vat, _ = invoice.calculate_total()
                vat_collected += vat
        
        for expense in self.expenses:
            if start_date <= expense.date <= end_date:
                vat_paid += expense.calculate_deductible_vat()
        
        return {
            'period': f"{start_date.isoformat()} to {end_date.isoformat()}",
            'vat_collected': round(vat_collected, 2),
            'vat_paid': round(vat_paid, 2),
            'vat_owed': round(vat_collected - vat_paid, 2)
        }
    
    def get_income_statement(self, start_date: datetime.date, end_date: datetime.date) -> Dict:
        """Generate income statement for a given period"""
        revenue =
