"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://globalchainsas.com
Prompt: Create a program to facilitate the representation of commercial entities in international trade, including licensing and permit management, based on the services offered by GlobalChain SAS.
Generated: DETERMINISTIC_b2f849353e4e3068
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
from datetime import datetime
from typing import List, Optional

class CommercialEntity:
    """
    Class to represent a commercial entity involved in international trade.
    """
    def __init__(self, name: str, registration_number: str, services: List[str]):
        """
        Initialize a CommercialEntity instance.

        :param name: Name of the commercial entity
        :param registration_number: Unique registration number
        :param services: List of services offered by the entity
        """
        self.name = name
        self.registration_number = registration_number
        self.services = services
        self.licenses_and_permits = []
        self.created_at = datetime.now()

    def add_license_or_permit(self, license_number: str, expiration_date: str):
        """
        Add a license or permit to the commercial entity.

        :param license_number: License or permit number
        :param expiration_date: Expiration date of the license or permit in 'YYYY-MM-DD' format
        """
        try:
            expiration = datetime.strptime(expiration_date, '%Y-%m-%d')
            self.licenses_and_permits.append((license_number, expiration))
        except ValueError as e:
            print(f"Error adding license/permit: {e}")

    def get_active_licenses(self) -> List[str]:
        """
        Retrieve all active licenses and permits.

        :return: List of active license/permit numbers
        """
        active_licenses = []
        current_date = datetime.now()
        for license_number, expiration in self.licenses_and_permits:
            if expiration > current_date:
                active_licenses.append(license_number)
        return active_licenses

    def __str__(self):
        """
        String representation of the CommercialEntity.

        :return: Formatted string of the commercial entity details
        """
        return f"Entity Name: {self.name}, Registration Number: {self.registration_number}, Services: {self.services}, Active Licenses: {self.get_active_licenses()}"

class TradeManagementSystem:
    """
    Class to manage multiple commercial entities.
    """
    def __init__(self):
        """
        Initialize the Trade Management System.
        """
        self.entities = []

    def register_entity(self, entity: CommercialEntity):
        """
        Register a new commercial entity in the system.

        :param entity: Instance of CommercialEntity to register
        """
        self.entities.append(entity)

    def find_entity(self, registration_number: str) -> Optional[CommercialEntity]:
        """
        Find a commercial entity by its registration number.

        :param registration_number: Registration number of the entity to find
        :return: CommercialEntity object if found; otherwise, None
        """
        for entity in self.entities:
            if entity.registration_number == registration_number:
                return entity
        return None

    def display_all_entities(self):
        """
        Display all registered commercial entities in the system.
        """
        for entity in self.entities:
            print(entity)

# Example usage (to be removed in production code)
if __name__ == "__main__":
    # Initialize the trade management system
    trade_system = TradeManagementSystem()
    
    # Create a new commercial entity
    entity1 = CommercialEntity("GlobalChain SAS", "GC123456", ["Import", "Export", "Consulting"])
    entity1.add_license_or_permit("L123", "2025-12-31")
    entity1.add_license_or_permit("L456", "2024-05-15")
    
    # Register the entity in the system
    trade_system.register_entity(entity1)
    
    # Display all entities
    trade_system.display_all_entities()
```
