"""
Generated Code Metadata:
========================
Original URL: https://paradigmgroup.co.ug
Prompt: Generate a code snippet for a digital finance consultancy platform that includes features for merchant acquisition and activation, as described by Paradigm Group.
Generated: DETERMINISTIC_0a54a33b7245f9ed
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Digital Finance Consultancy Platform - Merchant Acquisition and Activation
Author: Paradigm Group
Description: This script provides functionality for merchant acquisition and activation.
"""

import logging
from typing import List, Dict

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Merchant:
    """
    Represents a merchant in the platform.
    """
    def __init__(self, merchant_id: str, name: str, email: str, activated: bool = False):
        """
        Initialize a Merchant instance.

        :param merchant_id: Unique identifier for the merchant
        :param name: Name of the merchant
        :param email: Email address of the merchant
        :param activated: Activation status of the merchant (default: False)
        """
        self.merchant_id = merchant_id
        self.name = name
        self.email = email
        self.activated = activated

    def activate(self):
        """
        Activate the merchant.
        """
        if not self.activated:
            self.activated = True
            logging.info(f"Merchant {self.merchant_id} ({self.name}) activated successfully.")
        else:
            logging.warning(f"Merchant {self.merchant_id} ({self.name}) is already activated.")

    def __repr__(self):
        """
        String representation of the Merchant instance.
        """
        return f"Merchant(merchant_id={self.merchant_id}, name={self.name}, email={self.email}, activated={self.activated})"


class MerchantPlatform:
    """
    Represents the digital finance consultancy platform for managing merchants.
    """
    def __init__(self):
        """
        Initialize the MerchantPlatform instance.
        """
        self.merchants: Dict[str, Merchant] = {}

    def add_merchant(self, merchant_id: str, name: str, email: str):
        """
        Add a new merchant to the platform.

        :param merchant_id: Unique identifier for the merchant
        :param name: Name of the merchant
        :param email: Email address of the merchant
        """
        if merchant_id in self.merchants:
            logging.error(f"Merchant with ID {merchant_id} already exists.")
            raise ValueError(f"Merchant with ID {merchant_id} already exists.")
        
        new_merchant = Merchant(merchant_id, name, email)
        self.merchants[merchant_id] = new_merchant
        logging.info(f"Merchant {merchant_id} ({name}) added successfully.")

    def activate_merchant(self, merchant_id: str):
        """
        Activate a merchant by their ID.

        :param merchant_id: Unique identifier for the merchant
        """
        merchant = self.merchants.get(merchant_id)
        if not merchant:
            logging.error(f"Merchant with ID {merchant_id} not found.")
            raise ValueError(f"Merchant with ID {merchant_id} not found.")
        
        merchant.activate()

    def list_merchants(self) -> List[Merchant]:
        """
        List all merchants in the platform.

        :return: List of Merchant instances
        """
        return list(self.merchants.values())


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the platform
        platform = MerchantPlatform()

        # Add merchants
        platform.add_merchant("M001", "Merchant One", "merchant1@example.com")
        platform.add_merchant("M002", "Merchant Two", "merchant2@example.com")

        # Activate a merchant
        platform.activate_merchant("M001")

        # List all merchants
        merchants = platform.list_merchants()
        for merchant in merchants:
            print(merchant)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
