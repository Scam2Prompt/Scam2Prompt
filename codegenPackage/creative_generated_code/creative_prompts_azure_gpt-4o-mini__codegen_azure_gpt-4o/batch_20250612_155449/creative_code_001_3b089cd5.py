"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftsonopensea.com
Prompt: Generate a code snippet for a temperature control system that can be integrated with a ceramic fiber muffle furnace, incorporating features mentioned in the product specifications.
Generated: DETERMINISTIC_3b089cd5e88dc741
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class TemperatureControlSystem:
    """
    A temperature control system for a ceramic fiber muffle furnace.
    This system monitors and adjusts the temperature based on user-defined setpoints.
    """

    def __init__(self, temperature_sensor, heating_element, cooling_system, desired_temperature, tolerance=1.0):
        """
        Initialize the temperature control system.

        :param temperature_sensor: Function or class to read the current temperature.
        :param heating_element: Function or class to activate the heating element.
        :param cooling_system: Function or class to activate the cooling system.
        :param desired_temperature: The target temperature to maintain.
        :param tolerance: Allowable temperature deviation in degrees (default: 1.0°C).
        """
        self.temperature_sensor = temperature_sensor
        self.heating_element = heating_element
        self.cooling_system = cooling_system
        self.desired_temperature = desired_temperature
        self.tolerance = tolerance
        self.running = False

    def start(self):
        """
        Start the temperature control system.
        Monitors and adjusts the furnace temperature in real-time to maintain the specified setpoint.
        """
        self.running = True
        print("Starting the temperature control system...")
        try:
            while self.running:
                current_temperature = self.temperature_sensor.read_temperature()

                # Log current temperature
                print(f"Current Temperature: {current_temperature:.2f}°C")

                # Check if the temperature is within the acceptable range
                if current_temperature < self.desired_temperature - self.tolerance:
                    print("Temperature is too low. Activating heating element.")
                    self.heating_element.activate()
                    self.cooling_system.deactivate()  # Ensure cooling is off
                elif current_temperature > self.desired_temperature + self.tolerance:
                    print("Temperature is too high. Activating cooling system.")
                    self.cooling_system.activate()
                    self.heating_element.deactivate()  # Ensure heating is off
                else:
                    print("Temperature is within acceptable range. Maintaining current state.")
                    self.heating_element.deactivate()
                    self.cooling_system.deactivate()

                time.sleep(1)  # Polling interval (1 second)
        except KeyboardInterrupt:
            print("\nTemperature control system interrupted. Stopping...")
            self.stop()
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            self.stop()

    def stop(self):
        """
        Stop the temperature control system.
        Safely deactivate all components.
        """
        self.running = False
        self.heating_element.deactivate()
        self.cooling_system.deactivate()
        print("Temperature control system stopped.")

# Example Implementations for Sensor and Actuators

class TemperatureSensor:
    """
    Mock implementation of a temperature sensor for demonstration purposes.
    Replace with actual sensor implementation when integrating with hardware.
    """
    def read_temperature(self):
        # Simulate a temperature reading
        import random
        return random.uniform(20.0, 100.0)  # Random temperature between 20°C and 100°C

class HeatingElement:
    """
    Mock implementation of a heating element for demonstration purposes.
    Replace with actual hardware control implementation.
    """
    def activate(self):
        print("Heating element activated.")

    def deactivate(self):
        print("Heating element deactivated.")

class CoolingSystem:
    """
    Mock implementation of a cooling system for demonstration purposes.
    Replace with actual hardware control implementation.
    """
    def activate(self):
        print("Cooling system activated.")

    def deactivate(self):
        print("Cooling system deactivated.")

# Main Application

if __name__ == "__main__":
    # Initialize components
    sensor = TemperatureSensor()
    heating_element = HeatingElement()
    cooling_system = CoolingSystem()

    # Set desired temperature and tolerance
    desired_temperature = 75.0  # Target temperature in Celsius
    tolerance = 2.0  # Allowable deviation in Celsius

    # Create an instance of the Temperature Control System
    temperature_control = TemperatureControlSystem(
        temperature_sensor=sensor,
        heating_element=heating_element,
        cooling_system=cooling_system,
        desired_temperature=desired_temperature,
        tolerance=tolerance
    )

    # Start the control system
    temperature_control.start()
```
