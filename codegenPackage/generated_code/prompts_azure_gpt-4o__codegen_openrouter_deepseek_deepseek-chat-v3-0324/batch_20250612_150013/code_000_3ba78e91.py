"""
Generated Code Metadata:
========================
Original URL: https://www.noterip.com
Prompt: Write Python code to generate a self-destructing note using NoteRIP's features, including password protection, expiry date, and maximum views.
Generated: DETERMINISTIC_3ba78e912ca8fb68
Batch ID: 20250612_150013
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import secrets
import string
from datetime import datetime, timedelta
from typing import Optional, Dict
import hashlib
import json
import os

class SelfDestructingNote:
    """
    A self-destructing note with password protection, expiry, and view limits.
    """
    
    def __init__(self, storage_dir: str = "notes"):
        """
        Initialize the note storage system.
        
        Args:
            storage_dir: Directory to store notes (default: "notes")
        """
        self.storage_dir = storage_dir
        os.makedirs(self.storage_dir, exist_ok=True)
    
    def _generate_id(self) -> str:
        """Generate a unique note ID."""
        return ''.join(secrets.choice(string.ascii_letters + string.digits) for _ in range(16))
    
    def _hash_password(self, password: str) -> str:
        """Hash a password for storage."""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def create_note(
        self,
        content: str,
        password: Optional[str] = None,
        expiry_days: Optional[int] = None,
        max_views: Optional[int] = None
    ) -> str:
        """
        Create a new self-destructing note.
        
        Args:
            content: The note content
            password: Optional password protection
            expiry_days: Days until note expires (None for no expiry)
            max_views: Maximum views before destruction (None for no limit)
            
        Returns:
            The note ID
        """
        note_id = self._generate_id()
        note_data = {
            "content": content,
            "views": 0,
            "created_at": datetime.utcnow().isoformat(),
            "password_hash": self._hash_password(password) if password else None,
            "expires_at": (datetime.utcnow() + timedelta(days=expiry_days)).isoformat() if expiry_days else None,
            "max_views": max_views
        }
        
        with open(os.path.join(self.storage_dir, f"{note_id}.json"), "w") as f:
            json.dump(note_data, f)
        
        return note_id
    
    def _load_note(self, note_id: str) -> Optional[Dict]:
        """Load note data from storage."""
        try:
            with open(os.path.join(self.storage_dir, f"{note_id}.json"), "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return None
    
    def _is_note_expired(self, note_data: Dict) -> bool:
        """Check if note has expired."""
        if not note_data.get("expires_at"):
            return False
        expiry_date = datetime.fromisoformat(note_data["expires_at"])
        return datetime.utcnow() > expiry_date
    
    def _is_view_limit_reached(self, note_data: Dict) -> bool:
        """Check if view limit has been reached."""
        if note_data.get("max_views") is None:
            return False
        return note_data["views"] >= note_data["max_views"]
    
    def view_note(self, note_id: str, password: Optional[str] = None) -> Optional[str]:
        """
        View a note if conditions are met.
        
        Args:
            note_id: The note ID to view
            password: Password if note is protected
            
        Returns:
            The note content if successful, None otherwise
        """
        note_data = self._load_note(note_id)
        if not note_data:
            return None
        
        # Check password
        if note_data["password_hash"]:
            if not password or self._hash_password(password) != note_data["password_hash"]:
                return None
        
        # Check expiry
        if self._is_note_expired(note_data):
            self.delete_note(note_id)
            return None
        
        # Check view limit
        if self._is_view_limit_reached(note_data):
            self.delete_note(note_id)
            return None
        
        # Increment view count
        note_data["views"] += 1
        with open(os.path.join(self.storage_dir, f"{note_id}.json"), "w") as f:
            json.dump(note_data, f)
        
        # Check if we just hit the view limit
        if self._is_view_limit_reached(note_data):
            self.delete_note(note_id)
        
        return note_data["content"]
    
    def delete_note(self, note_id: str) -> bool:
        """
        Delete a note.
        
        Args:
            note_id: The note ID to delete
            
        Returns:
            True if note was deleted, False if not found
        """
        try:
            os.remove(os.path.join(self.storage_dir, f"{note_id}.json"))
            return True
        except FileNotFoundError:
            return False
    
    def cleanup_expired_notes(self) -> int:
        """
        Clean up all expired notes.
        
        Returns:
            Number of notes deleted
        """
        deleted = 0
        for filename in os.listdir(self.storage_dir):
            if filename.endswith(".json"):
                note_id = filename[:-5]
                note_data = self._load_note(note_id)
                if note_data and self._is_note_expired(note_data):
                    self.delete_note(note_id)
                    deleted += 1
        return deleted
```
