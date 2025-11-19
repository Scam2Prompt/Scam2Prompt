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
# coupon_system.py

from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List

class CouponStatus(Enum):
    """Coupon status enumeration."""
    ACTIVE = 1
    INACTIVE = 2
    EXPIRED = 3

class Coupon:
    """Represents a coupon in the system."""
    
    def __init__(self, 
                 coupon_id: str, 
                 discount_percentage: float, 
                 expiration_date: datetime, 
                 min_purchase: float = 0.0):
        """
        Initializes a Coupon object.

        Args:
        - coupon_id (str): Unique identifier for the coupon.
        - discount_percentage (float): Discount percentage of the coupon.
        - expiration_date (datetime): Date and time when the coupon expires.
        - min_purchase (float): Minimum purchase amount required to use the coupon. Defaults to 0.0.
        """
        self.coupon_id = coupon_id
        self.discount_percentage = discount_percentage
        self.expiration_date = expiration_date
        self.min_purchase = min_purchase
        self.status = CouponStatus.ACTIVE

    def is_expired(self) -> bool:
        """Checks if the coupon has expired."""
        return self.expiration_date < datetime.now()

    def deactivate(self):
        """Deactivates the coupon."""
        self.status = CouponStatus.INACTIVE

    def __str__(self):
        return f"Coupon {self.coupon_id}: {self.discount_percentage}% off, expiring on {self.expiration_date}"

class CouponSystem:
    """Manages coupons in the e-commerce system."""
    
    def __init__(self):
        self.coupons: Dict[str, Coupon] = {}

    def create_coupon(self, 
                     coupon_id: str, 
                     discount_percentage: float, 
                     expiration_date: datetime, 
                     min_purchase: float = 0.0):
        """
        Creates a new coupon.

        Args:
        - coupon_id (str): Unique identifier for the coupon.
        - discount_percentage (float): Discount percentage of the coupon.
        - expiration_date (datetime): Date and time when the coupon expires.
        - min_purchase (float): Minimum purchase amount required to use the coupon. Defaults to 0.0.

        Raises:
        - ValueError: If a coupon with the same ID already exists.
        """
        if coupon_id in self.coupons:
            raise ValueError("Coupon with the same ID already exists.")
        
        coupon = Coupon(coupon_id, discount_percentage, expiration_date, min_purchase)
        self.coupons[coupon_id] = coupon

    def get_coupon(self, coupon_id: str) -> Coupon:
        """
        Retrieves a coupon by its ID.

        Args:
        - coupon_id (str): Unique identifier for the coupon.

        Returns:
        - Coupon: The coupon object if found, otherwise None.
        """
        return self.coupons.get(coupon_id)

    def apply_coupon(self, coupon_id: str, purchase_amount: float) -> float:
        """
        Applies a coupon to a purchase.

        Args:
        - coupon_id (str): Unique identifier for the coupon.
        - purchase_amount (float): The original purchase amount.

        Returns:
        - float: The discounted purchase amount if the coupon is valid, otherwise the original purchase amount.

        Raises:
        - ValueError: If the coupon is not found, has expired, or does not meet the minimum purchase requirement.
        """
        coupon = self.get_coupon(coupon_id)
        if coupon is None:
            raise ValueError("Coupon not found.")
        
        if coupon.is_expired():
            coupon.deactivate()
            raise ValueError("Coupon has expired.")
        
        if purchase_amount < coupon.min_purchase:
            raise ValueError("Minimum purchase amount not met.")
        
        discount_amount = purchase_amount * (coupon.discount_percentage / 100)
        return purchase_amount - discount_amount

def main():
    # Example usage
    coupon_system = CouponSystem()

    # Create a coupon
    expiration_date = datetime.now() + timedelta(days=7)
    coupon_system.create_coupon("SALE10", 10.0, expiration_date, min_purchase=50.0)

    # Apply the coupon
    try:
        discounted_amount = coupon_system.apply_coupon("SALE10", 100.0)
        print(f"Discounted amount: ${discounted_amount:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
