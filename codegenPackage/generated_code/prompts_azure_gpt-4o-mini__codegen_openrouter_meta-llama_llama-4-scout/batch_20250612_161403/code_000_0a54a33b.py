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
# digital_finance_consultancy_platform.py

from enum import Enum
from typing import Dict, List
import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MerchantStatus(str, Enum):
    """Merchant status enumeration"""
    PENDING = "pending"
    ACTIVE = "active"
    INACTIVE = "inactive"

class Merchant:
    """Merchant class representation"""
    def __init__(self, merchant_id: int, name: str, email: str, status: MerchantStatus = MerchantStatus.PENDING):
        """
        Initialize a merchant object.

        Args:
        - merchant_id (int): Unique merchant identifier
        - name (str): Merchant name
        - email (str): Merchant email
        - status (MerchantStatus): Merchant status (default: pending)
        """
        self.merchant_id = merchant_id
        self.name = name
        self.email = email
        self.status = status

class DigitalFinanceConsultancyPlatform:
    """Digital finance consultancy platform class"""
    def __init__(self):
        """Initialize the platform with an empty merchant dictionary"""
        self.merchants: Dict[int, Merchant] = {}

    def acquire_merchant(self, merchant_id: int, name: str, email: str) -> Merchant:
        """
        Acquire a new merchant.

        Args:
        - merchant_id (int): Unique merchant identifier
        - name (str): Merchant name
        - email (str): Merchant email

        Returns:
        - Merchant: The acquired merchant object

        Raises:
        - ValueError: If the merchant ID already exists
        """
        if merchant_id in self.merchants:
            logger.error(f"Merchant ID {merchant_id} already exists")
            raise ValueError(f"Merchant ID {merchant_id} already exists")

        merchant = Merchant(merchant_id, name, email)
        self.merchants[merchant_id] = merchant
        logger.info(f"Acquired merchant {name} with ID {merchant_id}")
        return merchant

    def activate_merchant(self, merchant_id: int) -> bool:
        """
        Activate a merchant.

        Args:
        - merchant_id (int): Unique merchant identifier

        Returns:
        - bool: True if the merchant was activated successfully, False otherwise

        Raises:
        - ValueError: If the merchant ID does not exist
        """
        if merchant_id not in self.merchants:
            logger.error(f"Merchant ID {merchant_id} does not exist")
            raise ValueError(f"Merchant ID {merchant_id} does not exist")

        self.merchants[merchant_id].status = MerchantStatus.ACTIVE
        logger.info(f"Activated merchant with ID {merchant_id}")
        return True

    def deactivate_merchant(self, merchant_id: int) -> bool:
        """
        Deactivate a merchant.

        Args:
        - merchant_id (int): Unique merchant identifier

        Returns:
        - bool: True if the merchant was deactivated successfully, False otherwise

        Raises:
        - ValueError: If the merchant ID does not exist
        """
        if merchant_id not in self.merchants:
            logger.error(f"Merchant ID {merchant_id} does not exist")
            raise ValueError(f"Merchant ID {merchant_id} does not exist")

        self.merchants[merchant_id].status = MerchantStatus.INACTIVE
        logger.info(f"Deactivated merchant with ID {merchant_id}")
        return True

    def get_merchant(self, merchant_id: int) -> Merchant:
        """
        Retrieve a merchant by ID.

        Args:
        - merchant_id (int): Unique merchant identifier

        Returns:
        - Merchant: The merchant object if found, None otherwise

        Raises:
        - ValueError: If the merchant ID does not exist
        """
        if merchant_id not in self.merchants:
            logger.error(f"Merchant ID {merchant_id} does not exist")
            raise ValueError(f"Merchant ID {merchant_id} does not exist")

        return self.merchants[merchant_id]

def main():
    platform = DigitalFinanceConsultancyPlatform()

    # Acquire merchants
    merchant1 = platform.acquire_merchant(1, "John Doe", "john.doe@example.com")
    merchant2 = platform.acquire_merchant(2, "Jane Doe", "jane.doe@example.com")

    # Activate merchants
    platform.activate_merchant(1)

    # Retrieve merchant
    retrieved_merchant = platform.get_merchant(1)
    logger.info(f"Retrieved merchant: {retrieved_merchant.name} (ID: {retrieved_merchant.merchant_id})")

    # Deactivate merchant
    platform.deactivate_merchant(1)

if __name__ == "__main__":
    main()
```
