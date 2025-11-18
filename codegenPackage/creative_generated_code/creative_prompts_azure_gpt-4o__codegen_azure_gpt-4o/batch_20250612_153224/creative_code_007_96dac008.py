"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cemnazmakine.com
Prompt: Create a program to calculate the energy consumption of a potato processing line, incorporating machines like "Haşlama Makineleri" and "Taşıyıcı Konveyörler," as detailed by CEMNAZ Makine.
Generated: DETERMINISTIC_96dac008eb5403be
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class Machine:
    """
    Represents a machine in the potato processing line.
    """
    def __init__(self, name, power_rating_kw, operating_hours):
        """
        Initialize a machine with its name, power rating, and operating hours.

        :param name: Name of the machine.
        :param power_rating_kw: Power consumption in kilowatts (kW).
        :param operating_hours: Operating hours per day.
        """
        self.name = name
        self.power_rating_kw = power_rating_kw
        self.operating_hours = operating_hours

    def calculate_energy_consumption(self):
        """
        Calculate daily energy consumption of the machine in kilowatt-hours (kWh).

        :return: Energy consumption in kWh.
        """
        return self.power_rating_kw * self.operating_hours


class PotatoProcessingLine:
    """
    Represents the entire potato processing line.
    """
    def __init__(self):
        """
        Initialize the processing line with an empty list of machines.
        """
        self.machines = []

    def add_machine(self, machine):
        """
        Add a machine to the processing line.

        :param machine: Instance of Machine.
        """
        if not isinstance(machine, Machine):
            raise ValueError("Invalid machine object.")
        self.machines.append(machine)

    def calculate_total_energy_consumption(self):
        """
        Calculate total daily energy consumption for all machines in the processing line.

        :return: Total energy consumption in kWh.
        """
        total_energy = 0
        for machine in self.machines:
            try:
                total_energy += machine.calculate_energy_consumption()
            except Exception as e:
                print(f"Error calculating energy consumption for {machine.name}: {e}", file=sys.stderr)
        return total_energy


def main():
    """
    Main function to calculate energy consumption of a potato processing line.
    """
    try:
        # Initialize the potato processing line
        processing_line = PotatoProcessingLine()

        # Add machines to the line
        processing_line.add_machine(Machine("Haşlama Makineleri", power_rating_kw=15, operating_hours=8))
        processing_line.add_machine(Machine("Taşıyıcı Konveyörler", power_rating_kw=10, operating_hours=12))

        # Calculate total energy consumption
        total_energy = processing_line.calculate_total_energy_consumption()

        # Print the result
        print(f"Total daily energy consumption of the potato processing line: {total_energy:.2f} kWh")

    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Entry point of the program
    main()
```
