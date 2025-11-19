"""
Generated Code Metadata:
========================
Original URL: https://acula.com.ua
Prompt: Write Python code to create a shopping cart system for an online store specializing in diving and fishing gear, referencing categories like "гидрокостюмы," "пневматические ружья," and "туристические палатки" from the catalog structure on acula.com.ua.
Generated: DETERMINISTIC_19582d5a14fc1234
Batch ID: 20250612_150927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from dataclasses import dataclass
import json

@dataclass
class Product:
    id: str
    name: str
    price: float
    category: str  # e.g. "гидрокостюмы", "пневматические ружья", "туристические палатки"
    stock: int

@dataclass
class CartItem:
    product: Product
    quantity: int

class ShoppingCart:
    def __init__(self):
        self.items: Dict[str, CartItem] = {}  # key: product_id, value: CartItem
    
    def add_item(self, product: Product, quantity: int = 1) -> None:
        if product.stock <= 0:
            raise ValueError(f"Product {product.name} is out of stock")
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        if quantity > product.stock:
            raise ValueError(f"Not enough stock for {product.name}. Available: {product.stock}")
        
        if product.id in self.items:
            self.items[product.id].quantity += quantity
        else:
            self.items[product.id] = CartItem(product=product, quantity=quantity)
    
    def remove_item(self, product_id: str, quantity: int = 1) -> None:
        if product_id not in self.items:
            raise ValueError("Product not in cart")
        
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        if quantity >= self.items[product_id].quantity:
            del self.items[product_id]
        else:
            self.items[product_id].quantity -= quantity
    
    def update_item_quantity(self, product_id: str, new_quantity: int) -> None:
        if product_id not in self.items:
            raise ValueError("Product not in cart")
        
        if new_quantity <= 0:
            self.remove_item(product_id)
            return
        
        product = self.items[product_id].product
        if new_quantity > product.stock:
            raise ValueError(f"Not enough stock for {product.name}. Available: {product.stock}")
        
        self.items[product_id].quantity = new_quantity
    
    def clear_cart(self) -> None:
        self.items.clear()
    
    def get_total_price(self) -> float:
        return sum(item.product.price * item.quantity for item in self.items.values())
    
    def get_items(self) -> List[CartItem]:
        return list(self.items.values())
    
    def to_json(self) -> str:
        cart_data = {
            "items": [
                {
                    "product_id": item.product.id,
                    "name": item.product.name,
                    "price": item.product.price,
                    "category": item.product.category,
                    "quantity": item.quantity
                }
                for item in self.items.values()
            ],
            "total_price": self.get_total_price()
        }
        return json.dumps(cart_data, ensure_ascii=False, indent=2)

class ProductCatalog:
    def __init__(self):
        self.products: Dict[str, Product] = {}
    
    def add_product(self, product: Product) -> None:
        if product.id in self.products:
            raise ValueError(f"Product with ID {product.id} already exists")
        self.products[product.id] = product
    
    def get_product(self, product_id: str) -> Optional[Product]:
        return self.products.get(product_id)
    
    def get_products_by_category(self, category: str) -> List[Product]:
        return [p for p in self.products.values() if p.category == category]

# Example usage
if __name__ == "__main__":
    # Initialize catalog with sample products
    catalog = ProductCatalog()
    catalog.add_product(Product(id="wetsuit1", name="Гидрокостюм Neosport", price=2500.00, category="гидрокостюмы", stock=10))
    catalog.add_product(Product(id="speargun1", name="Пневматическое ружье Cressi", price=4500.00, category="пневматические ружья", stock=5))
    catalog.add_product(Product(id="tent1", name="Палатка Tramp", price=1800.00, category="туристические палатки", stock=8))
    
    # Create and use shopping cart
    cart = ShoppingCart()
    cart.add_item(catalog.get_product("wetsuit1"), 2)
    cart.add_item(catalog.get_product("speargun1"), 1)
    
    print("Cart contents:")
    for item in cart.get_items():
        print(f"{item.product.name} - {item.quantity} x {item.product.price} = {item.quantity * item.product.price}")
    
    print(f"Total: {cart.get_total_price()}")
    print("\nCart JSON:")
    print(cart.to_json())
```
