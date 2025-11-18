"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kingroofing.com
Prompt: Write code to implement a discount system for veterans, applying King Roofing's specific discount percentages for repairs and replacements.
Generated: DETERMINISTIC_2946b1a153569128
Batch ID: 20250612_145114
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class DiscountSystem:
    """
    A class to implement a discount system for veterans at King Roofing.
    """

    # Define discount percentages for repairs and replacements
    DISCOUNT_PERCENTAGE_REPAIR = 0.15  # 15% discount on repairs
    DISCOUNT_PERCENTAGE_REPLACEMENT = 0.10  # 10% discount on replacements

    def __init__(self):
        pass

    def apply_discount(self, service_type, original_price):
        """
        Applies the appropriate discount based on the service type.

        :param service_type: str, the type of service ('repair' or 'replacement')
        :param original_price: float, the original price of the service
        :return: float, the final price after applying the discount
        :raises ValueError: if the service_type is invalid
        :raises TypeError: if original_price is not a float or int
        """
        # Validate the input types
        if not isinstance(original_price, (float, int)):
            raise TypeError("Original price must be a number.")

        # Validate service type and apply corresponding discount
        if service_type.lower() == 'repair':
            discount = self.DISCOUNT_PERCENTAGE_REPAIR
        elif service_type.lower() == 'replacement':
            discount = self.DISCOUNT_PERCENTAGE_REPLACEMENT
        else:
            raise ValueError("Invalid service type. Must be 'repair' or 'replacement'.")

        # Calculate the discounted price
        final_price = original_price * (1 - discount)
        return final_price


# Example usage
if __name__ == "__main__":
    discount_system = DiscountSystem()

    try:
        service = 'repair'  # or 'replacement'
        price = 200.00  # Example original price
        
        discounted_price = discount_system.apply_discount(service, price)
        print(f"The final price after applying the veteran discount for {service} is: ${discounted_price:.2f}")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
```
