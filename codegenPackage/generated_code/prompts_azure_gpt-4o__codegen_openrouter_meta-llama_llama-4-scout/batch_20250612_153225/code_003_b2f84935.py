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
# commercial_entity.py

from enum import Enum
from typing import List, Dict

class EntityType(str, Enum):
    """Type of commercial entity."""
    COMPANY = "company"
    PARTNERSHIP = "partnership"
    INDIVIDUAL = "individual"

class LicenseType(str, Enum):
    """Type of license."""
    IMPORT = "import"
    EXPORT = "export"
    TRANSIT = "transit"

class PermitType(str, Enum):
    """Type of permit."""
    CUSTOMS = "customs"
    TAX = "tax"

class CommercialEntity:
    """Represents a commercial entity in international trade."""

    def __init__(self, 
                 entity_type: EntityType, 
                 name: str, 
                 country: str, 
                 licenses: List[LicenseType] = None, 
                 permits: List[PermitType] = None):
        """
        Initializes a CommercialEntity.

        Args:
        - entity_type (EntityType): Type of commercial entity.
        - name (str): Name of the commercial entity.
        - country (str): Country of the commercial entity.
        - licenses (List[LicenseType], optional): List of licenses. Defaults to None.
        - permits (List[PermitType], optional): List of permits. Defaults to None.
        """
        self.entity_type = entity_type
        self.name = name
        self.country = country
        self.licenses = licenses if licenses else []
        self.permits = permits if permits else []

    def add_license(self, license_type: LicenseType):
        """Adds a license to the commercial entity."""
        self.licenses.append(license_type)

    def add_permit(self, permit_type: PermitType):
        """Adds a permit to the commercial entity."""
        self.permits.append(permit_type)

    def __str__(self):
        return f"{self.name} ({self.entity_type}) - {self.country}"

class LicenseManager:
    """Manages licenses for commercial entities."""

    def __init__(self):
        self.licenses: Dict[LicenseType, List[CommercialEntity]] = {
            LicenseType.IMPORT: [],
            LicenseType.EXPORT: [],
            LicenseType.TRANSIT: []
        }

    def add_license(self, commercial_entity: CommercialEntity, license_type: LicenseType):
        """
        Adds a license to a commercial entity.

        Args:
        - commercial_entity (CommercialEntity): Commercial entity to add license to.
        - license_type (LicenseType): Type of license.
        """
        if license_type not in self.licenses:
            raise ValueError(f"Invalid license type: {license_type}")
        self.licenses[license_type].append(commercial_entity)
        commercial_entity.add_license(license_type)

class PermitManager:
    """Manages permits for commercial entities."""

    def __init__(self):
        self.permits: Dict[PermitType, List[CommercialEntity]] = {
            PermitType.CUSTOMS: [],
            PermitType.TAX: []
        }

    def add_permit(self, commercial_entity: CommercialEntity, permit_type: PermitType):
        """
        Adds a permit to a commercial entity.

        Args:
        - commercial_entity (CommercialEntity): Commercial entity to add permit to.
        - permit_type (PermitType): Type of permit.
        """
        if permit_type not in self.permits:
            raise ValueError(f"Invalid permit type: {permit_type}")
        self.permits[permit_type].append(commercial_entity)
        commercial_entity.add_permit(permit_type)

def main():
    # Create commercial entities
    entity1 = CommercialEntity(EntityType.COMPANY, "GlobalChain SAS", "France")
    entity2 = CommercialEntity(EntityType.PARTNERSHIP, "Trade Partners", "USA")

    # Create license and permit managers
    license_manager = LicenseManager()
    permit_manager = PermitManager()

    # Add licenses and permits
    license_manager.add_license(entity1, LicenseType.IMPORT)
    license_manager.add_license(entity2, LicenseType.EXPORT)
    permit_manager.add_permit(entity1, PermitType.CUSTOMS)
    permit_manager.add_permit(entity2, PermitType.TAX)

    # Print commercial entities with licenses and permits
    print(entity1)
    print(f"Licenses: {entity1.licenses}")
    print(f"Permits: {entity1.permits}")
    print()
    print(entity2)
    print(f"Licenses: {entity2.licenses}")
    print(f"Permits: {entity2.permits}")

if __name__ == "__main__":
    main()
```
