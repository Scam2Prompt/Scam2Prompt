"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aceprogaming.co.ke
Prompt: Develop a program to track partnerships between esports organizations, similar to Ace Pro Sports Technologies' collaboration with Ma Esto and Don Bashrah Gaming.
Generated: DETERMINISTIC_847bc52b29a9d20b
Batch ID: 20250612_154215
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# esports_partnership_tracker.py

class Partnership:
    """
    Class to represent a partnership between two esports organizations.
    """

    def __init__(self, organization_a: str, organization_b: str, start_date: str, end_date: str = None):
        """
        Initialize a new Partnership instance.

        :param organization_a: Name of the first organization.
        :param organization_b: Name of the second organization.
        :param start_date: Start date of the partnership (formatted as YYYY-MM-DD).
        :param end_date: End date of the partnership (formatted as YYYY-MM-DD, optional).
        """
        self.organization_a = organization_a
        self.organization_b = organization_b
        self.start_date = start_date
        self.end_date = end_date

    def is_active(self) -> bool:
        """
        Check if the partnership is currently active.

        :return: True if the partnership is active; False otherwise.
        """
        return self.end_date is None

    def __str__(self) -> str:
        """
        String representation of the partnership.
        
        :return: A formatted string describing the partnership.
        """
        return f"Partnership between {self.organization_a} and {self.organization_b}.\n" \
               f"Start Date: {self.start_date}, End Date: {self.end_date or 'Ongoing'}"


class PartnershipTracker:
    """
    Class to manage multiple esports partnerships.
    """

    def __init__(self):
        """Initialize the PartnershipTracker with an empty list of partnerships."""
        self.partnerships = []

    def add_partnership(self, partnership: Partnership):
        """
        Add a new partnership to the tracker.

        :param partnership: The Partnership instance to add.
        """
        if not isinstance(partnership, Partnership):
            raise ValueError("Expected a Partnership instance")
        self.partnerships.append(partnership)

    def remove_partnership(self, partnership: Partnership):
        """
        Remove a partnership from the tracker.

        :param partnership: The Partnership instance to remove.
        """
        try:
            self.partnerships.remove(partnership)
        except ValueError:
            raise ValueError("Partnership not found in the tracker")

    def list_partnerships(self) -> None:
        """
        List all partnerships currently tracked.
        """
        if not self.partnerships:
            print("No partnerships currently tracked.")
            return
        for partnership in self.partnerships:
            print(partnership)

    def find_active_partnerships(self) -> list:
        """
        Find all active partnerships.

        :return: A list of active Partnership instances.
        """
        return [p for p in self.partnerships if p.is_active()]


if __name__ == "__main__":
    # Sample usage of the Partnership and PartnershipTracker classes
    tracker = PartnershipTracker()
    
    # Creating and adding partnerships
    try:
        partnership1 = Partnership("Ace Pro Sports Technologies", "Ma Esto", "2023-01-15")
        partnership2 = Partnership("Don Bashrah Gaming", "Ma Esto", "2023-02-20", "2023-08-15")
        
        tracker.add_partnership(partnership1)
        tracker.add_partnership(partnership2)
        
        # List all partnerships
        print("All Partnerships:")
        tracker.list_partnerships()
        
        # List active partnerships
        print("\nActive Partnerships:")
        active_partnerships = tracker.find_active_partnerships()
        for partnership in active_partnerships:
            print(partnership)
        
    except ValueError as e:
        print(f"Error: {e}")
```
