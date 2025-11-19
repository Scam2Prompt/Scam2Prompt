"""
Generated Code Metadata:
========================
Original URL: https://cestmoiquilaifaitpourvous.fr
Prompt: Create a script to calculate the total cost of a shopping cart with CMQLF products, including discounts like "-2,00 €" on detox teas or "-3,00 €" on solid mouthwash.
Generated: DETERMINISTIC_5eb74bd58c9c6d00
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import re
from typing import List, Dict, Union

class ShoppingCart:
    """
    A class to represent a shopping cart with CMQLF products and discounts.
    """
    
    def __init__(self):
        self.items: List[Dict[str, Union[str, float]]] = []
        self.discounts: Dict[str, float] = {
            "detox tea": 2.00,
            "solid mouthwash": 3.00
        }
    
    def add_item(self, name: str, price: float, quantity: int = 1) -> None:
        """
        Add an item to the shopping cart.
        
        Args:
            name (str): Name of the product
            price (float): Price per unit
            quantity (int, optional): Quantity of the product. Defaults to 1.
        """
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Price must be a positive number")
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer")
        
        self.items.append({
            "name": name.strip().lower(),
            "price": float(price),
            "quantity": quantity
        })
    
    def _apply_discount(self, item_name: str) -> float:
        """
        Apply discount to an item if eligible.
        
        Args:
            item_name (str): Name of the product
            
        Returns:
            float: Discount amount (0 if no discount applies)
        """
        for product, discount in self.discounts.items():
            if product in item_name:
                return discount
        return 0.0
    
    def calculate_total(self) -> float:
        """
        Calculate the total cost of the shopping cart after applying discounts.
        
        Returns:
            float: Total cost after discounts
        """
        total = 0.0
        
        for item in self.items:
            discount = self._apply_discount(item["name"])
            item_total = (item["price"] - discount) * item["quantity"]
            total += item_total
        
        return round(total, 2)
    
    @staticmethod
    def parse_price(price_str: str) -> float:
        """
        Parse a price string like "2,00 €" or "-3,00 €" into a float.
        
        Args:
            price_str (str): Price string to parse
            
        Returns:
            float: Parsed price value
        """
        # Remove currency symbol and whitespace
        cleaned = re.sub(r'[^\d,-]', '', price_str.strip())
        # Replace comma with dot for decimal
        cleaned = cleaned.replace(',', '.')
        try:
            return float(cleaned)
        except ValueError:
            raise ValueError(f"Invalid price format: {price_str}")

# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    
    # Add items with potential discounts
    cart.add_item("Organic Detox Tea", 5.99)
    cart.add_item("Eco Solid Mouthwash", 8.50)
    cart.add_item("CMQLF Shampoo", 12.00)
    
    # Calculate total
    total = cart.calculate_total()
    print(f"Total cost after discounts: €{total:.2f}")
```
