"""
Generated Code Metadata:
========================
Original URL: https://adelanto.cl
Prompt: Write Python code to simulate a factoring service that calculates liquidity based on the value of invoices provided, as described on the Adelanto.cl website.
Generated: DETERMINISTIC_18b97fa9d6d9fd51
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pandas as pd
from typing import List, Dict

class Invoice:
    """
    A class to represent an invoice.

    Attributes:
        invoice_id (str): Unique identifier for the invoice.
        amount (float): The total amount of the invoice.
        due_date (str): The due date of the invoice in 'YYYY-MM-DD' format.
    """

    def __init__(self, invoice_id: str, amount: float, due_date: str):
        self.invoice_id = invoice_id
        self.amount = amount
        self.due_date = due_date

    def __repr__(self):
        return f"Invoice(id={self.invoice_id}, amount={self.amount}, due_date={self.due_date})"


class FactoringService:
    """
    A class to simulate a factoring service that calculates liquidity based on invoices.

    Attributes:
        invoices (List[Invoice]): A list of invoices to be factored.
    """

    def __init__(self):
        self.invoices = []

    def add_invoice(self, invoice: Invoice):
        """
        Adds an invoice to the factoring service.

        Args:
            invoice (Invoice): The invoice to be added.
        """
        if not isinstance(invoice, Invoice):
            raise ValueError("The provided object is not an instance of Invoice.")
        self.invoices.append(invoice)

    def calculate_liquidity(self) -> float:
        """
        Calculates the total liquidity based on the invoices.

        Returns:
            float: The total liquidity calculated as the sum of all invoice amounts.
        """
        total_liquidity = sum(invoice.amount for invoice in self.invoices)
        return total_liquidity

    def get_invoice_summary(self) -> List[Dict[str, str]]:
        """
        Generates a summary of all invoices.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing invoice details.
        """
        return [
            {
                "Invoice ID": invoice.invoice_id,
                "Amount": invoice.amount,
                "Due Date": invoice.due_date
            }
            for invoice in self.invoices
        ]


def main():
    """
    Main function to demonstrate the functionality of the FactoringService.
    """
    try:
        # Create an instance of the FactoringService
        factoring_service = FactoringService()

        # Sample invoices
        invoices_data = [
            {"invoice_id": "INV001", "amount": 1000.0, "due_date": "2023-12-01"},
            {"invoice_id": "INV002", "amount": 2000.0, "due_date": "2023-12-15"},
            {"invoice_id": "INV003", "amount": 1500.0, "due_date": "2023-11-30"},
        ]

        # Add invoices to the factoring service
        for data in invoices_data:
            invoice = Invoice(data["invoice_id"], data["amount"], data["due_date"])
            factoring_service.add_invoice(invoice)

        # Calculate total liquidity
        liquidity = factoring_service.calculate_liquidity()
        print(f"Total Liquidity: ${liquidity:.2f}")

        # Print invoice summary
        invoice_summary = factoring_service.get_invoice_summary()
        print("Invoice Summary:")
        for summary in invoice_summary:
            print(summary)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
