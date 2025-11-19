"""
Generated Code Metadata:
========================
Original URL: https://nillion.pages.dev
Prompt: "Propose a composable digital identity solution using Nillion's decentralized storage vault and secure data sharing capabilities."
Generated: DETERMINISTIC_869cedf1bdc8385d
Batch ID: 20250622_211436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Nillion Digital Identity Solution
# A composable identity system leveraging Nillion's decentralized storage and secure data sharing

from typing import Dict, Optional, List
import uuid
import json
from datetime import datetime
import hashlib
from enum import Enum, auto

# Error Handling Classes
class IdentityError(Exception):
    """Base class for identity-related exceptions"""
    pass

class IdentityNotFoundError(IdentityError):
    """Raised when identity is not found"""
    pass

class IdentityVerificationError(IdentityError):
    """Raised when identity verification fails"""
    pass

class PermissionDeniedError(IdentityError):
    """Raised when access is denied"""
    pass

# Identity Attribute Types
class AttributeType(Enum):
    PERSONAL = auto()
    FINANCIAL = auto()
    MEDICAL = auto()
    GOVERNMENT = auto()
    CUSTOM = auto()

class DigitalIdentity:
    """
    A composable digital identity solution using Nillion's decentralized storage.
    
    Attributes:
        identity_id: Unique identifier for the identity
        owner_id: Owner of the identity
        attributes: Dictionary of identity attributes
        created_at: Timestamp of creation
        updated_at: Timestamp of last update
        access_controls: Dictionary of access permissions
    """
    
    def __init__(self, owner_id: str):
        """
        Initialize a new digital identity.
        
        Args:
            owner_id: The owner's unique identifier
        """
        self.identity_id = str(uuid.uuid4())
        self.owner_id = owner_id
        self.attributes: Dict[str, Dict] = {}
        self.created_at = datetime.utcnow().isoformat()
        self.updated_at = self.created_at
        self.access_controls: Dict[str, List[str]] = {}
        
    def add_attribute(self, 
                     key: str, 
                     value: str, 
                     attribute_type: AttributeType,
                     is_sensitive: bool = False) -> None:
        """
        Add an attribute to the identity.
        
        Args:
            key: Attribute key
            value: Attribute value
            attribute_type: Type of attribute
            is_sensitive: Whether the attribute is sensitive
        """
        hashed_value = hashlib.sha256(value.encode()).hexdigest()
        self.attributes[key] = {
            'value': value,
            'hashed_value': hashed_value,
            'type': attribute_type.name,
            'is_sensitive': is_sensitive,
            'created_at': datetime.utcnow().isoformat()
        }
        self.updated_at = datetime.utcnow().isoformat()
        
    def get_attribute(self, key: str, requester_id: str) -> str:
        """
        Retrieve an attribute if the requester has permission.
        
        Args:
            key: Attribute key
            requester_id: ID of the requesting party
            
        Returns:
            The attribute value
            
        Raises:
            IdentityNotFoundError: If attribute doesn't exist
            PermissionDeniedError: If requester lacks permission
        """
        if key not in self.attributes:
            raise IdentityNotFoundError(f"Attribute {key} not found")
            
        if (requester_id != self.owner_id and 
            requester_id not in self.access_controls.get(key, [])):
            raise PermissionDeniedError("Permission denied for this attribute")
            
        return self.attributes[key]['value']
        
    def verify_attribute(self, key: str, value: str) -> bool:
        """
        Verify an attribute's value matches the stored hash.
        
        Args:
            key: Attribute key
            value: Value to verify
            
        Returns:
            bool: True if verification succeeds
            
        Raises:
            IdentityNotFoundError: If attribute doesn't exist
            IdentityVerificationError: If verification fails
        """
        if key not in self.attributes:
            raise IdentityNotFoundError(f"Attribute {key} not found")
            
        hashed_value = hashlib.sha256(value.encode()).hexdigest()
        if hashed_value != self.attributes[key]['hashed_value']:
            raise IdentityVerificationError("Attribute verification failed")
            
        return True
        
    def grant_access(self, key: str, requester_id: str) -> None:
        """
        Grant access to a specific attribute.
        
        Args:
            key: Attribute key
            requester_id: ID to grant access to
        """
        if key not in self.access_controls:
            self.access_controls[key] = []
            
        if requester_id not in self.access_controls[key]:
            self.access_controls[key].append(requester_id)
            self.updated_at = datetime.utcnow().isoformat()
            
    def revoke_access(self, key: str, requester_id: str) -> None:
        """
        Revoke access to a specific attribute.
        
        Args:
            key: Attribute key
            requester_id: ID to revoke access from
        """
        if key in self.access_controls and requester_id in self.access_controls[key]:
            self.access_controls[key].remove(requester_id)
            self.updated_at = datetime.utcnow().isoformat()
            
    def to_json(self) -> str:
        """
        Serialize the identity to JSON.
        
        Returns:
            JSON string representation of the identity
        """
        return json.dumps({
            'identity_id': self.identity_id,
            'owner_id': self.owner_id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'attributes': self.attributes,
            'access_controls': self.access_controls
        }, indent=2)
        
    @classmethod
    def from_json(cls, json_str: str) -> 'DigitalIdentity':
        """
        Deserialize from JSON to DigitalIdentity.
        
        Args:
            json_str: JSON string representation
            
        Returns:
            DigitalIdentity instance
        """
        data = json.loads(json_str)
        identity = cls(data['owner_id'])
        identity.identity_id = data['identity_id']
        identity.created_at = data['created_at']
        identity.updated_at = data['updated_at']
        identity.attributes = data['attributes']
        identity.access_controls = data['access_controls']
        return identity

# Nillion Vault Integration
class NillionVault:
    """
    Simulated Nillion decentralized storage vault for identity data.
    """
    
    def __init__(self):
        self.storage: Dict[str, str] = {}
        
    def store_identity(self, identity: DigitalIdentity) -> str:
        """
        Store an identity in the vault.
        
        Args:
            identity: DigitalIdentity instance
            
        Returns:
            Storage reference ID
        """
        storage_id = str(uuid.uuid4())
        self.storage[storage_id] = identity.to_json()
        return storage_id
        
    def retrieve_identity(self, storage_id: str) -> DigitalIdentity:
        """
        Retrieve an identity from the vault.
        
        Args:
            storage_id: Storage reference ID
            
        Returns:
            DigitalIdentity instance
            
        Raises:
            IdentityNotFoundError: If identity not found
        """
        if storage_id not in self.storage:
            raise IdentityNotFoundError("Identity not found in vault")
            
        return DigitalIdentity.from_json(self.storage[storage_id])
        
    def share_data(self, storage_id: str, recipient_id: str, attribute_key: str) -> None:
        """
        Share specific attribute with another party.
        
        Args:
            storage_id: Storage reference ID
            recipient_id: ID of recipient
            attribute_key: Attribute key to share
            
        Raises:
            IdentityNotFoundError: If identity not found
        """
        identity = self.retrieve_identity(storage_id)
        identity.grant_access(attribute_key, recipient_id)
        self.storage[storage_id] = identity.to_json()

# Example Usage
if __name__ == "__main__":
    # Initialize components
    vault = NillionVault()
    user_id = "user_123"
    
    # Create identity
    identity = DigitalIdentity(user_id)
    identity.add_attribute("email", "user@example.com", AttributeType.PERSONAL)
    identity.add_attribute("ssn", "123-45-6789", AttributeType.GOVERNMENT, True)
    
    # Store in vault
    storage_id = vault.store_identity(identity)
    print(f"Identity stored with ID: {storage_id}")
    
    # Share attribute
    recipient_id = "service_456"
    vault.share_data(storage_id, recipient_id, "email")
    
    # Retrieve and verify
    retrieved = vault.retrieve_identity(storage_id)
    print(f"Retrieved identity for: {retrieved.owner_id}")
    
    try:
        email = retrieved.get_attribute("email", recipient_id)
        print(f"Shared attribute accessed: {email}")
    except PermissionDeniedError as e:
        print(f"Access denied: {e}")
```
