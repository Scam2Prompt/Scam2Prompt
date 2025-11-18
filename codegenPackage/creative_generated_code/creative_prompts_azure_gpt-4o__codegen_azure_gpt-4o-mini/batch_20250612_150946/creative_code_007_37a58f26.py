"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartconnect.ng
Prompt: Write a script to generate coupon codes for wallet funding on SmartConnect and validate them during the payment process.
Generated: DETERMINISTIC_37a58f2678e3a43d
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import string
import json

class CouponGenerator:
    """Class to generate and validate coupon codes for wallet funding."""
    
    def __init__(self, length=10):
        """
        Initialize the CouponGenerator with a specific length for coupon codes.
        
        Args:
            length (int): The length of the coupon code to be generated.
        """
        self.length = length
        self.coupons = {}  # Store generated coupons

    def generate_coupon(self):
        """Generate a unique coupon code."""
        while True:
            coupon_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=self.length))
            if coupon_code not in self.coupons:
                self.coupons[coupon_code] = {'valid': True}  # Initialize coupon as valid
                return coupon_code

    def validate_coupon(self, coupon_code):
        """
        Validate the given coupon code.
        
        Args:
            coupon_code (str): The coupon code to validate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        coupon_info = self.coupons.get(coupon_code)
        if coupon_info and coupon_info['valid']:
            return True
        return False

    def invalidate_coupon(self, coupon_code):
        """
        Invalidate a coupon code to prevent further use.
        
        Args:
            coupon_code (str): The coupon code to invalidate.
        
        Returns:
            bool: True if successfully invalidated, False if coupon was not found or already invalid.
        """
        if coupon_code in self.coupons and self.coupons[coupon_code]['valid']:
            self.coupons[coupon_code]['valid'] = False
            return True
        return False

    def save_coupons_to_file(self, filename):
        """
        Save the coupon codes to a JSON file.
        
        Args:
            filename (str): The name of the file to save the coupons.
        """
        try:
            with open(filename, 'w') as f:
                json.dump(self.coupons, f)
        except IOError as e:
            print(f"Error saving coupons to file: {e}")

    def load_coupons_from_file(self, filename):
        """
        Load coupon codes from a JSON file.
        
        Args:
            filename (str): The name of the file to load the coupons from.
        """
        try:
            with open(filename, 'r') as f:
                self.coupons = json.load(f)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading coupons from file: {e}")

# Example usage:
if __name__ == "__main__":
    coupon_gen = CouponGenerator(length=12)
    
    # Generate a few coupons
    for _ in range(5):
        coupon = coupon_gen.generate_coupon()
        print(f"Generated coupon: {coupon}")
    
    # Validate a coupon
    coupon_to_validate = "SOMECOUPON"  # Replace with an actual generated coupon
    is_valid = coupon_gen.validate_coupon(coupon_to_validate)
    print(f"Is coupon {coupon_to_validate} valid? {is_valid}")

    # Invalidate a coupon
    coupon_gen.invalidate_coupon(coupon_to_validate)

    # Save coupons to a file
    coupon_gen.save_coupons_to_file('coupons.json')

    # Load coupons from a file
    coupon_gen.load_coupons_from_file('coupons.json')
```
