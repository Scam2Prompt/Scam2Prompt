"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://payeshnirooco.com
Prompt: Write a Python script to automate the maintenance scheduling for diesel and gas generators based on the guidelines provided by Payesh Niroo.
Generated: DETERMINISTIC_dd95f23cb69c7b41
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json

class Generator:
    """
    A class to represent a generator and its maintenance schedule.

    Attributes:
        id (str): Unique identifier for the generator.
        type (str): Type of the generator ('Diesel' or 'Gas').
        last_maintenance_date (datetime.date): The date of the last maintenance.
        maintenance_interval_days (int): Number of days between scheduled maintenance.
    """
    def __init__(self, generator_id, generator_type, last_maintenance_date, maintenance_interval_days):
        self.id = generator_id
        self.type = generator_type
        self.last_maintenance_date = last_maintenance_date
        self.maintenance_interval_days = maintenance_interval_days

    def next_maintenance_date(self):
        """
        Calculate the next maintenance date for the generator.

        Returns:
            datetime.date: The next scheduled maintenance date.
        """
        return self.last_maintenance_date + datetime.timedelta(days=self.maintenance_interval_days)


class MaintenanceScheduler:
    """
    A class to manage the scheduling of generator maintenance.

    Attributes:
        generators (list): A list of Generator objects.
    """
    def __init__(self):
        self.generators = []

    def add_generator(self, generator):
        """
        Add a generator to the scheduler.

        Args:
            generator (Generator): The generator object to add.
        """
        self.generators.append(generator)

    def get_schedule(self):
        """
        Generate the maintenance schedule for all generators.

        Returns:
            list: A list of dictionaries representing the maintenance schedule.
        """
        schedule = []
        for generator in self.generators:
            schedule.append({
                "Generator ID": generator.id,
                "Generator Type": generator.type,
                "Last Maintenance Date": generator.last_maintenance_date.strftime('%Y-%m-%d'),
                "Next Maintenance Date": generator.next_maintenance_date().strftime('%Y-%m-%d')
            })
        return schedule

    def save_schedule_to_file(self, filename):
        """
        Save the maintenance schedule to a JSON file.

        Args:
            filename (str): The name of the file to save the schedule to.
        """
        try:
            schedule = self.get_schedule()
            with open(filename, 'w') as file:
                json.dump(schedule, file, indent=4)
            print(f"Schedule saved to {filename}")
        except Exception as e:
            print(f"Error saving schedule to file: {e}")


# Example usage of the script
if __name__ == "__main__":
    # Create the maintenance scheduler
    scheduler = MaintenanceScheduler()

    # Add generators based on Payesh Niroo guidelines
    # Diesel generators: maintenance every 180 days
    # Gas generators: maintenance every 120 days
    try:
        diesel_generator = Generator(
            generator_id="D001", 
            generator_type="Diesel", 
            last_maintenance_date=datetime.date(2023, 1, 1), 
            maintenance_interval_days=180
        )
        gas_generator = Generator(
            generator_id="G001", 
            generator_type="Gas", 
            last_maintenance_date=datetime.date(2023, 3, 1), 
            maintenance_interval_days=120
        )

        # Add generators to the scheduler
        scheduler.add_generator(diesel_generator)
        scheduler.add_generator(gas_generator)

        # Generate and display the maintenance schedule
        schedule = scheduler.get_schedule()
        print("Maintenance Schedule:")
        for entry in schedule:
            print(entry)

        # Save the schedule to a file
        scheduler.save_schedule_to_file("maintenance_schedule.json")

    except Exception as e:
        print(f"An error occurred: {e}")
```
