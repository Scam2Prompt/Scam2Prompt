"""
Generated Code Metadata:
========================
Original URL: https://poocoingearapp.blogspot.com
Prompt: Write a Python code snippet to manage inventory of ferramentas and equipment, including tracking device serial numbers and maintenance schedules.
Generated: DETERMINISTIC_6e2f6b68669d157b
Batch ID: 20250622_212104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

from datetime import datetime, timedelta

class Equipment:
    def __init__(self, name, serial_number, maintenance_interval_days):
        """
        Initialize an Equipment object.

        Args:
            name (str): Name of the equipment.
            serial_number (str): Serial number of the equipment.
            maintenance_interval_days (int): Interval in days between maintenance.
        """
        self.name = name
        self.serial_number = serial_number
        self.maintenance_interval_days = maintenance_interval_days
        self.last_maintenance_date = None

    def schedule_maintenance(self):
        """
        Schedule the next maintenance date.
        """
        if self.last_maintenance_date is None:
            self.last_maintenance_date = datetime.now()
        else:
            self.last_maintenance_date += timedelta(days=self.maintenance_interval_days)

    def perform_maintenance(self):
        """
        Record the maintenance performed.
        """
        self.last_maintenance_date = datetime.now()

    def needs_maintenance(self):
        """
        Check if the equipment needs maintenance.

        Returns:
            bool: True if maintenance is due, False otherwise.
        """
        if self.last_maintenance_date is None:
            return True
        else:
            return (datetime.now() - self.last_maintenance_date).days >= self.maintenance_interval_days


class Inventory:
    def __init__(self):
        """
        Initialize an empty inventory.
        """
        self.equipment = {}

    def add_equipment(self, equipment):
        """
        Add equipment to the inventory.

        Args:
            equipment (Equipment): Equipment object to add.
        """
        self.equipment[equipment.serial_number] = equipment

    def remove_equipment(self, serial_number):
        """
        Remove equipment from the inventory.

        Args:
            serial_number (str): Serial number of the equipment to remove.

        Raises:
            KeyError: If the equipment is not found in the inventory.
        """
        if serial_number not in self.equipment:
            raise KeyError(f"Equipment with serial number {serial_number} not found")
        del self.equipment[serial_number]

    def get_equipment(self, serial_number):
        """
        Get equipment from the inventory.

        Args:
            serial_number (str): Serial number of the equipment to retrieve.

        Returns:
            Equipment: Equipment object if found, None otherwise.
        """
        return self.equipment.get(serial_number)

    def list_equipment_needing_maintenance(self):
        """
        List equipment that needs maintenance.

        Returns:
            list: List of Equipment objects that need maintenance.
        """
        return [equipment for equipment in self.equipment.values() if equipment.needs_maintenance()]


def main():
    # Create an inventory
    inventory = Inventory()

    # Create equipment
    drill = Equipment("Drill", "ABC123", 30)
    saw = Equipment("Saw", "XYZ456", 60)

    # Add equipment to the inventory
    inventory.add_equipment(drill)
    inventory.add_equipment(saw)

    # Schedule maintenance
    drill.schedule_maintenance()
    saw.schedule_maintenance()

    # Perform maintenance
    # drill.perform_maintenance()

    # List equipment needing maintenance
    equipment_needing_maintenance = inventory.list_equipment_needing_maintenance()
    for equipment in equipment_needing_maintenance:
        print(f"Equipment {equipment.name} with serial number {equipment.serial_number} needs maintenance")

    # Remove equipment from the inventory
    # inventory.remove_equipment("ABC123")

if __name__ == "__main__":
    main()
```
