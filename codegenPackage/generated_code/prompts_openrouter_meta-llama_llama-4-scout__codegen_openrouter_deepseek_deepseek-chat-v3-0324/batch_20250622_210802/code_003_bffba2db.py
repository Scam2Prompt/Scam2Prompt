"""
Generated Code Metadata:
========================
Original URL: https://trykart.in
Prompt: Write a code snippet in a programming language of your choice to implement a discount system, similar to Trykart's "Flat 5% Off" or "SAVE UPTO 10%" on certain products.
Generated: DETERMINISTIC_bffba2dbc165b7fa
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class DiscountSystem:
    """
    A class to manage product discounts with different discount types.
    Supports flat percentage discounts and tiered discounts (save up to X%).
    """
    
    def __init__(self):
        self.product_discounts = {}  # {product_id: {'type': str, 'value': float}}
    
    def add_discount(self, product_id: str, discount_type: str, discount_value: float) -> None:
        """
        Add a discount to a product.
        
        Args:
            product_id: Unique identifier for the product
            discount_type: Either 'flat' or 'tiered'
            discount_value: Percentage value (e.g., 5 for 5%)
            
        Raises:
            ValueError: If discount_type is invalid or discount_value is negative
        """
        if discount_type not in ['flat', 'tiered']:
            raise ValueError("Discount type must be either 'flat' or 'tiered'")
        if discount_value < 0:
            raise ValueError("Discount value cannot be negative")
            
        self.product_discounts[product_id] = {
            'type': discount_type,
            'value': discount_value
        }
    
    def remove_discount(self, product_id: str) -> None:
        """Remove discount from a product."""
        if product_id in self.product_discounts:
            del self.product_discounts[product_id]
    
    def calculate_discounted_price(self, product_id: str, original_price: float) -> float:
        """
        Calculate the discounted price for a product.
        
        Args:
            product_id: Product to calculate discount for
            original_price: Original price of the product
            
        Returns:
            Discounted price (original price if no discount exists)
            
        Raises:
            ValueError: If original_price is negative
        """
        if original_price < 0:
            raise ValueError("Price cannot be negative")
            
        if product_id not in self.product_discounts:
            return original_price
            
        discount = self.product_discounts[product_id]
        
        if discount['type'] == 'flat':
            return original_price * (1 - discount['value'] / 100)
        elif discount['type'] == 'tiered':
            # For tiered discounts, we apply the maximum possible discount
            return original_price * (1 - discount['value'] / 100)
        
        return original_price

# Example usage
if __name__ == "__main__":
    discount_system = DiscountSystem()
    
    # Add discounts
    discount_system.add_discount("P1001", "flat", 5)    # Flat 5% off
    discount_system.add_discount("P2002", "tiered", 10) # Save up to 10%
    
    # Calculate prices
    price1 = discount_system.calculate_discounted_price("P1001", 100.0)
    price2 = discount_system.calculate_discounted_price("P2002", 200.0)
    price3 = discount_system.calculate_discounted_price("P3003", 300.0) # No discount
    
    print(f"Discounted prices: {price1}, {price2}, {price3}")
```
