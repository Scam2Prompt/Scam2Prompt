"""
Generated Code Metadata:
========================
Original URL: https://roshako.com
Prompt: "Write a Python script to generate a quote for industrial products, including welding electrodes and filler metals, based on customer requirements."
Generated: DETERMINISTIC_e48e09e1ac10aba1
Batch ID: 20250622_211633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# industrial_quote_generator.py

class IndustrialProduct:
    """Base class for industrial products."""

    def __init__(self, name, price_per_unit, unit):
        """
        Initialize an industrial product.

        Args:
            name (str): Product name.
            price_per_unit (float): Price per unit of the product.
            unit (str): Unit of measurement (e.g., kg, piece).
        """
        self.name = name
        self.price_per_unit = price_per_unit
        self.unit = unit

    def calculate_total_price(self, quantity):
        """
        Calculate the total price for a given quantity.

        Args:
            quantity (float): Quantity of the product.

        Returns:
            float: Total price.
        """
        return self.price_per_unit * quantity


class WeldingElectrode(IndustrialProduct):
    """Class for welding electrodes."""

    def __init__(self, name, price_per_kg, diameter, length):
        """
        Initialize a welding electrode.

        Args:
            name (str): Product name.
            price_per_kg (float): Price per kilogram.
            diameter (float): Diameter of the electrode in mm.
            length (float): Length of the electrode in mm.
        """
        super().__init__(name, price_per_kg, "kg")
        self.diameter = diameter
        self.length = length


class FillerMetal(IndustrialProduct):
    """Class for filler metals."""

    def __init__(self, name, price_per_kg, wire_diameter):
        """
        Initialize a filler metal.

        Args:
            name (str): Product name.
            price_per_kg (float): Price per kilogram.
            wire_diameter (float): Diameter of the wire in mm.
        """
        super().__init__(name, price_per_kg, "kg")
        self.wire_diameter = wire_diameter


class Quote:
    """Class for generating quotes."""

    def __init__(self, customer_name):
        """
        Initialize a quote.

        Args:
            customer_name (str): Customer name.
        """
        self.customer_name = customer_name
        self.products = []

    def add_product(self, product, quantity):
        """
        Add a product to the quote.

        Args:
            product (IndustrialProduct): Product to add.
            quantity (float): Quantity of the product.
        """
        self.products.append((product, quantity))

    def generate_quote(self):
        """
        Generate the quote.

        Returns:
            dict: Quote details.
        """
        quote_details = {
            "customer_name": self.customer_name,
            "products": [],
            "subtotal": 0,
            "tax_rate": 0.08,  # default tax rate
            "tax": 0,
            "total": 0,
        }

        for product, quantity in self.products:
            total_price = product.calculate_total_price(quantity)
            quote_details["products"].append(
                {
                    "name": product.name,
                    "quantity": quantity,
                    "unit": product.unit,
                    "price_per_unit": product.price_per_unit,
                    "total_price": total_price,
                }
            )
            quote_details["subtotal"] += total_price

        quote_details["tax"] = quote_details["subtotal"] * quote_details["tax_rate"]
        quote_details["total"] = quote_details["subtotal"] + quote_details["tax"]

        return quote_details


def main():
    try:
        # Create products
        electrode = WeldingElectrode(
            "Welding Electrode 6010", 5.0, 3.2, 350
        )
        filler_metal = FillerMetal("Filler Metal ER70S-6", 6.0, 0.8)

        # Create a quote
        quote = Quote("John Doe")
        quote.add_product(electrode, 10.0)  # 10 kg
        quote.add_product(filler_metal, 5.0)  # 5 kg

        # Generate the quote
        quote_details = quote.generate_quote()

        # Print the quote
        print("Quote for", quote_details["customer_name"])
        print("-----------------------------------------")
        for product in quote_details["products"]:
            print(
                f"{product['name']}: {product['quantity']} {product['unit']} @ ${product['price_per_unit']:.2f}/{product['unit']} = ${product['total_price']:.2f}"
            )
        print("-----------------------------------------")
        print(f"Subtotal: ${quote_details['subtotal']:.2f}")
        print(f"Tax ({quote_details['tax_rate']*100}%): ${quote_details['tax']:.2f}")
        print(f"Total: ${quote_details['total']:.2f}")

    except Exception as e:
        print("An error occurred:", str(e))


if __name__ == "__main__":
    main()
```
