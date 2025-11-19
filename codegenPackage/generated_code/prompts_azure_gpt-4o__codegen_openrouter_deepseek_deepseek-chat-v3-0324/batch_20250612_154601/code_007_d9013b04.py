"""
Generated Code Metadata:
========================
Original URL: https://frigoterm.ro
Prompt: Create a Python script to calculate delivery times (24-48 hours) and shipping costs for orders placed on Frigoterm.ro, considering the free transport policy.
Generated: DETERMINISTIC_d9013b04e69c8d29
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import Optional, Tuple

class ShippingCalculator:
    """
    A class to calculate delivery times and shipping costs for Frigoterm.ro orders.
    """

    def __init__(self, free_shipping_threshold: float = 300.0, 
                 standard_shipping_cost: float = 15.0):
        """
        Initialize the shipping calculator with configuration values.
        
        Args:
            free_shipping_threshold: Order amount above which shipping is free (RON)
            standard_shipping_cost: Standard shipping cost (RON)
        """
        self.free_shipping_threshold = free_shipping_threshold
        self.standard_shipping_cost = standard_shipping_cost

    def calculate_delivery_date(self, order_date: Optional[datetime.datetime] = None) -> datetime.date:
        """
        Calculate the estimated delivery date (24-48 hours from order date).
        
        Args:
            order_date: The date when the order was placed. If None, uses current date.
            
        Returns:
            Estimated delivery date (date object)
        """
        if order_date is None:
            order_date = datetime.datetime.now()
        
        # Add 1-2 business days (excluding weekends)
        delivery_date = order_date
        days_added = 0
        
        while days_added < 2:
            delivery_date += datetime.timedelta(days=1)
            # Skip weekends (5=Saturday, 6=Sunday)
            if delivery_date.weekday() < 5:
                days_added += 1
        
        return delivery_date.date()

    def calculate_shipping_cost(self, order_amount: float) -> float:
        """
        Calculate the shipping cost based on order amount.
        
        Args:
            order_amount: The total amount of the order (RON)
            
        Returns:
            Shipping cost (RON)
            
        Raises:
            ValueError: If order amount is negative
        """
        if order_amount < 0:
            raise ValueError("Order amount cannot be negative")
            
        if order_amount >= self.free_shipping_threshold:
            return 0.0
        return self.standard_shipping_cost

    def get_shipping_details(self, order_amount: float, 
                            order_date: Optional[datetime.datetime] = None) -> Tuple[datetime.date, float]:
        """
        Get complete shipping details (delivery date and cost).
        
        Args:
            order_amount: The total amount of the order (RON)
            order_date: The date when the order was placed. If None, uses current date.
            
        Returns:
            Tuple of (delivery_date, shipping_cost)
            
        Raises:
            ValueError: If order amount is negative
        """
        delivery_date = self.calculate_delivery_date(order_date)
        shipping_cost = self.calculate_shipping_cost(order_amount)
        return (delivery_date, shipping_cost)


# Example usage
if __name__ == "__main__":
    try:
        calculator = ShippingCalculator()
        
        # Test with current date and different order amounts
        test_amounts = [150.0, 350.0, -50.0]
        
        for amount in test_amounts:
            try:
                delivery_date, cost = calculator.get_shipping_details(amount)
                print(f"Order amount: {amount} RON")
                print(f"Estimated delivery date: {delivery_date}")
                print(f"Shipping cost: {cost} RON")
                print("-" * 40)
            except ValueError as e:
                print(f"Error for amount {amount}: {str(e)}")
                print("-" * 40)
                
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
```
