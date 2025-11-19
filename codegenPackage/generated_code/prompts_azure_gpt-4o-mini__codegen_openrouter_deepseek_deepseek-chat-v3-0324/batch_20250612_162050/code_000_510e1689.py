"""
Generated Code Metadata:
========================
Original URL: https://southernbrass.com
Prompt: Generate code to integrate a Smart Key Control System for quick key replacement in a door hardware application.
Generated: DETERMINISTIC_510e1689898b927a
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional, Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class KeyStatus(Enum):
    """Enum representing possible key statuses."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    LOST = "lost"
    REVOKED = "revoked"

class DoorLockStatus(Enum):
    """Enum representing possible door lock statuses."""
    LOCKED = "locked"
    UNLOCKED = "unlocked"
    JAMMED = "jammed"

class SmartKey:
    """Class representing a smart key with unique identifier and status."""
    
    def __init__(self, key_id: str, status: KeyStatus = KeyStatus.ACTIVE):
        self.key_id = key_id
        self.status = status
    
    def update_status(self, new_status: KeyStatus) -> bool:
        """Update the key's status."""
        if not isinstance(new_status, KeyStatus):
            logger.error(f"Invalid status type: {type(new_status)}")
            return False
        
        self.status = new_status
        logger.info(f"Key {self.key_id} status updated to {new_status.value}")
        return True

class DoorLock:
    """Class representing a door lock that can be controlled by smart keys."""
    
    def __init__(self, lock_id: str):
        self.lock_id = lock_id
        self.status = DoorLockStatus.LOCKED
        self.authorized_keys: Dict[str, SmartKey] = {}
    
    def add_key(self, key: SmartKey) -> bool:
        """Authorize a new key for this lock."""
        if not isinstance(key, SmartKey):
            logger.error("Invalid key type")
            return False
        
        if key.key_id in self.authorized_keys:
            logger.warning(f"Key {key.key_id} already authorized for this lock")
            return False
        
        self.authorized_keys[key.key_id] = key
        logger.info(f"Key {key.key_id} added to lock {self.lock_id}")
        return True
    
    def remove_key(self, key_id: str) -> bool:
        """Remove key authorization from this lock."""
        if key_id not in self.authorized_keys:
            logger.warning(f"Key {key_id} not found in authorized keys")
            return False
        
        del self.authorized_keys[key_id]
        logger.info(f"Key {key_id} removed from lock {self.lock_id}")
        return True
    
    def unlock(self, key_id: str) -> bool:
        """Attempt to unlock the door with a key."""
        if self.status == DoorLockStatus.JAMMED:
            logger.error("Lock is jammed and cannot be operated")
            return False
        
        if key_id not in self.authorized_keys:
            logger.warning(f"Unauthorized key {key_id} attempted to unlock")
            return False
        
        key = self.authorized_keys[key_id]
        if key.status != KeyStatus.ACTIVE:
            logger.warning(f"Key {key_id} is not active (status: {key.status.value})")
            return False
        
        self.status = DoorLockStatus.UNLOCKED
        logger.info(f"Lock {self.lock_id} unlocked by key {key_id}")
        return True
    
    def lock(self) -> bool:
        """Lock the door."""
        if self.status == DoorLockStatus.JAMMED:
            logger.error("Lock is jammed and cannot be operated")
            return False
        
        self.status = DoorLockStatus.LOCKED
        logger.info(f"Lock {self.lock_id} locked")
        return True

class KeyManagementSystem:
    """Central system for managing smart keys and door locks."""
    
    def __init__(self):
        self.keys: Dict[str, SmartKey] = {}
        self.locks: Dict[str, DoorLock] = {}
    
    def register_key(self, key_id: str) -> Optional[SmartKey]:
        """Register a new smart key."""
        if key_id in self.keys:
            logger.warning(f"Key {key_id} already registered")
            return None
        
        key = SmartKey(key_id)
        self.keys[key_id] = key
        logger.info(f"Key {key_id} registered")
        return key
    
    def register_lock(self, lock_id: str) -> Optional[DoorLock]:
        """Register a new door lock."""
        if lock_id in self.locks:
            logger.warning(f"Lock {lock_id} already registered")
            return None
        
        lock = DoorLock(lock_id)
        self.locks[lock_id] = lock
        logger.info(f"Lock {lock_id} registered")
        return lock
    
    def replace_key(self, old_key_id: str, new_key_id: str) -> bool:
        """
        Replace a lost/compromised key with a new one across all locks.
        
        Args:
            old_key_id: The ID of the key to be replaced
            new_key_id: The ID of the new replacement key
            
        Returns:
            bool: True if replacement was successful, False otherwise
        """
        if old_key_id not in self.keys:
            logger.error(f"Old key {old_key_id} not found")
            return False
        
        if new_key_id in self.keys:
            logger.error(f"New key {new_key_id} already exists")
            return False
        
        # Mark old key as revoked
        self.keys[old_key_id].update_status(KeyStatus.REVOKED)
        
        # Create new key
        new_key = self.register_key(new_key_id)
        if not new_key:
            return False
        
        # Replace old key with new key in all locks
        for lock in self.locks.values():
            if old_key_id in lock.authorized_keys:
                lock.remove_key(old_key_id)
                lock.add_key(new_key)
        
        logger.info(f"Successfully replaced key {old_key_id} with {new_key_id}")
        return True
    
    def get_key_status(self, key_id: str) -> Optional[KeyStatus]:
        """Get the status of a registered key."""
        if key_id not in self.keys:
            logger.warning(f"Key {key_id} not found")
            return None
        return self.keys[key_id].status
    
    def get_lock_status(self, lock_id: str) -> Optional[DoorLockStatus]:
        """Get the status of a registered lock."""
        if lock_id not in self.locks:
            logger.warning(f"Lock {lock_id} not found")
            return None
        return self.locks[lock_id].status

# Example usage
if __name__ == "__main__":
    kms = KeyManagementSystem()
    
    # Register keys and locks
    key1 = kms.register_key("key001")
    key2 = kms.register_key("key002")
    lock1 = kms.register_lock("lock001")
    
    # Authorize keys for locks
    if lock1:
        lock1.add_key(key1)
        lock1.add_key(key2)
    
    # Test unlocking
    if lock1:
        lock1.unlock("key001")
        lock1.lock()
    
    # Replace a key
    kms.replace_key("key001", "key003")
```
