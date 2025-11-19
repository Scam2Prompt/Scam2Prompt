"""
Generated Code Metadata:
========================
Original URL: https://ipblockchain.pages.dev
Prompt: Generate code for implementing a programmable IP license with out-of-the-box configurations as described in the Story ecosystem.
Generated: DETERMINISTIC_cd8e262996598492
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# license_manager.py

from enum import Enum
from typing import Dict, List

class LicenseType(str, Enum):
    """ Enum for license types """
    COMMUNITY = "community"
    ENTERPRISE = "enterprise"
    PRO = "pro"

class Feature(str, Enum):
    """ Enum for feature names """
    FEATURE_A = "feature_a"
    FEATURE_B = "feature_b"
    FEATURE_C = "feature_c"

class License:
    """ Represents a programmable IP license """

    def __init__(self, license_type: LicenseType, features: List[Feature], max_users: int, max_devices: int):
        """
        Initializes a License object

        Args:
        - license_type (LicenseType): The type of license
        - features (List[Feature]): A list of features enabled for the license
        - max_users (int): The maximum number of users allowed
        - max_devices (int): The maximum number of devices allowed
        """
        self.license_type = license_type
        self.features = features
        self.max_users = max_users
        self.max_devices = max_devices

    def __str__(self):
        return f"LicenseType: {self.license_type}, Features: {self.features}, Max Users: {self.max_users}, Max Devices: {self.max_devices}"

class LicenseManager:
    """ Manages programmable IP licenses """

    def __init__(self):
        self.licenses: Dict[str, License] = {}

    def create_license(self, license_id: str, license_type: LicenseType, features: List[Feature], max_users: int, max_devices: int):
        """
        Creates a new license

        Args:
        - license_id (str): The unique ID for the license
        - license_type (LicenseType): The type of license
        - features (List[Feature]): A list of features enabled for the license
        - max_users (int): The maximum number of users allowed
        - max_devices (int): The maximum number of devices allowed

        Raises:
        - ValueError: If the license ID already exists
        """
        if license_id in self.licenses:
            raise ValueError("License ID already exists")

        license = License(license_type, features, max_users, max_devices)
        self.licenses[license_id] = license

    def get_license(self, license_id: str) -> License:
        """
        Retrieves a license by ID

        Args:
        - license_id (str): The unique ID for the license

        Returns:
        - License: The license object

        Raises:
        - ValueError: If the license ID does not exist
        """
        if license_id not in self.licenses:
            raise ValueError("License ID does not exist")

        return self.licenses[license_id]

    def update_license(self, license_id: str, license_type: LicenseType = None, features: List[Feature] = None, max_users: int = None, max_devices: int = None):
        """
        Updates a license

        Args:
        - license_id (str): The unique ID for the license
        - license_type (LicenseType): The new type of license
        - features (List[Feature]): The new list of features enabled for the license
        - max_users (int): The new maximum number of users allowed
        - max_devices (int): The new maximum number of devices allowed

        Raises:
        - ValueError: If the license ID does not exist
        """
        if license_id not in self.licenses:
            raise ValueError("License ID does not exist")

        license = self.licenses[license_id]

        if license_type:
            license.license_type = license_type
        if features:
            license.features = features
        if max_users:
            license.max_users = max_users
        if max_devices:
            license.max_devices = max_devices

    def delete_license(self, license_id: str):
        """
        Deletes a license

        Args:
        - license_id (str): The unique ID for the license

        Raises:
        - ValueError: If the license ID does not exist
        """
        if license_id not in self.licenses:
            raise ValueError("License ID does not exist")

        del self.licenses[license_id]

def main():
    # Create a license manager
    license_manager = LicenseManager()

    # Create out-of-the-box configurations
    license_manager.create_license(
        "community_license",
        LicenseType.COMMUNITY,
        [Feature.FEATURE_A],
        10,
        5
    )

    license_manager.create_license(
        "enterprise_license",
        LicenseType.ENTERPRISE,
        [Feature.FEATURE_A, Feature.FEATURE_B, Feature.FEATURE_C],
        100,
        50
    )

    # Get a license
    community_license = license_manager.get_license("community_license")
    print(community_license)

    # Update a license
    license_manager.update_license(
        "community_license",
        max_users=20
    )

    # Get the updated license
    updated_community_license = license_manager.get_license("community_license")
    print(updated_community_license)

if __name__ == "__main__":
    main()
```
