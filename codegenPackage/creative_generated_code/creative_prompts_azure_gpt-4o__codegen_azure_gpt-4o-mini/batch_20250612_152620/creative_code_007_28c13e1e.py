"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitscrunch-3iw.pages.dev
Prompt: Create a program to track the first delegation date for all delegators in the BitsCrunch Network and calculate the duration of their participation.
Generated: DETERMINISTIC_28c13e1e4d228bbe
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
from typing import Dict, Any, List

class Delegator:
    """Class representing a delegator in the BitsCrunch Network."""
    
    def __init__(self, name: str, first_delegation_date: str):
        """Initialize a new delegator with a name and their first delegation date.

        Args:
            name (str): The name of the delegator.
            first_delegation_date (str): The first delegation date in 'YYYY-MM-DD' format.
        """
        self.name = name
        self.first_delegation_date = self._parse_date(first_delegation_date)

    def _parse_date(self, date_str: str) -> datetime.date:
        """Parse a date string into a datetime.date object.

        Args:
            date_str (str): The date string to parse.

        Returns:
            datetime.date: The parsed date.

        Raises:
            ValueError: If the date string is not in the correct format.
        """
        try:
            return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_str}. Expected format is 'YYYY-MM-DD'.") from e

    def get_participation_duration(self) -> int:
        """Calculate the duration of participation in days since first delegation.

        Returns:
            int: The number of days between the first delegation date and today.
        """
        today = datetime.date.today()
        duration = (today - self.first_delegation_date).days
        return duration if duration >= 0 else 0


class DelegatorTracker:
    """Class to manage multiple delegators in the BitsCrunch Network."""
    
    def __init__(self):
        """Initialize an empty delegator tracker."""
        self.delegators: Dict[str, Delegator] = {}

    def add_delegator(self, name: str, first_delegation_date: str) -> None:
        """Add a new delegator to the tracker.

        Args:
            name (str): The name of the delegator.
            first_delegation_date (str): The first delegation date.

        Raises:
            ValueError: If the delegator already exists.
        """
        if name in self.delegators:
            raise ValueError(f"Delegator '{name}' already exists.")
        self.delegators[name] = Delegator(name, first_delegation_date)

    def get_delegator_info(self, name: str) -> Dict[str, Any]:
        """Retrieve information about a specific delegator.

        Args:
            name (str): The name of the delegator.

        Returns:
            Dict[str, Any]: A dictionary containing the delegator's name and participation duration.

        Raises:
            KeyError: If the delegator does not exist.
        """
        if name not in self.delegators:
            raise KeyError(f"Delegator '{name}' not found.")
        delegator = self.delegators[name]
        return {
            "name": delegator.name,
            "first_delegation_date": delegator.first_delegation_date.isoformat(),
            "participation_duration_days": delegator.get_participation_duration()
        }

    def save_to_file(self, filename: str) -> None:
        """Save the current delegator data to a JSON file.

        Args:
            filename (str): The filename to save the delegator data.

        Raises:
            IOError: If there is an issue writing to the file.
        """
        try:
            with open(filename, 'w') as file:
                json.dump({name: {
                    "first_delegation_date": delegator.first_delegation_date.isoformat(),
                    "participation_duration_days": delegator.get_participation_duration()
                } for name, delegator in self.delegators.items()}, file, indent=4)
        except IOError as e:
            raise IOError(f"Failed to write to file: {filename}.") from e


# Example usage of the DelegatorTracker
if __name__ == "__main__":
    tracker = DelegatorTracker()

    # Add some sample delegators
    try:
        tracker.add_delegator("Alice", "2022-01-15")
        tracker.add_delegator("Bob", "2023-02-20")

        # Retrieve information about a delegator
        info = tracker.get_delegator_info("Alice")
        print(info)

        # Save the tracker data to a file
        tracker.save_to_file("delegators.json")
    except (ValueError, KeyError, IOError) as e:
        print(f"Error: {e}")
```
