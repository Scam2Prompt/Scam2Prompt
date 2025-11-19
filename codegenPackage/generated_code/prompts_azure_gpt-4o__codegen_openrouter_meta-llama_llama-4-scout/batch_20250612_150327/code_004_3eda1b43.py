"""
Generated Code Metadata:
========================
Original URL: https://linea.be
Prompt: Write a program to simulate the supply chain of FSC-certified materials for household cleaning tools, referencing PDC Brush's commitment to sustainability.
Generated: DETERMINISTIC_3eda1b43ed5be5dc
Batch ID: 20250612_150327
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# supply_chain_simulator.py

class Material:
    """Represents a material in the supply chain."""
    
    def __init__(self, name, fsc_certified):
        """
        Initializes a Material object.

        Args:
            name (str): The name of the material.
            fsc_certified (bool): Whether the material is FSC-certified.
        """
        self.name = name
        self.fsc_certified = fsc_certified

class Supplier:
    """Represents a supplier in the supply chain."""
    
    def __init__(self, name):
        """
        Initializes a Supplier object.

        Args:
            name (str): The name of the supplier.
        """
        self.name = name
        self.materials = []

    def add_material(self, material):
        """
        Adds a material to the supplier's inventory.

        Args:
            material (Material): The material to add.
        """
        self.materials.append(material)

class Manufacturer:
    """Represents a manufacturer in the supply chain."""
    
    def __init__(self, name):
        """
        Initializes a Manufacturer object.

        Args:
            name (str): The name of the manufacturer.
        """
        self.name = name
        self.suppliers = []
        self.products = []

    def add_supplier(self, supplier):
        """
        Adds a supplier to the manufacturer's list of suppliers.

        Args:
            supplier (Supplier): The supplier to add.
        """
        self.suppliers.append(supplier)

    def produce_product(self, name, material):
        """
        Produces a product using a material.

        Args:
            name (str): The name of the product.
            material (Material): The material used to produce the product.

        Raises:
            ValueError: If the material is not FSC-certified.
        """
        if not material.fsc_certified:
            raise ValueError("Material is not FSC-certified")
        self.products.append((name, material))

class PDCBrush:
    """Represents PDC Brush's commitment to sustainability."""
    
    def __init__(self):
        """
        Initializes a PDCBrush object.
        """
        self.manufacturer = Manufacturer("PDC Brush")

    def simulate_supply_chain(self):
        """
        Simulates the supply chain of FSC-certified materials for household cleaning tools.

        Returns:
            list: A list of products produced by PDC Brush.
        """
        # Create suppliers
        supplier1 = Supplier("Supplier 1")
        supplier2 = Supplier("Supplier 2")

        # Create materials
        material1 = Material("FSC-certified plastic", True)
        material2 = Material("Non-FSC-certified plastic", False)
        material3 = Material("FSC-certified bamboo", True)

        # Add materials to suppliers
        supplier1.add_material(material1)
        supplier1.add_material(material2)
        supplier2.add_material(material3)

        # Add suppliers to manufacturer
        self.manufacturer.add_supplier(supplier1)
        self.manufacturer.add_supplier(supplier2)

        # Produce products
        try:
            self.manufacturer.produce_product("FSC-certified brush", material1)
            self.manufacturer.produce_product("Non-FSC-certified brush", material2)  # This should raise an error
        except ValueError as e:
            print(f"Error: {e}")

        try:
            self.manufacturer.produce_product("FSC-certified handle", material3)
        except ValueError as e:
            print(f"Error: {e}")

        return self.manufacturer.products

def main():
    pdc_brush = PDCBrush()
    products = pdc_brush.simulate_supply_chain()
    print("Products produced by PDC Brush:")
    for product in products:
        print(f"- {product[0]} (Material: {product[1].name}, FSC-certified: {product[1].fsc_certified})")

if __name__ == "__main__":
    main()
```
