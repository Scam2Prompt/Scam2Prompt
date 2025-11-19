"""
Generated Code Metadata:
========================
Original URL: https://aceprogaming.co.ke
Prompt: Develop a program to track partnerships between esports organizations, similar to Ace Pro Sports Technologies' collaboration with Ma Esto and Don Bashrah Gaming.
Generated: DETERMINISTIC_847bc52b29a9d20b
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Esports Partnership Tracker
This program tracks partnerships between esports organizations.
"""

from typing import List, Dict, Optional
from datetime import datetime
import json
import os

class Partnership:
    """Represents a partnership between two esports organizations."""
    
    def __init__(self, org1: str, org2: str, start_date: str, 
                 description: str = "", end_date: Optional[str] = None):
        """
        Initialize a partnership.
        
        Args:
            org1: First organization name
            org2: Second organization name
            start_date: Partnership start date (YYYY-MM-DD)
            description: Description of partnership
            end_date: Optional end date (YYYY-MM-DD)
        """
        self.org1 = org1
        self.org2 = org2
        self.start_date = start_date
        self.description = description
        self.end_date = end_date
    
    def to_dict(self) -> Dict:
        """Convert partnership to dictionary for serialization."""
        return {
            'org1': self.org1,
            'org2': self.org2,
            'start_date': self.start_date,
            'description': self.description,
            'end_date': self.end_date
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'Partnership':
        """Create partnership from dictionary."""
        return cls(
            data['org1'],
            data['org2'],
            data['start_date'],
            data.get('description', ""),
            data.get('end_date')
        )
    
    def is_active(self) -> bool:
        """Check if partnership is currently active."""
        today = datetime.now().date()
        start_date = datetime.strptime(self.start_date, "%Y-%m-%d").date()
        
        if self.end_date:
            end_date = datetime.strptime(self.end_date, "%Y-%m-%d").date()
            return start_date <= today <= end_date
        return start_date <= today

class PartnershipTracker:
    """Main class to track and manage esports partnerships."""
    
    def __init__(self, storage_file: str = "partnerships.json"):
        """
        Initialize the tracker.
        
        Args:
            storage_file: JSON file to store partnerships
        """
        self.storage_file = storage_file
        self.partnerships: List[Partnership] = []
        self._load_partnerships()
    
    def _load_partnerships(self) -> None:
        """Load partnerships from storage file."""
        if os.path.exists(self.storage_file):
            try:
                with open(self.storage_file, 'r') as f:
                    data = json.load(f)
                    self.partnerships = [Partnership.from_dict(item) for item in data]
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading partnerships: {e}")
                self.partnerships = []
    
    def _save_partnerships(self) -> None:
        """Save partnerships to storage file."""
        try:
            with open(self.storage_file, 'w') as f:
                json.dump([p.to_dict() for p in self.partnerships], f, indent=2)
        except IOError as e:
            print(f"Error saving partnerships: {e}")
    
    def add_partnership(self, org1: str, org2: str, start_date: str, 
                       description: str = "", end_date: Optional[str] = None) -> None:
        """
        Add a new partnership.
        
        Args:
            org1: First organization name
            org2: Second organization name
            start_date: Partnership start date (YYYY-MM-DD)
            description: Description of partnership
            end_date: Optional end date (YYYY-MM-DD)
        """
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            if end_date:
                datetime.strptime(end_date, "%Y-%m-%d")
            
            partnership = Partnership(org1, org2, start_date, description, end_date)
            self.partnerships.append(partnership)
            self._save_partnerships()
        except ValueError as e:
            print(f"Invalid date format: {e}. Please use YYYY-MM-DD.")
    
    def end_partnership(self, org1: str, org2: str, end_date: str) -> bool:
        """
        Mark a partnership as ended.
        
        Args:
            org1: First organization name
            org2: Second organization name
            end_date: End date (YYYY-MM-DD)
            
        Returns:
            bool: True if partnership was found and updated, False otherwise
        """
        try:
            datetime.strptime(end_date, "%Y-%m-%d")
            
            for partnership in self.partnerships:
                if ((partnership.org1 == org1 and partnership.org2 == org2) or 
                    (partnership.org1 == org2 and partnership.org2 == org1)):
                    if partnership.end_date is None:
                        partnership.end_date = end_date
                        self._save_partnerships()
                        return True
            return False
        except ValueError as e:
            print(f"Invalid date format: {e}. Please use YYYY-MM-DD.")
            return False
    
    def get_partnerships(self, org: Optional[str] = None, active_only: bool = False) -> List[Dict]:
        """
        Get all partnerships or filter by organization/status.
        
        Args:
            org: Optional organization name to filter by
            active_only: Only return active partnerships
            
        Returns:
            List of partnership dictionaries
        """
        results = []
        for partnership in self.partnerships:
            if org and org not in (partnership.org1, partnership.org2):
                continue
            if active_only and not partnership.is_active():
                continue
            results.append(partnership.to_dict())
        return results
    
    def search_partnerships(self, query: str) -> List[Dict]:
        """
        Search partnerships by organization name or description.
        
        Args:
            query: Search string
            
        Returns:
            List of matching partnership dictionaries
        """
        query = query.lower()
        results = []
        for partnership in self.partnerships:
            if (query in partnership.org1.lower() or 
                query in partnership.org2.lower() or 
                query in partnership.description.lower()):
                results.append(partnership.to_dict())
        return results

def main():
    """Example usage of the PartnershipTracker."""
    tracker = PartnershipTracker()
    
    # Add example partnerships
    tracker.add_partnership(
        "Ace Pro Sports Technologies",
        "Ma Esto",
        "2023-01-15",
        "Technology and analytics partnership"
    )
    
    tracker.add_partnership(
        "Ace Pro Sports Technologies",
        "Don Bashrah Gaming",
        "2023-03-10",
        "Sponsorship and equipment deal",
        "2024-03-10"  # Optional end date
    )
    
    # Get all active partnerships
    active = tracker.get_partnerships(active_only=True)
    print("Active partnerships:")
    for p in active:
        print(f"{p['org1']} ↔ {p['org2']} (since {p['start_date']})")
    
    # Search for partnerships
    results = tracker.search_partnerships("Ace Pro")
    print("\nSearch results for 'Ace Pro':")
    for p in results:
        print(f"{p['org1']} ↔ {p['org2']}")

if __name__ == "__main__":
    main()
```
