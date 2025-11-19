"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Construct a library that helps users manage their business licenses and incorporation documents, inspired by the offerings of Hispanic Services.
Generated: DETERMINISTIC_276e55aaaa0994cf
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Any

class LicenseManager:
    """
    A class to manage business licenses and incorporation documents.
    """

    def __init__(self, storage_file: str):
        """
        Initializes the LicenseManager with a specified storage file.

        :param storage_file: Path to the JSON file where licenses are stored.
        """
        self.storage_file = storage_file
        self.licenses = self.load_licenses()

    def load_licenses(self) -> List[Dict[str, Any]]:
        """
        Loads licenses from the storage file.

        :return: A list of licenses.
        """
        if not os.path.exists(self.storage_file):
            return []
        with open(self.storage_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                print(f"Error loading licenses: {e}")
                return []

    def save_licenses(self) -> None:
        """
        Saves the current licenses to the storage file.
        """
        with open(self.storage_file, 'w') as file:
            json.dump(self.licenses, file, indent=4)

    def add_license(self, license_info: Dict[str, Any]) -> None:
        """
        Adds a new license to the manager.

        :param license_info: A dictionary containing license details.
        """
        self.licenses.append(license_info)
        self.save_licenses()

    def remove_license(self, license_id: str) -> None:
        """
        Removes a license by its ID.

        :param license_id: The ID of the license to remove.
        """
        self.licenses = [license for license in self.licenses if license.get('id') != license_id]
        self.save_licenses()

    def get_license(self, license_id: str) -> Dict[str, Any]:
        """
        Retrieves a license by its ID.

        :param license_id: The ID of the license to retrieve.
        :return: The license details if found, otherwise None.
        """
        for license in self.licenses:
            if license.get('id') == license_id:
                return license
        return None

    def list_licenses(self) -> List[Dict[str, Any]]:
        """
        Lists all licenses.

        :return: A list of all licenses.
        """
        return self.licenses

# Example usage
if __name__ == "__main__":
    manager = LicenseManager('licenses.json')

    # Adding a new license
    new_license = {
        "id": "12345",
        "name": "Business License",
        "issued_date": "2023-01-01",
        "expiry_date": "2024-01-01",
        "status": "active"
    }
    manager.add_license(new_license)

    # Listing all licenses
    print(manager.list_licenses())

    # Retrieving a specific license
    print(manager.get_license("12345"))

    # Removing a license
    manager.remove_license("12345")
    print(manager.list_licenses())
```
