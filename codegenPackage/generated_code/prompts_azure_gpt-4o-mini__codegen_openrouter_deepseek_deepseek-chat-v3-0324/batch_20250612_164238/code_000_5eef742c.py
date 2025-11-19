"""
Generated Code Metadata:
========================
Original URL: https://www.tiktokshopvn.com.vn
Prompt: Generate a code snippet for an e-commerce platform that implements a discount system for products, similar to the 45% discount and coupon features mentioned on TikTok Shop Vietnam.
Generated: DETERMINISTIC_5eef742c08f556b3
Batch ID: 20250612_164238
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class Discount:
    """
    Represents a discount that can be applied to a product.
    """
    def __init__(self, discount_percentage: float, start_date: datetime.datetime, end_date: datetime.datetime):
        """
        Initialize a discount with percentage, start date, and end date.
        
        Args:
            discount_percentage: Percentage of discount (e.g., 45 for 45%)
            start_date: Start date of the discount
            end_date: End date of the discount
        """
        if discount_percentage < 0 or discount_percentage > 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        if start_date >= end_date:
            raise ValueError("Start date must be before end date")
        
        self.discount_percentage = discount_percentage
        self.start_date = start_date
        self.end_date = end_date

    def is_active(self) -> bool:
        """
        Check if the discount is currently active.
        
        Returns:
            bool: True if discount is active, False otherwise
        """
        now = datetime.datetime.now()
        return self.start_date <= now <= self.end_date

class Coupon(Discount):
    """
    Represents a coupon that can be applied to a product, extending Discount with a code.
    """
    def __init__(self, discount_percentage: float, start_date: datetime.datetime, 
                 end_date: datetime.datetime, code: str, max_uses: Optional[int] = None):
        """
        Initialize a coupon with code and optional max uses.
        
        Args:
            discount_percentage: Percentage of discount (e.g., 45 for 45%)
            start_date: Start date of the coupon
            end_date: End date of the coupon
            code: Unique coupon code
            max_uses: Maximum number of times the coupon can be used (None for unlimited)
        """
        super().__init__(discount_percentage, start_date, end_date)
        self.code = code
        self.max_uses = max_uses
        self.uses = 0

    def is_valid(self) -> bool:
        """
        Check if the coupon is valid (active and not exceeded max uses).
        
        Returns:
            bool: True if coupon is valid, False otherwise
        """
        if not self.is_active():
            return False
        if self.max_uses is not None and self.uses >= self.max_uses:
            return False
        return True

    def apply(self) -> None:
        """
        Apply the coupon (increment uses).
        
        Raises:
            ValueError: If coupon is not valid
        """
        if not self.is_valid():
            raise ValueError("Coupon is not valid")
        self.uses += 1

class Product:
    """
    Represents a product in the e-commerce platform.
    """
    def __init__(self, name: str, price: float):
        """
        Initialize a product with name and price.
        
        Args:
            name: Name of the product
            price: Original price of the product
        """
        self.name = name
        self.price = price
        self.discounts: List[Discount] = []
        self.coupons: List[Coupon] = []

    def add_discount(self, discount: Discount) -> None:
        """
        Add a discount to the product.
        
        Args:
            discount: Discount to add
        """
        self.discounts.append(discount)

    def add_coupon(self, coupon: Coupon) -> None:
        """
        Add a coupon to the product.
        
        Args:
            coupon: Coupon to add
        """
        self.coupons.append(coupon)

    def get_current_discount(self) -> Optional[Discount]:
        """
        Get the currently active discount with the highest percentage.
        
        Returns:
            Optional[Discount]: Active discount or None if no active discounts
        """
        active_discounts = [d for d in self.discounts if d.is_active()]
        if not active_discounts:
            return None
        return max(active_discounts, key=lambda d: d.discount_percentage)

    def get_coupon_by_code(self, code: str) -> Optional[Coupon]:
        """
        Get a coupon by its code.
        
        Args:
            code: Coupon code to search for
            
        Returns:
            Optional[Coupon]: Coupon if found, None otherwise
        """
        for coupon in self.coupons:
            if coupon.code == code:
                return coupon
        return None

    def get_final_price(self, coupon_code: Optional[str] = None) -> float:
        """
        Calculate the final price after applying discounts and coupon.
        
        Args:
            coupon_code: Optional coupon code to apply
            
        Returns:
            float: Final price after discounts
        """
        price = self.price
        
        # Apply highest active discount
        discount = self.get_current_discount()
        if discount:
            price *= (1 - discount.discount_percentage / 100)
        
        # Apply coupon if provided and valid
        if coupon_code:
            coupon = self.get_coupon_by_code(coupon_code)
            if coupon and coupon.is_valid():
                price *= (1 - coupon.discount_percentage / 100)
                coupon.apply()
        
        return round(price, 2)

# Example usage
if __name__ == "__main__":
    # Create a product
    product = Product("Smartphone", 1000.0)
    
    # Add a 45% discount for the next 7 days
    now = datetime.datetime.now()
    discount = Discount(45.0, now, now + datetime.timedelta(days=7))
    product.add_discount(discount)
    
    # Add a coupon for additional 10% off
    coupon = Coupon(10.0, now, now + datetime.timedelta(days=7), "TIKTOK10", max_uses=100)
    product.add_coupon(coupon)
    
    # Calculate final price
    print(f"Original price: ${product.price}")
    print(f"Price after discount: ${product.get_final_price()}")
    print(f"Price with coupon: ${product.get_final_price('TIKTOK10')}")
```
