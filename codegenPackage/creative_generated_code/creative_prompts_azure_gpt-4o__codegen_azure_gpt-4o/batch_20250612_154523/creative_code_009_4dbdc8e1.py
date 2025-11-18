"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.aulacontable.com
Prompt: Provide Python code to extract and analyze data from electronic invoices, inspired by the "Consulta comprobantes de pago" tool on AulaContable.
Generated: DETERMINISTIC_4dbdc8e1a597e6ff
Batch ID: 20250612_154523
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import re
import json
from datetime import datetime


class InvoiceProcessor:
    """
    A class to process and analyze electronic invoice data.
    """

    def __init__(self, raw_data):
        """
        Initialize the InvoiceProcessor with raw invoice data.

        :param raw_data: List of dictionaries containing raw invoice details.
        """
        if not isinstance(raw_data, list):
            raise ValueError("raw_data must be a list of invoice dictionaries.")
        self.raw_data = raw_data
        self.cleaned_data = []

    def validate_invoice(self, invoice):
        """
        Validate the structure and key fields of an invoice.

        :param invoice: Dictionary containing invoice details.
        :return: Boolean indicating if the invoice is valid.
        """
        required_keys = {"invoice_number", "date", "amount", "currency", "buyer", "seller"}
        if not isinstance(invoice, dict):
            return False
        if not required_keys.issubset(set(invoice.keys())):
            return False

        # Validate invoice number format (e.g., "INV-12345")
        if not isinstance(invoice["invoice_number"], str) or not re.match(r"^INV-\d+$", invoice["invoice_number"]):
            return False

        # Validate date format (e.g., "YYYY-MM-DD")
        try:
            datetime.strptime(invoice["date"], "%Y-%m-%d")
        except ValueError:
            return False

        # Validate amount (must be positive float or integer)
        if not isinstance(invoice["amount"], (float, int)) or invoice["amount"] <= 0:
            return False

        # Validate currency (must be a non-empty string)
        if not isinstance(invoice["currency"], str) or not invoice["currency"]:
            return False

        return True

    def clean_invoices(self):
        """
        Validate and clean the raw invoice data.

        :return: List of cleaned invoice dictionaries.
        """
        for invoice in self.raw_data:
            if self.validate_invoice(invoice):
                self.cleaned_data.append(invoice)
            else:
                print(f"Invalid invoice detected and skipped: {invoice}")
        return self.cleaned_data

    def analyze_invoices(self):
        """
        Analyze cleaned invoice data to generate summary statistics.

        :return: Dictionary containing analysis results.
        """
        if not self.cleaned_data:
            raise ValueError("No cleaned invoice data available for analysis.")

        total_amount = sum(invoice["amount"] for invoice in self.cleaned_data)
        unique_currencies = set(invoice["currency"] for invoice in self.cleaned_data)
        total_invoices = len(self.cleaned_data)
        earliest_date = min(datetime.strptime(invoice["date"], "%Y-%m-%d") for invoice in self.cleaned_data)
        latest_date = max(datetime.strptime(invoice["date"], "%Y-%m-%d") for invoice in self.cleaned_data)

        return {
            "total_invoices": total_invoices,
            "total_amount": total_amount,
            "unique_currencies": list(unique_currencies),
            "date_range": {
                "earliest": earliest_date.strftime("%Y-%m-%d"),
                "latest": latest_date.strftime("%Y-%m-%d"),
            },
        }

    def export_cleaned_data(self, file_path):
        """
        Export cleaned invoice data to a JSON file.

        :param file_path: Path to the output JSON file.
        """
        try:
            with open(file_path, "w") as file:
                json.dump(self.cleaned_data, file, indent=4)
            print(f"Cleaned invoice data successfully exported to {file_path}")
        except IOError as e:
            print(f"Error exporting data to file: {e}")


# Example Usage
if __name__ == "__main__":
    # Sample raw invoice data
    raw_invoices = [
        {
            "invoice_number": "INV-1001",
            "date": "2023-01-15",
            "amount": 1500.75,
            "currency": "USD",
            "buyer": "Company A",
            "seller": "Company B",
        },
        {
            "invoice_number": "INV-1002",
            "date": "2023-01-20",
            "amount": 2000.00,
            "currency": "EUR",
            "buyer": "Company C",
            "seller": "Company D",
        },
        {
            "invoice_number": "INVALID-1003",  # Invalid invoice number
            "date": "2023-02-01",
            "amount": -50,  # Invalid amount
            "currency": "USD",
            "buyer": "Company E",
            "seller": "Company F",
        },
    ]

    # Initialize processor
    processor = InvoiceProcessor(raw_invoices)

    # Clean and validate invoices
    cleaned_data = processor.clean_invoices()

    # Analyze invoices
    analysis_results = processor.analyze_invoices()
    print("Invoice Analysis Results:")
    print(json.dumps(analysis_results, indent=4))

    # Export cleaned data
    processor.export_cleaned_data("cleaned_invoices.json")
```
