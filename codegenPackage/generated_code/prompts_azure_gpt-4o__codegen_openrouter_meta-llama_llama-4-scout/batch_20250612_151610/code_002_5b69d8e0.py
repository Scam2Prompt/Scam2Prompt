"""
Generated Code Metadata:
========================
Original URL: https://multiservicios3l.com
Prompt: Generate code for a preventive maintenance scheduling system for industrial machinery, inspired by the maintenance services provided by Multiservicios Industriales 3L.
Generated: DETERMINISTIC_5b69d8e041c2b41a
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import Dict, List

class Machine:
    def __init__(self, id: int, name: str, maintenance_interval: int):
        """
        Initialize a Machine object.

        Args:
        id (int): Unique identifier for the machine.
        name (str): Name of the machine.
        maintenance_interval (int): Interval in days between maintenance sessions.
        """
        self.id = id
        self.name = name
        self.maintenance_interval = maintenance_interval
        self.last_maintenance_date = None

    def schedule_maintenance(self):
        """
        Schedule the next maintenance session for the machine.

        Returns:
        datetime: Date of the next maintenance session.
        """
        if self.last_maintenance_date is None:
            self.last_maintenance_date = datetime.now()
        next_maintenance_date = self.last_maintenance_date + timedelta(days=self.maintenance_interval)
        self.last_maintenance_date = next_maintenance_date
        return next_maintenance_date

    def perform_maintenance(self):
        """
        Record that maintenance has been performed on the machine.

        Returns:
        None
        """
        self.last_maintenance_date = datetime.now()


class MaintenanceScheduler:
    def __init__(self):
        """
        Initialize a MaintenanceScheduler object.
        """
        self.machines: Dict[int, Machine] = {}

    def add_machine(self, machine: Machine):
        """
        Add a machine to the scheduler.

        Args:
        machine (Machine): Machine to add.

        Returns:
        None
        """
        self.machines[machine.id] = machine

    def remove_machine(self, machine_id: int):
        """
        Remove a machine from the scheduler.

        Args:
        machine_id (int): ID of the machine to remove.

        Returns:
        None

        Raises:
        KeyError: If the machine is not found.
        """
        if machine_id not in self.machines:
            raise KeyError(f"Machine {machine_id} not found")
        del self.machines[machine_id]

    def schedule_maintenance_for_all(self) -> Dict[int, datetime]:
        """
        Schedule maintenance for all machines.

        Returns:
        Dict[int, datetime]: Dictionary of machine IDs to next maintenance dates.
        """
        maintenance_schedule: Dict[int, datetime] = {}
        for machine in self.machines.values():
            maintenance_schedule[machine.id] = machine.schedule_maintenance()
        return maintenance_schedule

    def perform_maintenance_on_machine(self, machine_id: int):
        """
        Record that maintenance has been performed on a machine.

        Args:
        machine_id (int): ID of the machine.

        Returns:
        None

        Raises:
        KeyError: If the machine is not found.
        """
        if machine_id not in self.machines:
            raise KeyError(f"Machine {machine_id} not found")
        self.machines[machine_id].perform_maintenance()


def main():
    scheduler = MaintenanceScheduler()

    # Create machines
    machine1 = Machine(1, "Machine 1", 30)  # Maintenance every 30 days
    machine2 = Machine(2, "Machine 2", 60)  # Maintenance every 60 days

    # Add machines to scheduler
    scheduler.add_machine(machine1)
    scheduler.add_machine(machine2)

    # Schedule maintenance for all machines
    maintenance_schedule = scheduler.schedule_maintenance_for_all()
    print("Maintenance Schedule:")
    for machine_id, maintenance_date in maintenance_schedule.items():
        print(f"Machine {machine_id}: {maintenance_date}")

    # Perform maintenance on a machine
    scheduler.perform_maintenance_on_machine(1)

    # Schedule maintenance for all machines again
    maintenance_schedule = scheduler.schedule_maintenance_for_all()
    print("\nUpdated Maintenance Schedule:")
    for machine_id, maintenance_date in maintenance_schedule.items():
        print(f"Machine {machine_id}: {maintenance_date}")


if __name__ == "__main__":
    main()
```
