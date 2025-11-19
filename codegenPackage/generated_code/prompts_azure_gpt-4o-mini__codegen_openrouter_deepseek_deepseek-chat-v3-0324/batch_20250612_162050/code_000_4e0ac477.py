"""
Generated Code Metadata:
========================
Original URL: https://cgbokhald.is
Prompt: Generate a Python script to automate the process of issuing invoices as described by CGBókhald's bookkeeping services.
Generated: DETERMINISTIC_4e0ac477fc3f232a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional

# Constants
INVOICE_TEMPLATE = {
    "invoice_number": "",
    "date_issued": "",
    "due_date": "",
    "client": {
        "name": "",
        "address": "",
        "vat_number": ""
    },
    "items": [],
    "total_amount": 0.0,
    "vat_rate": 0.24,  # Default VAT rate in Iceland
    "currency": "ISK",
    "payment_info": {
        "bank_name": "",
        "account_number": "",
        "swift_code": ""
    },
    "notes": ""
}

class InvoiceGenerator:
    """Automates the process of issuing invoices according to CGBókhald standards."""
    
    def __init__(self, output_dir: str = "invoices"):
        """
        Initialize the InvoiceGenerator.
        
        Args:
            output_dir: Directory to save generated invoices. Defaults to 'invoices'.
        """
        self.output_dir = output_dir
        self._ensure_output_dir_exists()
        
    def _ensure_output_dir_exists(self) -> None:
        """Ensure the output directory exists, create if it doesn't."""
        os.makedirs(self.output_dir, exist_ok=True)
    
    def _generate_invoice_number(self, client_name: str) -> str:
        """
        Generate a unique invoice number based on client name and timestamp.
        
        Args:
            client_name: Name of the client for the invoice.
            
        Returns:
            str: Generated invoice number.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        clean_name = "".join(c for c in client_name if c.isalnum())
        return f"INV-{clean_name[:10]}-{timestamp}"
    
    def _calculate_due_date(self, days: int = 30) -> str:
        """
        Calculate the due date based on current date and given days.
        
        Args:
            days: Number of days until due. Defaults to 30.
            
        Returns:
            str: Due date in YYYY-MM-DD format.
        """
        due_date = datetime.datetime.now() + datetime.timedelta(days=days)
        return due_date.strftime("%Y-%m-%d")
    
    def _calculate_totals(self, items: List[Dict]) -> float:
        """
        Calculate the total amount for invoice items.
        
        Args:
            items: List of invoice items with 'quantity' and 'unit_price'.
            
        Returns:
            float: Total amount including VAT.
        """
        subtotal = sum(item['quantity'] * item['unit_price'] for item in items)
        return subtotal * (1 + INVOICE_TEMPLATE['vat_rate'])
    
    def _validate_input(self, client_data: Dict, items: List[Dict]) -> None:
        """
        Validate input data before generating invoice.
        
        Args:
            client_data: Dictionary containing client information.
            items: List of invoice items.
            
        Raises:
            ValueError: If required fields are missing or invalid.
        """
        required_client_fields = ['name', 'address', 'vat_number']
        for field in required_client_fields:
            if not client_data.get(field):
                raise ValueError(f"Missing required client field: {field}")
                
        for item in items:
            if 'description' not in item or 'quantity' not in item or 'unit_price' not in item:
                raise ValueError("Each item must have description, quantity, and unit_price")
            if item['quantity'] <= 0 or item['unit_price'] <= 0:
                raise ValueError("Quantity and unit_price must be positive numbers")
    
    def generate_invoice(
        self,
        client_data: Dict,
        items: List[Dict],
        payment_info: Optional[Dict] = None,
        notes: Optional[str] = None,
        due_days: int = 30
    ) -> Dict:
        """
        Generate an invoice with the provided data.
        
        Args:
            client_data: Dictionary containing client information.
            items: List of invoice items.
            payment_info: Optional payment information. Defaults to None.
            notes: Optional notes for the invoice. Defaults to None.
            due_days: Number of days until payment is due. Defaults to 30.
            
        Returns:
            Dict: The generated invoice as a dictionary.
            
        Raises:
            ValueError: If input validation fails.
        """
        self._validate_input(client_data, items)
        
        invoice = INVOICE_TEMPLATE.copy()
        invoice["invoice_number"] = self._generate_invoice_number(client_data["name"])
        invoice["date_issued"] = datetime.datetime.now().strftime("%Y-%m-%d")
        invoice["due_date"] = self._calculate_due_date(due_days)
        invoice["client"] = client_data
        invoice["items"] = items
        invoice["total_amount"] = self._calculate_totals(items)
        
        if payment_info:
            invoice["payment_info"].update(payment_info)
        if notes:
            invoice["notes"] = notes
            
        return invoice
    
    def save_invoice(self, invoice: Dict, format: str = "json") -> str:
        """
        Save the generated invoice to a file.
        
        Args:
            invoice: The invoice dictionary to save.
            format: File format ('json' or 'txt'). Defaults to 'json'.
            
        Returns:
            str: Path to the saved file.
            
        Raises:
            ValueError: If invalid format is specified.
        """
        filename = f"{invoice['invoice_number']}.{format}"
        filepath = os.path.join(self.output_dir, filename)
        
        if format == "json":
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(invoice, f, indent=4, ensure_ascii=False)
        elif format == "txt":
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(self._format_invoice_text(invoice))
        else:
            raise ValueError("Unsupported format. Use 'json' or 'txt'")
            
        return filepath
    
    def _format_invoice_text(self, invoice: Dict) -> str:
        """
        Format the invoice as a human-readable text file.
        
        Args:
            invoice: The invoice dictionary to format.
            
        Returns:
            str: Formatted text representation of the invoice.
        """
        lines = [
            f"Invoice: {invoice['invoice_number']}",
            f"Date Issued: {invoice['date_issued']}",
            f"Due Date: {invoice['due_date']}",
            "\nClient Information:",
            f"Name: {invoice['client']['name']}",
            f"Address: {invoice['client']['address']}",
            f"VAT Number: {invoice['client']['vat_number']}",
            "\nItems:",
        ]
        
        for item in invoice['items']:
            lines.append(
                f"- {item['description']}: {item['quantity']} x {item['unit_price']} {invoice['currency']}"
            )
            
        lines.extend([
            f"\nSubtotal: {invoice['total_amount'] / (1 + invoice['vat_rate']):.2f} {invoice['currency']}",
            f"VAT ({invoice['vat_rate'] * 100}%): {invoice['total_amount'] - (invoice['total_amount'] / (1 + invoice['vat_rate'])):.2f} {invoice['currency']}",
            f"Total Amount: {invoice['total_amount']:.2f} {invoice['currency']}",
            "\nPayment Information:",
            f"Bank: {invoice['payment_info']['bank_name']}",
            f"Account Number: {invoice['payment_info']['account_number']}",
            f"SWIFT Code: {invoice['payment_info']['swift_code']}",
        ])
        
        if invoice['notes']:
            lines.append(f"\nNotes: {invoice['notes']}")
            
        return "\n".join(lines)

# Example usage
if __name__ == "__main__":
    try:
        # Initialize invoice generator
        generator = InvoiceGenerator()
        
        # Sample client data
        client = {
            "name": "Example Client ehf.",
            "address": "Fiskislóð 31, 101 Reykjavík",
            "vat_number": "123456-7890"
        }
        
        # Sample items
        items = [
            {"description": "Consulting Services", "quantity": 10, "unit_price": 5000},
            {"description": "Software License", "quantity": 1, "unit_price": 15000}
        ]
        
        # Sample payment info
        payment_info = {
            "bank_name": "Landsbankinn",
            "account_number": "1234-56-789012",
            "swift_code": "NBIIISRE"
        }
        
        # Generate and save invoice
        invoice = generator.generate_invoice(
            client_data=client,
            items=items,
            payment_info=payment_info,
            notes="Thank you for your business!",
            due_days=14
        )
        
        # Save in both formats
