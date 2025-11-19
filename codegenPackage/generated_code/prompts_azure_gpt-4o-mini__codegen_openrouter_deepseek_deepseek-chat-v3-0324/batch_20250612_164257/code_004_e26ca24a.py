"""
Generated Code Metadata:
========================
Original URL: https://malkeenz.com
Prompt: Write a code example that demonstrates how to implement a discount system for first-time shoppers in a jewelry e-commerce application, referencing the "5% off" offer from Malkeenz.
Generated: DETERMINISTIC_e26ca24af8433391
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary modules
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

class CustomerType(Enum):
    """Enum representing different types of customers."""
    FIRST_TIME = auto()
    RETURNING = auto()
    VIP = auto()

@dataclass
class Customer:
    """Represents a customer with their type and discount eligibility."""
    customer_id: str
    name: str
    email: str
    customer_type: CustomerType
    has_used_discount: bool = False

class DiscountSystem:
    """Handles discount calculations for customers."""
    
    FIRST_TIME_DISCOUNT_RATE = 0.05  # 5% discount for first-time shoppers
    
    def __init__(self):
        """Initialize the discount system."""
        pass
    
    def is_eligible_for_first_time_discount(self, customer: Customer) -> bool:
        """Check if customer is eligible for first-time discount.
        
        Args:
            customer: Customer object to check eligibility
            
        Returns:
            bool: True if eligible, False otherwise
        """
        return (customer.customer_type == CustomerType.FIRST_TIME 
                and not customer.has_used_discount)
    
    def apply_discount(self, amount: float, customer: Customer) -> float:
        """Apply discount to purchase amount if eligible.
        
        Args:
            amount: Original purchase amount
            customer: Customer making the purchase
            
        Returns:
            float: Discounted amount if eligible, original amount otherwise
            
        Raises:
            ValueError: If amount is negative
        """
        if amount < 0:
            raise ValueError("Purchase amount cannot be negative")
            
        if self.is_eligible_for_first_time_discount(customer):
            discounted_amount = amount * (1 - self.FIRST_TIME_DISCOUNT_RATE)
            customer.has_used_discount = True
            return round(discounted_amount, 2)
        return amount

# Example usage
if __name__ == "__main__":
    # Create a first-time customer
    new_customer = Customer(
        customer_id="cust123",
        name="Alice Smith",
        email="alice@example.com",
        customer_type=CustomerType.FIRST_TIME
    )
    
    discount_system = DiscountSystem()
    
    # Try to apply discount
    purchase_amount = 1000.00
    try:
        discounted_amount = discount_system.apply_discount(purchase_amount, new_customer)
        print(f"Original amount: ${purchase_amount:.2f}")
        print(f"Discounted amount: ${discounted_amount:.2f}")
        print(f"Discount applied: {discount_system.FIRST_TIME_DISCOUNT_RATE * 100}%")
    except ValueError as e:
        print(f"Error applying discount: {e}")
```
