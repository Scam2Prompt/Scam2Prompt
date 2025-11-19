"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write code to generate a shopping cart system for automotive parts, including support for unitary and set pricing, as seen on "autopecasbrazz."
Generated: DETERMINISTIC_fba0ca3ef55f8b39
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# shopping_cart.py

class Part:
    """
    Represents an automotive part with its details and pricing.
    """
    def __init__(self, part_id, name, description, price, is_set=False, set_quantity=1):
        """
        Initialize a Part instance.
        
        Args:
            part_id (str): Unique identifier for the part
            name (str): Name of the part
            description (str): Description of the part
            price (float): Price of the part (per unit or per set)
            is_set (bool): Whether the part is sold as a set
            set_quantity (int): Number of items in the set (if is_set is True)
        """
        self.part_id = part_id
        self.name = name
        self.description = description
        self.price = price
        self.is_set = is_set
        self.set_quantity = set_quantity if is_set else 1

    def get_unit_price(self):
        """
        Returns the price per single unit.
        
        Returns:
            float: Price per unit
        """
        return self.price / self.set_quantity if self.is_set else self.price

    def __str__(self):
        return f"{self.name} ({self.part_id}) - ${self.price:.2f}" + \
               (f" (Set of {self.set_quantity})" if self.is_set else "")


class CartItem:
    """
    Represents an item in the shopping cart with quantity.
    """
    def __init__(self, part, quantity=1):
        """
        Initialize a CartItem instance.
        
        Args:
            part (Part): The part being added to cart
            quantity (int): Quantity of parts/sets
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        self.part = part
        self.quantity = quantity

    def get_total_price(self):
        """
        Calculate total price for this cart item.
        
        Returns:
            float: Total price for the quantity of this item
        """
        return self.part.price * self.quantity

    def get_total_units(self):
        """
        Calculate total number of units (considering sets).
        
        Returns:
            int: Total number of individual units
        """
        return self.quantity * (self.part.set_quantity if self.part.is_set else 1)

    def __str__(self):
        return f"{self.quantity} x {self.part} = ${self.get_total_price():.2f}"


class ShoppingCart:
    """
    Represents a shopping cart that holds automotive parts.
    """
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}

    def add_item(self, part, quantity=1):
        """
        Add an item to the cart or update quantity if already present.
        
        Args:
            part (Part): The part to add
            quantity (int): Quantity to add
            
        Returns:
            bool: True if item was added/updated, False otherwise
        """
        if not isinstance(part, Part):
            raise TypeError("Only Part objects can be added to cart")
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        if part.part_id in self.items:
            self.items[part.part_id].quantity += quantity
        else:
            self.items[part.part_id] = CartItem(part, quantity)
        return True

    def remove_item(self, part_id, quantity=None):
        """
        Remove an item from the cart or reduce its quantity.
        
        Args:
            part_id (str): ID of the part to remove
            quantity (int, optional): Quantity to remove. If None, removes all.
            
        Returns:
            bool: True if item was removed/updated, False if not found
        """
        if part_id not in self.items:
            return False
            
        if quantity is None:
            del self.items[part_id]
            return True
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        if quantity >= self.items[part_id].quantity:
            del self.items[part_id]
        else:
            self.items[part_id].quantity -= quantity
        return True

    def get_total_price(self):
        """
        Calculate the total price of all items in the cart.
        
        Returns:
            float: Total cart value
        """
        return sum(item.get_total_price() for item in self.items.values())

    def get_total_items(self):
        """
        Get the total count of items in the cart (counting sets as single items).
        
        Returns:
            int: Total number of items in cart
        """
        return sum(item.quantity for item in self.items.values())

    def get_total_units(self):
        """
        Get the total count of individual units in the cart.
        
        Returns:
            int: Total number of individual units
        """
        return sum(item.get_total_units() for item in self.items.values())

    def clear(self):
        """Remove all items from the cart."""
        self.items.clear()

    def __str__(self):
        if not self.items:
            return "Shopping cart is empty"
        
        items_str = "\n".join(str(item) for item in self.items.values())
        return f"Shopping Cart ({self.get_total_items()} items, {self.get_total_units()} units):\n" + \
               f"{items_str}\nTotal: ${self.get_total_price():.2f}"


# Example usage
if __name__ == "__main__":
    # Create some parts
    spark_plug = Part("SP-101", "Spark Plug", "Iridium spark plug", 12.99)
    oil_filter = Part("OF-202", "Oil Filter", "Premium oil filter", 15.50)
    brake_pad_set = Part("BP-303", "Brake Pads", "Ceramic brake pads", 89.99, is_set=True, set_quantity=4)
    tire_set = Part("T-404", "Tires", "All-season tires", 499.99, is_set=True, set_quantity=4)

    # Create a shopping cart
    cart = ShoppingCart()

    # Add items to cart
    cart.add_item(spark_plug, 4)
    cart.add_item(oil_filter, 2)
    cart.add_item(brake_pad_set, 1)
    cart.add_item(tire_set, 2)

    # Print cart contents
    print(cart)

    # Remove some items
    cart.remove_item("SP-101", 2)
    cart.remove_item("OF-202")

    # Print updated cart
    print("\nAfter removing some items:")
    print(cart)
```
