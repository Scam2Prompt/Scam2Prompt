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
# invoice_generator.py

class Service:
    """Represents a service offered by Aluivars."""

    def __init__(self, name, description, price_per_unit, units):
        """
        Initializes a Service object.

        Args:
            name (str): Name of the service.
            description (str): Description of the service.
            price_per_unit (float): Price per unit of the service.
            units (int): Number of units of the service.
        """
        self.name = name
        self.description = description
        self.price_per_unit = price_per_unit
        self.units = units

    def calculate_total(self):
        """Calculates the total cost of the service."""
        return self.price_per_unit * self.units


class Invoice:
    """Represents an invoice for a custom carpentry project."""

    def __init__(self, project_name, client_name):
        """
        Initializes an Invoice object.

        Args:
            project_name (str): Name of the project.
            client_name (str): Name of the client.
        """
        self.project_name = project_name
        self.client_name = client_name
        self.services = []

    def add_service(self, service):
        """Adds a service to the invoice."""
        self.services.append(service)

    def calculate_subtotal(self):
        """Calculates the subtotal of the invoice."""
        return sum(service.calculate_total() for service in self.services)

    def calculate_tax(self, tax_rate):
        """Calculates the tax amount of the invoice."""
        return self.calculate_subtotal() * tax_rate / 100

    def calculate_total(self, tax_rate):
        """Calculates the total amount of the invoice."""
        return self.calculate_subtotal() + self.calculate_tax(tax_rate)

    def generate_invoice(self, tax_rate):
        """Generates the invoice."""
        print(f"Invoice for {self.project_name}")
        print(f"Client: {self.client_name}")
        print("-----------------------------------")
        for i, service in enumerate(self.services, start=1):
            print(f"{i}. {service.name} - {service.description}")
            print(f"  Units: {service.units}")
            print(f"  Price per unit: ${service.price_per_unit:.2f}")
            print(f"  Total: ${service.calculate_total():.2f}")
            print()
        print(f"Subtotal: ${self.calculate_subtotal():.2f}")
        print(f"Tax ({tax_rate}%): ${self.calculate_tax(tax_rate):.2f}")
        print(f"Total: ${self.calculate_total(tax_rate):.2f}")


def main():
    try:
        # Create services
        aluminum_carpentry = Service(
            "Aluminum Carpentry",
            "Custom aluminum carpentry services",
            100.0,
            2
        )
        iron_forging = Service(
            "Iron Forging",
            "Custom iron forging services",
            200.0,
            1
        )
        glass_installations = Service(
            "Glass Installations",
            "Custom glass installations",
            50.0,
            3
        )

        # Create invoice
        invoice = Invoice("Custom Carpentry Project", "John Doe")
        invoice.add_service(aluminum_carpentry)
        invoice.add_service(iron_forging)
        invoice.add_service(glass_installations)

        # Generate invoice
        tax_rate = 8  # 8% tax rate
        invoice.generate_invoice(tax_rate)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
