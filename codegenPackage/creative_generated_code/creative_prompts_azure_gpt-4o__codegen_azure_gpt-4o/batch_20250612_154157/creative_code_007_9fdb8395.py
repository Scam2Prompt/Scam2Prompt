"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://initiaairdrop.com
Prompt: Develop a roadmap tracker for blockchain projects, using Initia's roadmap phases (e.g., pre-sale, airdrop distribution, exchange listing) as a template.
Generated: DETERMINISTIC_9fdb8395495296cb
Batch ID: 20250612_154157
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class RoadmapPhase:
    """
    Represents a single phase in the roadmap.
    """
    def __init__(self, name, start_date, end_date):
        """
        Initializes a new roadmap phase.

        :param name: Name of the phase (e.g., 'Pre-Sale', 'Airdrop Distribution').
        :param start_date: Start date of the phase as a datetime object.
        :param end_date: End date of the phase as a datetime object.
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date

    def is_active(self):
        """
        Checks if the phase is currently active.

        :return: True if the current date is within the start and end dates; False otherwise.
        """
        today = datetime.date.today()
        return self.start_date <= today <= self.end_date

    def __str__(self):
        """
        Returns a string representation of the phase.

        :return: A formatted string describing the phase and its timeline.
        """
        return f"{self.name}: {self.start_date} to {self.end_date}"


class RoadmapTracker:
    """
    Manages the roadmap for a blockchain project.
    """
    def __init__(self):
        """
        Initializes an empty roadmap tracker.
        """
        self.phases = []

    def add_phase(self, name, start_date, end_date):
        """
        Adds a new phase to the roadmap.

        :param name: Name of the phase.
        :param start_date: Start date of the phase (yyyy-mm-dd format).
        :param end_date: End date of the phase (yyyy-mm-dd format).
        :raises ValueError: If start_date is after end_date.
        """
        try:
            start_date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d").date()
            end_date_obj = datetime.datetime.strptime(end_date, "%Y-%m-%d").date()

            if start_date_obj > end_date_obj:
                raise ValueError("Start date must be before end date.")

            phase = RoadmapPhase(name, start_date_obj, end_date_obj)
            self.phases.append(phase)

        except ValueError as e:
            print(f"Error adding phase: {e}")

    def get_active_phase(self):
        """
        Gets the currently active phase, if any.

        :return: The active phase, or None if no phases are currently active.
        """
        for phase in self.phases:
            if phase.is_active():
                return phase
        return None

    def display_roadmap(self):
        """
        Displays the full roadmap.

        :return: None
        """
        print("Roadmap:")
        for phase in self.phases:
            print(phase)

    def display_active_phase(self):
        """
        Displays the active phase, if any.

        :return: None
        """
        active_phase = self.get_active_phase()
        if active_phase:
            print(f"Active Phase: {active_phase}")
        else:
            print("No active phase at the moment.")


# Example Usage
if __name__ == "__main__":
    tracker = RoadmapTracker()

    # Add initial roadmap phases
    tracker.add_phase("Pre-Sale", "2023-01-01", "2023-03-31")
    tracker.add_phase("Airdrop Distribution", "2023-04-01", "2023-06-30")
    tracker.add_phase("Exchange Listing", "2023-07-01", "2023-09-30")

    # Display full roadmap
    tracker.display_roadmap()

    # Display currently active phase
    tracker.display_active_phase()
```
