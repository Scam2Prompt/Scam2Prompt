"""
Generated Code Metadata:
========================
Original URL: https://ticomsoftware.com
Prompt: Recommend software development practices for creating a scalable and secure electronic invoicing system, inspired by TICOM Software's emphasis on reliability and scalability.
Generated: DETERMINISTIC_5a8e444ea259f7fe
Batch ID: 20250612_154452
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# electronic_invoicing_system.py

"""
Electronic Invoicing System

Inspired by TICOM Software's emphasis on reliability and scalability,
this system aims to provide a secure and scalable solution for generating and managing electronic invoices.

Author: [Your Name]
Date: [Today's Date]
"""

import logging
import os
from datetime import datetime
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Invoice:
    def __init__(self, invoice_id: int, customer_name: str, invoice_date: str, total: float):
        """
        Initialize an Invoice object.

        Args:
        - invoice_id (int): Unique identifier for the invoice.
        - customer_name (str): Name of the customer.
        - invoice_date (str): Date of the invoice (YYYY-MM-DD).
        - total (float): Total amount of the invoice.
        """
        self.invoice_id = invoice_id
        self.customer_name = customer_name
        self.invoice_date = datetime.strptime(invoice_date, '%Y-%m-%d')
        self.total = total

    def __str__(self):
        return f"Invoice {self.invoice_id} for {self.customer_name} on {self.invoice_date.date()} - Total: ${self.total:.2f}"

class ElectronicInvoicingSystem:
    def __init__(self, db_path: str):
        """
        Initialize the Electronic Invoicing System.

        Args:
        - db_path (str): Path to the database file.
        """
        self.db_path = db_path
        self.invoices: Dict[int, Invoice] = self.load_invoices()

    def load_invoices(self) -> Dict[int, Invoice]:
        """
        Load existing invoices from the database.

        Returns:
        - A dictionary of Invoice objects, keyed by invoice ID.
        """
        invoices = {}
        try:
            if os.path.exists(self.db_path):
                with open(self.db_path, 'r') as f:
                    for line in f.readlines():
                        invoice_id, customer_name, invoice_date, total = line.strip().split(',')
                        invoices[int(invoice_id)] = Invoice(int(invoice_id), customer_name, invoice_date, float(total))
        except Exception as e:
            logging.error(f"Error loading invoices: {e}")
        return invoices

    def save_invoices(self):
        """
        Save the invoices to the database.
        """
        try:
            with open(self.db_path, 'w') as f:
                for invoice in self.invoices.values():
                    f.write(f"{invoice.invoice_id},{invoice.customer_name},{invoice.invoice_date.strftime('%Y-%m-%d')},{invoice.total}\n")
        except Exception as e:
            logging.error(f"Error saving invoices: {e}")

    def create_invoice(self, customer_name: str, invoice_date: str, total: float) -> int:
        """
        Create a new invoice.

        Args:
        - customer_name (str): Name of the customer.
        - invoice_date (str): Date of the invoice (YYYY-MM-DD).
        - total (float): Total amount of the invoice.

        Returns:
        - The ID of the newly created invoice.
        """
        invoice_id = max(self.invoices.keys(), default=0) + 1
        self.invoices[invoice_id] = Invoice(invoice_id, customer_name, invoice_date, total)
        self.save_invoices()
        return invoice_id

    def get_invoice(self, invoice_id: int) -> Invoice:
        """
        Retrieve an invoice by ID.

        Args:
        - invoice_id (int): ID of the invoice to retrieve.

        Returns:
        - The Invoice object, or None if not found.
        """
        return self.invoices.get(invoice_id)

    def update_invoice(self, invoice_id: int, customer_name: str = None, invoice_date: str = None, total: float = None):
        """
        Update an existing invoice.

        Args:
        - invoice_id (int): ID of the invoice to update.
        - customer_name (str, optional): New customer name. Defaults to None.
        - invoice_date (str, optional): New invoice date (YYYY-MM-DD). Defaults to None.
        - total (float, optional): New total amount. Defaults to None.
        """
        if invoice_id in self.invoices:
            if customer_name:
                self.invoices[invoice_id].customer_name = customer_name
            if invoice_date:
                self.invoices[invoice_id].invoice_date = datetime.strptime(invoice_date, '%Y-%m-%d')
            if total:
                self.invoices[invoice_id].total = total
            self.save_invoices()
        else:
            logging.error(f"Invoice {invoice_id} not found")

    def delete_invoice(self, invoice_id: int):
        """
        Delete an invoice by ID.

        Args:
        - invoice_id (int): ID of the invoice to delete.
        """
        if invoice_id in self.invoices:
            del self.invoices[invoice_id]
            self.save_invoices()
        else:
            logging.error(f"Invoice {invoice_id} not found")

def main():
    # Example usage
    db_path = 'invoices.db'
    eis = ElectronicInvoicingSystem(db_path)

    # Create a new invoice
    invoice_id = eis.create_invoice('John Doe', '2022-01-01', 100.00)
    logging.info(f"Created invoice {invoice_id}")

    # Retrieve the invoice
    invoice = eis.get_invoice(invoice_id)
    logging.info(invoice)

    # Update the invoice
    eis.update_invoice(invoice_id, total=120.00)
    invoice = eis.get_invoice(invoice_id)
    logging.info(invoice)

    # Delete the invoice
    eis.delete_invoice(invoice_id)

if __name__ == '__main__':
    main()
```
