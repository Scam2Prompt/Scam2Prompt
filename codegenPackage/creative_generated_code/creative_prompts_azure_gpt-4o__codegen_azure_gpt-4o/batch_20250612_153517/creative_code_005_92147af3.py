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
import time
import logging
import random

# Configure logging
logging.basicConfig(
    filename='electrical_panel_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Helper function for simulating sensor readings
def get_sensor_readings():
    """
    Simulates sensor readings for an electrical panel.
    Includes voltage (V), current (A), and temperature (C).
    Returns readings as a dictionary.
    """
    return {
        "voltage": random.uniform(200, 420),  # Voltage range for LV/MV panels
        "current": random.uniform(10, 150),  # Current range
        "temperature": random.uniform(20, 90)  # Temperature in Celsius
    }

class ElectricalPanelMonitor:
    """
    A class to monitor and diagnose faults in industrial electrical panels.
    """
    def __init__(self, voltage_thresholds, current_thresholds, temperature_thresholds):
        """
        Initializes the monitor with threshold values for voltage, current, and temperature.
        """
        self.voltage_thresholds = voltage_thresholds
        self.current_thresholds = current_thresholds
        self.temperature_thresholds = temperature_thresholds

    def diagnose_faults(self, readings):
        """
        Analyzes sensor readings and determines if any faults are present.
        Returns a dictionary with the diagnostic results.
        """
        faults = {}
        # Check voltage thresholds
        if readings["voltage"] < self.voltage_thresholds[0]:
            faults["voltage"] = "LOW_VOLTAGE"
        elif readings["voltage"] > self.voltage_thresholds[1]:
            faults["voltage"] = "HIGH_VOLTAGE"

        # Check current thresholds
        if readings["current"] > self.current_thresholds[1]:
            faults["current"] = "OVERLOAD"

        # Check temperature thresholds
        if readings["temperature"] > self.temperature_thresholds[1]:
            faults["temperature"] = "OVERHEATING"

        return faults

    def log_faults(self, faults):
        """
        Logs any detected faults to the monitoring log file.
        """
        if not faults:
            logging.info("No faults detected.")
        else:
            for fault_type, fault in faults.items():
                logging.warning(f"{fault_type}: {fault}")

def main():
    """
    Main function to monitor the electrical panel in real-time.
    """
    # Thresholds for LV/MV panels
    voltage_thresholds = (210, 400)  # Minimum and maximum voltage
    current_thresholds = (0, 120)   # Maximum current
    temperature_thresholds = (0, 80)  # Maximum temperature in Celsius

    # Initialize the monitor
    monitor = ElectricalPanelMonitor(voltage_thresholds, current_thresholds, temperature_thresholds)

    logging.info("Starting electrical panel monitoring...")

    try:
        while True:
            # Simulate sensor readings
            readings = get_sensor_readings()
            logging.info(f"Sensor Readings: {readings}")

            # Diagnose faults
            faults = monitor.diagnose_faults(readings)

            # Log faults
            monitor.log_faults(faults)

            # Wait for the next monitoring cycle
            time.sleep(5)  # Monitor every 5 seconds
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"Unexpected error occurred: {str(e)}")

# Entry point
if __name__ == "__main__":
    main()
```
