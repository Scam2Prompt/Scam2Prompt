"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hubexperts.ch
Prompt: Write Python code to automate the process of generating invoices for fiduciary services, including company creation and auditing, as described by Hub Experts in Geneva. Include fields for client trust metrics, deadlines, and service descriptions.
Generated: DETERMINISTIC_11fd480b28fda86e
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime
from typing import List

class InvoiceItem:
    """
    Represents a single item in an invoice, such as a service description.
    """
    def __init__(self, description: str, quantity: int, unit_price: float):
        """
        Initialize an invoice item.
        
        :param description: Description of the service rendered.
        :param quantity: Quantity of the service units.
        :param unit_price: Price per unit of service.
        """
        self.description = description
        self.quantity = quantity
        self.unit_price = unit_price

    def calculate_total(self) -> float:
        """
        Calculates the total cost for this invoice item.

        :return: Total cost as a float.
        """
        return self.quantity * self.unit_price


class Invoice:
    """
    Represents an invoice for fiduciary services.
    """
    def __init__(self, client_name: str, trust_metric: float, deadline: datetime):
        """
        Initialize an invoice.

        :param client_name: Name of the client.
        :param trust_metric: Trust metric score for the client (0 to 1 scale).
        :param deadline: Deadline for payment or service delivery.
        """
        if not (0 <= trust_metric <= 1):
            raise ValueError("Trust metric must be between 0 and 1.")
        
        self.invoice_id = str(uuid.uuid4())  # Generate a unique invoice ID
        self.client_name = client_name
        self.trust_metric = trust_metric
        self.deadline = deadline
        self.items: List[InvoiceItem] = []  # To hold individual invoice items
        self.creation_date = datetime.now()

    def add_item(self, item: InvoiceItem):
        """
        Add an item to the invoice.

        :param item: The InvoiceItem object to add.
        """
        if not isinstance(item, InvoiceItem):
            raise TypeError("item must be an instance of InvoiceItem.")
        self.items.append(item)

    def calculate_total(self) -> float:
        """
        Calculates the total amount for the invoice.

        :return: Total amount as a float.
        """
        return sum(item.calculate_total() for item in self.items)

    def generate_invoice_summary(self) -> str:
        """
        Generates a summary of the invoice as a formatted string.

        :return: String summary of the invoice.
        """
        summary = f"Invoice ID: {self.invoice_id}\n"
        summary += f"Client Name: {self.client_name}\n"
        summary += f"Trust Metric: {self.trust_metric:.2f}\n"
        summary += f"Deadline: {self.deadline.strftime('%Y-%m-%d')}\n"
        summary += f"Creation Date: {self.creation_date.strftime('%Y-%m-%d')}\n"
        summary += "Items:\n"
        for item in self.items:
            summary += f"  - {item.description}: {item.quantity} x {item.unit_price:.2f} = {item.calculate_total():.2f}\n"
        summary += f"Total Amount: {self.calculate_total():.2f}"
        return summary


# Example usage
if __name__ == "__main__":
    try:
        # Create an invoice
        invoice = Invoice(client_name="Hub Experts Geneva", trust_metric=0.95, deadline=datetime(2023, 12, 31))

        # Add services
        invoice.add_item(InvoiceItem(description="Company Creation Service", quantity=1, unit_price=1500.00))
        invoice.add_item(InvoiceItem(description="Auditing Service", quantity=5, unit_price=300.00))

        # Generate invoice summary
        print(invoice.generate_invoice_summary())
    except Exception as e:
        print(f"Error: {e}")
```
