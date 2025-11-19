"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paradigmgroup.co.ug
Prompt: Generate a code snippet for a digital finance consultancy platform that includes features for merchant acquisition and activation, as described by Paradigm Group.
Generated: DETERMINISTIC_0a54a33b7245f9ed
Batch ID: 20250612_161403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# digital_finance_consultancy.py

import logging
from typing import List, Dict

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")


class Merchant:
    """
    Represents a merchant within the digital finance consultancy platform.
    """

    def __init__(self, merchant_id: int, name: str, email: str):
        """
        Initialize a merchant with the given details.
        """
        self.merchant_id = merchant_id
        self.name = name
        self.email = email
        self.is_active = False  # Activation status

    def activate(self) -> None:
        """
        Activates the merchant account.
        """
        self.is_active = True
        logging.info(f"Merchant {self.name} (ID: {self.merchant_id}) activated successfully.")


class MerchantAcquisition:
    """
    Handles merchant acquisition and activation processes.
    """

    def __init__(self):
        """
        Initialize the MerchantAcquisition system with an empty merchant list.
        """
        self.merchants: Dict[int, Merchant] = {}  # Store merchants by ID

    def add_merchant(self, merchant_id: int, name: str, email: str) -> None:
        """
        Adds a new merchant to the system.

        Args:
            merchant_id (int): Unique identifier for the merchant.
            name (str): Name of the merchant.
            email (str): Email address of the merchant.
        """
        if merchant_id in self.merchants:
            logging.error(f"Merchant ID {merchant_id} already exists. Cannot add duplicate.")
            raise ValueError(f"Merchant ID {merchant_id} already exists.")

        new_merchant = Merchant(merchant_id, name, email)
        self.merchants[merchant_id] = new_merchant
        logging.info(f"Merchant {name} (ID: {merchant_id}) added successfully.")

    def activate_merchant(self, merchant_id: int) -> None:
        """
        Activates a merchant in the system.

        Args:
            merchant_id (int): Unique identifier for the merchant.
        """
        merchant = self.merchants.get(merchant_id)
        if not merchant:
            logging.error(f"Merchant ID {merchant_id} not found. Activation failed.")
            raise ValueError(f"Merchant ID {merchant_id} not found.")

        merchant.activate()


# Example usage of the MerchantAcquisition class

if __name__ == "__main__":
    try:
        # Initialize the merchant acquisition system
        acquisition_system = MerchantAcquisition()

        # Add merchants
        acquisition_system.add_merchant(merchant_id=1, name="Merchant One", email="merchant1@example.com")
        acquisition_system.add_merchant(merchant_id=2, name="Merchant Two", email="merchant2@example.com")

        # Activate a merchant
        acquisition_system.activate_merchant(merchant_id=1)
        acquisition_system.activate_merchant(merchant_id=3)  # This will raise an error
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```

This code snippet is a complete implementation of a merchant acquisition and activation system for a digital finance consultancy platform. It includes error handling, logging, clean code structure, and follows Python best practices.
