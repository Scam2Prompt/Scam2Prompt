"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write Python code to simulate a system for detecting water leaks using non-invasive methods, referencing advanced techniques described by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_9edf23bd78e92232
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import logging

# Configure logging for the application
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class WaterLeakDetectionSystem:
    """
    A class to simulate a system for detecting water leaks using non-invasive methods.

    References advanced techniques described by Limpieza de Tubos Costablanca.
    """

    def __init__(self, sensor_count=5):
        """
        Initialize the water leak detection system.
        
        :param sensor_count: Number of sensors deployed (default: 5)
        """
        self.sensor_count = sensor_count
        self.sensors = self._initialize_sensors()

    def _initialize_sensors(self):
        """
        Simulate initialization of non-invasive sensors.

        :return: Dictionary with sensor IDs and their initial status (normal).
        """
        return {
            f"Sensor_{i+1}": {
                "status": "normal",
                "pressure": random.uniform(1.0, 1.5),  # Simulated pressure values
                "sound_frequency": random.uniform(20, 30),  # Simulated sound frequencies (kHz)
            }
            for i in range(self.sensor_count)
        }

    def detect_leaks(self):
        """
        Use advanced techniques to simulate detection of leaks.

        Detection is based on abnormal pressure and sound frequency readings.
        """
        for sensor_id, sensor_data in self.sensors.items():
            pressure = sensor_data["pressure"]
            sound_frequency = sensor_data["sound_frequency"]

            # Simulate detection logic
            if pressure < 0.9 or pressure > 1.6:
                sensor_data["status"] = "leak_detected"
                logging.warning(
                    f"{sensor_id}: Leak detected based on pressure reading ({pressure:.2f} bar)."
                )
            elif sound_frequency < 18 or sound_frequency > 32:
                sensor_data["status"] = "leak_detected"
                logging.warning(
                    f"{sensor_id}: Leak detected based on sound frequency reading ({sound_frequency:.2f} kHz)."
                )
            else:
                logging.info(f"{sensor_id}: No leaks detected. Readings are normal.")

    def simulate_data_update(self):
        """
        Simulate real-time data updates from sensors.

        :return: None
        """
        for sensor_id in self.sensors:
            self.sensors[sensor_id]["pressure"] = random.uniform(0.8, 1.7)  # Update pressure
            self.sensors[sensor_id]["sound_frequency"] = random.uniform(15, 35)  # Update sound frequency

    def print_sensor_status(self):
        """
        Print the current status of all sensors.
        
        :return: None
        """
        logging.info("Current sensor statuses:")
        for sensor_id, sensor_data in self.sensors.items():
            print(f"{sensor_id}: {sensor_data}")


def main():
    """
    Main function to run the water leak detection simulation.
    """
    try:
        logging.info("Starting water leak detection system simulation...")
        system = WaterLeakDetectionSystem(sensor_count=5)

        # Initial sensor status
        system.print_sensor_status()

        # Simulate periodic checks
        for _ in range(3):  # Simulate 3 cycles
            logging.info("Updating sensor data...")
            system.simulate_data_update()

            logging.info("Detecting leaks...")
            system.detect_leaks()

            logging.info("Updated sensor statuses:")
            system.print_sensor_status()

        logging.info("Simulation completed.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
