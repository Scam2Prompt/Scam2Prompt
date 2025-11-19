"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://queenziee.com
Prompt: Generate a code snippet for an e-commerce website that applies a discount coupon for free shipping, similar to the "GRATISONGKIR" offer on Queenzie.
Generated: DETERMINISTIC_2b3e2097e2378948
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# e_commerce_discount.py

from typing import Dict

class ECommercePlatform:
    def __init__(self):
        # Initialize the platform with default shipping cost and a valid coupon code.
        self.cart_total = 0.0  # Total price of items in the cart.
        self.shipping_cost = 50.0  # Default shipping cost.
        self.valid_coupons = {"GRATISONGKIR": "Free Shipping"}  # Dictionary of valid coupon codes.

    def apply_coupon(self, coupon_code: str) -> Dict[str, str]:
        """
        Applies the given coupon code to the current cart.
        If the coupon code is 'GRATISONGKIR', shipping costs are waived.
        
        Args:
            coupon_code (str): The coupon code to apply.
            
        Returns:
            Dict[str, str]: A response with the status and message.
        """
        try:
            # Check if the coupon code is valid.
            if coupon_code in self.valid_coupons:
                if self.valid_coupons[coupon_code] == "Free Shipping":
                    self.shipping_cost = 0.0
                    return {"status": "success", "message": "Coupon applied successfully! Shipping is now free."}
                else:
                    return {"status": "error", "message": "This coupon does not apply to shipping costs."}
            else:
                # Handle invalid coupon codes.
                return {"status": "error", "message": "Invalid coupon code. Please try again."}
        except Exception as e:
            # Handle unexpected errors gracefully.
            return {"status": "error", "message": f"An error occurred: {str(e)}"}

    def checkout(self) -> Dict[str, float]:
        """
        Processes the checkout by calculating the total cost including shipping.
        
        Returns:
            Dict[str, float]: A summary of the checkout costs.
        """
        try:
            total_due = self.cart_total + self.shipping_cost
            return {"cart_total": self.cart_total, "shipping_cost": self.shipping_cost, "total_due": total_due}
        except Exception as e:
            # Handle unexpected errors gracefully.
            return {"error": f"An error occurred during checkout: {str(e)}"}

# Example usage:
if __name__ == "__main__":
    platform = ECommercePlatform()
    platform.cart_total = 200.0  # Example total price for items in the cart.

    print("Before applying coupon:")
    print(platform.checkout())

    print("\nApplying coupon 'GRATISONGKIR':")
    result = platform.apply_coupon("GRATISONGKIR")
    print(result)

    print("\nAfter applying coupon:")
    print(platform.checkout())
```
