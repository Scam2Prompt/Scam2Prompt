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
import json
from typing import List, Dict, Optional

class Partnership:
    """Class to represent a partnership between esports organizations."""
    
    def __init__(self, organization_a: str, organization_b: str, start_date: str, end_date: Optional[str] = None):
        """
        Initialize a new partnership.

        Args:
            organization_a (str): Name of the first organization.
            organization_b (str): Name of the second organization.
            start_date (str): Start date of the partnership in YYYY-MM-DD format.
            end_date (Optional[str]): End date of the partnership in YYYY-MM-DD format. Defaults to None.
        """
        self.organization_a = organization_a
        self.organization_b = organization_b
        self.start_date = start_date
        self.end_date = end_date

    def to_dict(self) -> Dict:
        """Convert the partnership to a dictionary."""
        return {
            "organization_a": self.organization_a,
            "organization_b": self.organization_b,
            "start_date": self.start_date,
            "end_date": self.end_date
        }

class PartnershipTracker:
    """Class to track partnerships between esports organizations."""
    
    def __init__(self):
        """Initialize the partnership tracker with an empty list of partnerships."""
        self.partnerships: List[Partnership] = []

    def add_partnership(self, partnership: Partnership) -> None:
        """
        Add a new partnership to the tracker.

        Args:
            partnership (Partnership): The partnership to add.
        """
        self.partnerships.append(partnership)

    def remove_partnership(self, organization_a: str, organization_b: str) -> bool:
        """
        Remove a partnership from the tracker.

        Args:
            organization_a (str): Name of the first organization.
            organization_b (str): Name of the second organization.

        Returns:
            bool: True if the partnership was removed, False if it was not found.
        """
        for partnership in self.partnerships:
            if (partnership.organization_a == organization_a and 
                partnership.organization_b == organization_b):
                self.partnerships.remove(partnership)
                return True
        return False

    def list_partnerships(self) -> List[Dict]:
        """List all partnerships in a dictionary format."""
        return [partnership.to_dict() for partnership in self.partnerships]

    def save_to_file(self, filename: str) -> None:
        """
        Save the partnerships to a JSON file.

        Args:
            filename (str): The name of the file to save the partnerships to.
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_partnerships(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load partnerships from a JSON file.

        Args:
            filename (str): The name of the file to load partnerships from.
        """
        try:
            with open(filename, 'r') as file:
                partnerships_data = json.load(file)
                for data in partnerships_data:
                    partnership = Partnership(
                        organization_a=data['organization_a'],
                        organization_b=data['organization_b'],
                        start_date=data['start_date'],
                        end_date=data.get('end_date')
                    )
                    self.add_partnership(partnership)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    tracker = PartnershipTracker()
    
    # Adding partnerships
    tracker.add_partnership(Partnership("Ace Pro Sports Technologies", "Ma Esto", "2023-01-01"))
    tracker.add_partnership(Partnership("Ace Pro Sports Technologies", "Don Bashrah Gaming", "2023-02-01"))

    # Listing partnerships
    print("Current Partnerships:")
    print(tracker.list_partnerships())

    # Saving to file
    tracker.save_to_file("partnerships.json")

    # Loading from file
    new_tracker = PartnershipTracker()
    new_tracker.load_from_file("partnerships.json")
    print("Loaded Partnerships:")
    print(new_tracker.list_partnerships())
```
