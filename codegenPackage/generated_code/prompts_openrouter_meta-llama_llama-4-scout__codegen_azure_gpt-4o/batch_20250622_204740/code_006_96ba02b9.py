"""
Generated Code Metadata:
========================
Original URL: https://tramsipublicidad.com
Prompt: Create a data model for a tram system's fleet management, including parameters for optimizing operations and improving commuter experiences.
Generated: DETERMINISTIC_96ba02b9768a58fd
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from datetime import datetime
from typing import List, Optional

# Define the Tram class to represent individual tram units
class Tram:
    """
    Represents a single tram in the fleet.
    """
    def __init__(self, tram_id: str, capacity: int, status: str, last_maintenance_date: datetime):
        """
        Initialize a Tram instance.

        :param tram_id: Unique identifier for the tram.
        :param capacity: Maximum number of passengers the tram can hold.
        :param status: Current operational status of the tram (e.g., 'active', 'maintenance', 'inactive').
        :param last_maintenance_date: Date of the last maintenance check.
        """
        self.tram_id = tram_id
        self.capacity = capacity
        self.status = status
        self.last_maintenance_date = last_maintenance_date

    def needs_maintenance(self) -> bool:
        """
        Check if the tram needs maintenance based on the last maintenance date.

        :return: True if maintenance is overdue, False otherwise.
        """
        days_since_maintenance = (datetime.now() - self.last_maintenance_date).days
        return days_since_maintenance > 30  # Example threshold: 30 days

    def update_status(self, new_status: str):
        """
        Update the operational status of the tram.

        :param new_status: New status to set for the tram.
        """
        valid_statuses = ['active', 'maintenance', 'inactive']
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are {valid_statuses}.")
        self.status = new_status


# Define the Fleet class to manage the tram fleet
class Fleet:
    """
    Represents the entire tram fleet.
    """
    def __init__(self):
        """
        Initialize a Fleet instance.
        """
        self.trams: List[Tram] = []

    def add_tram(self, tram: Tram):
        """
        Add a tram to the fleet.

        :param tram: Tram instance to add.
        """
        self.trams.append(tram)

    def remove_tram(self, tram_id: str):
        """
        Remove a tram from the fleet by its ID.

        :param tram_id: ID of the tram to remove.
        """
        self.trams = [tram for tram in self.trams if tram.tram_id != tram_id]

    def get_tram_by_id(self, tram_id: str) -> Optional[Tram]:
        """
        Retrieve a tram by its ID.

        :param tram_id: ID of the tram to retrieve.
        :return: Tram instance if found, None otherwise.
        """
        for tram in self.trams:
            if tram.tram_id == tram_id:
                return tram
        return None

    def get_active_trams(self) -> List[Tram]:
        """
        Get a list of all active trams.

        :return: List of active Tram instances.
        """
        return [tram for tram in self.trams if tram.status == 'active']

    def get_trams_needing_maintenance(self) -> List[Tram]:
        """
        Get a list of trams that need maintenance.

        :return: List of Tram instances needing maintenance.
        """
        return [tram for tram in self.trams if tram.needs_maintenance()]

    def optimize_operations(self):
        """
        Optimize fleet operations by ensuring active trams are prioritized and maintenance is scheduled.

        This is a placeholder for more complex optimization logic.
        """
        for tram in self.trams:
            if tram.needs_maintenance():
                tram.update_status('maintenance')


# Example usage
if __name__ == "__main__":
    # Create a fleet instance
    fleet = Fleet()

    # Add trams to the fleet
    fleet.add_tram(Tram("T001", 100, "active", datetime(2023, 9, 1)))
    fleet.add_tram(Tram("T002", 80, "active", datetime(2023, 10, 1)))
    fleet.add_tram(Tram("T003", 120, "inactive", datetime(2023, 8, 15)))

    # Print active trams
    print("Active trams:")
    for tram in fleet.get_active_trams():
        print(f"Tram ID: {tram.tram_id}, Capacity: {tram.capacity}")

    # Print trams needing maintenance
    print("\nTrams needing maintenance:")
    for tram in fleet.get_trams_needing_maintenance():
        print(f"Tram ID: {tram.tram_id}, Last Maintenance: {tram.last_maintenance_date}")

    # Optimize operations
    fleet.optimize_operations()
    print("\nFleet operations optimized.")
```
