"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aluivars.com
Prompt: Create a program to generate invoices for custom carpentry projects, including detailed descriptions of services like aluminum carpentry, iron forging, and glass installations, inspired by Aluivars' offerings.
Generated: DETERMINISTIC_98053c55793e7894
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import uuid

class Invoice:
    """
    A class to create and manage invoices for custom carpentry projects.
    """

    def __init__(self, client_name, project_description, services):
        """
        Initialize an Invoice instance.

        :param client_name: Name of the customer/client
        :param project_description: Brief description of the carpentry project
        :param services: List of services with details (service name, quantity, unit price)
        """
        self.invoice_id = str(uuid.uuid4())  # Generate a unique invoice ID
        self.client_name = client_name
        self.project_description = project_description
        self.services = services
        self.date = datetime.datetime.now()  # Current date and time
        self.total_amount = self.calculate_total()

    def calculate_total(self):
        """
        Calculate the total amount for the invoice. Sum up costs for all services.

        :return: Total invoice amount
        """
        total = 0
        for service in self.services:
            quantity = service.get("quantity", 0)
            unit_price = service.get("unit_price", 0)
            total += quantity * unit_price
        return total

    def generate_invoice(self):
        """
        Generate the invoice details in a formatted string.

        :return: Formatted invoice string
        """
        invoice_str = f"Invoice ID: {self.invoice_id}\n"
        invoice_str += f"Date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}\n"
        invoice_str += f"Client Name: {self.client_name}\n"
        invoice_str += f"Project Description: {self.project_description}\n\n"
        invoice_str += "Services Provided:\n"
        invoice_str += f"{'Service Name':<20}{'Quantity':<10}{'Unit Price':<15}{'Total':<10}\n"
        invoice_str += "-" * 55 + "\n"

        for service in self.services:
            name = service.get("name", "Unknown Service")
            quantity = service.get("quantity", 0)
            unit_price = service.get("unit_price", 0)
            total = quantity * unit_price
            invoice_str += f"{name:<20}{quantity:<10}{unit_price:<15}{total:<10}\n"

        invoice_str += "-" * 55 + "\n"
        invoice_str += f"Total Amount Due: ${self.total_amount:.2f}\n"
        invoice_str += "-" * 55 + "\n"

        return invoice_str

# Example usage
if __name__ == "__main__":
    try:
        # Sample list of services
        services = [
            {"name": "Aluminum Carpentry", "quantity": 5, "unit_price": 120.50},
            {"name": "Iron Forging", "quantity": 3, "unit_price": 200.75},
            {"name": "Glass Installation", "quantity": 10, "unit_price": 65.00},
        ]

        # Create an invoice instance
        invoice = Invoice(
            client_name="John Doe",
            project_description="Custom carpentry for residential property",
            services=services,
        )

        # Generate and print invoice
        print(invoice.generate_invoice())
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred while generating the invoice: {str(e)}")
```
