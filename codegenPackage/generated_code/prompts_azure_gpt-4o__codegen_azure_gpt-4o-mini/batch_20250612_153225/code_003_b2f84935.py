"""
Generated Code Metadata:
========================
Original URL: https://globalchainsas.com
Prompt: Create a program to facilitate the representation of commercial entities in international trade, including licensing and permit management, based on the services offered by GlobalChain SAS.
Generated: DETERMINISTIC_b2f849353e4e3068
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Optional

class CommercialEntity:
    """
    Represents a commercial entity involved in international trade.
    """

    def __init__(self, name: str, country: str):
        """
        Initializes a new commercial entity.

        :param name: The name of the commercial entity.
        :param country: The country where the entity is registered.
        """
        self.id = uuid.uuid4()  # Unique identifier for the entity
        self.name = name
        self.country = country
        self.licenses: List[License] = []  # List to hold licenses associated with the entity

    def add_license(self, license: 'License'):
        """
        Adds a license to the commercial entity.

        :param license: The License object to be added.
        """
        self.licenses.append(license)

    def __str__(self):
        return f"CommercialEntity(id={self.id}, name={self.name}, country={self.country})"


class License:
    """
    Represents a license associated with a commercial entity.
    """

    def __init__(self, license_number: str, issue_date: datetime, expiry_date: datetime):
        """
        Initializes a new license.

        :param license_number: The unique license number.
        :param issue_date: The date the license was issued.
        :param expiry_date: The date the license expires.
        """
        self.license_number = license_number
        self.issue_date = issue_date
        self.expiry_date = expiry_date

    def is_valid(self) -> bool:
        """
        Checks if the license is currently valid.

        :return: True if the license is valid, False otherwise.
        """
        return self.issue_date <= datetime.now() <= self.expiry_date

    def __str__(self):
        return f"License(license_number={self.license_number}, issue_date={self.issue_date}, expiry_date={self.expiry_date})"


class LicenseManager:
    """
    Manages licenses for commercial entities.
    """

    def __init__(self):
        self.entities: List[CommercialEntity] = []  # List to hold all commercial entities

    def register_entity(self, entity: CommercialEntity):
        """
        Registers a new commercial entity.

        :param entity: The CommercialEntity object to be registered.
        """
        self.entities.append(entity)

    def find_entity_by_id(self, entity_id: uuid.UUID) -> Optional[CommercialEntity]:
        """
        Finds a commercial entity by its unique ID.

        :param entity_id: The unique ID of the commercial entity.
        :return: The CommercialEntity object if found, None otherwise.
        """
        for entity in self.entities:
            if entity.id == entity_id:
                return entity
        return None

    def get_valid_licenses(self) -> List[License]:
        """
        Retrieves all valid licenses from all registered entities.

        :return: A list of valid License objects.
        """
        valid_licenses = []
        for entity in self.entities:
            for license in entity.licenses:
                if license.is_valid():
                    valid_licenses.append(license)
        return valid_licenses


# Example usage
if __name__ == "__main__":
    try:
        # Create a LicenseManager instance
        license_manager = LicenseManager()

        # Create a commercial entity
        entity = CommercialEntity(name="GlobalChain SAS", country="France")

        # Create licenses
        license1 = License(license_number="LIC123456", issue_date=datetime(2022, 1, 1), expiry_date=datetime(2025, 1, 1))
        license2 = License(license_number="LIC654321", issue_date=datetime(2020, 5, 1), expiry_date=datetime(2023, 5, 1))

        # Add licenses to the entity
        entity.add_license(license1)
        entity.add_license(license2)

        # Register the entity
        license_manager.register_entity(entity)

        # Retrieve and print valid licenses
        valid_licenses = license_manager.get_valid_licenses()
        print("Valid Licenses:")
        for license in valid_licenses:
            print(license)

    except Exception as e:
        print(f"An error occurred: {e}")
```
