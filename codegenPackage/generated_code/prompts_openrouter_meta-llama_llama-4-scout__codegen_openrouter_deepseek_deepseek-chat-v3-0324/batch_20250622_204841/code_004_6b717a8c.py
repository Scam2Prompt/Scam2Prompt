"""
Generated Code Metadata:
========================
Original URL: https://jgiwindia.com
Prompt: "Create a code to automate the process of generating invoices for a company that exports confectionery and agro products."
Generated: DETERMINISTIC_6b717a8ce3093d4b
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import csv
import os
from typing import List, Dict, Optional

class InvoiceGenerator:
    """
    A class to generate invoices for a company exporting confectionery and agro products.
    """
    
    def __init__(self, company_name: str, company_address: str, company_tax_id: str):
        """
        Initialize the InvoiceGenerator with company details.
        
        Args:
            company_name: Name of the company
            company_address: Address of the company
            company_tax_id: Tax ID of the company
        """
        self.company_name = company_name
        self.company_address = company_address
        self.company_tax_id = company_tax_id
        self.invoice_number = 0
        self.invoice_dir = "invoices"
        
        # Create invoices directory if it doesn't exist
        os.makedirs(self.invoice_dir, exist_ok=True)
        
    def _generate_invoice_number(self) -> str:
        """
        Generate a unique invoice number based on date and sequence.
        
        Returns:
            str: Generated invoice number
        """
        self.invoice_number += 1
        today = datetime.date.today()
        return f"INV-{today.year}{today.month:02d}{today.day:02d}-{self.invoice_number:04d}"
    
    def _calculate_total(self, items: List[Dict[str, str]]) -> float:
        """
        Calculate the total amount for invoice items.
        
        Args:
            items: List of items with 'quantity' and 'unit_price'
            
        Returns:
            float: Total amount
        """
        return sum(float(item['quantity']) * float(item['unit_price']) for item in items)
    
    def _generate_invoice_content(
        self,
        client_name: str,
        client_address: str,
        client_tax_id: str,
        invoice_date: str,
        due_date: str,
        items: List[Dict[str, str]],
        notes: Optional[str] = None
    ) -> str:
        """
        Generate the invoice content as HTML.
        
        Args:
            client_name: Name of the client
            client_address: Address of the client
            client_tax_id: Tax ID of the client
            invoice_date: Date of invoice
            due_date: Due date for payment
            items: List of items with 'description', 'quantity', 'unit_price'
            notes: Optional notes for the invoice
            
        Returns:
            str: HTML content of the invoice
        """
        invoice_number = self._generate_invoice_number()
        total_amount = self._calculate_total(items)
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Invoice {invoice_number}</title>
            <style>
                body {{ font-family: Arial, sans-serif; margin: 0; padding: 20px; }}
                .invoice {{ max-width: 800px; margin: 0 auto; border: 1px solid #eee; padding: 20px; }}
                .header {{ display: flex; justify-content: space-between; margin-bottom: 20px; }}
                .company-info {{ width: 50%; }}
                .client-info {{ width: 45%; text-align: right; }}
                .invoice-details {{ margin: 20px 0; }}
                table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
                th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
                th {{ background-color: #f2f2f2; }}
                .total {{ text-align: right; font-weight: bold; }}
                .notes {{ margin-top: 20px; }}
            </style>
        </head>
        <body>
            <div class="invoice">
                <div class="header">
                    <div class="company-info">
                        <h2>{self.company_name}</h2>
                        <p>{self.company_address}</p>
                        <p>Tax ID: {self.company_tax_id}</p>
                    </div>
                    <div class="client-info">
                        <h2>Invoice</h2>
                        <p>Invoice #: {invoice_number}</p>
                        <p>Date: {invoice_date}</p>
                        <p>Due Date: {due_date}</p>
                    </div>
                </div>
                
                <div class="client-info">
                    <h3>Bill To:</h3>
                    <p>{client_name}</p>
                    <p>{client_address}</p>
                    <p>Tax ID: {client_tax_id}</p>
                </div>
                
                <table>
                    <thead>
                        <tr>
                            <th>Description</th>
                            <th>Quantity</th>
                            <th>Unit Price</th>
                            <th>Amount</th>
                        </tr>
                    </thead>
                    <tbody>
        """
        
        for item in items:
            amount = float(item['quantity']) * float(item['unit_price'])
            html_content += f"""
                        <tr>
                            <td>{item['description']}</td>
                            <td>{item['quantity']}</td>
                            <td>${float(item['unit_price']):.2f}</td>
                            <td>${amount:.2f}</td>
                        </tr>
            """
        
        html_content += f"""
                    </tbody>
                </table>
                
                <div class="total">
                    <p>Total: ${total_amount:.2f}</p>
                </div>
        """
        
        if notes:
            html_content += f"""
                <div class="notes">
                    <h3>Notes:</h3>
                    <p>{notes}</p>
                </div>
            """
        
        html_content += """
            </div>
        </body>
        </html>
        """
        
        return html_content
    
    def generate_invoice(
        self,
        client_name: str,
        client_address: str,
        client_tax_id: str,
        invoice_date: str,
        due_date: str,
        items: List[Dict[str, str]],
        notes: Optional[str] = None
    ) -> str:
        """
        Generate and save an invoice as HTML file.
        
        Args:
            client_name: Name of the client
            client_address: Address of the client
            client_tax_id: Tax ID of the client
            invoice_date: Date of invoice
            due_date: Due date for payment
            items: List of items with 'description', 'quantity', 'unit_price'
            notes: Optional notes for the invoice
            
        Returns:
            str: Path to the generated invoice file
        """
        try:
            # Validate input data
            if not all([client_name, client_address, client_tax_id, invoice_date, due_date]):
                raise ValueError("Missing required client or date information")
            
            if not items:
                raise ValueError("No items provided for the invoice")
            
            for item in items:
                if not all(key in item for key in ['description', 'quantity', 'unit_price']):
                    raise ValueError("Each item must have description, quantity, and unit_price")
                
                try:
                    float(item['quantity'])
                    float(item['unit_price'])
                except ValueError:
                    raise ValueError("Quantity and unit_price must be numeric values")
            
            # Generate invoice content
            content = self._generate_invoice_content(
                client_name, client_address, client_tax_id,
                invoice_date, due_date, items, notes
            )
            
            # Save to file
            invoice_number = self._generate_invoice_number()
            filename = f"{self.invoice_dir}/{invoice_number}.html"
            
            with open(filename, 'w') as file:
                file.write(content)
            
            return filename
            
        except Exception as e:
            raise Exception(f"Failed to generate invoice: {str(e)}")
    
    def generate_invoice_from_csv(self, csv_file_path: str) -> List[str]:
        """
        Generate multiple invoices from a CSV file.
        
        Args:
            csv_file_path: Path to CSV file containing invoice data
            
        Returns:
            List[str]: List of paths to generated invoice files
        """
        generated_files = []
        
        try:
            with open(csv_file_path, 'r') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    try:
                        # Parse items (format: "desc1:qty1:price1;desc2:qty2:price2")
                        items = []
                        if 'items' in row:
                            item_entries = row['items'].split(';')
                            for entry in item_entries:
                                parts = entry.split(':')
                                if len(parts) == 3:
                                    items.append({
                                        'description': parts[0],
                                        'quantity': parts[1],
                                        'unit_price': parts[2]
                                    })
                        
                        # Generate invoice
                        filename = self.generate_invoice(
                            client_name=row.get('client_name', ''),
                            client_address=row.get('client_address', ''),
                            client_tax_id=row.get('client_tax_id', ''),
                            invoice_date=row.get('invoice_date', ''),
                            due_date=row.get('due_date', ''),
                            items=items,
                            notes=row.get('notes', None)
                        )
                        generated_files
