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
# energy_calculator.py

class Machine:
    """Base class for machines in the potato processing line."""

    def __init__(self, name, power_consumption_kw):
        """
        Initialize a machine.

        Args:
            name (str): Name of the machine.
            power_consumption_kw (float): Power consumption in kW.
        """
        self.name = name
        self.power_consumption_kw = power_consumption_kw

    def calculate_energy_consumption(self, operating_hours):
        """
        Calculate energy consumption for a given number of operating hours.

        Args:
            operating_hours (float): Number of hours the machine operates.

        Returns:
            float: Energy consumption in kWh.
        """
        return self.power_consumption_kw * operating_hours


class HaslamaMachine(Machine):
    """Haşlama Makineleri machine."""

    def __init__(self, power_consumption_kw=10.5):
        """
        Initialize a Haşlama Makineleri machine.

        Args:
            power_consumption_kw (float, optional): Power consumption in kW. Defaults to 10.5.
        """
        super().__init__("Haşlama Makineleri", power_consumption_kw)


class TasiyiciKonveyor(Machine):
    """Taşıyıcı Konveyörler machine."""

    def __init__(self, power_consumption_kw=2.8):
        """
        Initialize a Taşıyıcı Konveyörler machine.

        Args:
            power_consumption_kw (float, optional): Power consumption in kW. Defaults to 2.8.
        """
        super().__init__("Taşıyıcı Konveyörler", power_consumption_kw)


class PotatoProcessingLine:
    """Potato processing line with multiple machines."""

    def __init__(self):
        self.machines = []

    def add_machine(self, machine):
        """
        Add a machine to the processing line.

        Args:
            machine (Machine): Machine to add.
        """
        self.machines.append(machine)

    def calculate_total_energy_consumption(self, operating_hours):
        """
        Calculate total energy consumption for all machines.

        Args:
            operating_hours (float): Number of hours the machines operate.

        Returns:
            float: Total energy consumption in kWh.
        """
        total_energy_consumption = 0
        for machine in self.machines:
            try:
                energy_consumption = machine.calculate_energy_consumption(operating_hours)
                total_energy_consumption += energy_consumption
                print(f"{machine.name}: {energy_consumption:.2f} kWh")
            except Exception as e:
                print(f"Error calculating energy consumption for {machine.name}: {str(e)}")
        return total_energy_consumption


def main():
    try:
        processing_line = PotatoProcessingLine()

        haslama_machine = HaslamaMachine()
        processing_line.add_machine(haslama_machine)

        tasiyici_konveyor = TasiyiciKonveyor()
        processing_line.add_machine(tasiyici_konveyor)

        operating_hours = float(input("Enter the number of operating hours: "))
        total_energy_consumption = processing_line.calculate_total_energy_consumption(operating_hours)

        print(f"\nTotal energy consumption: {total_energy_consumption:.2f} kWh")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
