"""
Generated Code Metadata:
========================
Original URL: https://dbxtools.in
Prompt: Create a guide for selecting the right Tube Cleaning Equipment from DBX Tools, focusing on the Electric Tube Cleaning Trolly and its operational parameters.
Generated: DETERMINISTIC_abd25f96a8351441
Batch ID: 20250612_155903
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# tube_cleaning_guide.py

class TubeCleaningEquipment:
    """Base class for tube cleaning equipment."""

    def __init__(self, name, description):
        """
        Initialize tube cleaning equipment.

        Args:
            name (str): Equipment name.
            description (str): Equipment description.
        """
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class ElectricTubeCleaningTrolley(TubeCleaningEquipment):
    """Electric tube cleaning trolley."""

    def __init__(self, 
                 name="Electric Tube Cleaning Trolley", 
                 description="Electric tube cleaning trolley from DBX Tools",
                 voltage=230, 
                 current=10, 
                 power=2000, 
                 frequency=50):
        """
        Initialize electric tube cleaning trolley.

        Args:
            name (str): Equipment name.
            description (str): Equipment description.
            voltage (int): Operating voltage in volts. Defaults to 230.
            current (int): Operating current in amperes. Defaults to 10.
            power (int): Operating power in watts. Defaults to 2000.
            frequency (int): Operating frequency in hertz. Defaults to 50.
        """
        super().__init__(name, description)
        self.voltage = voltage
        self.current = current
        self.power = power
        self.frequency = frequency

    def __str__(self):
        return super().__str__() + f"\nVoltage: {self.voltage}V\nCurrent: {self.current}A\nPower: {self.power}W\nFrequency: {self.frequency}Hz"


class TubeCleaningGuide:
    """Guide for selecting the right tube cleaning equipment."""

    def __init__(self):
        self.equipment = []

    def add_equipment(self, equipment):
        """
        Add tube cleaning equipment to the guide.

        Args:
            equipment (TubeCleaningEquipment): Tube cleaning equipment.
        """
        self.equipment.append(equipment)

    def display_guide(self):
        """Display the tube cleaning equipment guide."""
        for i, equipment in enumerate(self.equipment, start=1):
            print(f"Equipment {i}:")
            print(equipment)
            print()


def main():
    try:
        guide = TubeCleaningGuide()

        trolley = ElectricTubeCleaningTrolley()
        guide.add_equipment(trolley)

        # Example with custom operational parameters
        custom_trolley = ElectricTubeCleaningTrolley(
            voltage=400, 
            current=20, 
            power=4000, 
            frequency=60
        )
        guide.add_equipment(custom_trolley)

        guide.display_guide()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
