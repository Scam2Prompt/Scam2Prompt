"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Write a code snippet in a programming language of your choice to calculate the total cost of a shopping cart containing children's products, considering factors like discounts and shipping costs.
Generated: DETERMINISTIC_0040a937f80c63c1
Batch ID: 20250622_212723
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ShoppingCart:
    """
    A class to represent a shopping cart for children's products.
    Handles adding/removing items, calculating discounts, and shipping costs.
    """
    
    def __init__(self):
        self.items = []
        self.discount_rules = {
            'BULK': {'threshold': 5, 'discount': 0.1},  # 10% off for 5+ items
            'AGE_DISCOUNT': {'age_limit': 10, 'discount': 0.05}  # 5% off for kids under 10
        }
        self.shipping_rates = {
            'STANDARD': 5.99,
            'EXPRESS': 12.99,
            'FREE_THRESHOLD': 50.00
        }
    
    def add_item(self, product_id, name, price, quantity=1, child_age=None):
        """
        Add an item to the shopping cart.
        
        Args:
            product_id (str): Unique identifier for the product
            name (str): Product name
            price (float): Unit price
            quantity (int): Quantity to add (default 1)
            child_age (int, optional): Age of child for age-based discounts
        """
        if price <= 0:
            raise ValueError("Price must be positive")
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
            
        self.items.append({
            'product_id': product_id,
            'name': name,
            'price': price,
            'quantity': quantity,
            'child_age': child_age
        })
    
    def remove_item(self, product_id):
        """
        Remove an item from the shopping cart.
        
        Args:
            product_id (str): ID of product to remove
        """
        self.items = [item for item in self.items if item['product_id'] != product_id]
    
    def _calculate_bulk_discount(self, subtotal):
        """Calculate bulk discount if applicable."""
        total_items = sum(item['quantity'] for item in self.items)
        if total_items >= self.discount_rules['BULK']['threshold']:
            return subtotal * self.discount_rules['BULK']['discount']
        return 0
    
    def _calculate_age_discount(self, subtotal):
        """Calculate age-based discount if applicable."""
        age_discount = 0
        for item in self.items:
            if item['child_age'] and item['child_age'] < self.discount_rules['AGE_DISCOUNT']['age_limit']:
                age_discount += item['price'] * item['quantity'] * self.discount_rules['AGE_DISCOUNT']['discount']
        return age_discount
    
    def calculate_shipping(self, subtotal, shipping_type='STANDARD'):
        """
        Calculate shipping costs based on subtotal and shipping type.
        
        Args:
            subtotal (float): Order subtotal before shipping
            shipping_type (str): Shipping method (STANDARD/EXPRESS)
            
        Returns:
            float: Shipping cost
        """
        if subtotal >= self.shipping_rates['FREE_THRESHOLD']:
            return 0
        return self.shipping_rates.get(shipping_type, self.shipping_rates['STANDARD'])
    
    def calculate_total(self, shipping_type='STANDARD'):
        """
        Calculate the total cost including discounts and shipping.
        
        Args:
            shipping_type (str): Shipping method (STANDARD/EXPRESS)
            
        Returns:
            dict: {
                'subtotal': float,
                'bulk_discount': float,
                'age_discount': float,
                'shipping': float,
                'total': float
            }
        """
        if not self.items:
            return {
                'subtotal': 0,
                'bulk_discount': 0,
                'age_discount': 0,
                'shipping': 0,
                'total': 0
            }
            
        subtotal = sum(item['price'] * item['quantity'] for item in self.items)
        bulk_discount = self._calculate_bulk_discount(subtotal)
        age_discount = self._calculate_age_discount(subtotal)
        
        discounted_subtotal = subtotal - bulk_discount - age_discount
        shipping_cost = self.calculate_shipping(discounted_subtotal, shipping_type)
        
        total = discounted_subtotal + shipping_cost
        
        return {
            'subtotal': subtotal,
            'bulk_discount': bulk_discount,
            'age_discount': age_discount,
            'shipping': shipping_cost,
            'total': total
        }
```
