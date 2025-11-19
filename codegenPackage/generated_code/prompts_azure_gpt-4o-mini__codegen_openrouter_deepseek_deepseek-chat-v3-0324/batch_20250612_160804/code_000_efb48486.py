"""
Generated Code Metadata:
========================
Original URL: https://mechanics.ae
Prompt: Generate a code snippet for a car maintenance scheduling application that includes services like oil changes, brake inspections, and tire rotations, similar to the offerings at Mechanics.ae.
Generated: DETERMINISTIC_efb484860e1610d7
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum
import json
from typing import Dict, List, Optional


class ServiceType(Enum):
    """Enum representing different types of car maintenance services."""
    OIL_CHANGE = "Oil Change"
    BRAKE_INSPECTION = "Brake Inspection"
    TIRE_ROTATION = "Tire Rotation"
    BATTERY_CHECK = "Battery Check"
    FLUID_TOP_UP = "Fluid Top Up"


class Car:
    """Class representing a car with maintenance details."""
    
    def __init__(self, make: str, model: str, year: int, mileage: int):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.service_history: List[Dict] = []

    def add_service(self, service_type: ServiceType, date: datetime, notes: str = "") -> None:
        """Add a service to the car's service history."""
        self.service_history.append({
            "service_type": service_type.value,
            "date": date.isoformat(),
            "mileage": self.mileage,
            "notes": notes
        })

    def get_service_history(self) -> List[Dict]:
        """Return the car's service history."""
        return self.service_history


class MaintenanceScheduler:
    """Class for scheduling and managing car maintenance services."""
    
    def __init__(self):
        self.cars: Dict[str, Car] = {}  # key: car_id, value: Car object
        self.service_intervals = {
            ServiceType.OIL_CHANGE: {"mileage": 5000, "days": 180},
            ServiceType.BRAKE_INSPECTION: {"mileage": 15000, "days": 365},
            ServiceType.TIRE_ROTATION: {"mileage": 8000, "days": 180},
            ServiceType.BATTERY_CHECK: {"mileage": 10000, "days": 365},
            ServiceType.FLUID_TOP_UP: {"mileage": 10000, "days": 365}
        }

    def add_car(self, car_id: str, car: Car) -> None:
        """Add a car to the maintenance scheduler."""
        if car_id in self.cars:
            raise ValueError(f"Car with ID {car_id} already exists.")
        self.cars[car_id] = car

    def get_upcoming_services(self, car_id: str) -> List[Dict]:
        """Get upcoming services for a car based on mileage and time intervals."""
        if car_id not in self.cars:
            raise ValueError(f"Car with ID {car_id} not found.")
        
        car = self.cars[car_id]
        upcoming_services = []
        
        for service_type, intervals in self.service_intervals.items():
            last_service = self._get_last_service(car, service_type)
            
            mileage_due = (car.mileage - last_service["mileage"]) >= intervals["mileage"] if last_service else True
            time_due = (datetime.now() - datetime.fromisoformat(last_service["date"])) >= timedelta(days=intervals["days"]) if last_service else True
            
            if mileage_due or time_due:
                upcoming_services.append({
                    "service_type": service_type.value,
                    "due_by_mileage": mileage_due,
                    "due_by_time": time_due
                })
        
        return upcoming_services

    def _get_last_service(self, car: Car, service_type: ServiceType) -> Optional[Dict]:
        """Get the last service of a given type for a car."""
        last_service = None
        for service in car.service_history:
            if service["service_type"] == service_type.value:
                if not last_service or service["date"] > last_service["date"]:
                    last_service = service
        return last_service

    def schedule_service(self, car_id: str, service_type: ServiceType, date: datetime, notes: str = "") -> None:
        """Schedule a service for a car."""
        if car_id not in self.cars:
            raise ValueError(f"Car with ID {car_id} not found.")
        
        car = self.cars[car_id]
        car.add_service(service_type, date, notes)

    def save_to_file(self, filename: str) -> None:
        """Save the maintenance scheduler data to a JSON file."""
        data = {
            "cars": {
                car_id: {
                    "make": car.make,
                    "model": car.model,
                    "year": car.year,
                    "mileage": car.mileage,
                    "service_history": car.service_history
                }
                for car_id, car in self.cars.items()
            },
            "service_intervals": {
                service_type.value: interval 
                for service_type, interval in self.service_intervals.items()
            }
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_from_file(self, filename: str) -> None:
        """Load the maintenance scheduler data from a JSON file."""
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self.cars = {}
        for car_id, car_data in data["cars"].items():
            car = Car(
                make=car_data["make"],
                model=car_data["model"],
                year=car_data["year"],
                mileage=car_data["mileage"]
            )
            car.service_history = car_data["service_history"]
            self.cars[car_id] = car
        
        self.service_intervals = {
            ServiceType(service_type): interval 
            for service_type, interval in data["service_intervals"].items()
        }


# Example usage
if __name__ == "__main__":
    scheduler = MaintenanceScheduler()
    
    # Add a car
    car1 = Car(make="Toyota", model="Camry", year=2020, mileage=15000)
    scheduler.add_car("car1", car1)
    
    # Schedule a service
    scheduler.schedule_service(
        car_id="car1",
        service_type=ServiceType.OIL_CHANGE,
        date=datetime.now(),
        notes="Used synthetic oil"
    )
    
    # Get upcoming services
    upcoming = scheduler.get_upcoming_services("car1")
    print("Upcoming services:", upcoming)
    
    # Save to file
    scheduler.save_to_file("maintenance_data.json")
    
    # Load from file
    new_scheduler = MaintenanceScheduler()
    new_scheduler.load_from_file("maintenance_data.json")
```
