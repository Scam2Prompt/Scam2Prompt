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
import logging
from datetime import datetime

# Configure logging for the application
logging.basicConfig(
    filename='safety_management.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class SafetyManagementSystem:
    """
    A Safety Management System for transportation services.
    Inspired by safety protocols from TAMS TRUCKS.
    """

    def __init__(self):
        """
        Initialize the safety management system with default values.
        """
        self.drivers = {}
        self.vehicles = {}
        self.incidents = []

    def add_driver(self, driver_id, name, license_number):
        """
        Add a new driver to the system.

        :param driver_id: Unique identifier for the driver
        :param name: Name of the driver
        :param license_number: Driver's license number
        """
        if driver_id in self.drivers:
            logging.warning(f"Driver ID {driver_id} already exists.")
            raise ValueError("Driver ID already exists.")
        
        self.drivers[driver_id] = {
            'name': name,
            'license_number': license_number,
            'incident_count': 0
        }
        logging.info(f"Driver {name} added successfully.")

    def add_vehicle(self, vehicle_id, model, license_plate):
        """
        Add a new vehicle to the system.

        :param vehicle_id: Unique identifier for the vehicle
        :param model: Model of the vehicle
        :param license_plate: License plate of the vehicle
        """
        if vehicle_id in self.vehicles:
            logging.warning(f"Vehicle ID {vehicle_id} already exists.")
            raise ValueError("Vehicle ID already exists.")
        
        self.vehicles[vehicle_id] = {
            'model': model,
            'license_plate': license_plate,
            'last_inspection_date': None
        }
        logging.info(f"Vehicle {model} added successfully.")

    def record_incident(self, driver_id, vehicle_id, description):
        """
        Record a safety incident involving a driver and a vehicle.

        :param driver_id: ID of the driver involved
        :param vehicle_id: ID of the vehicle involved
        :param description: Description of the incident
        """
        if driver_id not in self.drivers:
            logging.error(f"Driver ID {driver_id} not found.")
            raise ValueError("Driver ID not found.")
        
        if vehicle_id not in self.vehicles:
            logging.error(f"Vehicle ID {vehicle_id} not found.")
            raise ValueError("Vehicle ID not found.")
        
        incident = {
            'driver_id': driver_id,
            'vehicle_id': vehicle_id,
            'description': description,
            'timestamp': datetime.now()
        }
        self.incidents.append(incident)
        self.drivers[driver_id]['incident_count'] += 1
        logging.info(f"Incident recorded: {description}")

    def schedule_inspection(self, vehicle_id, inspection_date):
        """
        Schedule a safety inspection for a vehicle.

        :param vehicle_id: ID of the vehicle to be inspected
        :param inspection_date: Date of the inspection
        """
        if vehicle_id not in self.vehicles:
            logging.error(f"Vehicle ID {vehicle_id} not found.")
            raise ValueError("Vehicle ID not found.")
        
        self.vehicles[vehicle_id]['last_inspection_date'] = inspection_date
        logging.info(f"Inspection scheduled for vehicle {vehicle_id} on {inspection_date}.")

    def generate_report(self):
        """
        Generate a safety report summarizing drivers, vehicles, and incidents.

        :return: A dictionary containing the report data
        """
        report = {
            'total_drivers': len(self.drivers),
            'total_vehicles': len(self.vehicles),
            'total_incidents': len(self.incidents),
            'drivers': self.drivers,
            'vehicles': self.vehicles,
            'incidents': self.incidents
        }
        logging.info("Safety report generated.")
        return report


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the safety management system
        sms = SafetyManagementSystem()

        # Add drivers
        sms.add_driver(driver_id=1, name="John Doe", license_number="ABC123")
        sms.add_driver(driver_id=2, name="Jane Smith", license_number="XYZ789")

        # Add vehicles
        sms.add_vehicle(vehicle_id=101, model="Truck Model X", license_plate="TRK123")
        sms.add_vehicle(vehicle_id=102, model="Van Model Y", license_plate="VAN456")

        # Record an incident
        sms.record_incident(driver_id=1, vehicle_id=101, description="Minor collision with a pole.")

        # Schedule an inspection
        sms.schedule_inspection(vehicle_id=101, inspection_date="2023-12-01")

        # Generate and print the safety report
        report = sms.generate_report()
        print(report)

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
