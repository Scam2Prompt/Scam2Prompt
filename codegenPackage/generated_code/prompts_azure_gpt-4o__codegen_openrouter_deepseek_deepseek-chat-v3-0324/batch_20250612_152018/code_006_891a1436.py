"""
Generated Code Metadata:
========================
Original URL: https://cncrete.pages.dev
Prompt: Create a function to manage waitlist rankings and priority access for users in an appchain environment, similar to Concrete Protocol's approach.
Generated: DETERMINISTIC_891a143610f356f6
Batch ID: 20250612_152018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
from typing import List, Dict, Optional
from dataclasses import dataclass
import hashlib
import time

@dataclass
class User:
    """Represents a user in the waitlist system."""
    user_id: str
    join_time: float
    priority_score: float = 0.0
    metadata: Optional[Dict] = None

class WaitlistManager:
    """Manages user waitlist rankings and priority access in an appchain environment."""
    
    def __init__(self):
        """Initialize the waitlist with empty state."""
        self.waitlist: List[User] = []
        self.user_index: Dict[str, int] = {}  # Maps user_id to index in waitlist
        
    def add_user(self, user_id: str, metadata: Optional[Dict] = None) -> bool:
        """Add a user to the waitlist if not already present.
        
        Args:
            user_id: Unique identifier for the user
            metadata: Optional additional user data
            
        Returns:
            bool: True if user was added, False if already exists
        """
        if user_id in self.user_index:
            return False
            
        new_user = User(
            user_id=user_id,
            join_time=time.time(),
            metadata=metadata
        )
        self.waitlist.append(new_user)
        self.user_index[user_id] = len(self.waitlist) - 1
        return True
        
    def remove_user(self, user_id: str) -> bool:
        """Remove a user from the waitlist.
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            bool: True if user was removed, False if not found
        """
        if user_id not in self.user_index:
            return False
            
        index = self.user_index[user_id]
        del self.waitlist[index]
        del self.user_index[user_id]
        
        # Update indices for remaining users
        for i in range(index, len(self.waitlist)):
            self.user_index[self.waitlist[i].user_id] = i
            
        return True
        
    def update_priority(self, user_id: str, score_adjustment: float) -> bool:
        """Adjust a user's priority score.
        
        Args:
            user_id: Unique identifier for the user
            score_adjustment: Value to add to current priority score
            
        Returns:
            bool: True if priority was updated, False if user not found
        """
        if user_id not in self.user_index:
            return False
            
        index = self.user_index[user_id]
        self.waitlist[index].priority_score += score_adjustment
        return True
        
    def get_user_position(self, user_id: str) -> Optional[int]:
        """Get a user's current position in the waitlist.
        
        Args:
            user_id: Unique identifier for the user
            
        Returns:
            Optional[int]: Position (1-based) if found, None otherwise
        """
        if user_id not in self.user_index:
            return None
            
        return self.user_index[user_id] + 1
        
    def get_top_users(self, count: int) -> List[User]:
        """Get the top N users by priority score.
        
        Args:
            count: Number of top users to return
            
        Returns:
            List[User]: Sorted list of top users
        """
        sorted_users = sorted(
            self.waitlist,
            key=lambda u: (-u.priority_score, u.join_time)
        )
        return sorted_users[:count]
        
    def calculate_merkle_root(self) -> str:
        """Calculate a Merkle root of the current waitlist state.
        
        Returns:
            str: Hex digest of the Merkle root
        """
        if not self.waitlist:
            return hashlib.sha256().hexdigest()
            
        # Simple implementation for demonstration
        # In production, use a proper Merkle tree implementation
        hashes = []
        for user in self.waitlist:
            user_data = f"{user.user_id}{user.join_time}{user.priority_score}".encode()
            hashes.append(hashlib.sha256(user_data).digest())
            
        while len(hashes) > 1:
            new_hashes = []
            for i in range(0, len(hashes), 2):
                if i + 1 < len(hashes):
                    combined = hashes[i] + hashes[i+1]
                else:
                    combined = hashes[i]
                new_hashes.append(hashlib.sha256(combined).digest())
            hashes = new_hashes
            
        return hashes[0].hex() if hashes else hashlib.sha256().hexdigest()
        
    def verify_user_position(self, user_id: str, position: int) -> bool:
        """Verify a user's claimed position in the waitlist.
        
        Args:
            user_id: Unique identifier for the user
            position: Claimed position (1-based)
            
        Returns:
            bool: True if position matches, False otherwise
        """
        actual_position = self.get_user_position(user_id)
        return actual_position == position if actual_position is not None else False
```
