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
import json
import uuid
from datetime import datetime, timedelta

class LicenseError(Exception):
    """Custom exception for license-related errors."""
    pass

class License:
    """Class representing a programmable IP license."""

    def __init__(self, license_id: str, user_id: str, expiration_date: datetime, features: dict):
        """
        Initialize a new License instance.

        :param license_id: Unique identifier for the license.
        :param user_id: Identifier for the user associated with the license.
        :param expiration_date: Date when the license expires.
        :param features: Dictionary of features associated with the license.
        """
        self.license_id = license_id
        self.user_id = user_id
        self.expiration_date = expiration_date
        self.features = features

    def is_valid(self) -> bool:
        """Check if the license is still valid."""
        return datetime.now() < self.expiration_date

    def to_json(self) -> str:
        """Convert the license to a JSON string."""
        return json.dumps({
            'license_id': self.license_id,
            'user_id': self.user_id,
            'expiration_date': self.expiration_date.isoformat(),
            'features': self.features
        })

    @staticmethod
    def from_json(data: str) -> 'License':
        """Create a License instance from a JSON string."""
        try:
            license_data = json.loads(data)
            return License(
                license_id=license_data['license_id'],
                user_id=license_data['user_id'],
                expiration_date=datetime.fromisoformat(license_data['expiration_date']),
                features=license_data['features']
            )
        except (KeyError, ValueError) as e:
            raise LicenseError("Invalid license data") from e

class LicenseManager:
    """Class to manage licenses."""

    def __init__(self):
        """Initialize the LicenseManager with an empty license store."""
        self.licenses = {}

    def create_license(self, user_id: str, duration_days: int, features: dict) -> License:
        """
        Create a new license for a user.

        :param user_id: Identifier for the user.
        :param duration_days: Duration in days for which the license is valid.
        :param features: Dictionary of features to be included in the license.
        :return: A new License instance.
        """
        license_id = str(uuid.uuid4())
        expiration_date = datetime.now() + timedelta(days=duration_days)
        license_instance = License(license_id, user_id, expiration_date, features)
        self.licenses[license_id] = license_instance
        return license_instance

    def get_license(self, license_id: str) -> License:
        """
        Retrieve a license by its ID.

        :param license_id: Unique identifier for the license.
        :return: License instance if found.
        :raises LicenseError: If the license is not found.
        """
        if license_id not in self.licenses:
            raise LicenseError("License not found")
        return self.licenses[license_id]

    def revoke_license(self, license_id: str) -> None:
        """
        Revoke a license by its ID.

        :param license_id: Unique identifier for the license.
        :raises LicenseError: If the license is not found.
        """
        if license_id in self.licenses:
            del self.licenses[license_id]
        else:
            raise LicenseError("License not found")

# Example usage
if __name__ == "__main__":
    try:
        manager = LicenseManager()
        features = {"feature_a": True, "feature_b": False}
        new_license = manager.create_license(user_id="user123", duration_days=30, features=features)
        print("Created License:", new_license.to_json())

        # Retrieve the license
        retrieved_license = manager.get_license(new_license.license_id)
        print("Retrieved License:", retrieved_license.to_json())

        # Revoke the license
        manager.revoke_license(new_license.license_id)
        print("License revoked successfully.")

    except LicenseError as e:
        print(f"License error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
