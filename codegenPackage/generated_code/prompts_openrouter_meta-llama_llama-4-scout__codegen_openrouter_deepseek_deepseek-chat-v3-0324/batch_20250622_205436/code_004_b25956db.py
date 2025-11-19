"""
Generated Code Metadata:
========================
Original URL: https://codestiers.com
Prompt: "Design a simple e-commerce coupon system using a programming language of your choice, inspired by Codestiers' features and functionality."
Generated: DETERMINISTIC_b25956db91d0a5f6
Batch ID: 20250622_205436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class Coupon:
    """
    Represents an e-commerce coupon with discount functionality.
    """
    def __init__(
        self,
        code: str,
        discount_type: str,
        discount_value: float,
        min_order_amount: float = 0.0,
        max_discount: Optional[float] = None,
        valid_from: Optional[datetime] = None,
        valid_to: Optional[datetime] = None,
        max_uses: Optional[int] = None,
        current_uses: int = 0,
        is_active: bool = True
    ):
        """
        Initialize a coupon with the given parameters.
        
        Args:
            code: Unique coupon code
            discount_type: 'percentage' or 'fixed'
            discount_value: Discount amount (percentage or fixed)
            min_order_amount: Minimum order amount to apply coupon
            max_discount: Maximum discount amount (for percentage coupons)
            valid_from: Coupon validity start date
            valid_to: Coupon validity end date
            max_uses: Maximum number of times coupon can be used
            current_uses: Current number of times coupon has been used
            is_active: Whether coupon is active
        """
        self.code = code
        self.discount_type = discount_type
        self.discount_value = discount_value
        self.min_order_amount = min_order_amount
        self.max_discount = max_discount
        self.valid_from = valid_from or datetime.now()
        self.valid_to = valid_to or (datetime.now() + timedelta(days=30))
        self.max_uses = max_uses
        self.current_uses = current_uses
        self.is_active = is_active

    def is_valid(self) -> bool:
        """
        Check if the coupon is valid based on:
        - Active status
        - Validity dates
        - Usage limits
        """
        now = datetime.now()
        return (
            self.is_active and
            now >= self.valid_from and
            now <= self.valid_to and
            (self.max_uses is None or self.current_uses < self.max_uses)
        )

    def apply_discount(self, order_amount: float) -> float:
        """
        Apply coupon discount to order amount.
        
        Args:
            order_amount: Original order amount
            
        Returns:
            Discount amount
            
        Raises:
            ValueError: If coupon is invalid or order amount is too low
        """
        if not self.is_valid():
            raise ValueError("Coupon is not valid")
        
        if order_amount < self.min_order_amount:
            raise ValueError(f"Order amount must be at least {self.min_order_amount}")
        
        if self.discount_type == 'percentage':
            discount = order_amount * (self.discount_value / 100)
            if self.max_discount is not None:
                discount = min(discount, self.max_discount)
            return discount
        elif self.discount_type == 'fixed':
            return min(self.discount_value, order_amount)
        else:
            raise ValueError("Invalid discount type")

    def increment_usage(self) -> None:
        """
        Increment the usage count of the coupon.
        """
        if self.max_uses is not None and self.current_uses >= self.max_uses:
            raise ValueError("Coupon has reached maximum usage limit")
        self.current_uses += 1

class CouponSystem:
    """
    Manages creation, storage, and validation of coupons.
    """
    def __init__(self):
        self.coupons: Dict[str, Coupon] = {}

    def generate_coupon_code(self) -> str:
        """
        Generate a unique coupon code.
        
        Returns:
            Generated coupon code
        """
        return str(uuid.uuid4()).replace('-', '')[:10].upper()

    def create_coupon(
        self,
        discount_type: str,
        discount_value: float,
        min_order_amount: float = 0.0,
        max_discount: Optional[float] = None,
        valid_days: int = 30,
        max_uses: Optional[int] = None,
        code: Optional[str] = None
    ) -> Coupon:
        """
        Create and store a new coupon.
        
        Args:
            discount_type: 'percentage' or 'fixed'
            discount_value: Discount amount
            min_order_amount: Minimum order amount
            max_discount: Maximum discount (for percentage)
            valid_days: Number of days coupon is valid
            max_uses: Maximum uses
            code: Optional custom coupon code
            
        Returns:
            Created coupon
            
        Raises:
            ValueError: If discount type is invalid
        """
        if discount_type not in ['percentage', 'fixed']:
            raise ValueError("Discount type must be 'percentage' or 'fixed'")
            
        coupon_code = code or self.generate_coupon_code()
        valid_from = datetime.now()
        valid_to = valid_from + timedelta(days=valid_days)
        
        coupon = Coupon(
            code=coupon_code,
            discount_type=discount_type,
            discount_value=discount_value,
            min_order_amount=min_order_amount,
            max_discount=max_discount,
            valid_from=valid_from,
            valid_to=valid_to,
            max_uses=max_uses
        )
        
        self.coupons[coupon_code] = coupon
        return coupon

    def get_coupon(self, code: str) -> Optional[Coupon]:
        """
        Retrieve a coupon by its code.
        
        Args:
            code: Coupon code
            
        Returns:
            Coupon if found, None otherwise
        """
        return self.coupons.get(code)

    def validate_coupon(self, code: str, order_amount: float) -> bool:
        """
        Validate if a coupon can be applied to an order.
        
        Args:
            code: Coupon code
            order_amount: Order amount
            
        Returns:
            True if coupon is valid, False otherwise
        """
        coupon = self.get_coupon(code)
        if not coupon:
            return False
        
        try:
            coupon.apply_discount(order_amount)
            return True
        except ValueError:
            return False

    def apply_coupon(self, code: str, order_amount: float) -> float:
        """
        Apply a coupon to an order and return the discount amount.
        
        Args:
            code: Coupon code
            order_amount: Order amount
            
        Returns:
            Discount amount
            
        Raises:
            ValueError: If coupon is invalid or cannot be applied
        """
        coupon = self.get_coupon(code)
        if not coupon:
            raise ValueError("Coupon not found")
        
        discount = coupon.apply_discount(order_amount)
        coupon.increment_usage()
        return discount

    def get_all_coupons(self) -> List[Coupon]:
        """
        Get all coupons in the system.
        
        Returns:
            List of all coupons
        """
        return list(self.coupons.values())

    def deactivate_coupon(self, code: str) -> None:
        """
        Deactivate a coupon.
        
        Args:
            code: Coupon code
            
        Raises:
            ValueError: If coupon not found
        """
        coupon = self.get_coupon(code)
        if not coupon:
            raise ValueError("Coupon not found")
        coupon.is_active = False

    def activate_coupon(self, code: str) -> None:
        """
        Activate a coupon.
        
        Args:
            code: Coupon code
            
        Raises:
            ValueError: If coupon not found
        """
        coupon = self.get_coupon(code)
        if not coupon:
            raise ValueError("Coupon not found")
        coupon.is_active = True

# Example usage
if __name__ == "__main__":
    system = CouponSystem()
    
    # Create some coupons
    coupon1 = system.create_coupon(
        discount_type='percentage',
        discount_value=15.0,
        min_order_amount=50.0,
        max_discount=20.0,
        valid_days=60
    )
    
    coupon2 = system.create_coupon(
        discount_type='fixed',
        discount_value=10.0,
        min_order_amount=30.0,
        max_uses=100
    )
    
    # Try applying coupons
    try:
        discount = system.apply_coupon(coupon1.code, 100.0)
        print(f"Applied coupon {coupon1.code}, discount: ${discount:.2f}")
    except ValueError as e:
        print(f"Error applying coupon: {e}")
    
    try:
        discount = system.apply_coupon(coupon2.code, 40.0)
        print(f"Applied coupon {coupon2.code}, discount: ${discount:.2f}")
    except ValueError as e:
        print(f"Error applying coupon: {e}")
    
    # Try invalid coupon
    try:
        discount = system.apply_coupon("INVALID", 100.0)
    except ValueError as e:
        print(f"Expected error: {e}")
```
