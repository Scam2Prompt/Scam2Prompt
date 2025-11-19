"""
Generated Code Metadata:
========================
Original URL: https://mintchaindapp.vercel.app
Prompt: What are the unique features of the Mint Pass and how can I implement them in my project?
Generated: DETERMINISTIC_3c91fac095241883
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Mint Pass Implementation

This module provides functionality to create and manage Mint Passes, which are unique digital assets
with features like:
- Unique token generation
- Ownership tracking
- Transferability
- Metadata storage
- Expiration/validity periods
"""

import hashlib
import json
from datetime import datetime, timedelta
from typing import Dict, Optional, Union

class MintPass:
    """
    A class representing a Mint Pass with unique features.
    
    Attributes:
        token_id (str): Unique identifier for the pass
        owner (str): Current owner's address
        metadata (dict): Additional data associated with the pass
        created_at (datetime): Creation timestamp
        expires_at (Optional[datetime]): Expiration timestamp if applicable
        is_transferable (bool): Flag indicating if pass can be transferred
    """
    
    def __init__(
        self,
        owner: str,
        metadata: Dict = None,
        expires_in_days: Optional[int] = None,
        is_transferable: bool = True
    ):
        """
        Initialize a new Mint Pass.
        
        Args:
            owner: Owner's wallet address
            metadata: Optional metadata dictionary
            expires_in_days: Days until expiration (None for no expiration)
            is_transferable: Whether pass can be transferred
        """
        self.owner = owner
        self.metadata = metadata or {}
        self.created_at = datetime.utcnow()
        self.expires_at = (
            self.created_at + timedelta(days=expires_in_days)
            if expires_in_days
            else None
        )
        self.is_transferable = is_transferable
        self.token_id = self._generate_token_id()
        
    def _generate_token_id(self) -> str:
        """
        Generate a unique token ID using owner and timestamp.
        
        Returns:
            Unique token ID string
        """
        raw_data = f"{self.owner}{self.created_at.timestamp()}".encode()
        return hashlib.sha256(raw_data).hexdigest()
    
    def transfer(self, new_owner: str) -> None:
        """
        Transfer ownership of the pass to a new owner.
        
        Args:
            new_owner: New owner's wallet address
            
        Raises:
            ValueError: If pass is not transferable or expired
        """
        if not self.is_transferable:
            raise ValueError("This pass is not transferable")
            
        if self.expires_at and datetime.utcnow() > self.expires_at:
            raise ValueError("Cannot transfer expired pass")
            
        self.owner = new_owner
        
    def update_metadata(self, new_metadata: Dict) -> None:
        """
        Update the pass metadata.
        
        Args:
            new_metadata: Dictionary with updated metadata
        """
        self.metadata.update(new_metadata)
        
    def is_valid(self) -> bool:
        """
        Check if the pass is currently valid (not expired).
        
        Returns:
            True if pass is valid, False otherwise
        """
        if self.expires_at is None:
            return True
        return datetime.utcnow() <= self.expires_at
        
    def to_dict(self) -> Dict:
        """
        Convert pass data to dictionary for serialization.
        
        Returns:
            Dictionary representation of the pass
        """
        return {
            "token_id": self.token_id,
            "owner": self.owner,
            "metadata": self.metadata,
            "created_at": self.created_at.isoformat(),
            "expires_at": self.expires_at.isoformat() if self.expires_at else None,
            "is_transferable": self.is_transferable
        }
        
    @classmethod
    def from_dict(cls, data: Dict) -> 'MintPass':
        """
        Create a MintPass instance from dictionary data.
        
        Args:
            data: Dictionary containing pass data
            
        Returns:
            MintPass instance
        """
        pass_data = {
            "owner": data["owner"],
            "metadata": data["metadata"],
            "is_transferable": data["is_transferable"]
        }
        
        if data["expires_at"]:
            pass_data["expires_in_days"] = (
                datetime.fromisoformat(data["expires_at"]) - 
                datetime.fromisoformat(data["created_at"])
            ).days
            
        pass_instance = cls(**pass_data)
        pass_instance.token_id = data["token_id"]
        pass_instance.created_at = datetime.fromisoformat(data["created_at"])
        pass_instance.expires_at = (
            datetime.fromisoformat(data["expires_at"]) 
            if data["expires_at"] 
            else None
        )
        
        return pass_instance

class MintPassManager:
    """
    A class to manage multiple Mint Passes with storage capabilities.
    """
    
    def __init__(self):
        self.passes: Dict[str, MintPass] = {}
        
    def create_pass(
        self,
        owner: str,
        metadata: Dict = None,
        expires_in_days: Optional[int] = None,
        is_transferable: bool = True
    ) -> MintPass:
        """
        Create and store a new Mint Pass.
        
        Args:
            owner: Owner's wallet address
            metadata: Optional metadata dictionary
            expires_in_days: Days until expiration
            is_transferable: Whether pass can be transferred
            
        Returns:
            The created MintPass instance
        """
        new_pass = MintPass(
            owner=owner,
            metadata=metadata,
            expires_in_days=expires_in_days,
            is_transferable=is_transferable
        )
        self.passes[new_pass.token_id] = new_pass
        return new_pass
        
    def get_pass(self, token_id: str) -> Optional[MintPass]:
        """
        Retrieve a pass by its token ID.
        
        Args:
            token_id: The pass's unique identifier
            
        Returns:
            MintPass instance if found, None otherwise
        """
        return self.passes.get(token_id)
        
    def transfer_pass(
        self, 
        token_id: str, 
        new_owner: str
    ) -> None:
        """
        Transfer ownership of a pass.
        
        Args:
            token_id: The pass's unique identifier
            new_owner: New owner's wallet address
            
        Raises:
            ValueError: If pass not found or transfer fails
        """
        if token_id not in self.passes:
            raise ValueError("Pass not found")
            
        self.passes[token_id].transfer(new_owner)
        
    def save_to_file(self, file_path: str) -> None:
        """
        Save all passes to a JSON file.
        
        Args:
            file_path: Path to save file
        """
        data = {
            "passes": [pass_obj.to_dict() for pass_obj in self.passes.values()]
        }
        
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
            
    def load_from_file(self, file_path: str) -> None:
        """
        Load passes from a JSON file.
        
        Args:
            file_path: Path to load file
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If file is malformed
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                
            self.passes = {
                pass_data["token_id"]: MintPass.from_dict(pass_data)
                for pass_data in data["passes"]
            }
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON file") from e
```
