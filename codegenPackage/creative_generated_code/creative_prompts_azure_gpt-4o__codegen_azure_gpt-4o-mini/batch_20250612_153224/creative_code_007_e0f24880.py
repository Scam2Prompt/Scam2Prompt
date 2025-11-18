"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://instrumentacionum.com
Prompt: Provide a step-by-step guide to configure and program industrial control panels for managing multiple sensors, based on Instrumentación UM's offerings.
Generated: DETERMINISTIC_e0f2488072b6ba5d
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random

class Sensor:
    """
    A class to represent a sensor with the ability to read its value.
    """

    def __init__(self, name: str):
        """
        Initialize a new Sensor with a given name.
        
        :param name: The name of the sensor
        """
        self.name = name
        self.value = 0

    def read_value(self) -> float:
        """
        Simulate reading a sensor value.
        
        :return: A simulated sensor value
        """
        self.value = random.uniform(0, 100)  # Simulate a sensor reading
        return self.value


class ControlPanel:
    """
    A class to control multiple sensors.
    """

    def __init__(self):
        """
        Initialize the ControlPanel with an empty list of sensors.
        """
        self.sensors = []

    def add_sensor(self, sensor: Sensor):
        """
        Add a sensor to the control panel.
        
        :param sensor: An instance of Sensor to be added
        """
        if not isinstance(sensor, Sensor):
            raise ValueError("Only instances of Sensor can be added.")
        self.sensors.append(sensor)

    def read_sensors(self):
        """
        Read values from all sensors and return a dictionary of their values.
        
        :return: A dictionary mapping sensor names to their current values
        """
        sensor_values = {}
        for sensor in self.sensors:
            sensor_values[sensor.name] = sensor.read_value()
        return sensor_values

    def display_sensor_values(self):
        """
        Display the current values of all sensors in a readable format.
        """
        sensor_values = self.read_sensors()
        for name, value in sensor_values.items():
            print(f"Sensor '{name}': {value:.2f}")


def main():
    """
    Main function to configure and manage the industrial control panel.
    """
    try:
        # Create a control panel instance
        control_panel = ControlPanel()

        # Add sensors to the control panel
        control_panel.add_sensor(Sensor("Temperature Sensor"))
        control_panel.add_sensor(Sensor("Pressure Sensor"))
        control_panel.add_sensor(Sensor("Humidity Sensor"))

        # Main loop to continuously read and display sensor values
        while True:
            control_panel.display_sensor_values()
            time.sleep(5)  # Pause for 5 seconds before the next reading

    except KeyboardInterrupt:
        print("Control panel terminated by user.")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
