"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://longhuigolf.com
Prompt: Generate code to track factory machine usage and maintenance schedules for molding and material processing machines, as described in Longhui Golf’s factory configuration details.
Generated: DETERMINISTIC_f6eacdb822c2b8ab
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime


class Machine:
    """
    A class to represent a factory machine and its usage and maintenance schedule.
    """
    def __init__(self, name, machine_type):
        """
        Initialize the machine with a name and type.

        :param name: Name of the machine
        :param machine_type: Type of the machine (e.g., molding, material processing)
        """
        self.name = name
        self.machine_type = machine_type
        self.usage_hours = 0
        self.last_maintenance_date = None
        self.maintenance_interval_days = 30  # Default maintenance interval
        self.maintenance_log = []

    def log_usage(self, hours):
        """
        Log machine usage in hours.

        :param hours: Number of hours the machine was used
        """
        if hours < 0:
            raise ValueError("Usage hours cannot be negative.")
        self.usage_hours += hours

    def schedule_maintenance(self):
        """
        Schedule maintenance for the machine.
        """
        self.last_maintenance_date = datetime.date.today()
        self.maintenance_log.append({
            "date": self.last_maintenance_date,
            "usage_hours_at_maintenance": self.usage_hours,
        })
        print(f"Maintenance scheduled for {self.name} on {self.last_maintenance_date}.")

    def needs_maintenance(self):
        """
        Check if the machine needs maintenance based on the interval.

        :return: Boolean indicating whether the machine needs maintenance
        """
        if self.last_maintenance_date is None:
            return True  # Maintenance should be scheduled if never done
        next_maintenance_due = self.last_maintenance_date + datetime.timedelta(days=self.maintenance_interval_days)
        return datetime.date.today() >= next_maintenance_due

    def __str__(self):
        """
        Return a string representation of the machine's status.
        """
        status = f"Machine Name: {self.name}\n" \
                 f"Type: {self.machine_type}\n" \
                 f"Usage Hours: {self.usage_hours}\n" \
                 f"Last Maintenance: {self.last_maintenance_date or 'Never'}\n" \
                 f"Needs Maintenance: {'Yes' if self.needs_maintenance() else 'No'}\n"
        return status


class Factory:
    """
    A class to represent the factory and its machines.
    """
    def __init__(self):
        """
        Initialize the factory with an empty list of machines.
        """
        self.machines = []

    def add_machine(self, machine):
        """
        Add a machine to the factory.

        :param machine: Instance of the Machine class to add
        """
        if not isinstance(machine, Machine):
            raise TypeError("Only instances of the Machine class can be added.")
        self.machines.append(machine)

    def log_machine_usage(self, machine_name, hours):
        """
        Log usage hours for a specific machine.

        :param machine_name: Name of the machine
        :param hours: Number of hours to log
        """
        machine = self.get_machine_by_name(machine_name)
        if machine:
            machine.log_usage(hours)
        else:
            print(f"Machine with name '{machine_name}' not found.")

    def schedule_maintenance_for_machine(self, machine_name):
        """
        Schedule maintenance for a specific machine.

        :param machine_name: Name of the machine
        """
        machine = self.get_machine_by_name(machine_name)
        if machine:
            machine.schedule_maintenance()
        else:
            print(f"Machine with name '{machine_name}' not found.")

    def get_machine_by_name(self, machine_name):
        """
        Retrieve a machine by its name.

        :param machine_name: Name of the machine to retrieve
        :return: Machine instance or None if not found
        """
        for machine in self.machines:
            if machine.name == machine_name:
                return machine
        return None

    def display_machine_statuses(self):
        """
        Display the status of all machines in the factory.
        """
        for machine in self.machines:
            print(machine)
            print('-' * 40)


# Example usage
if __name__ == "__main__":
    # Create factory
    factory = Factory()

    # Add machines to factory
    factory.add_machine(Machine("Molding Machine 1", "Molding"))
    factory.add_machine(Machine("Material Processor 1", "Material Processing"))

    # Log usage
    factory.log_machine_usage("Molding Machine 1", 120)
    factory.log_machine_usage("Material Processor 1", 80)

    # Check maintenance status
    factory.display_machine_statuses()

    # Schedule maintenance
    factory.schedule_maintenance_for_machine("Molding Machine 1")

    # Display updated statuses
    factory.display_machine_statuses()
```
