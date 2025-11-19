"""
Generated Code Metadata:
========================
Original URL: https://aluivars.com
Prompt: Create a program to generate invoices for custom carpentry projects, including detailed descriptions of services like aluminum carpentry, iron forging, and glass installations, inspired by Aluivars' offerings.
Generated: DETERMINISTIC_98053c55793e7894
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class Invoice:
    """
    A class to represent an invoice for carpentry projects.
    """

    def __init__(self, client_name, project_details, services, invoice_number):
        """
        Initializes the Invoice with client details, project description, services, and invoice number.

        :param client_name: Name of the client
        :param project_details: Description of the carpentry project
        :param services: List of services provided
        :param invoice_number: Unique invoice number
        """
        self.client_name = client_name
        self.project_details = project_details
        self.services = services
        self.invoice_number = invoice_number
        self.date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def calculate_total(self):
        """
        Calculates the total cost of the services provided.

        :return: Total cost as a float
        """
        total = sum(service['price'] for service in self.services)
        return total

    def generate_invoice(self):
        """
        Generates a formatted invoice as a dictionary.

        :return: A dictionary containing invoice details
        """
        total_cost = self.calculate_total()
        invoice_data = {
            "invoice_number": self.invoice_number,
            "client_name": self.client_name,
            "project_details": self.project_details,
            "date_created": self.date_created,
            "services": self.services,
            "total_cost": total_cost
        }
        return invoice_data

    def save_invoice(self, filename):
        """
        Saves the invoice to a JSON file.

        :param filename: Name of the file to save the invoice
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.generate_invoice(), file, indent=4)
            print(f"Invoice saved successfully to {filename}")
        except IOError as e:
            print(f"Error saving invoice: {e}")

def main():
    """
    Main function to create and save an invoice for a carpentry project.
    """
    client_name = "John Doe"
    project_details = "Custom carpentry project including aluminum carpentry, iron forging, and glass installations."
    services = [
        {"description": "Aluminum Carpentry", "price": 1500.00},
        {"description": "Iron Forging", "price": 1200.00},
        {"description": "Glass Installation", "price": 800.00}
    ]
    invoice_number = "INV-2023-001"

    # Create an invoice instance
    invoice = Invoice(client_name, project_details, services, invoice_number)

    # Save the invoice to a file
    invoice.save_invoice("invoice.json")

if __name__ == "__main__":
    main()
```
