"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tibvanboxtel.nl
Prompt: Provide an example of how to integrate a micro-inverter system for solar panels as recommended by Technisch Installatiebedrijf van Boxtel.
Generated: DETERMINISTIC_e90b49fd533bcd21
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class MicroInverter:
    """
    Class representing a micro-inverter for a solar panel system.
    """

    def __init__(self, inverter_id: str, max_power_output: float):
        """
        Initializes the micro-inverter with an ID and maximum power output.

        :param inverter_id: Unique identifier for the micro-inverter.
        :param max_power_output: Maximum power output in watts.
        """
        self.inverter_id = inverter_id
        self.max_power_output = max_power_output
        self.current_output = 0.0  # Current power output in watts

    def update_power_output(self, power: float):
        """
        Updates the inverter's current power output, ensuring it does not exceed max power.

        :param power: The new power output to set.
        :raises ValueError: If the power exceeds the maximum allowed output.
        """
        if power < 0:
            raise ValueError("Power output cannot be negative.")
        if power > self.max_power_output:
            raise ValueError("Power output exceeds maximum capability.")

        self.current_output = power
        print(f"Inverter {self.inverter_id}: Power output updated to {self.current_output}W.")

    def get_power_output(self) -> float:
        """
        Returns the current power output of the inverter.

        :return: Current power output in watts.
        """
        return self.current_output


class SolarPanelSystem:
    """
    Class representing a solar panel system integrating multiple micro-inverters.
    """

    def __init__(self):
        """
        Initializes the solar panel system with an empty list of micro-inverters.
        """
        self.inverters = []

    def add_inverter(self, inverter: MicroInverter):
        """
        Adds a micro-inverter to the solar panel system.

        :param inverter: An instance of MicroInverter to be added.
        """
        self.inverters.append(inverter)
        print(f"Inverter {inverter.inverter_id} added to the system.")

    def update_inverter_output(self, inverter_id: str, power: float):
        """
        Updates the power output of a specified micro-inverter.

        :param inverter_id: The ID of the inverter to update.
        :param power: The new power output to set.
        :raises LookupError: If the inverter with given ID is not found.
        """
        inverter = self.find_inverter(inverter_id)
        inverter.update_power_output(power)

    def find_inverter(self, inverter_id: str) -> MicroInverter:
        """
        Finds a micro-inverter in the system by its ID.

        :param inverter_id: The ID of the inverter to find.
        :return: An instance of MicroInverter if found.
        :raises LookupError: If no inverter with that ID exists.
        """
        for inverter in self.inverters:
            if inverter.inverter_id == inverter_id:
                return inverter
        raise LookupError(f"Inverter with ID {inverter_id} not found.")

    def get_total_output(self) -> float:
        """
        Calculates the total power output of all micro-inverters in the system.

        :return: Total power output in watts.
        """
        total_output = sum(inverter.get_power_output() for inverter in self.inverters)
        print(f"Total power output of the system: {total_output}W.")
        return total_output


# Example Usage
if __name__ == "__main__":
    # Create a solar panel system
    solar_system = SolarPanelSystem()

    # Add micro-inverters to the system
    inverter1 = MicroInverter("INV001", 3000)
    inverter2 = MicroInverter("INV002", 3000)
    
    solar_system.add_inverter(inverter1)
    solar_system.add_inverter(inverter2)

    # Update power output for each inverter
    try:
        solar_system.update_inverter_output("INV001", 2500)
        solar_system.update_inverter_output("INV002", 2800)
    except (ValueError, LookupError) as e:
        print(f"Error: {e}")

    # Get total output of the system
    solar_system.get_total_output()
```
