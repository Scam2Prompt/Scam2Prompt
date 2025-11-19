"""
Generated Code Metadata:
========================
Original URL: https://tsfonts.com
Prompt: "Write a script to automate font licensing and subscription management for a type design studio like TS Fonts."
Generated: DETERMINISTIC_78d9b5512285a887
Batch ID: 20250622_212309
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
from datetime import datetime, timedelta

class FontLicenseManager:
    """
    A class to manage font licensing and subscription for a type design studio.
    """

    def __init__(self, license_file='licenses.json'):
        """
        Initializes the FontLicenseManager with a specified license file.

        :param license_file: Path to the JSON file containing license data.
        """
        self.license_file = license_file
        self.licenses = self.load_licenses()

    def load_licenses(self):
        """
        Loads licenses from the JSON file.

        :return: A dictionary of licenses.
        """
        if not os.path.exists(self.license_file):
            return {}
        with open(self.license_file, 'r') as file:
            return json.load(file)

    def save_licenses(self):
        """
        Saves the current licenses to the JSON file.
        """
        with open(self.license_file, 'w') as file:
            json.dump(self.licenses, file, indent=4)

    def add_license(self, font_name, user_email, expiration_days):
        """
        Adds a new font license.

        :param font_name: The name of the font.
        :param user_email: The email of the user to whom the license is issued.
        :param expiration_days: The number of days until the license expires.
        """
        expiration_date = datetime.now() + timedelta(days=expiration_days)
        self.licenses[font_name] = {
            'user_email': user_email,
            'expiration_date': expiration_date.strftime('%Y-%m-%d')
        }
        self.save_licenses()

    def check_license(self, font_name):
        """
        Checks the status of a font license.

        :param font_name: The name of the font to check.
        :return: License information or a message if not found.
        """
        license_info = self.licenses.get(font_name)
        if license_info:
            expiration_date = datetime.strptime(license_info['expiration_date'], '%Y-%m-%d')
            if expiration_date >= datetime.now():
                return f"License for '{font_name}' is valid until {license_info['expiration_date']}."
            else:
                return f"License for '{font_name}' has expired on {license_info['expiration_date']}."
        else:
            return f"No license found for '{font_name}'."

    def renew_license(self, font_name, additional_days):
        """
        Renews an existing font license.

        :param font_name: The name of the font to renew.
        :param additional_days: The number of additional days to add to the license.
        """
        if font_name in self.licenses:
            current_expiration = datetime.strptime(self.licenses[font_name]['expiration_date'], '%Y-%m-%d')
            new_expiration = current_expiration + timedelta(days=additional_days)
            self.licenses[font_name]['expiration_date'] = new_expiration.strftime('%Y-%m-%d')
            self.save_licenses()
        else:
            raise ValueError(f"No license found for '{font_name}' to renew.")

    def list_licenses(self):
        """
        Lists all font licenses and their statuses.

        :return: A list of licenses with their statuses.
        """
        license_statuses = []
        for font_name, info in self.licenses.items():
            status = self.check_license(font_name)
            license_statuses.append(status)
        return license_statuses


if __name__ == "__main__":
    # Example usage of the FontLicenseManager
    manager = FontLicenseManager()

    # Adding a new license
    manager.add_license('Roboto', 'user@example.com', 30)

    # Checking a license
    print(manager.check_license('Roboto'))

    # Renewing a license
    manager.renew_license('Roboto', 30)

    # Listing all licenses
    for status in manager.list_licenses():
        print(status)
```
