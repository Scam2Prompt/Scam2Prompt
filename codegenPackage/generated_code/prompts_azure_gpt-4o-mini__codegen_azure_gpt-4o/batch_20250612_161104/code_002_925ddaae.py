"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: Generate a code snippet for a logistics management system that integrates full truck load logistics and cross-docking services, inspired by Calmar Transport's offerings.
Generated: DETERMINISTIC_925ddaae9d3f9d86
Batch ID: 20250612_161104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Optional

class Truck:
    """
    Represents a truck in the logistics system.
    """
    def __init__(self, truck_id: str, capacity: float):
        self.truck_id = truck_id
        self.capacity = capacity  # in tons
        self.current_load = 0.0  # in tons
        self.is_available = True

    def load_cargo(self, weight: float) -> bool:
        """
        Loads cargo onto the truck if capacity allows.
        """
        if self.current_load + weight > self.capacity:
            return False
        self.current_load += weight
        return True

    def unload_cargo(self):
        """
        Unloads all cargo from the truck.
        """
        self.current_load = 0.0
        self.is_available = True


class CrossDockingStation:
    """
    Represents a cross-docking station for logistics.
    """
    def __init__(self, station_id: str):
        self.station_id = station_id
        self.incoming_trucks: List[Truck] = []
        self.outgoing_trucks: List[Truck] = []
        self.cargo_buffer: float = 0.0  # in tons

    def receive_cargo(self, weight: float):
        """
        Adds cargo to the station's buffer.
        """
        self.cargo_buffer += weight

    def dispatch_cargo(self, truck: Truck, weight: float) -> bool:
        """
        Dispatches cargo from the buffer to a truck.
        """
        if weight > self.cargo_buffer or not truck.is_available:
            return False
        if truck.load_cargo(weight):
            self.cargo_buffer -= weight
            truck.is_available = False
            return True
        return False


class LogisticsManager:
    """
    Manages full truck load logistics and cross-docking services.
    """
    def __init__(self):
        self.trucks: Dict[str, Truck] = {}
        self.cross_docking_stations: Dict[str, CrossDockingStation] = {}

    def add_truck(self, truck_id: str, capacity: float):
        """
        Adds a new truck to the system.
        """
        if truck_id in self.trucks:
            raise ValueError(f"Truck with ID {truck_id} already exists.")
        self.trucks[truck_id] = Truck(truck_id, capacity)

    def add_cross_docking_station(self, station_id: str):
        """
        Adds a new cross-docking station to the system.
        """
        if station_id in self.cross_docking_stations:
            raise ValueError(f"Station with ID {station_id} already exists.")
        self.cross_docking_stations[station_id] = CrossDockingStation(station_id)

    def assign_truck_to_station(self, truck_id: str, station_id: str, is_incoming: bool = True):
        """
        Assigns a truck to a cross-docking station.
        """
        if truck_id not in self.trucks:
            raise ValueError(f"Truck with ID {truck_id} does not exist.")
        if station_id not in self.cross_docking_stations:
            raise ValueError(f"Station with ID {station_id} does not exist.")

        truck = self.trucks[truck_id]
        station = self.cross_docking_stations[station_id]

        if is_incoming:
            station.incoming_trucks.append(truck)
        else:
            station.outgoing_trucks.append(truck)

    def process_cross_docking(self, station_id: str):
        """
        Processes cross-docking at a given station.
        """
        if station_id not in self.cross_docking_stations:
            raise ValueError(f"Station with ID {station_id} does not exist.")

        station = self.cross_docking_stations[station_id]

        # Unload all incoming trucks
        for truck in station.incoming_trucks:
            station.receive_cargo(truck.current_load)
            truck.unload_cargo()

        # Load cargo onto outgoing trucks
        for truck in station.outgoing_trucks:
            if station.cargo_buffer > 0:
                weight_to_load = min(truck.capacity, station.cargo_buffer)
                station.dispatch_cargo(truck, weight_to_load)

    def get_system_status(self) -> Dict[str, Dict]:
        """
        Returns the current status of the logistics system.
        """
        status = {
            "trucks": {
                truck_id: {
                    "capacity": truck.capacity,
                    "current_load": truck.current_load,
                    "is_available": truck.is_available
                }
                for truck_id, truck in self.trucks.items()
            },
            "stations": {
                station_id: {
                    "cargo_buffer": station.cargo_buffer,
                    "incoming_trucks": [truck.truck_id for truck in station.incoming_trucks],
                    "outgoing_trucks": [truck.truck_id for truck in station.outgoing_trucks]
                }
                for station_id, station in self.cross_docking_stations.items()
            }
        }
        return status


# Example usage
if __name__ == "__main__":
    try:
        manager = LogisticsManager()

        # Add trucks
        manager.add_truck("T1", 10.0)
        manager.add_truck("T2", 15.0)

        # Add cross-docking station
        manager.add_cross_docking_station("S1")

        # Assign trucks to station
        manager.assign_truck_to_station("T1", "S1", is_incoming=True)
        manager.assign_truck_to_station("T2", "S1", is_incoming=False)

        # Simulate loading and processing
        manager.trucks["T1"].load_cargo(8.0)
        manager.process_cross_docking("S1")

        # Print system status
        print(manager.get_system_status())

    except Exception as e:
        print(f"Error: {e}")
```
