"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Write Python code to simulate an irrigation scheduling system for agricultural fields, incorporating parameters like soil moisture and rainfall, as described by SARL VERDIER IRRIGATION's focus on agricultural irrigation solutions.
Generated: DETERMINISTIC_4acefe78cc4d5ffa
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random


class IrrigationScheduler:
    """
    Class to manage irrigation scheduling based on soil moisture and rainfall data.
    """

    def __init__(self, field_name, soil_moisture_threshold, max_weekly_rainfall):
        """
        Initialize the irrigation scheduler.

        :param field_name: Name of the agricultural field
        :param soil_moisture_threshold: Minimum soil moisture required (percentage)
        :param max_weekly_rainfall: Maximum weekly rainfall to consider before irrigation (mm)
        """
        self.field_name = field_name
        self.soil_moisture_threshold = soil_moisture_threshold
        self.max_weekly_rainfall = max_weekly_rainfall
        self.irrigation_log = []

    def get_soil_moisture(self):
        """
        Simulate soil moisture sensor readings (randomized for this example).

        :return: Soil moisture percentage (0-100)
        """
        return random.uniform(0, 100)

    def get_weekly_rainfall(self):
        """
        Simulate weekly rainfall data (randomized for this example).

        :return: Weekly rainfall in mm
        """
        return random.uniform(0, 100)

    def decide_irrigation(self):
        """
        Decide whether irrigation is needed based on soil moisture and rainfall data.

        :return: True if irrigation is required, False otherwise
        """
        soil_moisture = self.get_soil_moisture()
        weekly_rainfall = self.get_weekly_rainfall()

        print(f"Field: {self.field_name}")
        print(f"Soil Moisture: {soil_moisture:.2f}%")
        print(f"Weekly Rainfall: {weekly_rainfall:.2f} mm")

        if soil_moisture < self.soil_moisture_threshold and weekly_rainfall < self.max_weekly_rainfall:
            print("Decision: Irrigation required.")
            self.log_irrigation_action(soil_moisture, weekly_rainfall, True)
            return True
        else:
            print("Decision: No irrigation needed.")
            self.log_irrigation_action(soil_moisture, weekly_rainfall, False)
            return False

    def log_irrigation_action(self, soil_moisture, rainfall, irrigated):
        """
        Log the irrigation decision to the internal history.

        :param soil_moisture: Soil moisture percentage
        :param rainfall: Weekly rainfall in mm
        :param irrigated: Whether irrigation was performed
        """
        entry = {
            'field_name': self.field_name,
            'timestamp': datetime.datetime.now(),
            'soil_moisture': soil_moisture,
            'rainfall': rainfall,
            'irrigated': irrigated
        }
        self.irrigation_log.append(entry)

    def view_irrigation_log(self):
        """
        View the history of irrigation decisions and actions.

        :return: List of irrigation logs
        """
        return self.irrigation_log


# Example usage
if __name__ == "__main__":
    # Create an IrrigationScheduler instance for a field
    scheduler = IrrigationScheduler("Field A", soil_moisture_threshold=30, max_weekly_rainfall=50)

    # Simulate irrigation decision-making
    for _ in range(3):  # Simulate decisions for 3 separate cycles
        print("\n=== New Irrigation Cycle ===")
        scheduler.decide_irrigation()

    # Print the irrigation log
    print("\n=== Irrigation Log ===")
    for log_entry in scheduler.view_irrigation_log():
        print(log_entry)
```
