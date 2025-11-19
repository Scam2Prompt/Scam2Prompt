"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Develop a code example that integrates a safety management system for transportation services, inspired by the safety protocols mentioned by TAMS TRUCKS.
Generated: DETERMINISTIC_e77b9fc412c4a5f4
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime
from typing import Dict, List, Optional

class SafetyViolationError(Exception):
    """Custom exception for safety violations."""
    pass

class Driver:
    """Represents a driver with safety-related attributes."""
    
    def __init__(self, driver_id: str, name: str, license_number: str, hours_worked: float = 0.0):
        """
        Initialize a Driver instance.
        
        Args:
            driver_id: Unique identifier for the driver.
            name: Full name of the driver.
            license_number: Driver's license number.
            hours_worked: Total hours worked in current shift.
        """
        self.driver_id = driver_id
        self.name = name
        self.license_number = license_number
        self.hours_worked = hours_worked
        self.last_rest_time = None
    
    def log_hours(self, hours: float) -> None:
        """
        Log additional hours worked by the driver.
        
        Args:
            hours: Hours to add to the driver's total.
            
        Raises:
            SafetyViolationError: If hours exceed legal limits.
        """
        if self.hours_worked + hours > 14:
            raise SafetyViolationError(f"Driver {self.name} exceeds maximum allowed working hours (14 hours)")
        self.hours_worked += hours
    
    def take_rest(self) -> None:
        """Record the time when the driver starts resting."""
        self.last_rest_time = datetime.now()
        self.hours_worked = 0.0
    
    def is_rested(self) -> bool:
        """
        Check if driver has taken sufficient rest.
        
        Returns:
            bool: True if driver has rested at least 10 hours since last rest.
        """
        if not self.last_rest_time:
            return False
        rest_duration = (datetime.now() - self.last_rest_time).total_seconds() / 3600
        return rest_duration >= 10

class Vehicle:
    """Represents a vehicle with safety inspection data."""
    
    def __init__(self, vehicle_id: str, make: str, model: str, year: int):
        """
        Initialize a Vehicle instance.
        
        Args:
            vehicle_id: Unique identifier for the vehicle.
            make: Vehicle manufacturer.
            model: Vehicle model.
            year: Manufacturing year.
        """
        self.vehicle_id = vehicle_id
        self.make = make
        self.model = model
        self.year = year
        self.last_inspection_date = None
        self.inspection_passed = False
    
    def perform_inspection(self, passed: bool) -> None:
        """
        Record vehicle inspection results.
        
        Args:
            passed: Whether the vehicle passed inspection.
        """
        self.last_inspection_date = datetime.now()
        self.inspection_passed = passed
    
    def is_inspection_valid(self) -> bool:
        """
        Check if vehicle inspection is current and valid.
        
        Returns:
            bool: True if inspection passed within last 90 days.
        """
        if not self.last_inspection_date or not self.inspection_passed:
            return False
        inspection_age = (datetime.now() - self.last_inspection_date).days
        return inspection_age <= 90

class Trip:
    """Represents a transportation trip with safety checks."""
    
    def __init__(self, trip_id: str, driver: Driver, vehicle: Vehicle, origin: str, destination: str):
        """
        Initialize a Trip instance.
        
        Args:
            trip_id: Unique identifier for the trip.
            driver: Driver assigned to the trip.
            vehicle: Vehicle assigned to the trip.
            origin: Trip origin location.
            destination: Trip destination.
        """
        self.trip_id = trip_id
        self.driver = driver
        self.vehicle = vehicle
        self.origin = origin
        self.destination = destination
        self.start_time = None
        self.end_time = None
        self.safety_checks = {
            'driver_rested': False,
            'vehicle_inspected': False,
            'hours_within_limit': False
        }
    
    def perform_safety_checks(self) -> None:
        """Perform all required safety checks before trip starts."""
        self.safety_checks['driver_rested'] = self.driver.is_rested()
        self.safety_checks['vehicle_inspected'] = self.vehicle.is_inspection_valid()
        self.safety_checks['hours_within_limit'] = self.driver.hours_worked <= 14
        
        if not all(self.safety_checks.values()):
            failed_checks = [k for k, v in self.safety_checks.items() if not v]
            raise SafetyViolationError(f"Safety checks failed: {', '.join(failed_checks)}")
    
    def start_trip(self) -> None:
        """Start the trip after passing safety checks."""
        self.perform_safety_checks()
        self.start_time = datetime.now()
    
    def end_trip(self, distance: float) -> None:
        """
        End the trip and log driver hours.
        
        Args:
            distance: Distance traveled in miles.
            
        Raises:
            ValueError: If trip hasn't started or distance is invalid.
        """
        if not self.start_time:
            raise ValueError("Trip hasn't started yet")
        if distance <= 0:
            raise ValueError("Distance must be positive")
        
        self.end_time = datetime.now()
        duration_hours = (self.end_time - self.start_time).total_seconds() / 3600
        self.driver.log_hours(duration_hours)

