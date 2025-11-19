"""
Generated Code Metadata:
========================
Original URL: https://connectnetwork.lojavirtualnuvem.com.br
Prompt: Generate a code snippet to implement a discount system for products in a Lojavirtualnuvem store, similar to the 20% OFF and 35% OFF promotions shown on the webpage.
Generated: DETERMINISTIC_36eec794b21eee82
Batch ID: 20250622_205849
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
    A class to manage product discounts in an e-commerce store.
    Supports applying percentage-based discounts to products.
    """
    
    def __init__(self):
        self.discounts = {}  # {product_id: discount_percentage}
    
    def add_discount(self, product_id: str, discount_percentage: float) -> None:
        """
        Add a discount to a product.
        
        Args:
            product_id: Unique identifier for the product
            discount_percentage: Discount percentage (e.g., 20 for 20% off)
            
        Raises:
            ValueError: If discount_percentage is invalid
        """
        if not 0 <= discount_percentage <= 100:
            raise ValueError("Discount percentage must be between 0 and 100")
        self.discounts[product_id] = discount_percentage
    
    def remove_discount(self, product_id: str) -> None:
        """
        Remove discount from a product.
        
        Args:
            product_id: Unique identifier for the product
        """
        self.discounts.pop(product_id, None)
    
    def apply_discount(self, product_id: str, original_price: float) -> float:
        """
        Apply discount to a product's price.
        
        Args:
            product_id: Unique identifier for the product
            original_price: Original price of the product
            
        Returns:
            Final price after discount
            
        Raises:
            KeyError: If product has no discount
        """
        if product_id not in self.discounts:
            raise KeyError(f"No discount found for product {product_id}")
            
        discount = self.discounts[product_id]
        return original_price * (1 - discount / 100)
    
    def get_discount(self, product_id: str) -> float:
        """
        Get discount percentage for a product.
        
        Args:
            product_id: Unique identifier for the product
            
        Returns:
            Discount percentage (0 if no discount exists)
        """
        return self.discounts.get(product_id, 0)


# Example usage
if __name__ == "__main__":
    discount_system = DiscountSystem()
    
    # Add discounts
    discount_system.add_discount("prod001", 20)  # 20% off
    discount_system.add_discount("prod002", 35)  # 35% off
    
    # Apply discounts
    try:
        price_after_discount = discount_system.apply_discount("prod001", 100.0)
        print(f"Price after discount: ${price_after_discount:.2f}")
        
        # Try to apply discount to product without discount
        discount_system.apply_discount("prod003", 50.0)
    except KeyError as e:
        print(f"Error: {e}")
```
