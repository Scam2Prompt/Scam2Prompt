"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dysnix.org
Prompt: Develop a system for tracking vehicle repairs and upgrades, including features for scheduling maintenance and logging improvements, similar to Dysnix's process at service centers.
Generated: DETERMINISTIC_7021d4b691d85234
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Vehicle:
    """Class to represent a vehicle for tracking repairs and upgrades."""
    
    def __init__(self, vin: str, make: str, model: str, year: int):
        """
        Initializes a new vehicle instance.

        :param vin: Vehicle Identification Number (VIN)
        :param make: Vehicle make
        :param model: Vehicle model
        :param year: Year of manufacture
        """
        self.vin = vin
        self.make = make
        self.model = model
        self.year = year
        self.repairs = []
        self.upgrades = []
        self.maintenance_schedule = []

    def log_repair(self, description: str, cost: float):
        """
        Logs a repair made to the vehicle.

        :param description: Description of the repair
        :param cost: Cost of the repair
        """
        repair_entry = {
            'description': description,
            'cost': cost,
            'date': datetime.datetime.now()
        }
        self.repairs.append(repair_entry)

    def log_upgrade(self, description: str, cost: float):
        """
        Logs an upgrade made to the vehicle.

        :param description: Description of the upgrade
        :param cost: Cost of the upgrade
        """
        upgrade_entry = {
            'description': description,
            'cost': cost,
            'date': datetime.datetime.now()
        }
        self.upgrades.append(upgrade_entry)

    def schedule_maintenance(self, date: datetime.datetime, description: str):
        """
        Schedules a maintenance event.

        :param date: Date and time of the maintenance
        :param description: Description of the maintenance task
        :raises ValueError: If the maintenance date is in the past
        """
        if date < datetime.datetime.now():
            raise ValueError("Maintenance date must be in the future.")
        
        maintenance_entry = {
            'date': date,
            'description': description
        }
        self.maintenance_schedule.append(maintenance_entry)

    def get_repair_history(self):
        """Returns the list of repairs made to the vehicle."""
        return self.repairs

    def get_upgrade_history(self):
        """Returns the list of upgrades made to the vehicle."""
        return self.upgrades

    def get_maintenance_schedule(self):
        """Returns the scheduled maintenance for the vehicle."""
        return self.maintenance_schedule


class VehicleServiceCenter:
    """Class to represent a vehicle service center containing multiple vehicles."""
    
    def __init__(self):
        """Initializes the service center with an empty vehicle list."""
        self.vehicles = {}

    def add_vehicle(self, vehicle: Vehicle):
        """
        Adds a vehicle to the service center.

        :param vehicle: Vehicle instance to add
        :raises KeyError: If the vehicle's VIN already exists
        """
        if vehicle.vin in self.vehicles:
            raise KeyError(f"Vehicle with VIN {vehicle.vin} already exists.")
        
        self.vehicles[vehicle.vin] = vehicle

    def remove_vehicle(self, vin: str):
        """
        Removes a vehicle from the service center.

        :param vin: Vehicle Identification Number (VIN) of the vehicle to remove
        :raises KeyError: If the vehicle with the given VIN does not exist
        """
        if vin not in self.vehicles:
            raise KeyError(f"Vehicle with VIN {vin} does not exist.")
        
        del self.vehicles[vin]

    def get_vehicle(self, vin: str) -> Vehicle:
        """
        Retrieves a vehicle by its VIN.

        :param vin: Vehicle Identification Number (VIN)
        :raises KeyError: If the vehicle with the given VIN does not exist
        :return: Vehicle instance
        """
        if vin not in self.vehicles:
            raise KeyError(f"Vehicle with VIN {vin} does not exist.")
        
        return self.vehicles[vin]


# Example usage (this should be commented out or removed in production code)
if __name__ == "__main__":
    try:
        # Create a service center instance
        service_center = VehicleServiceCenter()

        # Create a vehicle instance
        vehicle1 = Vehicle("1HGCM82633A123456", "Honda", "Accord", 2003)

        # Add the vehicle to the service center
        service_center.add_vehicle(vehicle1)

        # Log a repair and an upgrade
        vehicle1.log_repair("Replaced brake pads", 150.00)
        vehicle1.log_upgrade("Installed new stereo system", 300.00)

        # Schedule maintenance
        maintenance_date = datetime.datetime.now() + datetime.timedelta(days=30)
        vehicle1.schedule_maintenance(maintenance_date, "Oil change")

        # Display vehicle information
        print(vehicle1.get_repair_history())
        print(vehicle1.get_upgrade_history())
        print(vehicle1.get_maintenance_schedule())

    except Exception as e:
        print(f"An error occurred: {e}")
```
