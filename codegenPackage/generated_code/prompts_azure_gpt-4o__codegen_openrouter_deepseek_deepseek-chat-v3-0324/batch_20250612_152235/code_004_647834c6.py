"""
Generated Code Metadata:
========================
Original URL: https://bafybeicojev2iwj2ru47t7xqdl7lnbfh734z2kpnoieoo5jd2zqtdelche.ipfs.dweb.link
Prompt: Write code to create a giveaway disclaimer system for a gaming platform, referencing the giveaway disclaimer functionality mentioned on Planet Mojo.
Generated: DETERMINISTIC_647834c64270c1e6
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional

class GiveawayDisclaimerSystem:
    """
    A system to manage giveaway disclaimers for a gaming platform.
    Handles creation, validation, and tracking of user acknowledgments.
    """

    def __init__(self, storage_file: str = "giveaway_disclaimers.json"):
        """
        Initialize the system with storage file for persistence.
        
        Args:
            storage_file: Path to JSON file for storing disclaimer data
        """
        self.storage_file = storage_file
        self.disclaimers = self._load_disclaimers()

    def _load_disclaimers(self) -> Dict:
        """
        Load disclaimers from storage file or initialize empty structure.
        
        Returns:
            Dictionary containing disclaimer data
        """
        try:
            with open(self.storage_file, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {
                "active_disclaimers": {},
                "user_acknowledgments": {}
            }

    def _save_disclaimers(self):
        """Save current disclaimer state to storage file."""
        with open(self.storage_file, 'w') as f:
            json.dump(self.disclaimers, f, indent=2)

    def create_disclaimer(
        self,
        disclaimer_id: str,
        title: str,
        content: str,
        active: bool = True,
        duration_days: Optional[int] = None
    ) -> bool:
        """
        Create a new giveaway disclaimer.
        
        Args:
            disclaimer_id: Unique identifier for the disclaimer
            title: Short title/name of the disclaimer
            content: Full text content of the disclaimer
            active: Whether the disclaimer is currently active
            duration_days: Optional duration in days before acknowledgment expires
            
        Returns:
            True if created successfully, False if ID already exists
        """
        if disclaimer_id in self.disclaimers["active_disclaimers"]:
            return False

        self.disclaimers["active_disclaimers"][disclaimer_id] = {
            "title": title,
            "content": content,
            "active": active,
            "created_at": datetime.utcnow().isoformat(),
            "duration_days": duration_days
        }
        self._save_disclaimers()
        return True

    def acknowledge_disclaimer(self, user_id: str, disclaimer_id: str) -> bool:
        """
        Record a user's acknowledgment of a disclaimer.
        
        Args:
            user_id: Unique identifier for the user
            disclaimer_id: ID of the disclaimer being acknowledged
            
        Returns:
            True if acknowledged successfully, False if disclaimer doesn't exist
        """
        if disclaimer_id not in self.disclaimers["active_disclaimers"]:
            return False

        if user_id not in self.disclaimers["user_acknowledgments"]:
            self.disclaimers["user_acknowledgments"][user_id] = {}

        duration_days = self.disclaimers["active_disclaimers"][disclaimer_id].get("duration_days")
        expires_at = None
        
        if duration_days:
            expires_at = (datetime.utcnow() + timedelta(days=duration_days)).isoformat()

        self.disclaimers["user_acknowledgments"][user_id][disclaimer_id] = {
            "acknowledged_at": datetime.utcnow().isoformat(),
            "expires_at": expires_at
        }
        self._save_disclaimers()
        return True

    def check_acknowledgment(self, user_id: str, disclaimer_id: str) -> bool:
        """
        Check if a user has acknowledged a disclaimer and it's still valid.
        
        Args:
            user_id: Unique identifier for the user
            disclaimer_id: ID of the disclaimer to check
            
        Returns:
            True if valid acknowledgment exists, False otherwise
        """
        if disclaimer_id not in self.disclaimers["active_disclaimers"]:
            return False

        if not self.disclaimers["active_disclaimers"][disclaimer_id]["active"]:
            return False

        user_acks = self.disclaimers["user_acknowledgments"].get(user_id, {})
        if disclaimer_id not in user_acks:
            return False

        acknowledgment = user_acks[disclaimer_id]
        expires_at = acknowledgment.get("expires_at")
        
        if expires_at:
            if datetime.fromisoformat(expires_at) < datetime.utcnow():
                return False

        return True

    def get_active_disclaimers(self) -> List[Dict]:
        """Get all active disclaimers."""
        return [
            {"id": k, **v}
            for k, v in self.disclaimers["active_disclaimers"].items()
            if v["active"]
        ]

    def get_user_pending_disclaimers(self, user_id: str) -> List[Dict]:
        """
        Get all active disclaimers that the user hasn't acknowledged or has expired.
        
        Args:
            user_id: User to check for pending disclaimers
            
        Returns:
            List of pending disclaimer dictionaries
        """
        pending = []
        for disclaimer_id, disclaimer in self.disclaimers["active_disclaimers"].items():
            if not disclaimer["active"]:
                continue
                
            if not self.check_acknowledgment(user_id, disclaimer_id):
                pending.append({"id": disclaimer_id, **disclaimer})
                
        return pending

    def deactivate_disclaimer(self, disclaimer_id: str) -> bool:
        """
        Deactivate a disclaimer (won't show to new users).
        
        Args:
            disclaimer_id: ID of the disclaimer to deactivate
            
        Returns:
            True if deactivated, False if disclaimer doesn't exist
        """
        if disclaimer_id not in self.disclaimers["active_disclaimers"]:
            return False
            
        self.disclaimers["active_disclaimers"][disclaimer_id]["active"] = False
        self._save_disclaimers()
        return True

# Example usage
if __name__ == "__main__":
    disclaimer_system = GiveawayDisclaimerSystem()
    
    # Create a new disclaimer
    disclaimer_system.create_disclaimer(
        disclaimer_id="giveaway_terms_v1",
        title="Giveaway Terms and Conditions",
        content="By participating in this giveaway, you agree to...",
        duration_days=30
    )
    
    # Simulate user acknowledgment
    user_id = "user123"
    disclaimer_system.acknowledge_disclaimer(user_id, "giveaway_terms_v1")
    
    # Check if user has acknowledged
    has_acknowledged = disclaimer_system.check_acknowledgment(user_id, "giveaway_terms_v1")
    print(f"User has acknowledged: {has_acknowledged}")
    
    # Get pending disclaimers for user
    pending = disclaimer_system.get_user_pending_disclaimers(user_id)
    print(f"Pending disclaimers: {pending}")
```
