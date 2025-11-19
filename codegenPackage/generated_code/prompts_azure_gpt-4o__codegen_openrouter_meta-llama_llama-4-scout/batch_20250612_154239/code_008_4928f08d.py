"""
Generated Code Metadata:
========================
Original URL: https://fujimitsudynamic.com
Prompt: Create a script to simulate the operation of air pollution control systems, inspired by Fujimitsu Dynamic's industrial solutions.
Generated: DETERMINISTIC_4928f08d8b2b1d84
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# air_pollution_control_system.py

class AirPollutant:
    """Represents an air pollutant with a name and concentration."""

    def __init__(self, name, concentration):
        """
        Initializes an AirPollutant instance.

        Args:
            name (str): The name of the pollutant.
            concentration (float): The concentration of the pollutant in μg/m³.
        """
        self.name = name
        self.concentration = concentration


class AirPollutionControlSystem:
    """Simulates the operation of an air pollution control system."""

    def __init__(self, efficiency):
        """
        Initializes an AirPollutionControlSystem instance.

        Args:
            efficiency (float): The efficiency of the control system as a decimal value.
        """
        self.efficiency = efficiency
        self.pollutants = []

    def add_pollutant(self, pollutant):
        """
        Adds an air pollutant to the system.

        Args:
            pollutant (AirPollutant): The pollutant to add.
        """
        self.pollutants.append(pollutant)

    def remove_pollutant(self, pollutant_name):
        """
        Removes an air pollutant from the system.

        Args:
            pollutant_name (str): The name of the pollutant to remove.

        Raises:
            ValueError: If the pollutant is not found in the system.
        """
        for pollutant in self.pollutants:
            if pollutant.name == pollutant_name:
                self.pollutants.remove(pollutant)
                return
        raise ValueError(f"Pollutant '{pollutant_name}' not found in the system.")

    def control_pollution(self):
        """
        Simulates the operation of the air pollution control system.

        Returns:
            list[AirPollutant]: The list of pollutants with reduced concentrations.
        """
        controlled_pollutants = []
        for pollutant in self.pollutants:
            controlled_concentration = pollutant.concentration * (1 - self.efficiency)
            controlled_pollutant = AirPollutant(pollutant.name, controlled_concentration)
            controlled_pollutants.append(controlled_pollutant)
        return controlled_pollutants


def main():
    # Create air pollutants
    co2 = AirPollutant("CO2", 400.0)
    nox = AirPollutant("NOx", 50.0)
    so2 = AirPollutant("SO2", 20.0)

    # Create an air pollution control system with 90% efficiency
    apcs = AirPollutionControlSystem(0.9)

    # Add pollutants to the system
    apcs.add_pollutant(co2)
    apcs.add_pollutant(nox)
    apcs.add_pollutant(so2)

    # Control pollution
    controlled_pollutants = apcs.control_pollution()

    # Print controlled pollutant concentrations
    print("Controlled Pollutant Concentrations:")
    for pollutant in controlled_pollutants:
        print(f"{pollutant.name}: {pollutant.concentration:.2f} μg/m³")

    # Remove a pollutant
    apcs.remove_pollutant("NOx")

    # Attempt to remove a non-existent pollutant
    try:
        apcs.remove_pollutant("PM2.5")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
