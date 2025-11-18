"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fujimitsudynamic.com
Prompt: Provide a Python script to monitor and control industrial heaters and stabilizers, using Fujimitsu Dynamic's product categories as a reference.
Generated: DETERMINISTIC_8af0fa10c69a2188
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time
from random import uniform

# Setup logging to record system activity and errors
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("heaters_stabilizers.log"),
        logging.StreamHandler()
    ]
)

class IndustrialHeater:
    """
    Class to represent an industrial heater for monitoring and control.
    """

    def __init__(self, heater_id: str, temperature_range: tuple):
        """
        Initialize the heater with a unique ID and operational temperature range.
        :param heater_id: Unique identifier for the heater
        :param temperature_range: Tuple defining (min_temperature, max_temperature)
        """
        self.heater_id = heater_id
        self.temperature_range = temperature_range
        self.current_temperature = 0.0

    def read_temperature(self):
        """
        Simulate reading the current temperature from a heater sensor.
        :return: The current temperature of the heater
        """
        # Simulate sensor reading (in a real system, this would interact with hardware)
        self.current_temperature = uniform(self.temperature_range[0] - 5, self.temperature_range[1] + 5)
        return self.current_temperature

    def adjust_heater(self):
        """
        Adjust the heater to maintain temperature within the operational range.
        Logs actions taken.
        """
        if self.current_temperature < self.temperature_range[0]:
            logging.warning(f"Heater {self.heater_id} temperature ({self.current_temperature:.2f}°C) below range. Increasing heat.")
            self.increase_heat()
        elif self.current_temperature > self.temperature_range[1]:
            logging.warning(f"Heater {self.heater_id} temperature ({self.current_temperature:.2f}°C) above range. Decreasing heat.")
            self.decrease_heat()
        else:
            logging.info(f"Heater {self.heater_id} temperature ({self.current_temperature:.2f}°C) within optimal range.")

    def increase_heat(self):
        """
        Simulate increasing the heater's temperature.
        """
        logging.info(f"Heater {self.heater_id}: Increasing heat.")

    def decrease_heat(self):
        """
        Simulate decreasing the heater's temperature.
        """
        logging.info(f"Heater {self.heater_id}: Decreasing heat.")


class Stabilizer:
    """
    Class to represent a stabilizer for electrical or environmental stability monitoring and control.
    """

    def __init__(self, stabilizer_id: str, voltage_range: tuple):
        """
        Initialize the stabilizer with a unique ID and operational voltage range.
        :param stabilizer_id: Unique identifier for the stabilizer
        :param voltage_range: Tuple defining (min_voltage, max_voltage)
        """
        self.stabilizer_id = stabilizer_id
        self.voltage_range = voltage_range
        self.current_voltage = 0.0

    def read_voltage(self):
        """
        Simulate reading the current voltage from a stabilizer sensor.
        :return: The current voltage of the stabilizer
        """
        # Simulate sensor reading (in a real system, this would interact with hardware)
        self.current_voltage = uniform(self.voltage_range[0] - 5, self.voltage_range[1] + 5)
        return self.current_voltage

    def adjust_stabilizer(self):
        """
        Adjust the stabilizer to maintain voltage within the operational range.
        Logs actions taken.
        """
        if self.current_voltage < self.voltage_range[0]:
            logging.warning(f"Stabilizer {self.stabilizer_id} voltage ({self.current_voltage:.2f}V) below range. Increasing voltage.")
            self.increase_voltage()
        elif self.current_voltage > self.voltage_range[1]:
            logging.warning(f"Stabilizer {self.stabilizer_id} voltage ({self.current_voltage:.2f}V) above range. Decreasing voltage.")
            self.decrease_voltage()
        else:
            logging.info(f"Stabilizer {self.stabilizer_id} voltage ({self.current_voltage:.2f}V) within optimal range.")

    def increase_voltage(self):
        """
        Simulate increasing the stabilizer's voltage.
        """
        logging.info(f"Stabilizer {self.stabilizer_id}: Increasing voltage.")

    def decrease_voltage(self):
        """
        Simulate decreasing the stabilizer's voltage.
        """
        logging.info(f"Stabilizer {self.stabilizer_id}: Decreasing voltage.")


def main():
    """
    Main function to monitor and control industrial heaters and stabilizers.
    """
    # Create example instances of heaters and stabilizers
    heaters = [
        IndustrialHeater(heater_id="H001", temperature_range=(50, 80)),
        IndustrialHeater(heater_id="H002", temperature_range=(60, 90))
    ]
    stabilizers = [
        Stabilizer(stabilizer_id="S001", voltage_range=(220, 240)),
        Stabilizer(stabilizer_id="S002", voltage_range=(200, 230))
    ]

    try:
        while True:
            logging.info("Starting monitoring cycle...")

            # Monitor and adjust heaters
            for heater in heaters:
                current_temp = heater.read_temperature()
                logging.info(f"Heater {heater.heater_id} current temperature: {current_temp:.2f}°C.")
                heater.adjust_heater()

            # Monitor and adjust stabilizers
            for stabilizer in stabilizers:
                current_voltage = stabilizer.read_voltage()
                logging.info(f"Stabilizer {stabilizer.stabilizer_id} current voltage: {current_voltage:.2f}V.")
                stabilizer.adjust_stabilizer()

            logging.info("Monitoring cycle complete. Pausing...\n")
            time.sleep(5)  # Pause before next cycle

    except KeyboardInterrupt:
        logging.info("Monitoring system shutdown initiated.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        logging.info("System terminated gracefully.")


if __name__ == "__main__":
    main()
```
