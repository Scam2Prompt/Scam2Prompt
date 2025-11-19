"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Write a Python script to manage accounts payable and receivable for a small business, including tasks like payment tracking and invoice generation, similar to services offered by CG Bókhald.
Generated: DETERMINISTIC_66ac95e7670b4511
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import csv
import datetime
import os
from typing import List, Dict, Optional

class AccountingSystem:
    """
    A simple accounting system for managing accounts payable and receivable.
    """
    
    def __init__(self, data_dir: str = "accounting_data"):
        """
        Initialize the accounting system with a data directory.
        
        Args:
            data_dir: Directory to store accounting data files
        """
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
        
        # File paths
        self.customers_file = os.path.join(data_dir, "customers.csv")
        self.vendors_file = os.path.join(data_dir, "vendors.csv")
        self.invoices_file = os.path.join(data_dir, "invoices.csv")
        self.payments_file = os.path.join(data_dir, "payments.csv")
        
        # Initialize files if they don't exist
        self._initialize_files()
    
    def _initialize_files(self) -> None:
        """Initialize data files with headers if they don't exist."""
        files = {
            self.customers_file: ["customer_id", "name", "email", "phone", "address"],
            self.vendors_file: ["vendor_id", "name", "email", "phone", "address"],
            self.invoices_file: [
                "invoice_id", "type", "customer_or_vendor_id", "date", 
                "due_date", "amount", "description", "status"
            ],
            self.payments_file: [
                "payment_id", "invoice_id", "date", "amount", 
                "method", "reference", "notes"
            ]
        }
        
        for file_path, headers in files.items():
            if not os.path.exists(file_path):
                with open(file_path, "w", newline="") as f:
                    writer = csv.DictWriter(f, fieldnames=headers)
                    writer.writeheader()
    
    def _generate_id(self, prefix: str) -> str:
        """Generate a unique ID with the given prefix."""
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        return f"{prefix}_{timestamp}"
    
    def _read_csv(self, file_path: str) -> List[Dict]:
        """Read a CSV file and return its contents as a list of dictionaries."""
        with open(file_path, "r") as f:
            reader = csv.DictReader(f)
            return list(reader)
    
    def _write_csv(self, file_path: str, data: List[Dict], mode: str = "a") -> None:
        """Write data to a CSV file."""
        with open(file_path, mode, newline="") as f:
            if len(data) == 0:
                return
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            if mode == "w":
                writer.writeheader()
            writer.writerows(data)
    
    def add_customer(self, name: str, email: str, phone: str, address: str) -> str:
        """
        Add a new customer to the system.
        
        Args:
            name: Customer name
            email: Customer email
            phone: Customer phone number
            address: Customer address
            
        Returns:
            The generated customer ID
        """
        customer_id = self._generate_id("CUST")
        customer = {
            "customer_id": customer_id,
            "name": name,
            "email": email,
            "phone": phone,
            "address": address
        }
        self._write_csv(self.customers_file, [customer])
        return customer_id
    
    def add_vendor(self, name: str, email: str, phone: str, address: str) -> str:
        """
        Add a new vendor to the system.
        
        Args:
            name: Vendor name
            email: Vendor email
            phone: Vendor phone number
            address: Vendor address
            
        Returns:
            The generated vendor ID
        """
        vendor_id = self._generate_id("VEND")
        vendor = {
            "vendor_id": vendor_id,
            "name": name,
            "email": email,
            "phone": phone,
            "address": address
        }
        self._write_csv(self.vendors_file, [vendor])
        return vendor_id
    
    def create_invoice(
        self,
        invoice_type: str,
        customer_or_vendor_id: str,
        amount: float,
        description: str,
        due_date: Optional[str] = None,
        date: Optional[str] = None
    ) -> str:
        """
        Create a new invoice (accounts receivable or payable).
        
        Args:
            invoice_type: Either 'receivable' or 'payable'
            customer_or_vendor_id: ID of customer (for receivable) or vendor (for payable)
            amount: Invoice amount
            description: Description of the invoice
            due_date: Due date in YYYY-MM-DD format (default: 30 days from today)
            date: Invoice date in YYYY-MM-DD format (default: today)
            
        Returns:
            The generated invoice ID
            
        Raises:
            ValueError: If invoice_type is invalid
        """
        if invoice_type not in ["receivable", "payable"]:
            raise ValueError("Invoice type must be either 'receivable' or 'payable'")
        
        invoice_id = self._generate_id("INV")
        today = datetime.date.today()
        
        if not date:
            date = today.strftime("%Y-%m-%d")
        
        if not due_date:
            due_date = (today + datetime.timedelta(days=30)).strftime("%Y-%m-%d")
        
        invoice = {
            "invoice_id": invoice_id,
            "type": invoice_type,
            "customer_or_vendor_id": customer_or_vendor_id,
            "date": date,
            "due_date": due_date,
            "amount": amount,
            "description": description,
            "status": "unpaid"
        }
        
        self._write_csv(self.invoices_file, [invoice])
        return invoice_id
    
    def record_payment(
        self,
        invoice_id: str,
        amount: float,
        method: str,
        reference: str,
        notes: str = "",
        date: Optional[str] = None
    ) -> str:
        """
        Record a payment against an invoice.
        
        Args:
            invoice_id: ID of the invoice being paid
            amount: Payment amount
            method: Payment method (e.g., 'cash', 'check', 'bank transfer')
            reference: Payment reference number
            notes: Additional notes about the payment
            date: Payment date in YYYY-MM-DD format (default: today)
            
        Returns:
            The generated payment ID
            
        Raises:
            ValueError: If invoice doesn't exist or is already paid
        """
        invoices = self._read_csv(self.invoices_file)
        target_invoice = None
        
        for invoice in invoices:
            if invoice["invoice_id"] == invoice_id:
                target_invoice = invoice
                break
        
        if not target_invoice:
            raise ValueError(f"Invoice with ID {invoice_id} not found")
        
        if target_invoice["status"] == "paid":
            raise ValueError(f"Invoice {invoice_id} is already paid")
        
        payment_id = self._generate_id("PAY")
        today = datetime.date.today()
        
        if not date:
            date = today.strftime("%Y-%m-%d")
        
        payment = {
            "payment_id": payment_id,
            "invoice_id": invoice_id,
            "date": date,
            "amount": amount,
            "method": method,
            "reference": reference,
            "notes": notes
        }
        
        # Update invoice status if full payment is made
        if float(target_invoice["amount"]) <= amount:
            for invoice in invoices:
                if invoice["invoice_id"] == invoice_id:
                    invoice["status"] = "paid"
                    break
            
            # Rewrite all invoices with updated status
            self._write_csv(self.invoices_file, invoices, mode="w")
        
        self._write_csv(self.payments_file, [payment])
        return payment_id
    
    def get_customer_invoices(self, customer_id: str) -> List[Dict]:
        """
        Get all invoices for a specific customer.
        
        Args:
            customer_id: ID of the customer
            
        Returns:
            List of invoices for the customer
        """
        invoices = self._read_csv(self.invoices_file)
        return [
            inv for inv in invoices 
            if inv["type"] == "receivable" and inv["customer_or_vendor_id"] == customer_id
        ]
    
    def get_vendor_invoices(self, vendor_id: str) -> List[Dict]:
        """
        Get all invoices for a specific vendor.
        
        Args:
            vendor_id: ID of the vendor
            
        Returns:
            List of invoices for the vendor
        """
        invoices = self._read_csv(self.invoices_file)
        return [
            inv for inv in invoices 
            if inv["type"] == "payable" and inv["customer_or_vendor_id"] == vendor_id
        ]
    
    def get_outstanding_invoices(self, invoice_type: str) -> List[Dict]:
        """
        Get all outstanding (unpaid) invoices of a specific type.
        
        Args:
