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
from datetime import datetime, timedelta
from typing import List, Optional

class Tram:
    """
    Represents a tram in the fleet.
    Attributes:
        tram_id (str): Unique identifier for the tram.
        capacity (int): Maximum number of passengers the tram can carry.
        current_passengers (int): Current number of passengers on the tram.
        operational_status (bool): Indicates if the tram is operational.
        last_service_date (datetime): The last date the tram was serviced.
    """
    
    def __init__(self, tram_id: str, capacity: int, last_service_date: datetime):
        self.tram_id = tram_id
        self.capacity = capacity
        self.current_passengers = 0
        self.operational_status = True
        self.last_service_date = last_service_date

    def board_passengers(self, number: int) -> bool:
        """
        Boards passengers onto the tram.
        Args:
            number (int): Number of passengers to board.
        Returns:
            bool: True if boarding was successful, False otherwise.
        """
        if not self.operational_status:
            raise Exception(f"Tram {self.tram_id} is not operational.")
        
        if self.current_passengers + number > self.capacity:
            return False  # Not enough capacity
        
        self.current_passengers += number
        return True

    def alight_passengers(self, number: int) -> bool:
        """
        Alights passengers from the tram.
        Args:
            number (int): Number of passengers to alight.
        Returns:
            bool: True if alighting was successful, False otherwise.
        """
        if number > self.current_passengers:
            return False  # Cannot alight more passengers than present
        
        self.current_passengers -= number
        return True

    def service_tram(self):
        """Services the tram and updates the last service date."""
        self.last_service_date = datetime.now()

    def needs_service(self) -> bool:
        """
        Checks if the tram needs servicing based on a 30-day interval.
        Returns:
            bool: True if the tram needs service, False otherwise.
        """
        return (datetime.now() - self.last_service_date) > timedelta(days=30)


class FleetManager:
    """
    Manages a fleet of trams.
    Attributes:
        trams (List[Tram]): List of trams in the fleet.
    """
    
    def __init__(self):
        self.trams: List[Tram] = []

    def add_tram(self, tram: Tram):
        """Adds a tram to the fleet."""
        self.trams.append(tram)

    def remove_tram(self, tram_id: str) -> Optional[Tram]:
        """
        Removes a tram from the fleet by its ID.
        Args:
            tram_id (str): The ID of the tram to remove.
        Returns:
            Optional[Tram]: The removed tram or None if not found.
        """
        for tram in self.trams:
            if tram.tram_id == tram_id:
                self.trams.remove(tram)
                return tram
        return None  # Tram not found

    def get_operational_trams(self) -> List[Tram]:
        """Returns a list of operational trams."""
        return [tram for tram in self.trams if tram.operational_status]

    def service_due_trams(self) -> List[Tram]:
        """Returns a list of trams that are due for servicing."""
        return [tram for tram in self.trams if tram.needs_service()]

    def optimize_operations(self):
        """
        Placeholder for optimization logic.
        This method can be expanded to include algorithms for optimizing tram schedules,
        routes, and passenger distribution.
        """
        pass  # Implement optimization logic here


# Example usage
if __name__ == "__main__":
    fleet_manager = FleetManager()
    
    # Adding trams to the fleet
    tram1 = Tram(tram_id="T001", capacity=100, last_service_date=datetime.now() - timedelta(days=31))
    tram2 = Tram(tram_id="T002", capacity=80, last_service_date=datetime.now())
    
    fleet_manager.add_tram(tram1)
    fleet_manager.add_tram(tram2)

    # Board passengers
    try:
        tram1.board_passengers(50)
        tram2.board_passengers(90)  # This will fail due to capacity
    except Exception as e:
        print(e)

    # Check for trams needing service
    due_trams = fleet_manager.service_due_trams()
    print(f"Trams due for service: {[tram.tram_id for tram in due_trams]}")
```
