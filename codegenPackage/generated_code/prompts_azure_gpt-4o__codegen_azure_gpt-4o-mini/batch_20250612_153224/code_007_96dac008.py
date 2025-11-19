"""
Generated Code Metadata:
========================
Original URL: https://cemnazmakine.com
Prompt: Create a program to calculate the energy consumption of a potato processing line, incorporating machines like "Haşlama Makineleri" and "Taşıyıcı Konveyörler," as detailed by CEMNAZ Makine.
Generated: DETERMINISTIC_96dac008eb5403be
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Machine:
    """
    A class to represent a machine in the potato processing line.
    """

    def __init__(self, name, power_rating, operating_hours):
        """
        Initializes a new machine instance.

        :param name: str - The name of the machine.
        :param power_rating: float - The power rating of the machine in kilowatts (kW).
        :param operating_hours: float - The number of hours the machine operates per day.
        """
        self.name = name
        self.power_rating = power_rating  # in kW
        self.operating_hours = operating_hours  # in hours

    def calculate_energy_consumption(self):
        """
        Calculates the energy consumption of the machine.

        :return: float - The energy consumption in kilowatt-hours (kWh).
        """
        return self.power_rating * self.operating_hours


class PotatoProcessingLine:
    """
    A class to represent a potato processing line consisting of multiple machines.
    """

    def __init__(self):
        """
        Initializes a new potato processing line instance with an empty list of machines.
        """
        self.machines = []

    def add_machine(self, machine):
        """
        Adds a machine to the processing line.

        :param machine: Machine - An instance of the Machine class.
        """
        if not isinstance(machine, Machine):
            raise ValueError("The provided object is not a Machine instance.")
        self.machines.append(machine)

    def calculate_total_energy_consumption(self):
        """
        Calculates the total energy consumption of all machines in the processing line.

        :return: float - The total energy consumption in kilowatt-hours (kWh).
        """
        total_energy = 0.0
        for machine in self.machines:
            total_energy += machine.calculate_energy_consumption()
        return total_energy


def main():
    """
    Main function to execute the energy consumption calculation for the potato processing line.
    """
    try:
        # Create instances of machines
        boiling_machine = Machine("Haşlama Makineleri", power_rating=10.0, operating_hours=8.0)
        conveyor_belt = Machine("Taşıyıcı Konveyörler", power_rating=5.0, operating_hours=10.0)

        # Create a potato processing line and add machines
        processing_line = PotatoProcessingLine()
        processing_line.add_machine(boiling_machine)
        processing_line.add_machine(conveyor_belt)

        # Calculate total energy consumption
        total_energy = processing_line.calculate_total_energy_consumption()
        print(f"Total energy consumption of the potato processing line: {total_energy:.2f} kWh")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
