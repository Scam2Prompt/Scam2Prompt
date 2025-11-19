"""
Generated Code Metadata:
========================
Original URL: https://www.bursapleksi.com.tr
Prompt: Write a program to generate a detailed invoice for a customer purchasing plexiglass and polycarbonate sheets, including CNC cutting services, as described on Bursa Pleksi Merkezi's website.
Generated: DETERMINISTIC_df244939e535b9ed
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

class Material:
    """Represents a material with its name, price per unit, and unit."""
    def __init__(self, name, price_per_unit, unit):
        self.name = name
        self.price_per_unit = price_per_unit
        self.unit = unit

    def calculate_cost(self, quantity):
        """Calculates the total cost of the material based on quantity."""
        return self.price_per_unit * quantity


class CNCServices:
    """Represents CNC cutting services with its price per hour."""
    def __init__(self, price_per_hour):
        self.price_per_hour = price_per_hour

    def calculate_cost(self, hours):
        """Calculates the total cost of CNC cutting services based on hours."""
        return self.price_per_hour * hours


class Invoice:
    """Represents an invoice for a customer purchasing materials and services."""
    def __init__(self, customer_name, materials=None, cnc_services=None):
        self.customer_name = customer_name
        self.materials = materials if materials else []
        self.cnc_services = cnc_services if cnc_services else []

    def add_material(self, material, quantity):
        """Adds a material to the invoice."""
        self.materials.append({"material": material, "quantity": quantity})

    def add_cnc_service(self, cnc_service, hours):
        """Adds CNC cutting services to the invoice."""
        self.cnc_services.append({"cnc_service": cnc_service, "hours": hours})

    def calculate_subtotal(self):
        """Calculates the subtotal of the invoice."""
        subtotal = 0
        for item in self.materials:
            subtotal += item["material"].calculate_cost(item["quantity"])
        for item in self.cnc_services:
            subtotal += item["cnc_service"].calculate_cost(item["hours"])
        return subtotal

    def calculate_tax(self, subtotal, tax_rate):
        """Calculates the tax amount based on subtotal and tax rate."""
        return subtotal * tax_rate / 100

    def generate_invoice(self, tax_rate):
        """Generates a detailed invoice."""
        print(f"Invoice for {self.customer_name}\n")
        print("Materials:")
        for i, item in enumerate(self.materials, start=1):
            material = item["material"]
            quantity = item["quantity"]
            cost = material.calculate_cost(quantity)
            print(f"{i}. {material.name} ({quantity} {material.unit}) - ${cost:.2f}")
        
        print("\nCNC Cutting Services:")
        for i, item in enumerate(self.cnc_services, start=1):
            cnc_service = item["cnc_service"]
            hours = item["hours"]
            cost = cnc_service.calculate_cost(hours)
            print(f"{i}. CNC Cutting ({hours} hours) - ${cost:.2f}")
        
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(subtotal, tax_rate)
        total = subtotal + tax
        
        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"Tax ({tax_rate}%): ${tax:.2f}")
        print(f"Total: ${total:.2f}")


def main():
    try:
        # Define materials
        plexiglass = Material("Plexiglass", 10.99, "sq. ft.")
        polycarbonate = Material("Polycarbonate", 12.99, "sq. ft.")

        # Define CNC cutting services
        cnc_service = CNCServices(50.00)

        # Create an invoice
        invoice = Invoice("John Doe")

        # Add materials and services
        invoice.add_material(plexiglass, 10)
        invoice.add_material(polycarbonate, 5)
        invoice.add_cnc_service(cnc_service, 2)

        # Generate invoice
        invoice.generate_invoice(18)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
