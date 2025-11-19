"""
Generated Code Metadata:
========================
Original URL: https://medebooks.shop
Prompt: Develop a code snippet to implement a discount pricing system for an online store selling medical books and courses, similar to medebooks.shop's discount model.
Generated: DETERMINISTIC_517f891bb97b63a1
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Optional, List, Dict

class Discount:
    """Represents a discount rule for products."""
    
    def __init__(
        self,
        code: str,
        discount_type: str,
        value: float,
        start_date: datetime.date,
        end_date: datetime.date,
        applicable_products: Optional[List[str]] = None,
        min_purchase: Optional[float] = None,
        max_discount: Optional[float] = None
    ):
        """
        Initialize a discount rule.
        
        Args:
            code: Unique discount code
            discount_type: 'percentage' or 'fixed'
            value: Discount amount (percentage or fixed value)
            start_date: When discount becomes active
            end_date: When discount expires
            applicable_products: List of product IDs (None for all products)
            min_purchase: Minimum order amount to apply discount
            max_discount: Maximum discount amount (for percentage discounts)
        """
        self.code = code
        self.discount_type = discount_type.lower()
        self.value = value
        self.start_date = start_date
        self.end_date = end_date
        self.applicable_products = applicable_products or []
        self.min_purchase = min_purchase
        self.max_discount = max_discount
        
        if self.discount_type not in ['percentage', 'fixed']:
            raise ValueError("Discount type must be 'percentage' or 'fixed'")
        if self.value <= 0:
            raise ValueError("Discount value must be positive")
        if self.end_date < self.start_date:
            raise ValueError("End date must be after start date")

    def is_active(self, date: datetime.date = None) -> bool:
        """Check if discount is currently active."""
        date = date or datetime.date.today()
        return self.start_date <= date <= self.end_date

    def is_applicable(self, product_id: str = None, cart_total: float = None) -> bool:
        """
        Check if discount applies to a product or cart.
        
        Args:
            product_id: Product ID to check
            cart_total: Total cart amount to check against min_purchase
            
        Returns:
            bool: True if discount applies
        """
        if product_id and self.applicable_products and product_id not in self.applicable_products:
            return False
        if cart_total and self.min_purchase and cart_total < self.min_purchase:
            return False
        return True

    def calculate_discount(self, price: float) -> float:
        """Calculate discount amount for a given price."""
        if self.discount_type == 'percentage':
            discount = price * (self.value / 100)
            if self.max_discount:
                discount = min(discount, self.max_discount)
            return round(discount, 2)
        else:  # fixed
            return min(self.value, price)


class DiscountSystem:
    """Manages discount rules and calculations."""
    
    def __init__(self):
        self.discounts: Dict[str, Discount] = {}
    
    def add_discount(self, discount: Discount) -> None:
        """Add a new discount rule to the system."""
        if discount.code in self.discounts:
            raise ValueError(f"Discount code {discount.code} already exists")
        self.discounts[discount.code] = discount
    
    def get_discount(self, code: str) -> Optional[Discount]:
        """Retrieve a discount by its code."""
        return self.discounts.get(code)
    
    def validate_discount(
        self,
        code: str,
        product_id: str = None,
        cart_total: float = None,
        date: datetime.date = None
    ) -> bool:
        """
        Validate if a discount code is valid and applicable.
        
        Args:
            code: Discount code to validate
            product_id: Product ID to check applicability
            cart_total: Cart total to check minimum purchase
            date: Date to check if discount is active
            
        Returns:
            bool: True if discount is valid and applicable
        """
        discount = self.get_discount(code)
        if not discount:
            return False
        if not discount.is_active(date):
            return False
        return discount.is_applicable(product_id, cart_total)
    
    def calculate_discounted_price(
        self,
        code: str,
        original_price: float,
        product_id: str = None,
        cart_total: float = None
    ) -> float:
        """
        Calculate discounted price for a product.
        
        Args:
            code: Discount code to apply
            original_price: Original product price
            product_id: Product ID for applicability check
            cart_total: Cart total for minimum purchase check
            
        Returns:
            float: Discounted price
        """
        if not self.validate_discount(code, product_id, cart_total):
            return original_price
        
        discount = self.get_discount(code)
        discount_amount = discount.calculate_discount(original_price)
        return round(original_price - discount_amount, 2)


# Example usage
if __name__ == "__main__":
    # Initialize discount system
    discount_system = DiscountSystem()
    
    # Create some discounts
    today = datetime.date.today()
    next_week = today + datetime.timedelta(days=7)
    
    # Site-wide discount
    site_wide = Discount(
        code="MED20",
        discount_type="percentage",
        value=20,
        start_date=today,
        end_date=next_week,
        min_purchase=50
    )
    
    # Product-specific discount
    book_discount = Discount(
        code="BOOK15",
        discount_type="percentage",
        value=15,
        start_date=today,
        end_date=next_week,
        applicable_products=["book123", "book456"],
        max_discount=10
    )
    
    # Fixed amount discount
    course_discount = Discount(
        code="COURSE10",
        discount_type="fixed",
        value=10,
        start_date=today,
        end_date=next_week,
        applicable_products=["course789"]
    )
    
    # Add discounts to system
    discount_system.add_discount(site_wide)
    discount_system.add_discount(book_discount)
    discount_system.add_discount(course_discount)
    
    # Test calculations
    book_price = 45.00
    course_price = 99.00
    cart_total = 60.00
    
    print(f"Book price with MED20: {discount_system.calculate_discounted_price('MED20', book_price, cart_total=cart_total)}")
    print(f"Book price with BOOK15: {discount_system.calculate_discounted_price('BOOK15', book_price, 'book123')}")
    print(f"Course price with COURSE10: {discount_system.calculate_discounted_price('COURSE10', course_price, 'course789')}")
```
