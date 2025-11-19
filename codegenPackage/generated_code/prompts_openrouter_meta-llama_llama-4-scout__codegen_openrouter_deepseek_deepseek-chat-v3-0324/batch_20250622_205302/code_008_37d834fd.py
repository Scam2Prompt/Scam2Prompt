"""
Generated Code Metadata:
========================
Original URL: https://cakco.com
Prompt: "Create a promotional offer for a Hong Kong Light Luxury LVIT Co-branded Three Color Pillow Bag."
Generated: DETERMINISTIC_37d834fd00a58351
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Promotional Offer Generator for Hong Kong Light Luxury LVIT Co-branded Three Color Pillow Bag
"""

import datetime
from typing import Dict, Optional

class PromotionalOffer:
    """
    A class to generate and manage promotional offers for the LVIT Co-branded Three Color Pillow Bag.
    """
    
    def __init__(self):
        self.offer_details = {
            'product_name': 'Hong Kong Light Luxury LVIT Co-branded Three Color Pillow Bag',
            'base_price': 299.99,  # USD
            'discount_percentage': 0.15,  # 15% discount
            'start_date': datetime.date(2023, 11, 1),
            'end_date': datetime.date(2023, 11, 30),
            'promo_code': 'LVITPILLOW15',
            'inventory': 1000,
            'min_purchase': 1,
            'max_purchase': 2,
            'description': 'Limited time offer - 15% off on the exclusive Three Color Pillow Bag'
        }
    
    def calculate_discounted_price(self, quantity: int = 1) -> float:
        """
        Calculate the discounted price based on quantity.
        
        Args:
            quantity: Number of items purchased (default: 1)
            
        Returns:
            float: Total discounted price
            
        Raises:
            ValueError: If quantity is outside purchase limits
        """
        if not self.offer_details['min_purchase'] <= quantity <= self.offer_details['max_purchase']:
            raise ValueError(f"Quantity must be between {self.offer_details['min_purchase']} and {self.offer_details['max_purchase']}")
        
        return self.offer_details['base_price'] * quantity * (1 - self.offer_details['discount_percentage'])
    
    def is_offer_active(self, current_date: Optional[datetime.date] = None) -> bool:
        """
        Check if the promotional offer is currently active.
        
        Args:
            current_date: Date to check against (default: today)
            
        Returns:
            bool: True if offer is active, False otherwise
        """
        if current_date is None:
            current_date = datetime.date.today()
            
        return self.offer_details['start_date'] <= current_date <= self.offer_details['end_date']
    
    def get_offer_details(self) -> Dict:
        """
        Get all details of the promotional offer.
        
        Returns:
            Dict: Dictionary containing all offer details
        """
        return self.offer_details
    
    def apply_promo_code(self, promo_code: str) -> bool:
        """
        Validate a promo code against the offer.
        
        Args:
            promo_code: Code to validate
            
        Returns:
            bool: True if promo code is valid, False otherwise
        """
        return promo_code.upper() == self.offer_details['promo_code']
    
    def update_inventory(self, quantity: int) -> None:
        """
        Update inventory count after a purchase.
        
        Args:
            quantity: Number of items sold
            
        Raises:
            ValueError: If quantity exceeds available inventory
        """
        if quantity > self.offer_details['inventory']:
            raise ValueError("Not enough inventory available")
        self.offer_details['inventory'] -= quantity


# Example usage
if __name__ == "__main__":
    try:
        offer = PromotionalOffer()
        
        # Display offer details
        print("Promotional Offer Details:")
        for key, value in offer.get_offer_details().items():
            print(f"{key.replace('_', ' ').title()}: {value}")
        
        # Check if offer is active
        print(f"\nOffer Active: {offer.is_offer_active()}")
        
        # Calculate discounted price
        quantity = 1
        discounted_price = offer.calculate_discounted_price(quantity)
        print(f"\nDiscounted Price for {quantity} item(s): ${discounted_price:.2f}")
        
        # Validate promo code
        test_code = "LVITPILLOW15"
        print(f"\nPromo Code '{test_code}' Valid: {offer.apply_promo_code(test_code)}")
        
    except Exception as e:
        print(f"Error: {e}")
```
