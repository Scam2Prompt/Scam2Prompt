"""
Generated Code Metadata:
========================
Original URL: https://maderaselaboradas.com.ar
Prompt: Write a Python code snippet to manage inventory for a wood products company like Maderas Elaboradas, including classes for different types of products (e.g., Maderas Aserradas, Cabos, Muebles).
Generated: DETERMINISTIC_dc13454c73126e80
Batch ID: 20250622_212822
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """Base class for all products in the inventory."""
    
    def __init__(self, name, quantity, price_per_unit):
        """
        Initialize a new product.

        :param name: Name of the product
        :param quantity: Quantity of the product in stock
        :param price_per_unit: Price per unit of the product
        """
        self.name = name
        self.quantity = quantity
        self.price_per_unit = price_per_unit

    def update_quantity(self, amount):
        """
        Update the quantity of the product.

        :param amount: Amount to add (positive) or remove (negative)
        :raises ValueError: If the resulting quantity is negative
        """
        if self.quantity + amount < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity += amount

    def get_total_value(self):
        """
        Calculate the total value of the product in stock.

        :return: Total value of the product
        """
        return self.quantity * self.price_per_unit

    def __str__(self):
        """Return a string representation of the product."""
        return f"{self.name}: {self.quantity} units at ${self.price_per_unit:.2f} each"


class MaderaAserrada(Product):
    """Class representing sawn wood products."""
    
    def __init__(self, name, quantity, price_per_unit, wood_type):
        """
        Initialize a new sawn wood product.

        :param name: Name of the product
        :param quantity: Quantity of the product in stock
        :param price_per_unit: Price per unit of the product
        :param wood_type: Type of wood (e.g., Oak, Pine)
        """
        super().__init__(name, quantity, price_per_unit)
        self.wood_type = wood_type

    def __str__(self):
        """Return a string representation of the sawn wood product."""
        return f"{super().__str__()} (Wood Type: {self.wood_type})"


class Cabo(Product):
    """Class representing wood cables."""
    
    def __init__(self, name, quantity, price_per_unit, length):
        """
        Initialize a new cable product.

        :param name: Name of the product
        :param quantity: Quantity of the product in stock
        :param price_per_unit: Price per unit of the product
        :param length: Length of the cable in meters
        """
        super().__init__(name, quantity, price_per_unit)
        self.length = length

    def __str__(self):
        """Return a string representation of the cable product."""
        return f"{super().__str__()} (Length: {self.length}m)"


class Mueble(Product):
    """Class representing furniture products."""
    
    def __init__(self, name, quantity, price_per_unit, material):
        """
        Initialize a new furniture product.

        :param name: Name of the product
        :param quantity: Quantity of the product in stock
        :param price_per_unit: Price per unit of the product
        :param material: Material of the furniture (e.g., Wood, Metal)
        """
        super().__init__(name, quantity, price_per_unit)
        self.material = material

    def __str__(self):
        """Return a string representation of the furniture product."""
        return f"{super().__str__()} (Material: {self.material})"


class Inventory:
    """Class to manage the inventory of products."""
    
    def __init__(self):
        """Initialize an empty inventory."""
        self.products = {}

    def add_product(self, product):
        """
        Add a product to the inventory.

        :param product: Product object to add
        """
        if product.name in self.products:
            raise ValueError("Product already exists in inventory.")
        self.products[product.name] = product

    def update_product_quantity(self, product_name, amount):
        """
        Update the quantity of a specific product.

        :param product_name: Name of the product to update
        :param amount: Amount to add (positive) or remove (negative)
        :raises KeyError: If the product does not exist
        """
        if product_name not in self.products:
            raise KeyError("Product not found in inventory.")
        self.products[product_name].update_quantity(amount)

    def get_inventory_value(self):
        """
        Calculate the total value of the inventory.

        :return: Total value of all products in inventory
        """
        return sum(product.get_total_value() for product in self.products.values())

    def __str__(self):
        """Return a string representation of the inventory."""
        return "\n".join(str(product) for product in self.products.values())


# Example usage
if __name__ == "__main__":
    inventory = Inventory()
    
    # Adding products to the inventory
    try:
        inventory.add_product(MaderaAserrada("Oak Plank", 50, 2.5, "Oak"))
        inventory.add_product(Cabo("Wood Cable", 100, 1.5, 10))
        inventory.add_product(Mueble("Wooden Chair", 20, 45.0, "Wood"))
        
        # Updating product quantities
        inventory.update_product_quantity("Oak Plank", -10)
        inventory.update_product_quantity("Wooden Chair", 5)
        
        # Displaying inventory
        print("Current Inventory:")
        print(inventory)
        
        # Displaying total inventory value
        print(f"Total Inventory Value: ${inventory.get_inventory_value():.2f}")
        
    except (ValueError, KeyError) as e:
        print(f"Error: {e}")
```
