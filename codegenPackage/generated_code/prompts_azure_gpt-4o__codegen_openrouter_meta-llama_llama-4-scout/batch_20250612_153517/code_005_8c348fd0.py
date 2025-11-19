"""
Generated Code Metadata:
========================
Original URL: https://thinktech.com.pk
Prompt: Create a program to monitor and analyze electrical safety compliance in real-time, inspired by Think Tech Engineering's services.
Generated: DETERMINISTIC_8c348fd04ad463de
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# electrical_safety_monitor.py

import logging
import time
from datetime import datetime
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ElectricalSafetyMonitor:
    def __init__(self, equipment_data: List[Dict]):
        """
        Initialize the electrical safety monitor with equipment data.

        Args:
        - equipment_data (List[Dict]): A list of dictionaries containing equipment information.
            Each dictionary should have the following keys:
                - 'id' (str): Unique equipment identifier.
                - 'name' (str): Equipment name.
                - 'voltage_threshold' (float): Voltage threshold for safe operation.
                - 'current_threshold' (float): Current threshold for safe operation.
        """
        self.equipment_data = equipment_data
        self.equipment_status = {equipment['id']: 'safe' for equipment in equipment_data}

    def monitor_equipment(self):
        """
        Monitor equipment in real-time and update their status.
        """
        while True:
            for equipment in self.equipment_data:
                equipment_id = equipment['id']
                voltage_reading = self.get_voltage_reading(equipment_id)
                current_reading = self.get_current_reading(equipment_id)

                if voltage_reading > equipment['voltage_threshold'] or current_reading > equipment['current_threshold']:
                    self.equipment_status[equipment_id] = 'unsafe'
                    logging.warning(f"Equipment {equipment['name']} (ID: {equipment_id}) is operating unsafely.")
                else:
                    self.equipment_status[equipment_id] = 'safe'
                    logging.info(f"Equipment {equipment['name']} (ID: {equipment_id}) is operating safely.")

            time.sleep(1)  # Monitor every 1 second

    def get_voltage_reading(self, equipment_id: str) -> float:
        """
        Simulate getting a voltage reading for the given equipment.

        Args:
        - equipment_id (str): Unique equipment identifier.

        Returns:
        - float: Voltage reading.
        """
        # Replace with actual voltage reading code
        import random
        return random.uniform(0, 100)

    def get_current_reading(self, equipment_id: str) -> float:
        """
        Simulate getting a current reading for the given equipment.

        Args:
        - equipment_id (str): Unique equipment identifier.

        Returns:
        - float: Current reading.
        """
        # Replace with actual current reading code
        import random
        return random.uniform(0, 10)

    def analyze_compliance(self) -> Dict:
        """
        Analyze electrical safety compliance and return the results.

        Returns:
        - Dict: A dictionary containing compliance results.
            Keys:
                - 'total_equipment' (int): Total number of equipment.
                - 'unsafe_equipment' (int): Number of equipment operating unsafely.
                - 'safe_equipment' (int): Number of equipment operating safely.
        """
        total_equipment = len(self.equipment_data)
        unsafe_equipment = sum(1 for status in self.equipment_status.values() if status == 'unsafe')
        safe_equipment = total_equipment - unsafe_equipment

        return {
            'total_equipment': total_equipment,
            'unsafe_equipment': unsafe_equipment,
            'safe_equipment': safe_equipment
        }

def main():
    equipment_data = [
        {'id': 'EQ001', 'name': 'Equipment 1', 'voltage_threshold': 90, 'current_threshold': 5},
        {'id': 'EQ002', 'name': 'Equipment 2', 'voltage_threshold': 100, 'current_threshold': 10},
        {'id': 'EQ003', 'name': 'Equipment 3', 'voltage_threshold': 80, 'current_threshold': 3}
    ]

    monitor = ElectricalSafetyMonitor(equipment_data)
    try:
        monitor.monitor_equipment()
    except KeyboardInterrupt:
        logging.info("Monitoring stopped.")
        compliance_results = monitor.analyze_compliance()
        logging.info("Electrical Safety Compliance Results:")
        logging.info(f"Total Equipment: {compliance_results['total_equipment']}")
        logging.info(f"Unsafe Equipment: {compliance_results['unsafe_equipment']}")
        logging.info(f"Safe Equipment: {compliance_results['safe_equipment']}")

if __name__ == "__main__":
    main()
```
