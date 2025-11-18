"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://foolz.sellpass.io
Prompt: Write code to automate the generation of promo codes and coupons for a Sellpass storefront, ensuring exclusive pricing for specific customer groups.
Generated: DETERMINISTIC_1f00c67d073cb438
Batch ID: 20250612_151429
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import uuid
from datetime import datetime, timedelta

class PromoCodeGenerator:
    def __init__(self):
        self.promo_codes = {}

    def generate_promo_code(self, discount_percentage: float, expiration_days: int, customer_group: str) -> str:
        """
        Generate a unique promo code.

        Parameters:
        discount_percentage (float): The discount percentage for the promo code.
        expiration_days (int): The number of days until the promo code expires.
        customer_group (str): The customer group that can use this promo code.

        Returns:
        str: A unique promo code.
        """
        # Validate inputs
        if not (0 < discount_percentage <= 100):
            raise ValueError("Discount percentage must be between 0 and 100.")
        if expiration_days <= 0:
            raise ValueError("Expiration days must be greater than 0.")
        if not customer_group:
            raise ValueError("Customer group cannot be empty.")

        promo_code = str(uuid.uuid4()).split('-')[0]  # Generate a short unique code
        expiration_date = datetime.now() + timedelta(days=expiration_days)

        # Store the promo code with its details
        self.promo_codes[promo_code] = {
            'discount_percentage': discount_percentage,
            'expiration_date': expiration_date,
            'customer_group': customer_group
        }
        return promo_code

    def validate_promo_code(self, promo_code: str, customer_group: str) -> bool:
        """
        Validate a promo code to check if it is still valid and belongs to the customer group.

        Parameters:
        promo_code (str): The promo code to validate.
        customer_group (str): The customer group making the request.

        Returns:
        bool: True if the promo code is valid, False otherwise.
        """
        # Check if the promo code exists
        if promo_code not in self.promo_codes:
            return False

        promo_details = self.promo_codes[promo_code]
        
        # Check if the promo code is expired
        if datetime.now() > promo_details['expiration_date']:
            return False
        
        # Check if the customer group is eligible
        if promo_details['customer_group'] != customer_group:
            return False

        return True

    def get_discount(self, promo_code: str) -> float:
        """
        Retrieve the discount percentage associated with a promo code.

        Parameters:
        promo_code (str): The promo code to retrieve the discount for.

        Returns:
        float: The discount percentage, or raises an error if the promo code is invalid.
        """
        if promo_code not in self.promo_codes:
            raise ValueError("Invalid promo code.")
        
        return self.promo_codes[promo_code]['discount_percentage']

# Example usage
if __name__ == "__main__":
    generator = PromoCodeGenerator()
    
    try:
        promo_code = generator.generate_promo_code(15, 30, "VIP_Customers")
        print(f"Generated Promo Code: {promo_code}")

        # Validate the promo code
        is_valid = generator.validate_promo_code(promo_code, "VIP_Customers")
        print(f"Is the promo code valid? {'Yes' if is_valid else 'No'}")

        # Get the discount for the promo code
        discount = generator.get_discount(promo_code)
        print(f"Discount for promo code {promo_code}: {discount}%")
        
    except ValueError as e:
        print(f"Error: {e}")
```
