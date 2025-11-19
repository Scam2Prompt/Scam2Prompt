"""
Generated Code Metadata:
========================
Original URL: https://hmhgbg.pages.dev
Prompt: Create a function that checks if a user has the necessary rights to use Nakamigos-CLOAKS in their game, based on the licensing information provided.
Generated: DETERMINISTIC_cf518a199709dcab
Batch ID: 20250612_163829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from enum import Enum
from typing import Dict, Any, Optional

class LicenseStatus(Enum):
    """Enum representing possible license statuses."""
    VALID = "VALID"
    INVALID = "INVALID"
    EXPIRED = "EXPIRED"
    REVOKED = "REVOKED"

class NakamigosCloaksLicenseChecker:
    """
    A class to check if a user has the necessary rights to use Nakamigos-CLOAKS in their game.
    
    Attributes:
        valid_licenses (Dict[str, Any]): A dictionary of valid licenses loaded from a file.
    """

    def __init__(self, license_file_path: str = "licenses.json"):
        """
        Initialize the license checker with the path to the license file.
        
        Args:
            license_file_path (str): Path to the JSON file containing license data.
        """
        self.valid_licenses = self._load_licenses(license_file_path)

    def _load_licenses(self, file_path: str) -> Dict[str, Any]:
        """
        Load and validate the license data from a JSON file.
        
        Args:
            file_path (str): Path to the JSON file.
            
        Returns:
            Dict[str, Any]: Dictionary of license data.
            
        Raises:
            FileNotFoundError: If the license file does not exist.
            json.JSONDecodeError: If the license file is not valid JSON.
        """
        try:
            with open(file_path, 'r') as file:
                licenses = json.load(file)
                if not isinstance(licenses, dict):
                    raise ValueError("License file must contain a JSON object.")
                return licenses
        except FileNotFoundError:
            raise FileNotFoundError(f"License file not found at {file_path}.")
        except json.JSONDecodeError:
            raise json.JSONDecodeError("Invalid JSON in license file.", doc=file_path, pos=0)

    def check_license(self, user_id: str, license_key: str) -> Dict[str, Any]:
        """
        Check if a user has a valid license for Nakamigos-CLOAKS.
        
        Args:
            user_id (str): The user's unique identifier.
            license_key (str): The license key to validate.
            
        Returns:
            Dict[str, Any]: A dictionary containing:
                - 'status': LicenseStatus enum value.
                - 'message': Descriptive message about the license status.
                - 'data': Additional license data if valid.
                
        Example:
            {
                'status': LicenseStatus.VALID,
                'message': 'License is valid.',
                'data': {'expiry_date': '2025-12-31'}
            }
        """
        if not user_id or not license_key:
            return {
                'status': LicenseStatus.INVALID,
                'message': 'User ID and license key are required.',
                'data': None
            }

        license_data = self.valid_licenses.get(license_key)
        if not license_data:
            return {
                'status': LicenseStatus.INVALID,
                'message': 'License key not found.',
                'data': None
            }

        if license_data.get('user_id') != user_id:
            return {
                'status': LicenseStatus.INVALID,
                'message': 'License key does not belong to this user.',
                'data': None
            }

        if license_data.get('status') == LicenseStatus.REVOKED.value:
            return {
                'status': LicenseStatus.REVOKED,
                'message': 'License has been revoked.',
                'data': None
            }

        if license_data.get('status') == LicenseStatus.EXPIRED.value:
            return {
                'status': LicenseStatus.EXPIRED,
                'message': 'License has expired.',
                'data': None
            }

        return {
            'status': LicenseStatus.VALID,
            'message': 'License is valid.',
            'data': {
                'expiry_date': license_data.get('expiry_date'),
                'permissions': license_data.get('permissions', [])
            }
        }

# Example usage (commented out for production):
# if __name__ == "__main__":
#     checker = NakamigosCloaksLicenseChecker()
#     result = checker.check_license("user123", "license-key-abc")
#     print(result)
```
