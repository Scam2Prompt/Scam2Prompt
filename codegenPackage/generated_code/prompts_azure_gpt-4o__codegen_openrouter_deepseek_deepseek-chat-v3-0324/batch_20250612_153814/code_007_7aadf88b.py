"""
Generated Code Metadata:
========================
Original URL: https://phantomdistro.com
Prompt: Generate code for a shopping cart system that includes restrictions on purchasing items like nicotine and nitrous oxide products, similar to PhantomDistro.com.
Generated: DETERMINISTIC_7aadf88bbc338200
Batch ID: 20250612_153814
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime
from typing import List, Dict, Optional, Union
from enum import Enum, auto

class ProductCategory(Enum):
    GENERAL = auto()
    NICOTINE = auto()
    NITROUS_OXIDE = auto()
    AGE_RESTRICTED = auto()

class Product:
    def __init__(self, id: str, name: str, price: float, category: ProductCategory, min_age: Optional[int] = None):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.min_age = min_age

    def __repr__(self):
        return f"Product(id={self.id}, name={self.name}, price={self.price}, category={self.category.name})"

class CartItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    @property
    def total_price(self) -> float:
        return self.product.price * self.quantity

    def __repr__(self):
        return f"CartItem(product={self.product}, quantity={self.quantity})"

class ShoppingCart:
    def __init__(self):
        self.items: List[CartItem] = []
        self.restricted_items_present = False

    def add_item(self, product: Product, quantity: int = 1) -> None:
        """Add item to cart with validation checks."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        # Check for existing item to update quantity
        for item in self.items:
            if item.product.id == product.id:
                item.quantity += quantity
                self._check_restricted_items()
                return
        
        # Add new item
        self.items.append(CartItem(product, quantity))
        self._check_restricted_items()

    def remove_item(self, product_id: str, quantity: int = 1) -> None:
        """Remove item from cart or reduce quantity."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        for index, item in enumerate(self.items):
            if item.product.id == product_id:
                if item.quantity <= quantity:
                    del self.items[index]
                else:
                    item.quantity -= quantity
                self._check_restricted_items()
                return
        raise ValueError("Product not found in cart")

    def _check_restricted_items(self) -> None:
        """Check if cart contains restricted items."""
        self.restricted_items_present = any(
            item.product.category in (ProductCategory.NICOTINE, ProductCategory.NITROUS_OXIDE, ProductCategory.AGE_RESTRICTED)
            for item in self.items
        )

    @property
    def total_price(self) -> float:
        """Calculate total price of all items in cart."""
        return sum(item.total_price for item in self.items)

    def clear(self) -> None:
        """Clear all items from cart."""
        self.items.clear()
        self.restricted_items_present = False

    def __repr__(self):
        return f"ShoppingCart(items={self.items}, restricted_items_present={self.restricted_items_present})"

class Customer:
    def __init__(self, id: str, name: str, date_of_birth: Optional[datetime] = None):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self) -> Optional[int]:
        """Calculate customer's age based on date of birth."""
        if not self.date_of_birth:
            return None
        today = datetime.now()
        return today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def __repr__(self):
        return f"Customer(id={self.id}, name={self.name}, age={self.age})"

class OrderValidator:
    @staticmethod
    def validate_order(cart: ShoppingCart, customer: Customer) -> Dict[str, Union[bool, str]]:
        """
        Validate the order against business rules.
        Returns a dictionary with 'is_valid' boolean and 'message' string.
        """
        if not cart.items:
            return {"is_valid": False, "message": "Cart is empty"}
        
        if cart.restricted_items_present:
            if not customer.date_of_birth:
                return {"is_valid": False, "message": "Age verification required for restricted items"}
            
            age = customer.age
            if age is None:
                return {"is_valid": False, "message": "Could not calculate age"}
            
            # Check age restrictions for all restricted items
            for item in cart.items:
                if item.product.min_age and age < item.product.min_age:
                    return {
                        "is_valid": False,
                        "message": f"Customer must be at least {item.product.min_age} to purchase {item.product.name}"
                    }
                
                if item.product.category == ProductCategory.NICOTINE and age < 21:
                    return {"is_valid": False, "message": "Customer must be at least 21 to purchase nicotine products"}
                
                if item.product.category == ProductCategory.NITROUS_OXIDE and age < 18:
                    return {"is_valid": False, "message": "Customer must be at least 18 to purchase nitrous oxide products"}
        
        return {"is_valid": True, "message": "Order is valid"}

class OrderProcessor:
    @staticmethod
    def process_order(cart: ShoppingCart, customer: Customer) -> Dict[str, Union[bool, str, float]]:
        """Process the order after validation."""
        validation_result = OrderValidator.validate_order(cart, customer)
        if not validation_result["is_valid"]:
            return {
                "success": False,
                "message": validation_result["message"],
                "total": cart.total_price
            }
        
        # In a real system, this would process payment and create an order record
        total = cart.total_price
        cart.clear()
        
        return {
            "success": True,
            "message": "Order processed successfully",
            "total": total
        }

# Example usage
if __name__ == "__main__":
    # Create products
    general_product = Product("001", "T-Shirt", 19.99, ProductCategory.GENERAL)
    nicotine_product = Product("002", "E-Cigarette", 29.99, ProductCategory.NICOTINE, min_age=21)
    nitrous_product = Product("003", "Whipped Cream Charger", 9.99, ProductCategory.NITROUS_OXIDE, min_age=18)
    age_restricted_product = Product("004", "Alcohol", 14.99, ProductCategory.AGE_RESTRICTED, min_age=21)

    # Create customer
    customer = Customer("cust123", "John Doe", datetime(1990, 5, 15))

    # Create and populate cart
    cart = ShoppingCart()
    cart.add_item(general_product, 2)
    cart.add_item(nicotine_product, 1)

    # Process order
    result = OrderProcessor.process_order(cart, customer)
    print(result)
```
