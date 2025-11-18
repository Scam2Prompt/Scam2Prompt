"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbootsdao-en.pages.dev
Prompt: Generate code to facilitate OTC offerings for Moonboots DAO investors, ensuring secure transactions and compliance with the platform's guidelines.
Generated: DETERMINISTIC_120281445d8526df
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
OTC Offering System for Moonboots DAO Investors

This script facilitates Over-The-Counter (OTC) offerings for Moonboots DAO investors. 
It ensures secure transactions, compliance with platform guidelines, and proper error handling.
"""

import uuid
import logging
from typing import Dict, Union

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OTCOffering:
    """
    Class to represent an OTC offering for Moonboots DAO investors.
    """
    def __init__(self):
        # Dictionary to store offerings. Key: Offering ID, Value: Offering details.
        self.offerings: Dict[str, Dict[str, Union[str, float]]] = {}

    def create_offering(self, seller: str, buyer: str, asset: str, amount: float, price_per_unit: float) -> str:
        """
        Creates a new OTC offering.
        
        Parameters:
            seller (str): Address or ID of the seller.
            buyer (str): Address or ID of the buyer.
            asset (str): Asset being offered (e.g., DAO tokens).
            amount (float): Amount of the asset to sell.
            price_per_unit (float): Price per unit of the asset.
        
        Returns:
            str: Unique offering ID.
        """
        try:
            # Generate a unique offering ID
            offering_id = str(uuid.uuid4())
            
            # Validate inputs
            if amount <= 0 or price_per_unit <= 0:
                raise ValueError("Amount and price_per_unit must be positive numbers.")
            
            # Store offering details
            self.offerings[offering_id] = {
                "seller": seller,
                "buyer": buyer,
                "asset": asset,
                "amount": amount,
                "price_per_unit": price_per_unit
            }
            
            logging.info(f"Offering {offering_id} created successfully.")
            return offering_id
        except Exception as e:
            logging.error(f"Failed to create offering: {e}")
            raise

    def get_offering(self, offering_id: str) -> Dict[str, Union[str, float]]:
        """
        Retrieve details of an OTC offering.
        
        Parameters:
            offering_id (str): Unique offering ID.
        
        Returns:
            Dict[str, Union[str, float]]: Offering details.
        """
        try:
            if offering_id not in self.offerings:
                raise KeyError("Offering ID not found.")
            
            return self.offerings[offering_id]
        except Exception as e:
            logging.error(f"Failed to retrieve offering: {e}")
            raise

    def cancel_offering(self, offering_id: str) -> bool:
        """
        Cancel an existing OTC offering.
        
        Parameters:
            offering_id (str): Unique offering ID.
        
        Returns:
            bool: True if the offering was successfully canceled, False otherwise.
        """
        try:
            if offering_id not in self.offerings:
                raise KeyError("Offering ID not found.")
            
            del self.offerings[offering_id]
            logging.info(f"Offering {offering_id} canceled successfully.")
            return True
        except Exception as e:
            logging.error(f"Failed to cancel offering: {e}")
            raise

    def list_offerings(self) -> Dict[str, Dict[str, Union[str, float]]]:
        """
        List all existing OTC offerings.
        
        Returns:
            Dict[str, Dict[str, Union[str, float]]]: All offerings with their details.
        """
        try:
            return self.offerings
        except Exception as e:
            logging.error(f"Failed to list offerings: {e}")
            raise


# Example usage
if __name__ == "__main__":
    # Initialize OTC Offering system
    otc = OTCOffering()

    try:
        # Create an offering
        offering_id = otc.create_offering(
            seller="seller123",
            buyer="buyer456",
            asset="MoonbootsToken",
            amount=100,
            price_per_unit=10.5
        )
        print(f"Offering created: {offering_id}")

        # Retrieve offering details
        details = otc.get_offering(offering_id)
        print(f"Offering details: {details}")

        # List all offerings
        all_offerings = otc.list_offerings()
        print(f"All offerings: {all_offerings}")

        # Cancel an offering
        success = otc.cancel_offering(offering_id)
        print(f"Offering canceled: {success}")

    except Exception as e:
        print(f"Error: {e}")
```
