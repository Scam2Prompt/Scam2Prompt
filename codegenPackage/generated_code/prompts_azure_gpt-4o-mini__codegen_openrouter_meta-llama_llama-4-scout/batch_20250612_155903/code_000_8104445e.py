"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Generate code to implement a hydraulic tube expansion system using the specifications provided for the Hydraulic Expansion Powerpack from DBX Tools.
Generated: DETERMINISTIC_8104445e25213f1e
Batch ID: 20250612_155903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Hydraulic Tube Expansion System

class HydraulicExpansionPowerpack:
    """
    Represents a hydraulic expansion powerpack.

    Attributes:
        pressure (float): The current pressure in bar.
        temperature (float): The current temperature in Celsius.
        max_pressure (float): The maximum allowed pressure in bar.
        max_temperature (float): The maximum allowed temperature in Celsius.
    """

    def __init__(self, max_pressure=700, max_temperature=80):
        """
        Initializes a new hydraulic expansion powerpack.

        Args:
            max_pressure (float, optional): The maximum allowed pressure in bar. Defaults to 700.
            max_temperature (float, optional): The maximum allowed temperature in Celsius. Defaults to 80.
        """
        self.pressure = 0.0
        self.temperature = 0.0
        self.max_pressure = max_pressure
        self.max_temperature = max_temperature

    def set_pressure(self, pressure):
        """
        Sets the current pressure.

        Args:
            pressure (float): The new pressure in bar.

        Raises:
            ValueError: If the pressure exceeds the maximum allowed pressure.
        """
        if pressure > self.max_pressure:
            raise ValueError(f"Pressure cannot exceed {self.max_pressure} bar")
        self.pressure = pressure

    def set_temperature(self, temperature):
        """
        Sets the current temperature.

        Args:
            temperature (float): The new temperature in Celsius.

        Raises:
            ValueError: If the temperature exceeds the maximum allowed temperature.
        """
        if temperature > self.max_temperature:
            raise ValueError(f"Temperature cannot exceed {self.max_temperature} Celsius")
        self.temperature = temperature

    def expand_tube(self, tube_diameter, tube_length):
        """
        Expands a tube using the hydraulic expansion powerpack.

        Args:
            tube_diameter (float): The diameter of the tube in mm.
            tube_length (float): The length of the tube in mm.

        Returns:
            float: The expanded diameter of the tube in mm.

        Raises:
            Exception: If the expansion process fails.
        """
        try:
            # Simulate the expansion process
            expanded_diameter = tube_diameter * (1 + (self.pressure / 1000))
            return expanded_diameter
        except Exception as e:
            raise Exception(f"Expansion process failed: {str(e)}")

    def get_status(self):
        """
        Gets the current status of the hydraulic expansion powerpack.

        Returns:
            dict: A dictionary containing the current pressure, temperature, and status.
        """
        status = {
            "pressure": self.pressure,
            "temperature": self.temperature,
            "status": "OK" if self.pressure <= self.max_pressure and self.temperature <= self.max_temperature else "FAULT"
        }
        return status


class HydraulicTubeExpansionSystem:
    """
    Represents a hydraulic tube expansion system.

    Attributes:
        powerpack (HydraulicExpansionPowerpack): The hydraulic expansion powerpack.
    """

    def __init__(self, powerpack):
        """
        Initializes a new hydraulic tube expansion system.

        Args:
            powerpack (HydraulicExpansionPowerpack): The hydraulic expansion powerpack.
        """
        self.powerpack = powerpack

    def expand_tubes(self, tubes):
        """
        Expands multiple tubes using the hydraulic tube expansion system.

        Args:
            tubes (list): A list of tuples containing the diameter and length of each tube.

        Returns:
            list: A list of expanded diameters for each tube.

        Raises:
            Exception: If any tube expansion process fails.
        """
        expanded_diameters = []
        for tube in tubes:
            try:
                expanded_diameter = self.powerpack.expand_tube(tube[0], tube[1])
                expanded_diameters.append(expanded_diameter)
            except Exception as e:
                raise Exception(f"Tube expansion process failed: {str(e)}")
        return expanded_diameters


def main():
    # Create a new hydraulic expansion powerpack
    powerpack = HydraulicExpansionPowerpack()

    # Set the pressure and temperature
    powerpack.set_pressure(500)
    powerpack.set_temperature(50)

    # Create a new hydraulic tube expansion system
    system = HydraulicTubeExpansionSystem(powerpack)

    # Define the tubes to expand
    tubes = [(10, 100), (20, 200), (30, 300)]

    try:
        # Expand the tubes
        expanded_diameters = system.expand_tubes(tubes)
        print("Expanded Diameters:")
        for i, diameter in enumerate(expanded_diameters):
            print(f"Tube {i+1}: {diameter} mm")

        # Get the powerpack status
        status = powerpack.get_status()
        print("\nPowerpack Status:")
        print(f"Pressure: {status['pressure']} bar")
        print(f"Temperature: {status['temperature']} Celsius")
        print(f"Status: {status['status']}")

    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()
```
