"""
Generated Code Metadata:
========================
Original URL: https://www-elt-gala-app-games.blogspot.com
Prompt: Generate code to calculate the shipping cost for an order of electronic components, considering free shipping rules and conditions.
Generated: DETERMINISTIC_d6369433967d5251
Batch ID: 20250622_212609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ShippingCalculator:
    """
    Calculates shipping costs for electronic components orders based on predefined rules.
    Supports free shipping conditions based on order value and customer status.
    """
    
    def __init__(self, base_shipping_cost: float = 5.99, free_shipping_threshold: float = 100.0):
        """
        Initialize shipping calculator with configurable parameters.
        
        Args:
            base_shipping_cost: Default shipping cost for orders below threshold
            free_shipping_threshold: Minimum order value to qualify for free shipping
        """
        self.base_shipping_cost = base_shipping_cost
        self.free_shipping_threshold = free_shipping_threshold
    
    def calculate_shipping(
        self,
        order_value: float,
        is_premium_customer: bool = False,
        is_international: bool = False,
        international_surcharge: float = 15.0
    ) -> float:
        """
        Calculate shipping cost based on order parameters.
        
        Args:
            order_value: Total value of the order
            is_premium_customer: Whether customer has premium status
            is_international: Whether shipping is international
            international_surcharge: Additional cost for international shipping
            
        Returns:
            Calculated shipping cost
            
        Raises:
            ValueError: If order_value is negative
        """
        if order_value < 0:
            raise ValueError("Order value cannot be negative")
        
        # Premium customers always get free shipping
        if is_premium_customer:
            return 0.0
            
        # Free shipping for domestic orders above threshold
        if not is_international and order_value >= self.free_shipping_threshold:
            return 0.0
            
        shipping_cost = self.base_shipping_cost
        
        # Add international surcharge if applicable
        if is_international:
            shipping_cost += international_surcharge
            
        return shipping_cost


# Example usage
if __name__ == "__main__":
    calculator = ShippingCalculator()
    
    try:
        # Domestic order below threshold
        cost = calculator.calculate_shipping(50.0)
        print(f"Shipping cost: ${cost:.2f}")
        
        # Domestic order above threshold
        cost = calculator.calculate_shipping(150.0)
        print(f"Shipping cost: ${cost:.2f}")
        
        # International order
        cost = calculator.calculate_shipping(50.0, is_international=True)
        print(f"Shipping cost: ${cost:.2f}")
        
        # Premium customer
        cost = calculator.calculate_shipping(50.0, is_premium_customer=True)
        print(f"Shipping cost: ${cost:.2f}")
        
        # Invalid order value
        cost = calculator.calculate_shipping(-10.0)
    except ValueError as e:
        print(f"Error calculating shipping: {e}")
```
