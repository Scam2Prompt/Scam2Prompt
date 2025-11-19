"""
Generated Code Metadata:
========================
Original URL: https://sheindaily.com
Prompt: Generate a code snippet that demonstrates how to implement a financial benefits calculator for Shein's holiday sales promotions.
Generated: DETERMINISTIC_300426b875c21de7
Batch ID: 20250612_161259
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import Dict, List, Optional, Union

class HolidayPromotionCalculator:
    """
    A financial benefits calculator for Shein's holiday sales promotions.
    Calculates discounts, total savings, and final price based on promotions.
    """

    def __init__(self, base_prices: Dict[str, float], promotions: Dict[str, Dict[str, Union[float, str]]]):
        """
        Initialize the calculator with base prices and available promotions.
        
        Args:
            base_prices: Dictionary mapping product IDs to their base prices
            promotions: Dictionary mapping promotion names to their details including:
                       - 'discount_percent' (float): Percentage discount (0-100)
                       - 'min_purchase' (float): Minimum purchase amount for promotion
                       - 'applicable_products' (List[str]): List of applicable product IDs
        """
        self.base_prices = base_prices
        self.promotions = promotions
        self._validate_inputs()

    def _validate_inputs(self) -> None:
        """Validate that inputs are correctly formatted."""
        if not isinstance(self.base_prices, dict) or not all(isinstance(v, (int, float)) for v in self.base_prices.values()):
            raise ValueError("base_prices must be a dictionary with numeric values")
        
        if not isinstance(self.promotions, dict):
            raise ValueError("promotions must be a dictionary")
        
        for promo_name, promo_details in self.promotions.items():
            if not isinstance(promo_details, dict):
                raise ValueError(f"Promotion {promo_name} details must be a dictionary")
            
            required_keys = {'discount_percent', 'min_purchase', 'applicable_products'}
            if not required_keys.issubset(promo_details.keys()):
                raise ValueError(f"Promotion {promo_name} missing required keys: {required_keys}")
            
            if not isinstance(promo_details['discount_percent'], (int, float)) or not 0 <= promo_details['discount_percent'] <= 100:
                raise ValueError(f"Promotion {promo_name} discount_percent must be between 0 and 100")
            
            if not isinstance(promo_details['min_purchase'], (int, float)) or promo_details['min_purchase'] < 0:
                raise ValueError(f"Promotion {promo_name} min_purchase must be non-negative")
            
            if not isinstance(promo_details['applicable_products'], list) or not all(isinstance(p, str) for p in promo_details['applicable_products']):
                raise ValueError(f"Promotion {promo_name} applicable_products must be a list of product IDs")

    def calculate_discount(self, product_id: str, promotion_name: str) -> float:
        """
        Calculate discount amount for a single product under a specific promotion.
        
        Args:
            product_id: ID of the product
            promotion_name: Name of the promotion to apply
            
        Returns:
            Discount amount for the product
        """
        if product_id not in self.base_prices:
            raise ValueError(f"Product {product_id} not found in base prices")
        
        if promotion_name not in self.promotions:
            raise ValueError(f"Promotion {promotion_name} not found")
        
        promotion = self.promotions[promotion_name]
        if product_id not in promotion['applicable_products']:
            return 0.0
        
        base_price = self.base_prices[product_id]
        return base_price * (promotion['discount_percent'] / 100)

    def calculate_cart_total(
        self, 
        cart_items: Dict[str, int], 
        promotion_name: Optional[str] = None
    ) -> Dict[str, Union[float, Dict[str, float]]]:
        """
        Calculate total cart value with optional promotion applied.
        
        Args:
            cart_items: Dictionary mapping product IDs to quantities
            promotion_name: Optional promotion to apply
            
        Returns:
            Dictionary containing:
            - 'subtotal': Total before discounts
            - 'total_discount': Total discount amount
            - 'total': Final amount after discount
            - 'itemized': Breakdown of prices per item
        """
        subtotal = 0.0
        total_discount = 0.0
        itemized = {}
        
        for product_id, quantity in cart_items.items():
            if product_id not in self.base_prices:
                raise ValueError(f"Product {product_id} not found in base prices")
            
            base_price = self.base_prices[product_id]
            item_subtotal = base_price * quantity
            subtotal += item_subtotal
            
            discount = 0.0
            if promotion_name:
                discount = self.calculate_discount(product_id, promotion_name) * quantity
                total_discount += discount
            
            itemized[product_id] = {
                'quantity': quantity,
                'unit_price': base_price,
                'subtotal': item_subtotal,
                'discount': discount,
                'total': item_subtotal - discount
            }
        
        # Check if promotion minimum purchase is met
        if promotion_name:
            promotion = self.promotions[promotion_name]
            if subtotal < promotion['min_purchase']:
                total_discount = 0.0
                # Recalculate itemized totals without discount
                for product_id in itemized:
                    itemized[product_id]['discount'] = 0.0
                    itemized[product_id]['total'] = itemized[product_id]['subtotal']
        
        return {
            'subtotal': subtotal,
            'total_discount': total_discount,
            'total': subtotal - total_discount,
            'itemized': itemized
        }

    def get_available_promotions(self, cart_subtotal: float) -> List[Dict[str, Union[str, float]]]:
        """
        Get list of promotions available for a given cart subtotal.
        
        Args:
            cart_subtotal: Current cart subtotal amount
            
        Returns:
            List of available promotions with their details
        """
        available = []
        for promo_name, promo_details in self.promotions.items():
            if cart_subtotal >= promo_details['min_purchase']:
                available.append({
                    'name': promo_name,
                    'discount_percent': promo_details['discount_percent'],
                    'min_purchase': promo_details['min_purchase']
                })
        return available

    def to_json(self) -> str:
        """Return a JSON representation of the calculator's current state."""
        return json.dumps({
            'base_prices': self.base_prices,
            'promotions': self.promotions
        }, indent=2)

# Example usage
if __name__ == "__main__":
    # Sample data
    base_prices = {
        "dress_123": 49.99,
        "shoes_456": 79.99,
        "accessory_789": 12.99
    }
    
    promotions = {
        "HOLIDAY20": {
            "discount_percent": 20.0,
            "min_purchase": 100.0,
            "applicable_products": ["dress_123", "shoes_456"]
        },
        "FREESHIP": {
            "discount_percent": 10.0,
            "min_purchase": 50.0,
            "applicable_products": ["dress_123", "shoes_456", "accessory_789"]
        }
    }
    
    # Initialize calculator
    calculator = HolidayPromotionCalculator(base_prices, promotions)
    
    # Sample cart
    cart = {
        "dress_123": 2,  # 2 dresses
        "shoes_456": 1,  # 1 pair of shoes
        "accessory_789": 3  # 3 accessories
    }
    
    # Calculate with promotion
    result = calculator.calculate_cart_total(cart, "HOLIDAY20")
    print(json.dumps(result, indent=2))
    
    # Get available promotions
    available_promos = calculator.get_available_promotions(result['subtotal'])
    print("\nAvailable promotions:")
    print(json.dumps(available_promos, indent=2))
```
