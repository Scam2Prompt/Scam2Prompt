"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://loghouses-woodcraft.com
Prompt: Generate code to calculate the total energy consumption of QS series pumps over a 24-hour operational cycle.
Generated: DETERMINISTIC_0b2f6df05016de55
Batch ID: 20250612_154502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class QSPump:
    """
    A class to represent a QS series pump and calculate its energy consumption.

    Attributes
    ----------
    power_rating : float
        The power rating of the pump in kilowatts (kW).
    operational_hours : float
        The number of operational hours (should not exceed 24).
    efficiency : float
        The efficiency of the pump in percentage (0-100).

    Methods
    -------
    calculate_energy_consumption():
        Calculates the total energy consumption of the pump over the operational hours.
    """

    def __init__(self, power_rating: float, operational_hours: float, efficiency: float):
        """
        Constructs all the necessary attributes for the QSPump object.

        Parameters
        ----------
        power_rating : float
            The power rating of the pump in kilowatts.
        operational_hours : float
            The number of operational hours for the pump.
        efficiency : float
            The efficiency of the pump in percentage.
        """
        if operational_hours < 0 or operational_hours > 24:
            raise ValueError("Operational hours must be between 0 and 24.")
        if efficiency < 0 or efficiency > 100:
            raise ValueError("Efficiency must be between 0 and 100.")

        self.power_rating = power_rating  # in kW
        self.operational_hours = operational_hours  # in hours
        self.efficiency = efficiency / 100  # converting percentage to decimal

    def calculate_energy_consumption(self) -> float:
        """
        Calculates the total energy consumption of the pump over the operational hours.

        Returns
        -------
        float
            The total energy consumption in kilowatt-hours (kWh).
        """
        # Calculate the effective power consumption based on efficiency
        effective_power = self.power_rating * self.efficiency
        # Calculate energy consumption over the operational period
        energy_consumption = effective_power * self.operational_hours
        return energy_consumption


def main():
    """
    Main function to demonstrate the energy consumption calculation for QS series pumps.
    """
    try:
        # Example pump specifications
        pump_power_rating = 10.0  # kW
        pump_operational_hours = 24.0  # hours
        pump_efficiency = 85.0  # percentage

        # Creating an instance of QSPump
        pump = QSPump(pump_power_rating, pump_operational_hours, pump_efficiency)

        # Calculate energy consumption
        total_energy = pump.calculate_energy_consumption()
        print(f"Total energy consumption over {pump.operational_hours} hours: {total_energy:.2f} kWh")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    main()
```
