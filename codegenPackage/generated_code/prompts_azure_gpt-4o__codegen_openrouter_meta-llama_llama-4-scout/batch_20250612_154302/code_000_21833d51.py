"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Write Python code to simulate the operation of a hydraulic tube expansion system, referencing the features of the Hydraulic Expansion Powerpack (HEP 500) described on the DBX Tools website.
Generated: DETERMINISTIC_21833d51d3583d92
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time

class HydraulicExpansionPowerpack:
    """
    Simulates the operation of a hydraulic tube expansion system.

    References:
    - HEP 500 features from DBX Tools website
    """

    def __init__(self):
        """
        Initializes the HydraulicExpansionPowerpack with default settings.
        """
        self.max_pressure = 500  # Maximum pressure in bar
        self.max_temperature = 200  # Maximum temperature in Celsius
        self.pressure = 0  # Current pressure in bar
        self.temperature = 20  # Current temperature in Celsius
        self.expansion_tool_connected = False

    def connect_expansion_tool(self):
        """
        Simulates connecting an expansion tool to the powerpack.
        """
        self.expansion_tool_connected = True
        print("Expansion tool connected.")

    def disconnect_expansion_tool(self):
        """
        Simulates disconnecting an expansion tool from the powerpack.
        """
        self.expansion_tool_connected = False
        print("Expansion tool disconnected.")

    def set_pressure(self, pressure):
        """
        Sets the pressure of the powerpack.

        Args:
            pressure (int): The desired pressure in bar.

        Raises:
            ValueError: If the pressure exceeds the maximum allowed pressure.
        """
        if pressure > self.max_pressure:
            raise ValueError(f"Pressure cannot exceed {self.max_pressure} bar")
        self.pressure = pressure
        print(f"Pressure set to {pressure} bar.")

    def set_temperature(self, temperature):
        """
        Sets the temperature of the powerpack.

        Args:
            temperature (int): The desired temperature in Celsius.

        Raises:
            ValueError: If the temperature exceeds the maximum allowed temperature.
        """
        if temperature > self.max_temperature:
            raise ValueError(f"Temperature cannot exceed {self.max_temperature} Celsius")
        self.temperature = temperature
        print(f"Temperature set to {temperature} Celsius.")

    def expand_tube(self):
        """
        Simulates expanding a tube using the connected expansion tool.

        Raises:
            RuntimeError: If no expansion tool is connected.
        """
        if not self.expansion_tool_connected:
            raise RuntimeError("Expansion tool is not connected")
        print("Expanding tube...")
        time.sleep(2)  # Simulate expansion time
        print("Tube expanded.")

    def status(self):
        """
        Prints the current status of the powerpack.
        """
        print(f"Pressure: {self.pressure} bar")
        print(f"Temperature: {self.temperature} Celsius")
        print(f"Expansion tool connected: {self.expansion_tool_connected}")


def main():
    powerpack = HydraulicExpansionPowerpack()

    try:
        powerpack.connect_expansion_tool()
        powerpack.set_pressure(400)
        powerpack.set_temperature(50)
        powerpack.expand_tube()
        powerpack.status()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        powerpack.disconnect_expansion_tool()


if __name__ == "__main__":
    main()
```