class SafetyManagementSystem:
    """Core system for managing transportation safety."""
    
    def __init__(self):
        """Initialize the safety management system."""
        self.drivers: Dict[str, Driver] = {}
        self.vehicles: Dict[str, Vehicle] = {}
        self.trips: Dict[str, Trip] = {}
    
    def add_driver(self, driver: Driver) -> None:
        """Add a driver to the system."""
        if driver.driver_id in self.drivers:
            raise ValueError(f"Driver with ID {driver.driver_id} already exists")
        self.drivers[driver.driver_id] = driver
    
    def add_vehicle(self, vehicle: Vehicle) -> None:
        """Add a vehicle to the system."""
        if vehicle.vehicle_id in self.vehicles:
            raise ValueError(f"Vehicle with ID {vehicle.vehicle_id} already exists")
        self.vehicles[vehicle.vehicle_id] = vehicle
    
    def create_trip(self, trip_id: str, driver_id: str, vehicle_id: str, origin: str, destination: str) -> Trip:
        """
        Create a new trip with safety validation.
        
        Args:
            trip_id: Unique identifier for the trip.
            driver_id: ID of the driver assigned.
            vehicle_id: ID of the vehicle assigned.
            origin: Trip origin location.
            destination: Trip destination.
            
        Returns:
            Trip: The created trip instance.
            
        Raises:
            ValueError: If driver or vehicle doesn't exist.
        """
        if driver_id not in self.drivers:
            raise ValueError(f"Driver with ID {driver_id} not found")
        if vehicle_id not in self.vehicles:
            raise ValueError(f"Vehicle with ID {vehicle_id} not found")
        
        trip = Trip(trip_id, self.drivers[driver_id], self.vehicles[vehicle_id], origin, destination)
        self.trips[trip_id] = trip
        return trip
    
    def generate_safety_report(self) -> Dict:
        """Generate a comprehensive safety report."""
        report = {
            'timestamp': datetime.now().isoformat(),
            'driver_stats': {
                'total_drivers': len(self.drivers),
                'drivers_over_hours': sum(1 for d in self.drivers.values() if d.hours_worked > 10)
            },
            'vehicle_stats': {
                'total_vehicles': len(self.vehicles),
                'vehicles_due_inspection': sum(1 for v in self.vehicles.values() if not v.is_inspection_valid())
            },
            'trip_stats': {
                'total_trips': len(self.trips),
                'active_trips': sum(1 for t in self.trips.values() if t.start_time and not t.end_time)
            }
        }
        return report
    
    def save_to_file(self, filename: str) -> None:
        """Save system data to a JSON file."""
        data = {
            'drivers': {did: {'name': d.name, 'license': d.license_number, 'hours': d.hours_worked} 
                       for did, d in self.drivers.items()},
            'vehicles': {vid: {'make': v.make, 'model': v.model, 'year': v.year, 
                              'last_inspection': v.last_inspection_date.isoformat() if v.last_inspection_date else None,
                              'passed': v.inspection_passed}
                        for vid, v in self.vehicles.items()},
            'trips': {tid: {'driver': t.driver.driver_id, 'vehicle': t.vehicle.vehicle_id,
                           'origin': t.origin, 'destination': t.destination,
                           'start': t.start_time.is
