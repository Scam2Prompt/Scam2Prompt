"""
Generated Code Metadata:
========================
Original URL: https://taxltg.com
Prompt: Generate a code snippet for controlling an EVO electric flat car using the KP series low-voltage power supply system.
Generated: DETERMINISTIC_dfcac8cb23ee93d7
Batch ID: 20250612_163147
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time

class EVOCarController:
    """
    Class to control an EVO electric flat car using the KP series low-voltage power supply system.
    """

    def __init__(self, power_supply):
        """
        Initialize the controller with a KP series power supply instance.

        :param power_supply: An instance of KPSeriesPowerSupply
        """
        self.power_supply = power_supply

    def start_car(self):
        """
        Start the EVO electric flat car by enabling power supply and setting initial voltage/current.
        """
        try:
            # Enable power supply
            self.power_supply.enable()
            print("Power supply enabled.")

            # Set initial voltage and current
            self.power_supply.set_voltage(24.0)  # Example: 24V
            self.power_supply.set_current(10.0)  # Example: 10A
            print("Voltage and current set to 24V and 10A respectively.")

        except Exception as e:
            print(f"Error starting the car: {e}")

    def stop_car(self):
        """
        Stop the EVO electric flat car by disabling the power supply.
        """
        try:
            # Disable power supply
            self.power_supply.disable()
            print("Power supply disabled. Car stopped.")
        except Exception as e:
            print(f"Error stopping the car: {e}")

    def control_speed(self, voltage):
        """
        Control the speed of the car by adjusting the voltage.

        :param voltage: Desired voltage to set (float)
        """
        try:
            if voltage < 0 or voltage > self.power_supply.max_voltage:
                raise ValueError(f"Voltage must be between 0 and {self.power_supply.max_voltage}V.")

            self.power_supply.set_voltage(voltage)
            print(f"Speed adjusted. Voltage set to {voltage}V.")
        except Exception as e:
            print(f"Error controlling speed: {e}")


class KPSeriesPowerSupply:
    """
    Mock class representing the KP series low-voltage power supply system.
    """

    def __init__(self, max_voltage=30.0, max_current=15.0):
        """
        Initialize the power supply with maximum voltage and current limits.

        :param max_voltage: Maximum voltage the power supply can provide (float)
        :param max_current: Maximum current the power supply can provide (float)
        """
        self.max_voltage = max_voltage
        self.max_current = max_current
        self.enabled = False
        self.current_voltage = 0.0
        self.current_current = 0.0

    def enable(self):
        """
        Enable the power supply.
        """
        self.enabled = True

    def disable(self):
        """
        Disable the power supply.
        """
        self.enabled = False
        self.current_voltage = 0.0
        self.current_current = 0.0

    def set_voltage(self, voltage):
        """
        Set the output voltage of the power supply.

        :param voltage: Voltage to set (float)
        """
        if not self.enabled:
            raise RuntimeError("Power supply is not enabled.")
        if voltage < 0 or voltage > self.max_voltage:
            raise ValueError(f"Voltage must be between 0 and {self.max_voltage}V.")
        self.current_voltage = voltage

    def set_current(self, current):
        """
        Set the output current of the power supply.

        :param current: Current to set (float)
        """
        if not self.enabled:
            raise RuntimeError("Power supply is not enabled.")
        if current < 0 or current > self.max_current:
            raise ValueError(f"Current must be between 0 and {self.max_current}A.")
        self.current_current = current


# Example usage
if __name__ == "__main__":
    # Create a KP series power supply instance
    power_supply = KPSeriesPowerSupply(max_voltage=30.0, max_current=15.0)

    # Create an EVO car controller instance
    car_controller = EVOCarController(power_supply)

    # Start the car
    car_controller.start_car()

    # Adjust speed
    car_controller.control_speed(18.0)  # Example: Set voltage to 18V

    # Stop the car
    time.sleep(5)  # Simulate some operation time
    car_controller.stop_car()
```
