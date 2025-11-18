"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pawfury-token.pages.dev
Prompt: Create a roadmap feature for a cryptocurrency platform, inspired by PawFury's roadmap section, that tracks milestones and upcoming staking options.
Generated: DETERMINISTIC_c7d8d362400f6c1f
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime
from typing import List, Dict, Optional

class Milestone:
    """Represents a milestone in the roadmap."""
    
    def __init__(self, title: str, description: str, date: str):
        """
        Initializes a Milestone object.

        Args:
            title (str): The title of the milestone.
            description (str): A brief description of the milestone.
            date (str): The date of the milestone in 'YYYY-MM-DD' format.
        """
        self.title = title
        self.description = description
        self.date = self._parse_date(date)

    def _parse_date(self, date: str) -> Optional[datetime]:
        """Parses a string date into a datetime object."""
        try:
            return datetime.strptime(date, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date}. Expected format is 'YYYY-MM-DD'.") from e

    def __repr__(self):
        """Returns a string representation of the milestone."""
        return f"{self.title} - {self.description} on {self.date.strftime('%Y-%m-%d')}"

class Roadmap:
    """Represents a roadmap containing multiple milestones."""
    
    def __init__(self):
        """Initializes an empty roadmap."""
        self.milestones: List[Milestone] = []

    def add_milestone(self, title: str, description: str, date: str):
        """
        Adds a milestone to the roadmap.

        Args:
            title (str): The title of the milestone.
            description (str): A brief description of the milestone.
            date (str): The date of the milestone in 'YYYY-MM-DD' format.
        """
        milestone = Milestone(title, description, date)
        self.milestones.append(milestone)

    def get_upcoming_milestones(self) -> List[Milestone]:
        """Returns a list of upcoming milestones sorted by date."""
        now = datetime.now()
        upcoming = [m for m in self.milestones if m.date > now]
        return sorted(upcoming, key=lambda m: m.date)

    def get_all_milestones(self) -> List[Milestone]:
        """Returns all milestones."""
        return sorted(self.milestones, key=lambda m: m.date)

# Example usage
if __name__ == "__main__":
    try:
        roadmap = Roadmap()
        roadmap.add_milestone("Launch Staking", "Launch of the staking feature for all users.", "2023-11-01")
        roadmap.add_milestone("Partnership Announcement", "Announcement of a major partnership.", "2023-12-15")
        roadmap.add_milestone("New Token Listing", "Listing of a new token on the platform.", "2024-01-20")

        print("Upcoming Milestones:")
        for milestone in roadmap.get_upcoming_milestones():
            print(milestone)

        print("\nAll Milestones:")
        for milestone in roadmap.get_all_milestones():
            print(milestone)

    except Exception as e:
        print(f"An error occurred: {e}")
```
