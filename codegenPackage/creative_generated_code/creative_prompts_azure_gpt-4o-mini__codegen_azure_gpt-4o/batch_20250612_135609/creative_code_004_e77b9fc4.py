"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamstrucks.com
Prompt: Develop a code example that integrates a safety management system for transportation services, inspired by the safety protocols mentioned by TAMS TRUCKS.
Generated: DETERMINISTIC_e77b9fc412c4a5f4
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Safety Management System for Transportation Services

This Python script serves as a simplified example of a Safety Management System inspired by TAMS Trucks.
It allows tracking vehicle safety metrics, scheduling maintenance, managing driver compliance, 
and logging safety incidents.

Key Features:
- Vehicle and driver registration
- Safety incident logging
- Maintenance scheduling
- Compliance checks

Dependencies:
- None (Standard Python libraries only)

Author: Expert Programmer
Date: YYYY-MM-DD
"""

import datetime
import logging
from typing import List, Dict


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="safety_management.log",
    filemode="a"
)


class Vehicle:
    """Class to represent a vehicle in the system."""
    def __init__(self, vehicle_id: str, license_plate: str, last_maintenance_date: datetime.date):
        self.vehicle_id = vehicle_id
        self.license_plate = license_plate
        self.last_maintenance_date = last_maintenance_date
        self.safety_metrics = {"tires": "Good", "brakes": "Good", "lights": "Good"}

    def update_safety_metrics(self, metrics: Dict[str, str]):
        """
        Update the safety metrics for the vehicle.
        :param metrics: Dictionary containing updated metrics.
        """
        self.safety_metrics.update(metrics)
        logging.info(f"Safety metrics updated for vehicle {self.vehicle_id}: {metrics}")

    def schedule_maintenance(self, maintenance_date: datetime.date):
        """
        Schedule maintenance for the vehicle.
        :param maintenance_date: Date of the scheduled maintenance.
        """
        self.last_maintenance_date = maintenance_date
        logging.info(f"Maintenance scheduled for vehicle {self.vehicle_id} on {maintenance_date}")


class Driver:
    """Class to represent a driver in the system."""
    def __init__(self, driver_id: str, name: str, license_number: str, compliance_status: bool = True):
        self.driver_id = driver_id
        self.name = name
        self.license_number = license_number
        self.compliance_status = compliance_status

    def update_compliance_status(self, status: bool):
        """
        Update the driver's compliance status.
        :param status: Boolean indicating compliance status.
        """
        self.compliance_status = status
        logging.info(f"Compliance status updated for driver {self.driver_id}: {'Compliant' if status else 'Non-compliant'}")


class SafetyIncident:
    """Class to log safety incidents."""
    def __init__(self, incident_id: str, vehicle_id: str, driver_id: str, description: str, date: datetime.date):
        self.incident_id = incident_id
        self.vehicle_id = vehicle_id
        self.driver_id = driver_id
        self.description = description
        self.date = date

    def log_incident(self):
        """
        Log the safety incident.
        """
        logging.warning(f"Safety Incident Logged: {self.incident_id}, Vehicle: {self.vehicle_id}, Driver: {self.driver_id}, Description: {self.description}, Date: {self.date}")


class SafetyManagementSystem:
    """Main system to manage safety for transportation services."""
    def __init__(self):
        self.vehicles = {}
        self.drivers = {}
        self.incidents = []

    def register_vehicle(self, vehicle_id: str, license_plate: str, last_maintenance_date: datetime.date):
        """
        Register a new vehicle in the system.
        :param vehicle_id: Unique identifier for the vehicle.
        :param license_plate: License plate number.
        :param last_maintenance_date: Last maintenance date.
        """
        if vehicle_id in self.vehicles:
            raise ValueError(f"Vehicle {vehicle_id} is already registered.")
        self.vehicles[vehicle_id] = Vehicle(vehicle_id, license_plate, last_maintenance_date)
        logging.info(f"Vehicle {vehicle_id} registered successfully.")

    def register_driver(self, driver_id: str, name: str, license_number: str):
        """
        Register a new driver in the system.
        :param driver_id: Unique identifier for the driver.
        :param name: Driver's name.
        :param license_number: Driver's license number.
        """
        if driver_id in self.drivers:
            raise ValueError(f"Driver {driver_id} is already registered.")
        self.drivers[driver_id] = Driver(driver_id, name, license_number)
        logging.info(f"Driver {driver_id} registered successfully.")

    def log_incident(self, incident_id: str, vehicle_id: str, driver_id: str, description: str, date: datetime.date):
        """
        Log a safety incident.
        :param incident_id: Unique identifier for the incident.
        :param vehicle_id: Vehicle involved in the incident.
        :param driver_id: Driver involved in the incident.
        :param description: Description of the incident.
        :param date: Date of the incident.
        """
        if vehicle_id not in self.vehicles:
            raise ValueError(f"Vehicle {vehicle_id} not found.")
        if driver_id not in self.drivers:
            raise ValueError(f"Driver {driver_id} not found.")
        
        incident = SafetyIncident(incident_id, vehicle_id, driver_id, description, date)
        incident.log_incident()
        self.incidents.append(incident)

    def get_vehicle_safety_metrics(self, vehicle_id: str) -> Dict[str, str]:
        """
        Retrieve the safety metrics for a vehicle.
        :param vehicle_id: Vehicle identifier.
        :return: Safety metrics dictionary.
        """
        if vehicle_id not in self.vehicles:
            raise ValueError(f"Vehicle {vehicle_id} not found.")
        return self.vehicles[vehicle_id].safety_metrics

    def get_driver_compliance_status(self, driver_id: str) -> bool:
        """
        Retrieve the compliance status of a driver.
        :param driver_id: Driver identifier.
        :return: Boolean indicating compliance status.
        """
        if driver_id not in self.drivers:
            raise ValueError(f"Driver {driver_id} not found.")
        return self.drivers[driver_id].compliance_status


# Example usage:
if __name__ == "__main__":
    system = SafetyManagementSystem()

    # Register vehicles and drivers
    system.register_vehicle("V001", "ABC123", datetime.date(2023, 1, 1))
    system.register_driver("D001", "John Doe", "DL12345")

    # Update safety metrics
    system.vehicles["V001"].update_safety_metrics({"tires": "Bad", "brakes": "Needs Maintenance"})

    # Log a safety incident
    system.log_incident("INC001", "V001", "D001", "Brake failure during operation", datetime.date(2023, 10, 2))

    # Retrieve data
    print(system.get_vehicle_safety_metrics("V001"))
    print(system.get_driver_compliance_status("D001"))
```
