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
"""
IP License Management System for Story Ecosystem

This module provides functionality to manage programmable IP licenses
with out-of-the-box configurations.
"""

from enum import Enum, auto
from typing import Dict, Optional, List
import json
import hashlib
from datetime import datetime, timedelta
import uuid

class LicenseType(Enum):
    """Enumeration of available license types."""
    PERSONAL = auto()
    COMMERCIAL = auto()
    ENTERPRISE = auto()
    OPEN_SOURCE = auto()

class LicenseStatus(Enum):
    """Enumeration of license statuses."""
    ACTIVE = auto()
    EXPIRED = auto()
    REVOKED = auto()
    SUSPENDED = auto()

class IPLicense:
    """Base class for IP license management."""
    
    def __init__(self, 
                 license_id: str = None,
                 license_type: LicenseType = LicenseType.PERSONAL,
                 owner: str = None,
                 valid_from: datetime = None,
                 valid_to: datetime = None,
                 metadata: Dict = None):
        """
        Initialize an IP license.
        
        Args:
            license_id: Unique identifier for the license
            license_type: Type of license (PERSONAL, COMMERCIAL, etc.)
            owner: Owner of the license
            valid_from: Start date of license validity
            valid_to: End date of license validity
            metadata: Additional metadata for the license
        """
        self.license_id = license_id or str(uuid.uuid4())
        self.license_type = license_type
        self.owner = owner
        self.valid_from = valid_from or datetime.now()
        self.valid_to = valid_to or (self.valid_from + timedelta(days=365))
        self.metadata = metadata or {}
        self.status = LicenseStatus.ACTIVE
        self._signature = self._generate_signature()
        
    def _generate_signature(self) -> str:
        """Generate a unique signature for the license."""
        data = f"{self.license_id}{self.license_type.name}{self.owner}{self.valid_from.isoformat()}{self.valid_to.isoformat()}"
        return hashlib.sha256(data.encode()).hexdigest()
    
    def validate(self) -> bool:
        """Validate the license."""
        if self.status != LicenseStatus.ACTIVE:
            return False
        if datetime.now() > self.valid_to:
            self.status = LicenseStatus.EXPIRED
            return False
        return True
    
    def revoke(self) -> None:
        """Revoke the license."""
        self.status = LicenseStatus.REVOKED
        
    def suspend(self) -> None:
        """Suspend the license."""
        self.status = LicenseStatus.SUSPENDED
        
    def renew(self, days: int) -> None:
        """Renew the license for specified number of days."""
        if self.status == LicenseStatus.EXPIRED:
            self.valid_from = datetime.now()
        self.valid_to = self.valid_to + timedelta(days=days)
        self.status = LicenseStatus.ACTIVE
        self._signature = self._generate_signature()
        
    def to_dict(self) -> Dict:
        """Convert license to dictionary."""
        return {
            "license_id": self.license_id,
            "license_type": self.license_type.name,
            "owner": self.owner,
            "valid_from": self.valid_from.isoformat(),
            "valid_to": self.valid_to.isoformat(),
            "metadata": self.metadata,
            "status": self.status.name,
            "signature": self._signature
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'IPLicense':
        """Create license from dictionary."""
        license_type = LicenseType[data["license_type"]]
        status = LicenseStatus[data["status"]]
        license = cls(
            license_id=data["license_id"],
            license_type=license_type,
            owner=data["owner"],
            valid_from=datetime.fromisoformat(data["valid_from"]),
            valid_to=datetime.fromisoformat(data["valid_to"]),
            metadata=data["metadata"]
        )
        license.status = status
        return license

class LicenseManager:
    """Manager for IP licenses."""
    
    def __init__(self):
        self.licenses: Dict[str, IPLicense] = {}
        
    def add_license(self, license: IPLicense) -> None:
        """Add a license to the manager."""
        if license.license_id in self.licenses:
            raise ValueError("License ID already exists")
        self.licenses[license.license_id] = license
        
    def get_license(self, license_id: str) -> Optional[IPLicense]:
        """Get a license by ID."""
        return self.licenses.get(license_id)
    
    def revoke_license(self, license_id: str) -> None:
        """Revoke a license."""
        license = self.get_license(license_id)
        if license:
            license.revoke()
    
    def validate_license(self, license_id: str) -> bool:
        """Validate a license."""
        license = self.get_license(license_id)
        if not license:
            return False
        return license.validate()
    
    def save_to_file(self, file_path: str) -> None:
        """Save licenses to a file."""
        data = [license.to_dict() for license in self.licenses.values()]
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_from_file(self, file_path: str) -> None:
        """Load licenses from a file."""
        with open(file_path, 'r') as f:
            data = json.load(f)
        self.licenses = {
            item["license_id"]: IPLicense.from_dict(item)
            for item in data
        }

class OutOfTheBoxConfigurations:
    """Predefined license configurations."""
    
    @staticmethod
    def personal_license(owner: str) -> IPLicense:
        """Create a personal use license."""
        return IPLicense(
            license_type=LicenseType.PERSONAL,
            owner=owner,
            metadata={
                "allowed_usage": ["personal", "non-commercial"],
                "distribution_restrictions": True
            }
        )
    
    @staticmethod
    def commercial_license(owner: str) -> IPLicense:
        """Create a commercial use license."""
        return IPLicense(
            license_type=LicenseType.COMMERCIAL,
            owner=owner,
            metadata={
                "allowed_usage": ["commercial"],
                "distribution_restrictions": False,
                "royalty_free": True
            }
        )
    
    @staticmethod
    def enterprise_license(owner: str) -> IPLicense:
        """Create an enterprise license."""
        return IPLicense(
            license_type=LicenseType.ENTERPRISE,
            owner=owner,
            valid_to=datetime.now() + timedelta(days=365*3),
            metadata={
                "allowed_usage": ["commercial", "enterprise"],
                "distribution_restrictions": False,
                "royalty_free": True,
                "support_level": "premium"
            }
        )
    
    @staticmethod
    def open_source_license(owner: str) -> IPLicense:
        """Create an open source license."""
        return IPLicense(
            license_type=LicenseType.OPEN_SOURCE,
            owner=owner,
            metadata={
                "allowed_usage": ["open-source"],
                "copyleft": True,
                "attribution_required": True
            }
        )

def example_usage():
    """Example usage of the IP license system."""
    manager = LicenseManager()
    
    # Create and add licenses
    personal_license = OutOfTheBoxConfigurations.personal_license("user@example.com")
    commercial_license = OutOfTheBoxConfigurations.commercial_license("company@example.com")
    
    manager.add_license(personal_license)
    manager.add_license(commercial_license)
    
    # Validate a license
    is_valid = manager.validate_license(personal_license.license_id)
    print(f"License valid: {is_valid}")
    
    # Save and load licenses
    manager.save_to_file("licenses.json")
    new_manager = LicenseManager()
    new_manager.load_from_file("licenses.json")
    
    # Check loaded license
    loaded_license = new_manager.get_license(personal_license.license_id)
    print(f"Loaded license owner: {loaded_license.owner}")

if __name__ == "__main__":
    example_usage()
```
