"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Generate a code snippet that demonstrates how to implement a factoring service for small businesses, focusing on immediate liquidity and document management.
Generated: DETERMINISTIC_b50114eed68f2bd7
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Dict

class Invoice:
    """
    Represents an invoice for factoring purposes.
    """
    def __init__(self, invoice_id: str, amount: float, due_date: datetime, client_name: str):
        self.invoice_id = invoice_id
        self.amount = amount
        self.due_date = due_date
        self.client_name = client_name
        self.is_factored = False

    def factor_invoice(self):
        """
        Marks the invoice as factored.
        """
        self.is_factored = True


class FactoringService:
    """
    A service for factoring invoices to provide immediate liquidity to small businesses.
    """
    def __init__(self):
        self.invoices: List[Invoice] = []
        self.factored_invoices: List[Invoice] = []

    def add_invoice(self, amount: float, due_date: datetime, client_name: str) -> str:
        """
        Adds a new invoice to the system.

        :param amount: The amount of the invoice.
        :param due_date: The due date of the invoice.
        :param client_name: The name of the client associated with the invoice.
        :return: The ID of the created invoice.
        """
        try:
            invoice_id = str(uuid.uuid4())
            new_invoice = Invoice(invoice_id, amount, due_date, client_name)
            self.invoices.append(new_invoice)
            return invoice_id
        except Exception as e:
            raise RuntimeError(f"Failed to add invoice: {e}")

    def factor_invoice(self, invoice_id: str) -> Dict[str, str]:
        """
        Factors an invoice, providing immediate liquidity.

        :param invoice_id: The ID of the invoice to factor.
        :return: A dictionary containing the invoice details and factoring status.
        """
        try:
            for invoice in self.invoices:
                if invoice.invoice_id == invoice_id:
                    if invoice.is_factored:
                        raise ValueError("Invoice has already been factored.")
                    invoice.factor_invoice()
                    self.factored_invoices.append(invoice)
                    return {
                        "invoice_id": invoice.invoice_id,
                        "amount": f"${invoice.amount:.2f}",
                        "client_name": invoice.client_name,
                        "status": "Factored"
                    }
            raise ValueError("Invoice not found.")
        except Exception as e:
            raise RuntimeError(f"Failed to factor invoice: {e}")

    def list_invoices(self) -> List[Dict[str, str]]:
        """
        Lists all invoices in the system.

        :return: A list of dictionaries containing invoice details.
        """
        try:
            return [
                {
                    "invoice_id": invoice.invoice_id,
                    "amount": f"${invoice.amount:.2f}",
                    "due_date": invoice.due_date.strftime("%Y-%m-%d"),
                    "client_name": invoice.client_name,
                    "status": "Factored" if invoice.is_factored else "Pending"
                }
                for invoice in self.invoices
            ]
        except Exception as e:
            raise RuntimeError(f"Failed to list invoices: {e}")


# Example usage
if __name__ == "__main__":
    # Initialize the factoring service
    service = FactoringService()

    # Add invoices
    invoice_id_1 = service.add_invoice(5000.00, datetime(2023, 12, 15), "Client A")
    invoice_id_2 = service.add_invoice(3000.00, datetime(2023, 11, 30), "Client B")

    # Factor an invoice
    factored_invoice = service.factor_invoice(invoice_id_1)
    print("Factored Invoice:", factored_invoice)

    # List all invoices
    all_invoices = service.list_invoices()
    print("All Invoices:", all_invoices)
```
