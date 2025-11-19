"""
Generated Code Metadata:
========================
Original URL: https://atlas3io-moonseeker.web.app
Prompt: Generate a script to track and display raffle entries for a DAO whitelist application, including features like entry requirements and task completion, inspired by the Atlas3 MoonSeeker DAO.
Generated: DETERMINISTIC_4d36af4863ff3d4d
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import hashlib
import time
from typing import List, Dict, Optional
from dataclasses import dataclass, field
from datetime import datetime, timedelta

@dataclass
class RaffleEntry:
    """Represents a single raffle entry with participant details and task completion status."""
    participant_address: str
    tasks_completed: Dict[str, bool] = field(default_factory=dict)
    entry_time: datetime = field(default_factory=datetime.now)
    verified: bool = False

    def complete_task(self, task_name: str) -> None:
        """Mark a specific task as completed."""
        self.tasks_completed[task_name] = True

    def meets_requirements(self, required_tasks: List[str]) -> bool:
        """Check if participant has completed all required tasks."""
        return all(self.tasks_completed.get(task, False) for task in required_tasks)

    def to_dict(self) -> Dict:
        """Convert entry to dictionary for serialization."""
        return {
            'participant_address': self.participant_address,
            'tasks_completed': self.tasks_completed,
            'entry_time': self.entry_time.isoformat(),
            'verified': self.verified
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'RaffleEntry':
        """Create entry from dictionary."""
        entry = cls(
            participant_address=data['participant_address'],
            tasks_completed=data['tasks_completed'],
            verified=data['verified']
        )
        entry.entry_time = datetime.fromisoformat(data['entry_time'])
        return entry

class RaffleTracker:
    """Main class to track and manage raffle entries for DAO whitelist."""
    
    def __init__(self, required_tasks: List[str], max_entries: int = 1000):
        """
        Initialize raffle tracker with required tasks and maximum entries.
        
        Args:
            required_tasks: List of task names that must be completed for valid entry
            max_entries: Maximum number of entries allowed
        """
        self.required_tasks = required_tasks
        self.max_entries = max_entries
        self.entries: List[RaffleEntry] = []
        self.entry_hashes = set()

    def add_entry(self, participant_address: str, tasks_completed: Dict[str, bool]) -> bool:
        """
        Add a new raffle entry if requirements are met and there's space.
        
        Args:
            participant_address: Participant's wallet address
            tasks_completed: Dictionary of task completion status
            
        Returns:
            bool: True if entry was added successfully
        """
        if len(self.entries) >= self.max_entries:
            return False

        entry_hash = hashlib.sha256(participant_address.encode()).hexdigest()
        if entry_hash in self.entry_hashes:
            return False

        entry = RaffleEntry(participant_address, tasks_completed)
        if not entry.meets_requirements(self.required_tasks):
            return False

        self.entries.append(entry)
        self.entry_hashes.add(entry_hash)
        return True

    def verify_entry(self, participant_address: str) -> bool:
        """Verify a participant's entry if all requirements are met."""
        for entry in self.entries:
            if entry.participant_address == participant_address:
                if entry.meets_requirements(self.required_tasks):
                    entry.verified = True
                    return True
        return False

    def get_verified_entries(self) -> List[RaffleEntry]:
        """Get all verified entries."""
        return [entry for entry in self.entries if entry.verified]

    def get_pending_entries(self) -> List[RaffleEntry]:
        """Get all entries pending verification."""
        return [entry for entry in self.entries if not entry.verified]

    def save_to_file(self, filename: str) -> bool:
        """Save raffle data to JSON file."""
        try:
            data = {
                'required_tasks': self.required_tasks,
                'max_entries': self.max_entries,
                'entries': [entry.to_dict() for entry in self.entries],
                'entry_hashes': list(self.entry_hashes)
            }
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False

    @classmethod
    def load_from_file(cls, filename: str) -> Optional['RaffleTracker']:
        """Load raffle data from JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            tracker = cls(data['required_tasks'], data['max_entries'])
            tracker.entries = [RaffleEntry.from_dict(entry) for entry in data['entries']]
            tracker.entry_hashes = set(data['entry_hashes'])
            return tracker
        except Exception as e:
            print(f"Error loading file: {e}")
            return None

    def display_entries(self, verified_only: bool = False) -> None:
        """Display all entries in a readable format."""
        entries = self.get_verified_entries() if verified_only else self.entries
        print(f"\n{'Verified ' if verified_only else ''}Raffle Entries ({len(entries)}):")
        print("-" * 50)
        for idx, entry in enumerate(entries, 1):
            status = "VERIFIED" if entry.verified else "PENDING"
            print(f"{idx}. {entry.participant_address[:10]}... ({status})")
            print(f"   Tasks: {', '.join([f'{k}: {"✓" if v else "✗"}' for k, v in entry.tasks_completed.items()])}")
            print(f"   Entry Time: {entry.entry_time.strftime('%Y-%m-%d %H:%M:%S')}")
            print("-" * 50)

def main():
    """Example usage of the RaffleTracker."""
    # Example required tasks for the DAO whitelist
    required_tasks = [
        "follow_twitter",
        "join_discord",
        "retweet_pin",
        "wallet_connected"
    ]
    
    # Initialize tracker
    tracker = RaffleTracker(required_tasks, max_entries=500)
    
    # Add some example entries
    tracker.add_entry(
        "0x1234567890abcdef1234567890abcdef12345678",
        {"follow_twitter": True, "join_discord": True, "retweet_pin": True, "wallet_connected": True}
    )
    
    tracker.add_entry(
        "0xabcdef1234567890abcdef1234567890abcdef12",
        {"follow_twitter": True, "join_discord": False, "retweet_pin": True, "wallet_connected": True}
    )
    
    # Verify entries that meet requirements
    tracker.verify_entry("0x1234567890abcdef1234567890abcdef12345678")
    
    # Display all entries
    tracker.display_entries()
    
    # Display only verified entries
    tracker.display_entries(verified_only=True)
    
    # Save to file
    tracker.save_to_file("raffle_entries.json")
    
    # Load from file
    loaded_tracker = RaffleTracker.load_from_file("raffle_entries.json")
    if loaded_tracker:
        loaded_tracker.display_entries()

if __name__ == "__main__":
    main()
```
