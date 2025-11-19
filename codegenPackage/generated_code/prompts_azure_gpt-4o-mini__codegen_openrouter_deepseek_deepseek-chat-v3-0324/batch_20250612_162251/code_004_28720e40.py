"""
Generated Code Metadata:
========================
Original URL: https://parallels.top
Prompt: Explain how to implement a system for users to showcase their Avatars in future Parallel media and comics.
Generated: DETERMINISTIC_28720e4041b0aabf
Batch ID: 20250612_162251
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# avatar_showcase_system.py

import os
import json
from typing import Dict, List, Optional
from dataclasses import dataclass, asdict
from uuid import uuid4
from datetime import datetime

# Error classes
class AvatarShowcaseError(Exception):
    """Base exception for Avatar Showcase system errors."""
    pass

class AvatarNotFoundError(AvatarShowcaseError):
    """Raised when an avatar is not found."""
    pass

class UserNotFoundError(AvatarShowcaseError):
    """Raised when a user is not found."""
    pass

class InvalidAvatarDataError(AvatarShowcaseError):
    """Raised when avatar data is invalid."""
    pass

@dataclass
class Avatar:
    """Represents a user's avatar with metadata."""
    avatar_id: str
    user_id: str
    name: str
    image_url: str
    traits: Dict[str, str]
    created_at: str
    updated_at: str
    is_public: bool = False

    def to_dict(self) -> Dict:
        """Convert Avatar instance to dictionary."""
        return asdict(self)

