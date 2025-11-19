"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hispanicservices.com
Prompt: Construct a library that helps users manage their business licenses and incorporation documents, inspired by the offerings of Hispanic Services.
Generated: DETERMINISTIC_276e55aaaa0994cf
Batch ID: 20250612_164222
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os
from typing import List, Dict, Optional

class LicenseManager:
    """A class to manage business licenses and incorporation documents."""

    def __init__(self, storage_file: str):
        """
        Initialize the LicenseManager with a storage file.

        Args:
            storage_file (str): The path to the JSON file for storing documents.
        """
        self.storage_file = storage_file
        self.licenses = self.load_licenses()

    def load_licenses(self) -> List[Dict]:
        """Load licenses from the JSON file."""
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                return json.load(file)
        return []

    def save_licenses(self) -> None:
        """Save the current licenses to the JSON file."""
        with open(self.storage_file, 'w') as file:
            json.dump(self.licenses, file, indent=4)

    def add_license(self, name: str, license_type: str, issue_date: str, expiry_date: str) -> None:
        """
        Add a new license to the manager.

        Args:
            name (str): Name of the business.
            license_type (str): Type of license.
            issue_date (str): Date the license was issued.
            expiry_date (str): Date the license expires.

        Raises:
            ValueError: If any required field is missing.
        """
        if not all([name, license_type, issue_date, expiry_date]):
            raise ValueError("All fields are required to add a license.")

        new_license = {
            "name": name,
            "license_type": license_type,
            "issue_date": issue_date,
            "expiry_date": expiry_date
        }
        self.licenses.append(new_license)
        self.save_licenses()

    def remove_license(self, name: str) -> None:
        """
        Remove a license by name.

        Args:
            name (str): Name of the business to remove.

        Raises:
            ValueError: If the license does not exist.
        """
        for license in self.licenses:
            if license['name'] == name:
                self.licenses.remove(license)
                self.save_licenses()
                return
        raise ValueError("License not found.")

    def get_license(self, name: str) -> Optional[Dict]:
        """
        Retrieve a license by name.

        Args:
            name (str): Name of the business.

        Returns:
            Optional[Dict]: The license details if found, otherwise None.
        """
        for license in self.licenses:
            if license['name'] == name:
                return license
        return None

    def list_licenses(self) -> List[Dict]:
        """Return a list of all managed licenses."""
        return self.licenses

# Example usage of LicenseManager
if __name__ == "__main__":
    manager = LicenseManager('licenses.json')
    
    # Adding a new license
    try:
        manager.add_license("Example Business", "Business License", "2023-01-01", "2025-01-01")
        print("License added successfully.")
    except ValueError as e:
        print(f"Error: {e}")

    # Listing all licenses
    licenses = manager.list_licenses()
    print("Current Licenses:", licenses)

    # Getting a specific license
    license_info = manager.get_license("Example Business")
    print("License Info:", license_info)

    # Removing a license
    try:
        manager.remove_license("Example Business")
        print("License removed successfully.")
    except ValueError as e:
        print(f"Error: {e}")
```
