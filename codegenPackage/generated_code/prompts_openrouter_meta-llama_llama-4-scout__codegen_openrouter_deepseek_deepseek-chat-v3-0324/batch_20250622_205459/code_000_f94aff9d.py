"""
Generated Code Metadata:
========================
Original URL: https://kalgatetechnology.com.ng
Prompt: Write a Python script to manage a fleet of 240 vehicles, including tracking and maintenance scheduling, inspired by Kalgate Technology's services.
Generated: DETERMINISTIC_f94aff9d4909a198
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os
from typing import Dict, List, Optional, Tuple


class Vehicle:
    """Represents a vehicle in the fleet with maintenance tracking capabilities."""

    def __init__(self, vehicle_id: str, make: str, model: str, year: int, mileage: int):
        """
        Initialize a Vehicle instance.

        Args:
            vehicle_id: Unique identifier for the vehicle
            make: Manufacturer of the vehicle
            model: Model of the vehicle
            year: Year of manufacture
            mileage: Current mileage of the vehicle
        """
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.maintenance_history: List[Dict] = []
        self.next_maintenance_mileage = mileage + 5000  # Default maintenance interval

    def add_maintenance_record(self, service_type: str, date: str, cost: float, notes: str = "") -> None:
        """
        Add a maintenance record to the vehicle's history.

        Args:
            service_type: Type of service performed
            date: Date of service (YYYY-MM-DD)
            cost: Cost of the service
            notes: Additional notes about the service
        """
        try:
            datetime.datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")

        record = {
            "service_type": service_type,
            "date": date,
            "cost": cost,
            "notes": notes
        }
        self.maintenance_history.append(record)
        self.next_maintenance_mileage = self.mileage + 5000

    def update_mileage(self, new_mileage: int) -> None:
        """
        Update the vehicle's mileage.

        Args:
            new_mileage: New mileage value

        Raises:
            ValueError: If new mileage is less than current mileage
        """
        if new_mileage < self.mileage:
            raise ValueError("New mileage cannot be less than current mileage.")
        self.mileage = new_mileage

    def needs_maintenance(self) -> bool:
        """Check if the vehicle is due for maintenance."""
        return self.mileage >= self.next_maintenance_mileage

    def to_dict(self) -> Dict:
        """Convert Vehicle object to dictionary for serialization."""
        return {
            "vehicle_id": self.vehicle_id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "mileage": self.mileage,
            "maintenance_history": self.maintenance_history,
            "next_maintenance_mileage": self.next_maintenance_mileage
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Vehicle':
        """Create a Vehicle object from dictionary data."""
        vehicle = cls(
            data["vehicle_id"],
            data["make"],
            data["model"],
            data["year"],
            data["mileage"]
        )
        vehicle.maintenance_history = data.get("maintenance_history", [])
        vehicle.next_maintenance_mileage = data.get("next_maintenance_mileage", data["mileage"] + 5000)
        return vehicle


class FleetManager:
    """Manages a fleet of vehicles with maintenance scheduling."""

    def __init__(self, data_file: str = "fleet_data.json"):
        """
        Initialize the FleetManager.

        Args:
            data_file: Path to JSON file for persistent storage
        """
        self.data_file = data_file
        self.vehicles: Dict[str, Vehicle] = {}
        self._load_data()

    def _load_data(self) -> None:
        """Load fleet data from JSON file."""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                    self.vehicles = {
                        vid: Vehicle.from_dict(vdata) 
                        for vid, vdata in data.items()
                    }
            except (json.JSONDecodeError, IOError) as e:
                raise RuntimeError(f"Error loading fleet data: {e}")

    def _save_data(self) -> None:
        """Save fleet data to JSON file."""
        try:
            with open(self.data_file, "w") as f:
                json.dump(
                    {vid: v.to_dict() for vid, v in self.vehicles.items()},
                    f,
                    indent=2
                )
        except IOError as e:
            raise RuntimeError(f"Error saving fleet data: {e}")

    def add_vehicle(self, vehicle: Vehicle) -> None:
        """
        Add a vehicle to the fleet.

        Args:
            vehicle: Vehicle object to add

        Raises:
            ValueError: If vehicle ID already exists
        """
        if vehicle.vehicle_id in self.vehicles:
            raise ValueError(f"Vehicle with ID {vehicle.vehicle_id} already exists")
        self.vehicles[vehicle.vehicle_id] = vehicle
        self._save_data()

    def remove_vehicle(self, vehicle_id: str) -> None:
        """
        Remove a vehicle from the fleet.

        Args:
            vehicle_id: ID of vehicle to remove

        Raises:
            KeyError: If vehicle ID doesn't exist
        """
        if vehicle_id not in self.vehicles:
            raise KeyError(f"Vehicle with ID {vehicle_id} not found")
        del self.vehicles[vehicle_id]
        self._save_data()

    def get_vehicle(self, vehicle_id: str) -> Optional[Vehicle]:
        """Get a vehicle by ID."""
        return self.vehicles.get(vehicle_id)

    def list_vehicles(self) -> List[Vehicle]:
        """Get list of all vehicles in the fleet."""
        return list(self.vehicles.values())

    def list_vehicles_needing_maintenance(self) -> List[Tuple[str, int]]:
        """
        Get list of vehicles needing maintenance.

        Returns:
            List of tuples (vehicle_id, miles_over)
        """
        return [
            (v.vehicle_id, v.mileage - v.next_maintenance_mileage)
            for v in self.vehicles.values() 
            if v.needs_maintenance()
        ]

    def schedule_maintenance(self, vehicle_id: str, service_type: str, date: str, cost: float, notes: str = "") -> None:
        """
        Schedule maintenance for a vehicle.

        Args:
            vehicle_id: ID of vehicle to service
            service_type: Type of service
            date: Date of service (YYYY-MM-DD)
            cost: Cost of service
            notes: Additional notes

        Raises:
            KeyError: If vehicle ID doesn't exist
            ValueError: If date format is invalid
        """
        if vehicle_id not in self.vehicles:
            raise KeyError(f"Vehicle with ID {vehicle_id} not found")
        
        vehicle = self.vehicles[vehicle_id]
        vehicle.add_maintenance_record(service_type, date, cost, notes)
        self._save_data()

    def update_vehicle_mileage(self, vehicle_id: str, new_mileage: int) -> None:
        """
        Update a vehicle's mileage.

        Args:
            vehicle_id: ID of vehicle to update
            new_mileage: New mileage value

        Raises:
            KeyError: If vehicle ID doesn't exist
            ValueError: If new mileage is invalid
        """
        if vehicle_id not in self.vehicles:
            raise KeyError(f"Vehicle with ID {vehicle_id} not found")
        
        vehicle = self.vehicles[vehicle_id]
        vehicle.update_mileage(new_mileage)
        self._save_data()


# Example usage
if __name__ == "__main__":
    try:
        fleet = FleetManager()

        # Add some vehicles
        vehicle1 = Vehicle("V001", "Toyota", "Camry", 2020, 15000)
        vehicle2 = Vehicle("V002", "Ford", "Transit", 2019, 35000)
        
        fleet.add_vehicle(vehicle1)
        fleet.add_vehicle(vehicle2)

        # Schedule maintenance
        fleet.schedule_maintenance(
            "V001",
            "Oil Change",
            "2023-05-15",
            75.00,
            "Used synthetic oil"
        )

        # Update mileage
        fleet.update_vehicle_mileage("V002", 36000)

        # Check maintenance needs
        needs_maintenance = fleet.list_vehicles_needing_maintenance()
        print(f"Vehicles needing maintenance: {needs_maintenance}")

    except Exception as e:
        print(f"Error in fleet management: {e}")
```
