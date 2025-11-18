"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payeshnirooco.com
Prompt: Write code to monitor and diagnose faults in industrial electrical panels, including both LV and MV systems, based on پایش نیرو's expertise.
Generated: DETERMINISTIC_92147af3f3a5cb54
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import random
import time

# Configure logging
logging.basicConfig(
    filename='panel_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class ElectricalPanelMonitor:
    def __init__(self, panel_id):
        """
        Initializes the ElectricalPanelMonitor object.

        :param panel_id: Unique identifier for the electrical panel
        """
        self.panel_id = panel_id
        self.is_faulty = False

    def read_sensor_data(self):
        """
        Simulates reading sensor data from the electrical panel.
        
        :returns: A dictionary containing simulated voltage and current values
        """
        voltage = random.uniform(200, 480)  # Simulated voltage in volts
        current = random.uniform(0, 100)    # Simulated current in amperes
        return {'voltage': voltage, 'current': current}

    def diagnose_faults(self, data):
        """
        Diagnoses faults based on sensor data.

        :param data: Dictionary containing voltage and current readings
        :returns: None
        """
        if data['voltage'] < 210 or data['voltage'] > 480:
            self.is_faulty = True
            logging.warning(f"Voltage out of range in panel {self.panel_id}: {data['voltage']} V")

        if data['current'] > 90:
            self.is_faulty = True
            logging.warning(f"Current overload in panel {self.panel_id}: {data['current']} A")

    def monitor_panel(self):
        """
        Continuously monitors the electrical panel for faults.
        
        :returns: None
        """
        while True:
            try:
                sensor_data = self.read_sensor_data()
                logging.info(f"Panel {self.panel_id} - Reading: {sensor_data}")
                self.diagnose_faults(sensor_data)

                if self.is_faulty:
                    logging.error(f"Fault detected in panel {self.panel_id}. Immediate action required!")
                    self.is_faulty = False  # Reset for next iteration
                time.sleep(5)  # Wait before the next reading

            except Exception as e:
                logging.exception(f"An error occurred while monitoring panel {self.panel_id}: {e}")
                break  # Exit the loop on error


def main():
    """
    Main function to initiate the electrical panel monitoring.
    
    :returns: None
    """
    panel_id = 'Panel_01'
    monitor = ElectricalPanelMonitor(panel_id)
    monitor.monitor_panel()


if __name__ == '__main__':
    main()
```
