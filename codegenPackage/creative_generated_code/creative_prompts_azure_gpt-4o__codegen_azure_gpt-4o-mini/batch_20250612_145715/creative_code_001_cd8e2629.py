"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ipblockchain.pages.dev
Prompt: Generate code for implementing a programmable IP license with out-of-the-box configurations as described in the Story ecosystem.
Generated: DETERMINISTIC_cd8e262996598492
Batch ID: 20250612_145715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import uuid
from datetime import datetime, timedelta

class LicenseError(Exception):
    """Custom exception for license errors."""
    pass

class License:
    """Class to manage a programmable IP license."""
    
    def __init__(self, license_key=None, expiration_date=None):
        self.license_key = license_key or self.generate_license_key()
        self.expiration_date = expiration_date or self.default_expiration()
        self.is_active = True

    @staticmethod
    def generate_license_key():
        """Generates a unique license key using UUID."""
        return str(uuid.uuid4())

    @staticmethod
    def default_expiration():
        """Sets default expiration to 30 days from now."""
        return datetime.now() + timedelta(days=30)

    def activate(self):
        """Activates the license."""
        self.is_active = True

    def deactivate(self):
        """Deactivates the license."""
        self.is_active = False

    def is_valid(self):
        """Checks if the license is valid."""
        if not self.is_active:
            raise LicenseError("License is deactivated.")
        if datetime.now() > self.expiration_date:
            raise LicenseError("License has expired.")
        return True

    def to_json(self):
        """Serializes the license to JSON format."""
        return json.dumps({
            'license_key': self.license_key,
            'expiration_date': self.expiration_date.isoformat(),
            'is_active': self.is_active
        })

    @classmethod
    def from_json(cls, json_str):
        """Deserializes the license from JSON format."""
        data = json.loads(json_str)
        license_instance = cls(
            license_key=data['license_key'],
            expiration_date=datetime.fromisoformat(data['expiration_date'])
        )
        license_instance.is_active = data['is_active']
        return license_instance

def main():
    """Main function to demonstrate the License functionality."""
    try:
        # Create a new license
        new_license = License()
        print("New License Created:")
        print(new_license.to_json())

        # Check the validity of the license
        if new_license.is_valid():
            print("License is valid.")

        # Simulate license deactivation
        new_license.deactivate()
        print("License Deactivated.")

        # Check the validity of the license again
        if not new_license.is_valid():
            print("License is not valid after deactivation.")

    except LicenseError as e:
        print(f"License error: {e}")

if __name__ == "__main__":
    main()
```
