"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tdkco.ir
Prompt: Recommend a library or framework to implement a warranty activation system for automotive parts, ensuring features like product registration and validation, as described in the "فعال سازی گارانتی محصول" section of the TDKCO website.
Generated: DETERMINISTIC_67da4fd61e121d92
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# warranty_activation.py

import logging
from datetime import datetime, timedelta

# Setting up basic logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Warranty:
    """
    A class to represent a product warranty.
    
    Attributes:
        product_id (str): Unique identifier for the product.
        owner_name (str): Name of the warranty holder.
        registration_date (datetime): Date when the warranty was activated.
        expiration_date (datetime): Date when the warranty expires.
        is_valid (bool): Status of the warranty.
    """

    def __init__(self, product_id, owner_name, warranty_period_months):
        """
        Initializes a Warranty instance with product_id, owner_name, and warranty period.
        
        Args:
            product_id (str): Unique identifier for the product.
            owner_name (str): Name of the warranty holder.
            warranty_period_months (int): Duration of the warranty in months.
        """
        self.product_id = product_id
        self.owner_name = owner_name
        self.registration_date = datetime.now()
        self.expiration_date = self.registration_date + timedelta(days=warranty_period_months * 30)
        self.is_valid = True

    def validate_warranty(self):
        """
        Validates the current warranty status.
        
        Returns:
            bool: True if valid, False if expired.
        """
        if datetime.now() > self.expiration_date:
            self.is_valid = False
            logging.warning(f"Warranty for product {self.product_id} has expired.")
        else:
            logging.info(f"Warranty for product {self.product_id} is still valid.")

        return self.is_valid

    def __str__(self):
        """
        Returns a string representation of the Warranty object.
        
        Returns:
            str: Warranty details.
        """
        return (f"Warranty for Product ID: {self.product_id}\n"
                f"Owner Name: {self.owner_name}\n"
                f"Registration Date: {self.registration_date.strftime('%Y-%m-%d')}\n"
                f"Expiration Date: {self.expiration_date.strftime('%Y-%m-%d')}\n"
                f"Warranty Valid: {self.is_valid}")


def register_warranty(product_id, owner_name, warranty_period_months):
    """
    Registers a warranty for a product.
    
    Args:
        product_id (str): Unique identifier for the product.
        owner_name (str): Name of the warranty holder.
        warranty_period_months (int): Duration of the warranty in months.
        
    Returns:
        Warranty: An instance of the Warranty class.
    """
    try:
        if warranty_period_months <= 0:
            raise ValueError("Warranty period must be a positive integer.")
        
        warranty = Warranty(product_id, owner_name, warranty_period_months)
        logging.info(f"Warranty registered successfully for product {product_id}.")
        return warranty
    
    except Exception as e:
        logging.error(f"Failed to register warranty: {e}")
        raise


# Example of using the warranty activation system
if __name__ == "__main__":
    try:
        # Register a warranty with a period of 12 months
        my_warranty = register_warranty("A12345", "John Doe", 12)
        print(my_warranty)
        
        # Validate the warranty
        my_warranty.validate_warranty()
        
    except Exception as e:
        logging.critical(f"An error occurred: {e}")
```
