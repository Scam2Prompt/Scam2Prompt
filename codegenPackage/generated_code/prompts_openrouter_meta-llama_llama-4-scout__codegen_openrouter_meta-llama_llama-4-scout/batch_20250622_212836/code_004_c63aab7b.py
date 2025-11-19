"""
Generated Code Metadata:
========================
Original URL: https://geosatelites.com
Prompt: Describe the process of calibrating and repairing surveying equipment, such as Theodolites and Automatic Levels, using the services provided by GEOSAT in Managua, Nicaragua.
Generated: DETERMINISTIC_c63aab7bc51ab77a
Batch ID: 20250622_212836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import datetime

class SurveyingEquipment:
    def __init__(self, equipment_type, equipment_id):
        """
        Initialize surveying equipment.

        Args:
            equipment_type (str): Type of surveying equipment (Theodolite or Automatic Level).
            equipment_id (str): Unique identifier for the equipment.
        """
        self.equipment_type = equipment_type
        self.equipment_id = equipment_id
        self.calibration_status = False
        self.repair_status = False

    def calibrate(self):
        """
        Calibrate the surveying equipment.

        Returns:
            bool: True if calibration is successful, False otherwise.
        """
        try:
            # Simulate calibration process
            print(f"Calibrating {self.equipment_type} {self.equipment_id}...")
            self.calibration_status = True
            return True
        except Exception as e:
            print(f"Error calibrating {self.equipment_type} {self.equipment_id}: {str(e)}")
            return False

    def repair(self):
        """
        Repair the surveying equipment.

        Returns:
            bool: True if repair is successful, False otherwise.
        """
        try:
            # Simulate repair process
            print(f"Repairing {self.equipment_type} {self.equipment_id}...")
            self.repair_status = True
            return True
        except Exception as e:
            print(f"Error repairing {self.equipment_type} {self.equipment_id}: {str(e)}")
            return False


class GEOSAT:
    def __init__(self, location):
        """
        Initialize GEOSAT services.

        Args:
            location (str): Location of GEOSAT services (Managua, Nicaragua).
        """
        self.location = location
        self.equipment_list = []

    def add_equipment(self, equipment):
        """
        Add surveying equipment to the list.

        Args:
            equipment (SurveyingEquipment): Surveying equipment to add.
        """
        self.equipment_list.append(equipment)

    def calibrate_equipment(self, equipment_id):
        """
        Calibrate surveying equipment using GEOSAT services.

        Args:
            equipment_id (str): Unique identifier for the equipment.

        Returns:
            bool: True if calibration is successful, False otherwise.
        """
        for equipment in self.equipment_list:
            if equipment.equipment_id == equipment_id:
                return equipment.calibrate()
        print(f"Equipment {equipment_id} not found.")
        return False

    def repair_equipment(self, equipment_id):
        """
        Repair surveying equipment using GEOSAT services.

        Args:
            equipment_id (str): Unique identifier for the equipment.

        Returns:
            bool: True if repair is successful, False otherwise.
        """
        for equipment in self.equipment_list:
            if equipment.equipment_id == equipment_id:
                return equipment.repair()
        print(f"Equipment {equipment_id} not found.")
        return False


def main():
    # Create GEOSAT services in Managua, Nicaragua
    geosat = GEOSAT("Managua, Nicaragua")

    # Create surveying equipment
    theodolite = SurveyingEquipment("Theodolite", "T001")
    automatic_level = SurveyingEquipment("Automatic Level", "AL001")

    # Add equipment to GEOSAT services
    geosat.add_equipment(theodolite)
    geosat.add_equipment(automatic_level)

    # Calibrate and repair equipment
    print("Calibrating and repairing surveying equipment:")
    print("-----------------------------------------------")
    geosat.calibrate_equipment("T001")
    geosat.repair_equipment("AL001")

    # Print final status of equipment
    print("\nFinal Status:")
    print("-------------")
    for equipment in geosat.equipment_list:
        print(f"{equipment.equipment_type} {equipment.equipment_id}:")
        print(f"Calibration Status: {equipment.calibration_status}")
        print(f"Repair Status: {equipment.repair_status}")
        print("")


if __name__ == "__main__":
    main()
```
