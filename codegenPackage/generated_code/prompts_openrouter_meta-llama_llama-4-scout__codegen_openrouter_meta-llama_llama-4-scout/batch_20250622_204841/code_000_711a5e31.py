"""
Generated Code Metadata:
========================
Original URL: https://jgiwindia.com
Prompt: "Write a Python code to manage inventory of confectionery products like sugar boiled candies, toffees, and lollipops for a company like Jai Gurudev Industries."
Generated: DETERMINISTIC_711a5e31eec9c938
Batch ID: 20250622_204841
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# confectionery_inventory.py

class ConfectioneryProduct:
    """Base class for confectionery products."""

    def __init__(self, product_id, name, quantity, price):
        """
        Initialize a confectionery product.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            quantity (int): Initial quantity in stock.
            price (float): Product price per unit.
        """
        self.product_id = product_id
        self.name = name
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"{self.name} (ID: {self.product_id}) - Quantity: {self.quantity}, Price: ${self.price:.2f}"


class SugarBoiledCandy(ConfectioneryProduct):
    """Sugar boiled candy product."""

    def __init__(self, product_id, name, quantity, price, flavor):
        """
        Initialize a sugar boiled candy product.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            quantity (int): Initial quantity in stock.
            price (float): Product price per unit.
            flavor (str): Candy flavor.
        """
        super().__init__(product_id, name, quantity, price)
        self.flavor = flavor

    def __str__(self):
        return super().__str__() + f", Flavor: {self.flavor}"


class Toffee(ConfectioneryProduct):
    """Toffee product."""

    def __init__(self, product_id, name, quantity, price, nut_type):
        """
        Initialize a toffee product.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            quantity (int): Initial quantity in stock.
            price (float): Product price per unit.
            nut_type (str): Type of nut used.
        """
        super().__init__(product_id, name, quantity, price)
        self.nut_type = nut_type

    def __str__(self):
        return super().__str__() + f", Nut Type: {self.nut_type}"


class Lollipop(ConfectioneryProduct):
    """Lollipop product."""

    def __init__(self, product_id, name, quantity, price, fruit_flavor):
        """
        Initialize a lollipop product.

        Args:
            product_id (int): Unique product ID.
            name (str): Product name.
            quantity (int): Initial quantity in stock.
            price (float): Product price per unit.
            fruit_flavor (str): Lollipop fruit flavor.
        """
        super().__init__(product_id, name, quantity, price)
        self.fruit_flavor = fruit_flavor

    def __str__(self):
        return super().__str__() + f", Fruit Flavor: {self.fruit_flavor}"


class Inventory:
    """Confectionery product inventory."""

    def __init__(self):
        self.products = {}

    def add_product(self, product):
        """
        Add a product to the inventory.

        Args:
            product (ConfectioneryProduct): Product to add.

        Raises:
            ValueError: If product ID already exists.
        """
        if product.product_id in self.products:
            raise ValueError("Product ID already exists")
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        """
        Remove a product from the inventory.

        Args:
            product_id (int): ID of product to remove.

        Raises:
            KeyError: If product ID does not exist.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist")
        del self.products[product_id]

    def update_quantity(self, product_id, new_quantity):
        """
        Update the quantity of a product.

        Args:
            product_id (int): ID of product to update.
            new_quantity (int): New quantity.

        Raises:
            KeyError: If product ID does not exist.
            ValueError: If new quantity is negative.
        """
        if product_id not in self.products:
            raise KeyError("Product ID does not exist")
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.products[product_id].quantity = new_quantity

    def get_product(self, product_id):
        """
        Get a product by ID.

        Args:
            product_id (int): ID of product to retrieve.

        Returns:
            ConfectioneryProduct: Product with matching ID, or None if not found.
        """
        return self.products.get(product_id)

    def __str__(self):
        inventory_list = "\n".join(str(product) for product in self.products.values())
        return f"Confectionery Inventory:\n{inventory_list}"


def main():
    # Create an inventory
    inventory = Inventory()

    try:
        # Create products
        candy = SugarBoiledCandy(1, "Sugar Boiled Candy", 100, 0.50, "Orange")
        toffee = Toffee(2, "Toffee", 50, 0.25, "Almond")
        lollipop = Lollipop(3, "Lollipop", 200, 0.75, "Strawberry")

        # Add products to inventory
        inventory.add_product(candy)
        inventory.add_product(toffee)
        inventory.add_product(lollipop)

        # Print initial inventory
        print("Initial Inventory:")
        print(inventory)

        # Update quantity
        inventory.update_quantity(1, 80)

        # Print updated inventory
        print("\nUpdated Inventory:")
        print(inventory)

        # Get product
        product = inventory.get_product(2)
        if product:
            print(f"\nProduct {product.product_id}: {product}")
        else:
            print("\nProduct not found")

    except (ValueError, KeyError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