class AvatarShowcaseSystem:
    """System for users to showcase their Avatars in media and comics."""
    
    def __init__(self, storage_path: str = "avatar_data"):
        """
        Initialize the showcase system.
        
        Args:
            storage_path: Path to store avatar data (default: "avatar_data")
        """
        self.storage_path = storage_path
        os.makedirs(self.storage_path, exist_ok=True)
        
    def _get_user_filepath(self, user_id: str) -> str:
        """Get filepath for user's avatar data."""
        return os.path.join(self.storage_path, f"{user_id}.json")
    
    def _load_user_avatars(self, user_id: str) -> Dict[str, Avatar]:
        """Load a user's avatars from storage."""
        filepath = self._get_user_filepath(user_id)
        if not os.path.exists(filepath):
            return {}
            
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
                return {avatar_id: Avatar(**avatar_data) for avatar_id, avatar_data in data.items()}
        except (json.JSONDecodeError, IOError) as e:
            raise AvatarShowcaseError(f"Failed to load avatars for user {user_id}: {str(e)}")
    
    def _save_user_avatars(self, user_id: str, avatars: Dict[str, Avatar]) -> None:
        """Save a user's avatars to storage."""
        filepath = self._get_user_filepath(user_id)
        try:
            with open(filepath, 'w') as f:
                avatars_dict = {avatar_id: avatar.to_dict() for avatar_id, avatar in avatars.items()}
                json.dump(avatars_dict, f, indent=2)
        except (IOError, TypeError) as e:
            raise AvatarShowcaseError(f"Failed to save avatars for user {user_id}: {str(e)}")
    
    def create_avatar(
        self,
        user_id: str,
        name: str,
        image_url: str,
        traits: Dict[str, str],
        is_public: bool = False
    ) -> Avatar:
        """
        Create a new avatar for a user.
        
        Args:
            user_id: ID of the user
            name: Name of the avatar
            image_url: URL to the avatar image
            traits: Dictionary of avatar traits
            is_public: Whether the avatar is public (default: False)
            
        Returns:
            The created Avatar instance
            
        Raises:
            InvalidAvatarDataError: If required data is missing
        """
        if not all([user_id, name, image_url]):
            raise InvalidAvatarDataError("Missing required avatar data")
            
        timestamp = datetime.utcnow().isoformat()
        avatar_id = str(uuid4())
        
        avatar = Avatar(
            avatar_id=avatar_id,
            user_id=user_id,
            name=name,
            image_url=image_url,
            traits=traits,
            created_at=timestamp,
            updated_at=timestamp,
            is_public=is_public
        )
        
        avatars = self._load_user_avatars(user_id)
        avatars[avatar_id] = avatar
        self._save_user_avatars(user_id, avatars)
        
        return avatar
    
    def get_avatar(self, user_id: str, avatar_id: str) -> Avatar:
        """
        Get a specific avatar for a user.
        
        Args:
            user_id: ID of the user
            avatar_id: ID of the avatar
            
        Returns:
            The requested Avatar instance
            
        Raises:
            UserNotFoundError: If user doesn't exist
            AvatarNotFoundError: If avatar doesn't exist
        """
        avatars = self._load_user_avatars(user_id)
        if not avatars:
            raise UserNotFoundError(f"User {user_id} not found")
            
        if avatar_id not in avatars:
            raise AvatarNotFoundError(f"Avatar {avatar_id} not found for user {user_id}")
            
        return avatars[avatar_id]
    
    def update_avatar(
        self,
        user_id: str,
        avatar_id: str,
        name: Optional[str] = None,
        image_url: Optional[str] = None,
        traits: Optional[Dict[str, str]] = None,
        is_public: Optional[bool] = None
    ) -> Avatar:
        """
        Update an existing avatar.
        
        Args:
            user_id: ID of the user
            avatar_id: ID of the avatar
            name: New name (optional)
            image_url: New image URL (optional)
            traits: New traits (optional)
            is_public: New public status (optional)
            
        Returns:
            The updated Avatar instance
            
        Raises:
            UserNotFoundError: If user doesn't exist
            AvatarNotFoundError: If avatar doesn't exist
        """
        avatars = self._load_user_avatars(user_id)
        if not avatars:
            raise UserNotFoundError(f"User {user_id} not found")
            
        if avatar_id not in avatars:
            raise AvatarNotFoundError(f"Avatar {avatar_id} not found for user {user_id}")
            
        avatar = avatars[avatar_id]
        
        if name is not None:
            avatar.name = name
        if image_url is not None:
            avatar.image_url = image_url
        if traits is not None:
            avatar.traits = traits
        if is_public is not None:
            avatar.is_public = is_public
            
        avatar.updated_at = datetime.utcnow().isoformat()
        
        self._save_user_avatars(user_id, avatars)
        return avatar
    
    def delete_avatar(self, user_id: str, avatar_id: str) -> None:
        """
        Delete an avatar.
        
        Args:
            user_id: ID of the user
            avatar_id: ID of the avatar
            
        Raises:
            UserNotFoundError: If user doesn't exist
            AvatarNotFoundError: If avatar doesn't exist
        """
        avatars = self._load_user_avatars(user_id)
        if not avatars:
            raise UserNotFoundError(f"User {user_id} not found")
            
        if avatar_id not in avatars:
            raise AvatarNotFoundError(f"Avatar {avatar_id} not found for user {user_id}")
            
        del avatars[avatar_id]
        self._save_user_avatars(user_id, avatars)
    
    def list_user_avatars(self, user_id: str) -> List[Avatar]:
        """
        List all avatars for a user.
        
        Args:
            user_id: ID of the user
            
        Returns:
            List of Avatar instances
            
        Raises:
            UserNotFoundError: If user doesn't exist
        """
        avatars = self._load_user_avatars(user_id)
        if not avatars:
            raise UserNotFoundError(f"User {user_id} not found")
            
        return list(avatars.values())
    
    def list_public_avatars(self) -> List[Avatar]:
        """
        List all public avatars across all users.
        
        Returns:
            List of public Avatar instances
        """
        public_avatars = []
        
        for filename in os.listdir(self.storage_path):
            if filename.endswith('.json'):
                user_id = filename[:-5]  # Remove .json extension
                try:
                    avatars = self._load_user_avatars(user_id)
                    public_avatars.extend(
                        avatar for avatar in avatars.values() 
                        if avatar.is_public
                    )
                except AvatarShowcaseError:
                    continue
                    
        return public_avatars
```
