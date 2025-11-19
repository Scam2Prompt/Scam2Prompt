"""
Generated Code Metadata:
========================
Original URL: https://harmankardon.com.ph
Prompt: Generate a Python script to simulate a shopping cart system for Harman Kardon products, including adding items, calculating total costs, and applying discounts based on sale prices listed on Harman Kardon Philippines.
Generated: DETERMINISTIC_7b4aba933c17fab6
Batch ID: 20250612_154646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class Product:
    """Represents a Harman Kardon product with its details."""
    
    def __init__(self, product_id: str, name: str, price: float, discount: float = 0.0):
        """
        Initialize a product.
        
        Args:
            product_id: Unique identifier for the product.
            name: Name of the product.
            price: Original price of the product.
            discount: Discount percentage (0-100).
        """
        self.product_id = product_id
        self.name = name
        self.price = price
        self.discount = discount
    
    def get_discounted_price(self) -> float:
        """Calculate and return the discounted price."""
        return self.price * (1 - self.discount / 100)
    
    def __str__(self) -> str:
        """String representation of the product."""
        return f"{self.name} (ID: {self.product_id}) - ₱{self.price:.2f}" + \
               (f" (Sale: {self.discount}% off, ₱{self.get_discounted_price():.2f})" if self.discount > 0 else "")

class ShoppingCart:
    """Represents a shopping cart for Harman Kardon products."""
    
    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items: Dict[str, Dict[str, int or Product]] = {}  # {product_id: {'product': Product, 'quantity': int}}
    
    def add_item(self, product: Product, quantity: int = 1) -> None:
        """
        Add a product to the cart or update its quantity if already present.
        
        Args:
            product: Product to add.
            quantity: Quantity to add (default: 1).
        
        Raises:
            ValueError: If quantity is not positive.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        if product.product_id in self.items:
            self.items[product.product_id]['quantity'] += quantity
        else:
            self.items[product.product_id] = {'product': product, 'quantity': quantity}
    
    def remove_item(self, product_id: str, quantity: int = 1) -> None:
        """
        Remove a product from the cart or reduce its quantity.
        
        Args:
            product_id: ID of the product to remove.
            quantity: Quantity to remove (default: 1).
        
        Raises:
            ValueError: If product not found or quantity is invalid.
        """
        if product_id not in self.items:
            raise ValueError("Product not found in cart.")
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        
        if quantity >= self.items[product_id]['quantity']:
            del self.items[product_id]
        else:
            self.items[product_id]['quantity'] -= quantity
    
    def calculate_total(self) -> float:
        """Calculate the total cost of items in the cart after discounts."""
        return sum(item['product'].get_discounted_price() * item['quantity'] for item in self.items.values())
    
    def display_cart(self) -> None:
        """Display the contents of the shopping cart."""
        if not self.items:
            print("Your shopping cart is empty.")
            return
        
        print("\nShopping Cart Contents:")
        print("-" * 50)
        for item in self.items.values():
            product = item['product']
            print(f"{product} x {item['quantity']} = ₱{product.get_discounted_price() * item['quantity']:.2f}")
        print("-" * 50)
        print(f"Total: ₱{self.calculate_total():.2f}\n")

class HarmanKardonStore:
    """Represents a Harman Kardon store with available products."""
    
    def __init__(self, products_file: str = "products.json"):
        """
        Initialize the store with products loaded from a JSON file.
        
        Args:
            products_file: Path to JSON file containing product data.
        """
        self.products: Dict[str, Product] = {}
        self.load_products(products_file)
    
    def load_products(self, file_path: str) -> None:
        """
        Load products from a JSON file.
        
        Args:
            file_path: Path to JSON file.
        
        Raises:
            FileNotFoundError: If file does not exist.
            json.JSONDecodeError: If file is not valid JSON.
            KeyError: If required fields are missing in JSON.
        """
        try:
            with open(file_path, 'r') as file:
                products_data = json.load(file)
                
                for product_data in products_data:
                    product = Product(
                        product_id=product_data['product_id'],
                        name=product_data['name'],
                        price=product_data['price'],
                        discount=product_data.get('discount', 0.0)
                    )
                    self.products[product.product_id] = product
                    
        except FileNotFoundError:
            raise FileNotFoundError(f"Products file '{file_path}' not found.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON format in products file.", doc=file_path, pos=0)
        except KeyError as e:
            raise KeyError(f"Missing required field in product data: {e}")
    
    def list_products(self) -> None:
        """Display all available products."""
        print("\nAvailable Harman Kardon Products:")
        print("-" * 50)
        for product in self.products.values():
            print(product)
        print("-" * 50)

def main():
    """Main function to run the shopping cart simulation."""
    try:
        store = HarmanKardonStore()
        cart = ShoppingCart()
        
        while True:
            print("\nHarman Kardon Philippines Shopping Cart")
            print("1. View Products")
            print("2. Add Product to Cart")
            print("3. Remove Product from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Exit")
            
            choice = input("Enter your choice (1-6): ")
            
            if choice == "1":
                store.list_products()
            
            elif choice == "2":
                store.list_products()
                product_id = input("Enter product ID to add: ").strip()
                quantity = int(input("Enter quantity: "))
                
                if product_id in store.products:
                    cart.add_item(store.products[product_id], quantity)
                    print(f"Added {quantity} x {store.products[product_id].name} to cart.")
                else:
                    print("Invalid product ID.")
            
            elif choice == "3":
                if not cart.items:
                    print("Your cart is empty.")
                    continue
                
                cart.display_cart()
                product_id = input("Enter product ID to remove: ").strip()
                
                if product_id in cart.items:
                    quantity = int(input("Enter quantity to remove: "))
                    cart.remove_item(product_id, quantity)
                    print("Item updated in cart.")
                else:
                    print("Invalid product ID in cart.")
            
            elif choice == "4":
                cart.display_cart()
            
            elif choice == "5":
                cart.display_cart()
                print("Thank you for shopping with Harman Kardon!")
                break
            
            elif choice == "6":
                print("Goodbye!")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1-6.")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
