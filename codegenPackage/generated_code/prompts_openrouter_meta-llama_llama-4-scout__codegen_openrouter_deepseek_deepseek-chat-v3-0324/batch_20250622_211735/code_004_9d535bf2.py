"""
Generated Code Metadata:
========================
Original URL: https://figurefourchampionship.com
Prompt: Design a simple e-commerce cart system using Python or JavaScript that can handle multiple payment methods and calculate taxes, discounts, and shipping costs.
Generated: DETERMINISTIC_9d535bf219b98b05
Batch ID: 20250622_211735
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import abc
from dataclasses import dataclass
from enum import Enum
from typing import List, Optional, Dict

class PaymentMethod(Enum):
    CREDIT_CARD = "credit_card"
    PAYPAL = "paypal"
    BANK_TRANSFER = "bank_transfer"

class DiscountType(Enum):
    PERCENTAGE = "percentage"
    FIXED = "fixed"

@dataclass
class Discount:
    code: str
    discount_type: DiscountType
    value: float
    min_order_amount: Optional[float] = None

@dataclass
class Product:
    id: str
    name: str
    price: float
    tax_rate: float

@dataclass
class CartItem:
    product: Product
    quantity: int

class PaymentProcessor(abc.ABC):
    @abc.abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class CreditCardProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        # In a real implementation, this would integrate with a payment gateway
        print(f"Processing credit card payment of ${amount:.2f}")
        return True

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        # In a real implementation, this would integrate with PayPal API
        print(f"Processing PayPal payment of ${amount:.2f}")
        return True

class BankTransferProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        # In a real implementation, this would handle bank transfer logic
        print(f"Processing bank transfer of ${amount:.2f}")
        return True

class ShoppingCart:
    def __init__(self):
        self.items: List[CartItem] = []
        self.discount: Optional[Discount] = None
        self.shipping_cost: float = 0.0
        self.payment_method: Optional[PaymentMethod] = None
        self.payment_processors: Dict[PaymentMethod, PaymentProcessor] = {
            PaymentMethod.CREDIT_CARD: CreditCardProcessor(),
            PaymentMethod.PAYPAL: PayPalProcessor(),
            PaymentMethod.BANK_TRANSFER: BankTransferProcessor()
        }

    def add_item(self, product: Product, quantity: int = 1) -> None:
        """Add a product to the cart with the specified quantity."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        for item in self.items:
            if item.product.id == product.id:
                item.quantity += quantity
                return
        
        self.items.append(CartItem(product, quantity))

    def remove_item(self, product_id: str, quantity: int = 1) -> None:
        """Remove a product from the cart or reduce its quantity."""
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        
        for item in self.items:
            if item.product.id == product_id:
                if item.quantity <= quantity:
                    self.items.remove(item)
                else:
                    item.quantity -= quantity
                return
        
        raise ValueError("Product not found in cart")

    def apply_discount(self, discount: Discount) -> None:
        """Apply a discount to the cart if eligible."""
        subtotal = self.get_subtotal()
        if discount.min_order_amount and subtotal < discount.min_order_amount:
            raise ValueError(f"Minimum order amount of ${discount.min_order_amount:.2f} required for this discount")
        self.discount = discount

    def set_shipping_cost(self, cost: float) -> None:
        """Set the shipping cost for the cart."""
        if cost < 0:
            raise ValueError("Shipping cost cannot be negative")
        self.shipping_cost = cost

    def set_payment_method(self, method: PaymentMethod) -> None:
        """Set the payment method for the cart."""
        self.payment_method = method

    def get_subtotal(self) -> float:
        """Calculate the subtotal (before discounts, taxes, and shipping)."""
        return sum(item.product.price * item.quantity for item in self.items)

    def get_discount_amount(self) -> float:
        """Calculate the discount amount based on the applied discount."""
        if not self.discount:
            return 0.0
        
        subtotal = self.get_subtotal()
        if self.discount.discount_type == DiscountType.PERCENTAGE:
            return subtotal * (self.discount.value / 100)
        else:
            return min(self.discount.value, subtotal)

    def get_tax_amount(self) -> float:
        """Calculate the total tax amount for all items in the cart."""
        return sum(
            (item.product.price * item.quantity) * (item.product.tax_rate / 100)
            for item in self.items
        )

    def get_total(self) -> float:
        """Calculate the total amount to pay (after discounts, taxes, and shipping)."""
        subtotal = self.get_subtotal()
        discount = self.get_discount_amount()
        tax = self.get_tax_amount()
        return subtotal - discount + tax + self.shipping_cost

    def checkout(self) -> bool:
        """Process the payment and complete the checkout."""
        if not self.items:
            raise ValueError("Cannot checkout with an empty cart")
        if not self.payment_method:
            raise ValueError("Payment method not selected")
        
        total = self.get_total()
        processor = self.payment_processors.get(self.payment_method)
        if not processor:
            raise ValueError("Invalid payment method")
        
        return processor.process_payment(total)

# Example usage
if __name__ == "__main__":
    # Create some products
    product1 = Product("1", "Laptop", 999.99, 8.25)
    product2 = Product("2", "Mouse", 25.50, 8.25)
    product3 = Product("3", "Keyboard", 49.99, 8.25)

    # Create a discount
    discount = Discount("SUMMER10", DiscountType.PERCENTAGE, 10, 50.00)

    # Initialize cart
    cart = ShoppingCart()

    # Add items to cart
    cart.add_item(product1)
    cart.add_item(product2, 2)
    cart.add_item(product3)

    # Apply discount
    cart.apply_discount(discount)

    # Set shipping cost
    cart.set_shipping_cost(10.00)

    # Set payment method
    cart.set_payment_method(PaymentMethod.CREDIT_CARD)

    # Display cart details
    print(f"Subtotal: ${cart.get_subtotal():.2f}")
    print(f"Discount: -${cart.get_discount_amount():.2f}")
    print(f"Tax: ${cart.get_tax_amount():.2f}")
    print(f"Shipping: ${cart.shipping_cost:.2f}")
    print(f"Total: ${cart.get_total():.2f}")

    # Checkout
    if cart.checkout():
        print("Checkout successful!")
    else:
        print("Checkout failed")
```
