"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Write a Python script to manage a fleet of trucks like TAMS TRUCKS, including tracking and monitoring features.
Generated: DETERMINISTIC_338d3b498e264941
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime
from typing import List, Dict, Optional

class Truck:
    """Represents a truck in the fleet."""
    
    def __init__(self, truck_id: str, make: str, model: str, year: int, 
                 mileage: float, last_service_date: str, status: str = "available"):
        """
        Initialize a Truck instance.
        
        Args:
            truck_id: Unique identifier for the truck
            make: Manufacturer of the truck
            model: Model of the truck
            year: Year of manufacture
            mileage: Current mileage of the truck
            last_service_date: Date of last service (YYYY-MM-DD)
            status: Current status (available, in_use, maintenance)
        """
        self.truck_id = truck_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.last_service_date = last_service_date
        self.status = status
        
    def update_mileage(self, new_mileage: float) -> None:
        """Update the truck's mileage."""
        if new_mileage < self.mileage:
            raise ValueError("New mileage cannot be less than current mileage")
        self.mileage = new_mileage
        
    def update_status(self, new_status: str) -> None:
        """Update the truck's status."""
        valid_statuses = ["available", "in_use", "maintenance"]
        if new_status not in valid_statuses:
            raise ValueError(f"Invalid status. Must be one of: {valid_statuses}")
        self.status = new_status
        
    def needs_service(self, service_interval: int = 10000) -> bool:
        """Check if truck needs service based on mileage."""
        return self.mileage >= service_interval
        
    def to_dict(self) -> Dict:
        """Convert truck data to dictionary for serialization."""
        return {
            "truck_id": self.truck_id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "mileage": self.mileage,
            "last_service_date": self.last_service_date,
            "status": self.status
        }

class FleetManager:
    """Manages a fleet of trucks."""
    
    def __init__(self, data_file: str = "fleet_data.json"):
        """
        Initialize FleetManager.
        
        Args:
            data_file: Path to JSON file for storing fleet data
        """
        self.data_file = data_file
        self.trucks: Dict[str, Truck] = {}
        self.load_fleet()
        
    def add_truck(self, truck: Truck) -> None:
        """Add a truck to the fleet."""
        if truck.truck_id in self.trucks:
            raise ValueError(f"Truck with ID {truck.truck_id} already exists")
        self.trucks[truck.truck_id] = truck
        self.save_fleet()
        
    def remove_truck(self, truck_id: str) -> None:
        """Remove a truck from the fleet."""
        if truck_id not in self.trucks:
            raise ValueError(f"Truck with ID {truck_id} not found")
        del self.trucks[truck_id]
        self.save_fleet()
        
    def get_truck(self, truck_id: str) -> Optional[Truck]:
        """Get a truck by its ID."""
        return self.trucks.get(truck_id)
        
    def get_all_trucks(self) -> List[Truck]:
        """Get all trucks in the fleet."""
        return list(self.trucks.values())
        
    def get_trucks_by_status(self, status: str) -> List[Truck]:
        """Get all trucks with a specific status."""
        return [truck for truck in self.trucks.values() if truck.status == status]
        
    def save_fleet(self) -> None:
        """Save fleet data to file."""
        data = {
            "trucks": [truck.to_dict() for truck in self.trucks.values()]
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)
            
    def load_fleet(self) -> None:
        """Load fleet data from file."""
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)
                for truck_data in data.get("trucks", []):
                    truck = Truck(
                        truck_id=truck_data["truck_id"],
                        make=truck_data["make"],
                        model=truck_data["model"],
                        year=truck_data["year"],
                        mileage=truck_data["mileage"],
                        last_service_date=truck_data["last_service_date"],
                        status=truck_data["status"]
                    )
                    self.trucks[truck.truck_id] = truck
        except FileNotFoundError:
            # File doesn't exist yet, initialize empty fleet
            self.trucks = {}
            
    def generate_maintenance_report(self) -> Dict:
        """Generate a report of trucks needing maintenance."""
        report = {
            "generated_on": datetime.datetime.now().isoformat(),
            "trucks_needing_service": [],
            "trucks_in_maintenance": []
        }
        
        for truck in self.trucks.values():
            if truck.status == "maintenance":
                report["trucks_in_maintenance"].append(truck.to_dict())
            elif truck.needs_service():
                report["trucks_needing_service"].append(truck.to_dict())
                
        return report

class TruckTracker:
    """Tracks truck locations and movements."""
    
    def __init__(self, fleet_manager: FleetManager):
        """
        Initialize TruckTracker.
        
        Args:
            fleet_manager: FleetManager instance to work with
        """
        self.fleet_manager = fleet_manager
        self.locations: Dict[str, Dict] = {}  # truck_id: {lat, lon, timestamp}
        
    def update_location(self, truck_id: str, lat: float, lon: float) -> None:
        """Update a truck's location."""
        if truck_id not in self.fleet_manager.trucks:
            raise ValueError(f"Truck with ID {truck_id} not found in fleet")
            
        self.locations[truck_id] = {
            "lat": lat,
            "lon": lon,
            "timestamp": datetime.datetime.now().isoformat()
        }
        
    def get_location(self, truck_id: str) -> Optional[Dict]:
        """Get a truck's current location."""
        return self.locations.get(truck_id)
        
    def get_all_locations(self) -> Dict[str, Dict]:
        """Get all truck locations."""
        return self.locations

def main():
    """Example usage of the fleet management system."""
    try:
        # Initialize fleet manager
        fleet_manager = FleetManager()
        
        # Add some trucks
        truck1 = Truck(
            truck_id="TRUCK001",
            make="Ford",
            model="F-150",
            year=2020,
            mileage=45000,
            last_service_date="2023-01-15"
        )
        
        truck2 = Truck(
            truck_id="TRUCK002",
            make="Chevrolet",
            model="Silverado",
            year=2021,
            mileage=12000,
            last_service_date="2023-03-20",
            status="in_use"
        )
        
        fleet_manager.add_truck(truck1)
        fleet_manager.add_truck(truck2)
        
        # Initialize tracker
        tracker = TruckTracker(fleet_manager)
        tracker.update_location("TRUCK001", 34.0522, -118.2437)  # Los Angeles
        tracker.update_location("TRUCK002", 40.7128, -74.0060)  # New York
        
        # Generate reports
        maintenance_report = fleet_manager.generate_maintenance_report()
        print("Maintenance Report:")
        print(json.dumps(maintenance_report, indent=4))
        
        print("\nAll Truck Locations:")
        print(json.dumps(tracker.get_all_locations(), indent=4))
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
```
