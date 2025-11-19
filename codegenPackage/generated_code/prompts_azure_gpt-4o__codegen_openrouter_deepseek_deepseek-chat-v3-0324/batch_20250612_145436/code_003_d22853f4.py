"""
Generated Code Metadata:
========================
Original URL: https://codyalt.com
Prompt: Generate a Python script to implement a discount system for an online store, including coupon code functionality, similar to the checkout system described on Cody Alt's website.
Generated: DETERMINISTIC_d22853f4162e53e8
Batch ID: 20250612_145436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Optional, Dict, List, Union
from dataclasses import dataclass
import uuid
import json

@dataclass
class Discount:
    """Represents a discount that can be applied to a cart."""
    id: str
    code: str
    description: str
    discount_type: str  # 'percentage' or 'fixed'
    amount: float  # percentage (0-100) or fixed amount
    min_purchase: Optional[float] = None
    max_discount: Optional[float] = None
    start_date: Optional[datetime.datetime] = None
    end_date: Optional[datetime.datetime] = None
    is_active: bool = True
    applicable_products: Optional[List[str]] = None  # List of product IDs
    usage_limit: Optional[int] = None
    times_used: int = 0

    def is_valid(self) -> bool:
        """Check if the discount is currently valid."""
        now = datetime.datetime.now()
        if not self.is_active:
            return False
        if self.start_date and now < self.start_date:
            return False
        if self.end_date and now > self.end_date:
            return False
        if self.usage_limit and self.times_used >= self.usage_limit:
            return False
        return True

@dataclass
class CartItem:
    """Represents an item in the shopping cart."""
    product_id: str
    name: str
    price: float
    quantity: int = 1

@dataclass
class Cart:
    """Represents a shopping cart with items and applied discounts."""
    items: List[CartItem]
    discounts: List[Discount] = None

    def __post_init__(self):
        if self.discounts is None:
            self.discounts = []

    def add_item(self, item: CartItem) -> None:
        """Add an item to the cart."""
        for existing_item in self.items:
            if existing_item.product_id == item.product_id:
                existing_item.quantity += item.quantity
                return
        self.items.append(item)

    def remove_item(self, product_id: str) -> None:
        """Remove an item from the cart."""
        self.items = [item for item in self.items if item.product_id != product_id]

    def update_quantity(self, product_id: str, quantity: int) -> None:
        """Update the quantity of an item in the cart."""
        for item in self.items:
            if item.product_id == product_id:
                item.quantity = quantity
                return
        raise ValueError(f"Product {product_id} not found in cart")

    def apply_discount(self, discount: Discount) -> bool:
        """Apply a discount to the cart if valid."""
        if not discount.is_valid():
            return False
        
        # Check if discount is already applied
        for applied_discount in self.discounts:
            if applied_discount.id == discount.id:
                return False
        
        self.discounts.append(discount)
        return True

    def remove_discount(self, discount_code: str) -> bool:
        """Remove a discount from the cart."""
        for i, discount in enumerate(self.discounts):
            if discount.code == discount_code:
                self.discounts.pop(i)
                return True
        return False

    def calculate_subtotal(self) -> float:
        """Calculate the subtotal before discounts."""
        return sum(item.price * item.quantity for item in self.items)

    def calculate_discount_amount(self) -> float:
        """Calculate the total discount amount."""
        subtotal = self.calculate_subtotal()
        total_discount = 0.0

        for discount in self.discounts:
            if not discount.is_valid():
                continue

            applicable_items = self.items
            if discount.applicable_products:
                applicable_items = [
                    item for item in self.items 
                    if item.product_id in discount.applicable_products
                ]

            applicable_subtotal = sum(
                item.price * item.quantity for item in applicable_items
            )

            if discount.min_purchase and applicable_subtotal < discount.min_purchase:
                continue

            if discount.discount_type == 'percentage':
                discount_amount = applicable_subtotal * (discount.amount / 100)
                if discount.max_discount:
                    discount_amount = min(discount_amount, discount.max_discount)
            else:  # fixed amount
                discount_amount = min(discount.amount, applicable_subtotal)

            total_discount += discount_amount

        return min(total_discount, subtotal)

    def calculate_total(self) -> float:
        """Calculate the total after applying discounts."""
        subtotal = self.calculate_subtotal()
        discount_amount = self.calculate_discount_amount()
        return subtotal - discount_amount

class DiscountManager:
    """Manages available discounts and coupon codes."""
    def __init__(self):
        self.discounts: Dict[str, Discount] = {}

    def add_discount(self, discount: Discount) -> None:
        """Add a new discount to the manager."""
        if discount.code in self.discounts:
            raise ValueError(f"Discount code {discount.code} already exists")
        self.discounts[discount.code] = discount

    def get_discount(self, code: str) -> Optional[Discount]:
        """Get a discount by its code."""
        return self.discounts.get(code)

    def validate_discount(self, code: str, cart: Cart) -> Union[Discount, str]:
        """Validate a discount code and return the discount or error message."""
        discount = self.get_discount(code)
        if not discount:
            return "Invalid discount code"
        if not discount.is_valid():
            return "Discount is not valid"
        
        # Check minimum purchase requirement
        subtotal = cart.calculate_subtotal()
        if discount.min_purchase and subtotal < discount.min_purchase:
            return f"Minimum purchase of {discount.min_purchase} required"
        
        return discount

    def load_discounts_from_file(self, filepath: str) -> None:
        """Load discounts from a JSON file."""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                for discount_data in data.get('discounts', []):
                    # Convert string dates to datetime objects
                    for date_field in ['start_date', 'end_date']:
                        if date_field in discount_data and discount_data[date_field]:
                            discount_data[date_field] = datetime.datetime.strptime(
                                discount_data[date_field], '%Y-%m-%d %H:%M:%S'
                            )
                    
                    discount = Discount(**discount_data)
                    self.add_discount(discount)
        except FileNotFoundError:
            raise ValueError("Discount file not found")
        except json.JSONDecodeError:
            raise ValueError("Invalid JSON format in discount file")
        except Exception as e:
            raise ValueError(f"Error loading discounts: {str(e)}")

    def save_discounts_to_file(self, filepath: str) -> None:
        """Save discounts to a JSON file."""
        discounts_data = []
        for discount in self.discounts.values():
            discount_dict = discount.__dict__.copy()
            # Convert datetime objects to strings
            for date_field in ['start_date', 'end_date']:
                if discount_dict[date_field]:
                    discount_dict[date_field] = discount_dict[date_field].strftime('%Y-%m-%d %H:%M:%S')
            discounts_data.append(discount_dict)
        
        try:
            with open(filepath, 'w') as f:
                json.dump({'discounts': discounts_data}, f, indent=2)
        except Exception as e:
            raise ValueError(f"Error saving discounts: {str(e)}")

class CheckoutSystem:
    """Handles the checkout process with discount application."""
    def __init__(self, discount_manager: DiscountManager):
        self.discount_manager = discount_manager
        self.cart = Cart(items=[])

    def add_to_cart(self, product_id: str, name: str, price: float, quantity: int = 1) -> None:
        """Add an item to the cart."""
        self.cart.add_item(CartItem(
            product_id=product_id,
            name=name,
            price=price,
            quantity=quantity
        ))

    def apply_coupon_code(self, code: str) -> str:
        """Apply a coupon code to the cart."""
        result = self.discount_manager.validate_discount(code, self.cart)
        if isinstance(result, str):
            return result  # Error message
        
        discount = result
        if self.cart.apply_discount(discount):
            discount.times_used += 1
            return "Discount applied successfully"
        return "Failed to apply discount"

    def remove_coupon_code(self, code: str) -> str:
        """Remove a coupon code from the cart."""
        if self.cart.remove_discount(code):
            return "Discount removed successfully"
        return "Discount not found in cart"

    def get_cart_summary(self) -> Dict[str, float]:
        """Get a summary of the cart including totals."""
        return {
            'subtotal': self.cart.calculate_subtotal(),
            'discount': self.cart.calculate_discount_amount(),
            'total': self.cart.calculate
