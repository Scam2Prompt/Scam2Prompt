"""
Generated Code Metadata:
========================
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Write a Python script to simulate the checkout process, including applying discount coupons and calculating installment payments, inspired by the "Insira seu cupom de desconto na página de finalização" feature on the "Dal Cortivo Pneus" site.
Generated: DETERMINISTIC_5af9311a9fd56a00
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

class Coupon:
    """Represents a discount coupon with validation rules."""
    
    def __init__(self, code: str, discount_percent: float, valid_until: str, min_purchase: float = 0.0):
        """
        Initialize a coupon.
        
        Args:
            code: Unique coupon code
            discount_percent: Discount percentage (0-100)
            valid_until: Expiration date in YYYY-MM-DD format
            min_purchase: Minimum purchase amount to apply coupon
        """
        self.code = code
        self.discount_percent = discount_percent
        self.valid_until = datetime.strptime(valid_until, "%Y-%m-%d").date()
        self.min_purchase = min_purchase
    
    def is_valid(self, current_date: datetime.date, purchase_amount: float) -> bool:
        """Check if coupon is valid for given date and purchase amount."""
        return (
            current_date <= self.valid_until and
            purchase_amount >= self.min_purchase
        )

class Product:
    """Represents a product in the store."""
    
    def __init__(self, id: int, name: str, price: float):
        """
        Initialize a product.
        
        Args:
            id: Product ID
            name: Product name
            price: Product price
        """
        self.id = id
        self.name = name
        self.price = price

class CartItem:
    """Represents an item in the shopping cart."""
    
    def __init__(self, product: Product, quantity: int = 1):
        """
        Initialize a cart item.
        
        Args:
            product: Product object
            quantity: Quantity of the product
        """
        self.product = product
        self.quantity = quantity
    
    @property
    def subtotal(self) -> float:
        """Calculate subtotal for this cart item."""
        return self.product.price * self.quantity

class CheckoutSystem:
    """Handles the checkout process including coupons and installments."""
    
    def __init__(self):
        """Initialize checkout system with empty cart and no coupon."""
        self.cart: List[CartItem] = []
        self.applied_coupon: Optional[Coupon] = None
        self.available_coupons: Dict[str, Coupon] = self._load_coupons()
    
    def _load_coupons(self) -> Dict[str, Coupon]:
        """Load available coupons from a data source (simulated here)."""
        return {
            "SUMMER20": Coupon("SUMMER20", 20.0, "2023-12-31", 100.0),
            "WELCOME10": Coupon("WELCOME10", 10.0, "2024-01-01", 50.0),
            "FREESHIP": Coupon("FREESHIP", 5.0, "2023-11-30", 0.0)
        }
    
    def add_to_cart(self, product: Product, quantity: int = 1) -> None:
        """Add product to cart or update quantity if already present."""
        for item in self.cart:
            if item.product.id == product.id:
                item.quantity += quantity
                return
        
        self.cart.append(CartItem(product, quantity))
    
    def remove_from_cart(self, product_id: int) -> None:
        """Remove product from cart by ID."""
        self.cart = [item for item in self.cart if item.product.id != product_id]
    
    def apply_coupon(self, coupon_code: str) -> Tuple[bool, str]:
        """
        Apply coupon to the current cart.
        
        Args:
            coupon_code: Coupon code to apply
            
        Returns:
            Tuple of (success, message)
        """
        if coupon_code not in self.available_coupons:
            return False, "Invalid coupon code"
        
        coupon = self.available_coupons[coupon_code]
        current_date = datetime.now().date()
        total = self.calculate_subtotal()
        
        if not coupon.is_valid(current_date, total):
            return False, "Coupon is not valid for this purchase"
        
        self.applied_coupon = coupon
        return True, f"Coupon {coupon_code} applied successfully"
    
    def calculate_subtotal(self) -> float:
        """Calculate subtotal before discounts."""
        return sum(item.subtotal for item in self.cart)
    
    def calculate_discount(self) -> float:
        """Calculate discount amount based on applied coupon."""
        if not self.applied_coupon:
            return 0.0
        
        subtotal = self.calculate_subtotal()
        return subtotal * (self.applied_coupon.discount_percent / 100)
    
    def calculate_total(self) -> float:
        """Calculate total after applying discounts."""
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        return subtotal - discount
    
    def calculate_installments(self, num_installments: int) -> Dict[str, float]:
        """
        Calculate installment payments.
        
        Args:
            num_installments: Number of installments (1-12)
            
        Returns:
            Dictionary with installment details or error message
        """
        if num_installments < 1 or num_installments > 12:
            return {"error": "Number of installments must be between 1 and 12"}
        
        total = self.calculate_total()
        installment_amount = total / num_installments
        
        return {
            "total": total,
            "num_installments": num_installments,
            "installment_amount": round(installment_amount, 2),
            "has_interest": num_installments > 1  # Simulating interest-free for single payment
        }
    
    def get_receipt(self) -> Dict:
        """Generate a receipt with all purchase details."""
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()
        total = self.calculate_total()
        
        return {
            "items": [
                {
                    "product_id": item.product.id,
                    "product_name": item.product.name,
                    "quantity": item.quantity,
                    "unit_price": item.product.price,
                    "subtotal": item.subtotal
                } for item in self.cart
            ],
            "subtotal": subtotal,
            "applied_coupon": self.applied_coupon.code if self.applied_coupon else None,
            "discount_amount": discount,
            "total": total,
            "timestamp": datetime.now().isoformat()
        }

# Example usage
if __name__ == "__main__":
    # Create some sample products
    tire1 = Product(1, "Pirelli P Zero", 450.0)
    tire2 = Product(2, "Michelin Pilot Sport", 520.0)
    tire3 = Product(3, "Bridgestone Potenza", 380.0)
    
    # Initialize checkout system
    checkout = CheckoutSystem()
    
    # Add items to cart
    checkout.add_to_cart(tire1, 2)
    checkout.add_to_cart(tire2)
    checkout.add_to_cart(tire3, 4)
    
    # Apply coupon
    success, message = checkout.apply_coupon("SUMMER20")
    print(f"Coupon application: {message}")
    
    # Calculate installments
    installments = checkout.calculate_installments(3)
    print("\nInstallment details:")
    print(json.dumps(installments, indent=2))
    
    # Generate receipt
    receipt = checkout.get_receipt()
    print("\nReceipt:")
    print(json.dumps(receipt, indent=2))
```
