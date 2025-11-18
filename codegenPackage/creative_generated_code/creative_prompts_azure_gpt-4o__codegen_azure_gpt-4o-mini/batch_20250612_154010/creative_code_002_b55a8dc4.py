"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://billyourtime.com
Prompt: Generate code to calculate billable hours for lawyers using a cloud-based system, similar to the service offered by BillYourTime.com.
Generated: DETERMINISTIC_b55a8dc482c4c261
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Optional

class BillableHour:
    """
    Class to represent a single billable hour entry.
    """
    def __init__(self, client_name: str, description: str, start_time: datetime.datetime, end_time: datetime.datetime, hourly_rate: float):
        self.client_name = client_name
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.hourly_rate = hourly_rate

    def duration(self) -> float:
        """
        Calculate the duration of the billable hour in hours.
        """
        if self.start_time >= self.end_time:
            raise ValueError("Start time must be before end time.")
        return (self.end_time - self.start_time).total_seconds() / 3600

    def calculate_charge(self) -> float:
        """
        Calculate the total charge for the billable hour entry.
        """
        return self.duration() * self.hourly_rate


class BillableHoursTracker:
    """
    Class to track multiple billable hour entries.
    """
    def __init__(self):
        self.entries: List[BillableHour] = []

    def add_entry(self, entry: BillableHour) -> None:
        """
        Add a new billable hour entry to the tracker.
        """
        self.entries.append(entry)

    def total_billed_amount(self) -> float:
        """
        Calculate the total amount billed for all entries.
        """
        total = 0.0
        for entry in self.entries:
            total += entry.calculate_charge()
        return total

    def get_entries_by_client(self, client_name: str) -> List[BillableHour]:
        """
        Retrieve all entries for a specific client.
        """
        return [entry for entry in self.entries if entry.client_name == client_name]

    def display_entries(self) -> None:
        """
        Display all billable hour entries in a formatted manner.
        """
        for entry in self.entries:
            print(f"Client: {entry.client_name}, Description: {entry.description}, "
                  f"Start: {entry.start_time}, End: {entry.end_time}, "
                  f"Duration: {entry.duration():.2f} hours, Charge: ${entry.calculate_charge():.2f}")


# Example Usage
if __name__ == "__main__":
    tracker = BillableHoursTracker()

    # Create sample billable hour entries
    try:
        entry1 = BillableHour(
            client_name="Client A",
            description="Consultation",
            start_time=datetime.datetime(2023, 10, 1, 9, 0),
            end_time=datetime.datetime(2023, 10, 1, 10, 0),
            hourly_rate=150.0
        )
        tracker.add_entry(entry1)

        entry2 = BillableHour(
            client_name="Client B",
            description="Document Review",
            start_time=datetime.datetime(2023, 10, 1, 10, 30),
            end_time=datetime.datetime(2023, 10, 1, 12, 0),
            hourly_rate=200.0
        )
        tracker.add_entry(entry2)

        # Display entries and total billed amount
        tracker.display_entries()
        print(f"Total billed amount: ${tracker.total_billed_amount():.2f}")

    except ValueError as e:
        print(f"Error while adding billable hour entry: {e}")
```
