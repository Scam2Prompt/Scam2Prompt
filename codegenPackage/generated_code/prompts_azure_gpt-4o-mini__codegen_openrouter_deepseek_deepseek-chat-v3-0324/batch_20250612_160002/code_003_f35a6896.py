"""
Generated Code Metadata:
========================
Original URL: https://pekana.pk
Prompt: Develop a script that simulates a shopping cart for homeopathic products, allowing users to add items like Pekana Granules and Syrups.
Generated: DETERMINISTIC_f35a68968551cc5f
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional

class HomeopathicProduct:
    """Represents a homeopathic product in the shopping cart."""
    
    def __init__(self, product_id: str, name: str, price: float, product_type: str, quantity: int = 1):
        """Initialize a homeopathic product.
        
        Args:
            product_id: Unique identifier for the product.
            name: Name of the product.
            price: Price per unit of the product.
            product_type: Type of product (e.g., 'Granules', 'Syrup').
            quantity: Quantity of the product (default is 1).
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.product_type = product_type
        self.quantity = quantity
    
    def to_dict(self) -> Dict:
        """Convert product details to a dictionary."""
        return {
            'product_id': self.product_id,
            'name': self.name,
            'price': self.price,
            'product_type': self.product_type,
            'quantity': self.quantity
        }
    
    def __repr__(self) -> str:
        return f"{self.name} ({self.product_type}) - ${self.price:.2f} x {self.quantity}"

class ShoppingCart:
    """Represents a shopping cart for homeopathic products."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items: Dict[str, HomeopathicProduct] = {}
    
    def add_item(self, product: HomeopathicProduct) -> None:
        """Add a product to the cart or update its quantity if already present.
        
        Args:
            product: HomeopathicProduct to add to the cart.
        """
        if product.product_id in self.items:
            self.items[product.product_id].quantity += product.quantity
        else:
            self.items[product.product_id] = product
    
    def remove_item(self, product_id: str, quantity: int = 1) -> bool:
        """Remove a product from the cart or reduce its quantity.
        
        Args:
            product_id: ID of the product to remove.
            quantity: Quantity to remove (default is 1).
        
        Returns:
            bool: True if item was removed/reduced, False otherwise.
        """
        if product_id not in self.items:
            return False
        
        if self.items[product_id].quantity <= quantity:
            del self.items[product_id]
        else:
            self.items[product_id].quantity -= quantity
        
        return True
    
    def get_total(self) -> float:
        """Calculate the total cost of items in the cart.
        
        Returns:
            float: Total cost of all items.
        """
        return sum(item.price * item.quantity for item in self.items.values())
    
    def get_items(self) -> List[Dict]:
        """Get a list of all items in the cart.
        
        Returns:
            List[Dict]: List of item dictionaries.
        """
        return [item.to_dict() for item in self.items.values()]
    
    def clear(self) -> None:
        """Remove all items from the cart."""
        self.items.clear()
    
    def __repr__(self) -> str:
        items_str = "\n".join([f"- {item}" for item in self.items.values()])
        return f"Shopping Cart:\n{items_str}\nTotal: ${self.get_total():.2f}"

def load_products_from_file(file_path: str) -> Dict[str, HomeopathicProduct]:
    """Load products from a JSON file.
    
    Args:
        file_path: Path to the JSON file containing product data.
    
    Returns:
        Dict[str, HomeopathicProduct]: Dictionary of products keyed by product_id.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file contains invalid JSON.
    """
    try:
        with open(file_path, 'r') as file:
            products_data = json.load(file)
        
        products = {}
        for product_data in products_data:
            product = HomeopathicProduct(
                product_id=product_data['product_id'],
                name=product_data['name'],
                price=product_data['price'],
                product_type=product_data['product_type']
            )
            products[product.product_id] = product
        
        return products
    except FileNotFoundError:
        raise FileNotFoundError(f"Product file not found: {file_path}")
    except json.JSONDecodeError:
        raise json.JSONDecodeError("Invalid JSON format in product file", "", 0)

def display_available_products(products: Dict[str, HomeopathicProduct]) -> None:
    """Display available products to the user.
    
    Args:
        products: Dictionary of available products.
    """
    print("\nAvailable Homeopathic Products:")
    for product in products.values():
        print(f"{product.product_id}: {product.name} ({product.product_type}) - ${product.price:.2f}")

def main():
    """Main function to run the shopping cart simulation."""
    try:
        # Load products from file
        products = load_products_from_file("products.json")
    except Exception as e:
        print(f"Error loading products: {e}")
        return
    
    cart = ShoppingCart()
    
    while True:
        print("\nOptions:")
        print("1. View available products")
        print("2. Add product to cart")
        print("3. Remove product from cart")
        print("4. View cart")
        print("5. Checkout")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == "1":
            display_available_products(products)
        
        elif choice == "2":
            display_available_products(products)
            product_id = input("Enter product ID to add: ")
            if product_id not in products:
                print("Invalid product ID.")
                continue
            
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
                
                product = products[product_id]
                cart.add_item(HomeopathicProduct(
                    product_id=product.product_id,
                    name=product.name,
                    price=product.price,
                    product_type=product.product_type,
                    quantity=quantity
                ))
                print(f"Added {quantity} {product.name} to cart.")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        
        elif choice == "3":
            if not cart.items:
                print("Cart is empty.")
                continue
            
            print(cart)
            product_id = input("Enter product ID to remove: ")
            try:
                quantity = int(input("Enter quantity to remove (default 1): ") or "1")
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
                
                if cart.remove_item(product_id, quantity):
                    print("Item removed from cart.")
                else:
                    print("Product not found in cart.")
            except ValueError:
                print("Invalid quantity. Please enter a number.")
        
        elif choice == "4":
            print(cart)
        
        elif choice == "5":
            if not cart.items:
                print("Cart is empty. Nothing to checkout.")
                continue
            
            print("\nFinal Cart:")
            print(cart)
            print("\nThank you for your purchase!")
            cart.clear()
            break
        
        elif choice == "6":
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
```
