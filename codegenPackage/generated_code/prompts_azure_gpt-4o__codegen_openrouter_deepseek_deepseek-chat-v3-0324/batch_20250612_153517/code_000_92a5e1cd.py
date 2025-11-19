"""
Generated Code Metadata:
========================
Original URL: https://msagroup.ro
Prompt: Write Python code to simulate a shopping cart system for an online store that sells gardening tools, irrigation accessories, and household items, referencing categories like "Motocoasa," "Pompa Apa," and "Drujbe."
Generated: DETERMINISTIC_92a5e1cd12fdc0b5
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Product:
    """
    Represents a product in the online store.
    """
    def __init__(self, product_id: str, name: str, category: str, price: float, stock: int):
        """
        Initialize a product with given attributes.
        
        Args:
            product_id (str): Unique identifier for the product
            name (str): Name of the product
            category (str): Category of the product (e.g., "Motocoasa", "Pompa Apa", "Drujbe")
            price (float): Price of the product
            stock (int): Available quantity in stock
        """
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock = stock

    def update_stock(self, quantity: int) -> bool:
        """
        Update the product's stock quantity.
        
        Args:
            quantity (int): Quantity to add (positive) or remove (negative)
            
        Returns:
            bool: True if stock was updated successfully, False otherwise
        """
        if self.stock + quantity >= 0:
            self.stock += quantity
            return True
        return False


class ShoppingCart:
    """
    Represents a shopping cart for an online store.
    """
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items = {}  # {product_id: (product, quantity)}

    def add_item(self, product: Product, quantity: int = 1) -> bool:
        """
        Add a product to the shopping cart.
        
        Args:
            product (Product): Product to add
            quantity (int): Quantity to add
            
        Returns:
            bool: True if item was added successfully, False otherwise
        """
        if quantity <= 0:
            return False
            
        if product.product_id in self.items:
            existing_product, existing_quantity = self.items[product.product_id]
            if existing_product.update_stock(-quantity):
                self.items[product.product_id] = (existing_product, existing_quantity + quantity)
                return True
        else:
            if product.update_stock(-quantity):
                self.items[product.product_id] = (product, quantity)
                return True
        return False

    def remove_item(self, product_id: str, quantity: int = None) -> bool:
        """
        Remove a product from the shopping cart.
        
        Args:
            product_id (str): ID of the product to remove
            quantity (int, optional): Quantity to remove. If None, removes all.
            
        Returns:
            bool: True if item was removed successfully, False otherwise
        """
        if product_id not in self.items:
            return False
            
        product, existing_quantity = self.items[product_id]
        
        if quantity is None or quantity >= existing_quantity:
            if product.update_stock(existing_quantity):
                del self.items[product_id]
                return True
        else:
            if quantity > 0 and product.update_stock(quantity):
                self.items[product_id] = (product, existing_quantity - quantity)
                return True
        return False

    def get_total(self) -> float:
        """
        Calculate the total cost of items in the cart.
        
        Returns:
            float: Total cost
        """
        return sum(product.price * quantity for product, quantity in self.items.values())

    def clear(self) -> None:
        """Clear all items from the shopping cart."""
        for product_id, (product, quantity) in self.items.items():
            product.update_stock(quantity)
        self.items.clear()

    def __str__(self) -> str:
        """String representation of the shopping cart."""
        if not self.items:
            return "Shopping cart is empty."
            
        cart_str = "Shopping Cart:\n"
        cart_str += "-" * 30 + "\n"
        for product, quantity in self.items.values():
            cart_str += f"{product.name} ({product.category}) x{quantity}: ${product.price * quantity:.2f}\n"
        cart_str += "-" * 30 + "\n"
        cart_str += f"Total: ${self.get_total():.2f}"
        return cart_str


class OnlineStore:
    """
    Represents an online store with inventory management.
    """
    def __init__(self):
        """Initialize the store with sample inventory."""
        self.inventory = {
            "MT001": Product("MT001", "Motocoasa benzina", "Motocoasa", 299.99, 10),
            "MT002": Product("MT002", "Motocoasa electrica", "Motocoasa", 199.99, 15),
            "PA001": Product("PA001", "Pompa apa submersibila", "Pompa Apa", 149.99, 8),
            "PA002": Product("PA002", "Pompa apa de suprafata", "Pompa Apa", 129.99, 12),
            "DR001": Product("DR001", "Drujba electrica", "Drujbe", 399.99, 5),
            "DR002": Product("DR002", "Drujba benzina", "Drujbe", 499.99, 7),
            "HH001": Product("HH001", "Set unelte gradina", "Household", 49.99, 20),
            "HH002": Product("HH002", "Furtun irigatii", "Household", 29.99, 30)
        }

    def get_product(self, product_id: str) -> Product:
        """
        Get a product from inventory by ID.
        
        Args:
            product_id (str): Product ID to look up
            
        Returns:
            Product: The product if found, None otherwise
        """
        return self.inventory.get(product_id)

    def display_inventory(self, category: str = None) -> None:
        """
        Display the store's inventory, optionally filtered by category.
        
        Args:
            category (str, optional): Category to filter by
        """
        print("\nStore Inventory:")
        print("-" * 60)
        print(f"{'ID':<6} {'Name':<25} {'Category':<15} {'Price':<10} {'Stock'}")
        print("-" * 60)
        
        for product in self.inventory.values():
            if category is None or product.category == category:
                print(f"{product.product_id:<6} {product.name:<25} {product.category:<15} ${product.price:<9.2f} {product.stock}")
        print("-" * 60)


def main():
    """Main function to simulate the online store."""
    store = OnlineStore()
    cart = ShoppingCart()
    
    print("Welcome to the Gardening Tools Online Store!")
    
    while True:
        print("\nMenu:")
        print("1. Browse inventory")
        print("2. View cart")
        print("3. Add item to cart")
        print("4. Remove item from cart")
        print("5. Checkout")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            print("\nCategories:")
            print("1. All items")
            print("2. Motocoasa")
            print("3. Pompa Apa")
            print("4. Drujbe")
            print("5. Household")
            
            cat_choice = input("Choose category (1-5): ")
            
            if cat_choice == "1":
                store.display_inventory()
            elif cat_choice == "2":
                store.display_inventory("Motocoasa")
            elif cat_choice == "3":
                store.display_inventory("Pompa Apa")
            elif cat_choice == "4":
                store.display_inventory("Drujbe")
            elif cat_choice == "5":
                store.display_inventory("Household")
            else:
                print("Invalid category choice.")
                
        elif choice == "2":
            print(cart)
            
        elif choice == "3":
            product_id = input("Enter product ID to add: ").strip().upper()
            product = store.get_product(product_id)
            
            if product:
                try:
                    quantity = int(input(f"Enter quantity (available: {product.stock}): "))
                    if quantity > 0:
                        if cart.add_item(product, quantity):
                            print(f"Added {quantity} x {product.name} to cart.")
                        else:
                            print("Failed to add item. Not enough stock.")
                    else:
                        print("Quantity must be positive.")
                except ValueError:
                    print("Invalid quantity. Please enter a number.")
            else:
                print("Product not found.")
                
        elif choice == "4":
            product_id = input("Enter product ID to remove: ").strip().upper()
            
            if product_id in cart.items:
                product, current_quantity = cart.items[product_id]
                try:
                    quantity = input(f"Enter quantity to remove (current: {current_quantity}) or leave blank to remove all: ")
                    if quantity.strip() == "":
                        if cart.remove_item(product_id):
                            print(f"Removed all {product.name} from cart.")
                        else:
                            print("Failed to remove item.")
                    else:
                        quantity = int(quantity)
                        if
