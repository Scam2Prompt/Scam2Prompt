"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: What are the best practices for maintaining and repairing construction machinery like Pile Driver and Earth Auger Drill, and provide a sample maintenance schedule in Python.
Generated: DETERMINISTIC_f76fd77c51b1c1c6
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_maintenance.py

class ConstructionMachine:
    """Base class for construction machines."""

    def __init__(self, name, hours_used=0):
        """
        Initialize a construction machine.

        Args:
            name (str): Name of the machine.
            hours_used (int, optional): Hours the machine has been used. Defaults to 0.
        """
        self.name = name
        self.hours_used = hours_used

    def log_hours(self, hours):
        """
        Log hours used for the machine.

        Args:
            hours (int): Hours to log.
        """
        self.hours_used += hours


class PileDriver(ConstructionMachine):
    """Class for Pile Driver."""

    def __init__(self, name, hours_used=0, hammer_condition="good"):
        """
        Initialize a Pile Driver.

        Args:
            name (str): Name of the machine.
            hours_used (int, optional): Hours the machine has been used. Defaults to 0.
            hammer_condition (str, optional): Condition of the hammer. Defaults to "good".
        """
        super().__init__(name, hours_used)
        self.hammer_condition = hammer_condition

    def inspect_hammer(self):
        """Inspect the hammer condition."""
        return self.hammer_condition

    def replace_hammer(self):
        """Replace the hammer."""
        self.hammer_condition = "new"


class EarthAugerDrill(ConstructionMachine):
    """Class for Earth Auger Drill."""

    def __init__(self, name, hours_used=0, drill_bit_condition="good"):
        """
        Initialize an Earth Auger Drill.

        Args:
            name (str): Name of the machine.
            hours_used (int, optional): Hours the machine has been used. Defaults to 0.
            drill_bit_condition (str, optional): Condition of the drill bit. Defaults to "good".
        """
        super().__init__(name, hours_used)
        self.drill_bit_condition = drill_bit_condition

    def inspect_drill_bit(self):
        """Inspect the drill bit condition."""
        return self.drill_bit_condition

    def replace_drill_bit(self):
        """Replace the drill bit."""
        self.drill_bit_condition = "new"


class MaintenanceSchedule:
    """Class for maintenance schedule."""

    def __init__(self):
        """Initialize a maintenance schedule."""
        self.maintenance_schedule = {}

    def add_maintenance(self, machine, hours, action):
        """
        Add a maintenance task to the schedule.

        Args:
            machine (ConstructionMachine): Machine to add maintenance for.
            hours (int): Hours at which to perform maintenance.
            action (str): Action to perform.
        """
        if machine.name not in self.maintenance_schedule:
            self.maintenance_schedule[machine.name] = []
        self.maintenance_schedule[machine.name].append((hours, action))

    def print_schedule(self):
        """Print the maintenance schedule."""
        for machine, tasks in self.maintenance_schedule.items():
            print(f"Maintenance Schedule for {machine}:")
            for hours, action in tasks:
                print(f"  - After {hours} hours: {action}")


def main():
    try:
        # Create machines
        pile_driver = PileDriver("Pile Driver 1")
        earth_auger_drill = EarthAugerDrill("Earth Auger Drill 1")

        # Create maintenance schedule
        schedule = MaintenanceSchedule()

        # Add maintenance tasks
        schedule.add_maintenance(pile_driver, 50, "Inspect hammer")
        schedule.add_maintenance(pile_driver, 100, "Replace hammer")
        schedule.add_maintenance(earth_auger_drill, 20, "Inspect drill bit")
        schedule.add_maintenance(earth_auger_drill, 50, "Replace drill bit")

        # Log hours used
        pile_driver.log_hours(50)
        earth_auger_drill.log_hours(20)

        # Print maintenance schedule
        schedule.print_schedule()

        # Inspect machine conditions
        print(f"Pile Driver Hammer Condition: {pile_driver.inspect_hammer()}")
        print(f"Earth Auger Drill Drill Bit Condition: {earth_auger_drill.inspect_drill_bit()}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
