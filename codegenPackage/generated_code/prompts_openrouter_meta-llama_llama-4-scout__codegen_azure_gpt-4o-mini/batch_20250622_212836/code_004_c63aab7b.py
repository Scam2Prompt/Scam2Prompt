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
class SurveyingEquipment:
    """
    A class to represent surveying equipment and its calibration and repair process.
    """

    def __init__(self, equipment_type):
        """
        Initializes the SurveyingEquipment instance.

        :param equipment_type: str - Type of the surveying equipment (e.g., 'Theodolite', 'Automatic Level').
        """
        self.equipment_type = equipment_type
        self.is_calibrated = False
        self.is_functional = True

    def calibrate(self):
        """
        Calibrates the surveying equipment.
        Raises an error if the equipment is not functional.
        """
        if not self.is_functional:
            raise ValueError(f"{self.equipment_type} is not functional and cannot be calibrated.")
        
        # Simulate calibration process
        print(f"Calibrating {self.equipment_type}...")
        self.is_calibrated = True
        print(f"{self.equipment_type} has been calibrated successfully.")

    def repair(self):
        """
        Repairs the surveying equipment.
        Sets the equipment to functional state.
        """
        print(f"Repairing {self.equipment_type}...")
        self.is_functional = True
        print(f"{self.equipment_type} has been repaired and is now functional.")

    def service_equipment(self):
        """
        Services the equipment by attempting to calibrate it.
        If the equipment is not functional, it will first attempt to repair it.
        """
        try:
            if not self.is_functional:
                print(f"{self.equipment_type} is not functional. Attempting repair...")
                self.repair()
            self.calibrate()
        except ValueError as e:
            print(f"Error: {e}")

def main():
    """
    Main function to demonstrate the calibration and repair process of surveying equipment.
    """
    # Create instances of surveying equipment
    theodolite = SurveyingEquipment('Theodolite')
    automatic_level = SurveyingEquipment('Automatic Level')

    # Simulate a scenario where the equipment is not functional
    automatic_level.is_functional = False

    # Service the equipment
    theodolite.service_equipment()  # Should calibrate successfully
    automatic_level.service_equipment()  # Should repair and then calibrate

if __name__ == "__main__":
    main()
```
