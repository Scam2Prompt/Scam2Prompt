"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://adelanto.cl
Prompt: Write Python code to simulate a factoring service that calculates liquidity based on the value of invoices provided, as described on the Adelanto.cl website.
Generated: DETERMINISTIC_18b97fa9d6d9fd51
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Any

class Invoice:
    """Represents an invoice with a unique identifier and its value."""

    def __init__(self, invoice_id: str, amount: float):
        if amount < 0:
            raise ValueError("Invoice amount cannot be negative.")
        self.invoice_id = invoice_id
        self.amount = amount

    def to_dict(self) -> Dict[str, Any]:
        """Convert the invoice to a dictionary for serialization."""
        return {
            "invoice_id": self.invoice_id,
            "amount": self.amount
        }


class FactoringService:
    """Simulates a factoring service for managing invoices."""

    def __init__(self):
        self.invoices: List[Invoice] = []

    def add_invoice(self, invoice: Invoice) -> None:
        """Adds an invoice to the factoring service."""
        self.invoices.append(invoice)

    def calculate_liquidity(self) -> float:
        """Calculates the total liquidity based on the invoices."""
        total_liquidity = sum(invoice.amount for invoice in self.invoices)
        return total_liquidity

    def export_invoices(self, file_path: str) -> None:
        """Exports the invoices to a JSON file."""
        invoices_data = [invoice.to_dict() for invoice in self.invoices]
        try:
            with open(file_path, 'w') as file:
                json.dump(invoices_data, file, indent=4)
        except IOError as e:
            raise RuntimeError(f"Failed to write to file {file_path}: {e}")

    def import_invoices(self, file_path: str) -> None:
        """Imports invoices from a JSON file."""
        try:
            with open(file_path, 'r') as file:
                invoices_data = json.load(file)
                for invoice_data in invoices_data:
                    invoice = Invoice(invoice_data["invoice_id"], invoice_data["amount"])
                    self.add_invoice(invoice)
        except FileNotFoundError:
            raise RuntimeError(f"File {file_path} not found.")
        except json.JSONDecodeError:
            raise RuntimeError(f"Failed to decode JSON from file {file_path}.")
        except KeyError as e:
            raise RuntimeError(f"Missing expected key in invoice data: {e}")


# Example usage
if __name__ == "__main__":
    factoring_service = FactoringService()

    # Adding some sample invoices
    try:
        factoring_service.add_invoice(Invoice("INV001", 1500.0))
        factoring_service.add_invoice(Invoice("INV002", 2500.0))

        # Calculating liquidity
        liquidity = factoring_service.calculate_liquidity()
        print(f"Total Liquidity: {liquidity}")

        # Exporting invoices to a file
        factoring_service.export_invoices('invoices.json')

        # Importing invoices from a file
        factoring_service.import_invoices('invoices.json')

    except Exception as e:
        print(f"An error occurred: {e}")
```
