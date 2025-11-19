"""
Generated Code Metadata:
========================
Original URL: https://pneusml.com
Prompt: Write a Python script to manage a car maintenance schedule for a repair shop like Pneus ML, including reminders for tire rotation and alignment checks.
Generated: DETERMINISTIC_05046f0ca8ed25f9
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
import json
import os

class CarMaintenanceScheduler:
    """
    A class to manage car maintenance schedules, including tire rotation and alignment checks.
    """

    def __init__(self, data_file='maintenance_schedule.json'):
        """
        Initializes the scheduler with a data file to store maintenance records.
        
        :param data_file: The JSON file to store maintenance records.
        """
        self.data_file = data_file
        self.maintenance_records = self.load_records()

    def load_records(self):
        """
        Loads maintenance records from a JSON file.
        
        :return: A dictionary of maintenance records.
        """
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                return json.load(file)
        return {}

    def save_records(self):
        """
        Saves the current maintenance records to a JSON file.
        """
        with open(self.data_file, 'w') as file:
            json.dump(self.maintenance_records, file, indent=4)

    def add_car(self, car_id, last_rotation_date, last_alignment_date):
        """
        Adds a new car to the maintenance schedule.
        
        :param car_id: Unique identifier for the car.
        :param last_rotation_date: Date of the last tire rotation (YYYY-MM-DD).
        :param last_alignment_date: Date of the last alignment check (YYYY-MM-DD).
        """
        self.maintenance_records[car_id] = {
            'last_rotation_date': last_rotation_date,
            'last_alignment_date': last_alignment_date
        }
        self.save_records()

    def check_reminders(self):
        """
        Checks for upcoming maintenance reminders for all cars.
        
        :return: A list of reminders.
        """
        reminders = []
        today = datetime.date.today()

        for car_id, records in self.maintenance_records.items():
            last_rotation = datetime.datetime.strptime(records['last_rotation_date'], '%Y-%m-%d').date()
            last_alignment = datetime.datetime.strptime(records['last_alignment_date'], '%Y-%m-%d').date()

            # Check if tire rotation is due (every 6 months)
            if (today - last_rotation).days >= 180:
                reminders.append(f"Car {car_id}: Tire rotation is due.")

            # Check if alignment check is due (every 12 months)
            if (today - last_alignment).days >= 365:
                reminders.append(f"Car {car_id}: Alignment check is due.")

        return reminders

    def update_maintenance(self, car_id, rotation_date=None, alignment_date=None):
        """
        Updates the maintenance dates for a specific car.
        
        :param car_id: Unique identifier for the car.
        :param rotation_date: New date for the last tire rotation (YYYY-MM-DD).
        :param alignment_date: New date for the last alignment check (YYYY-MM-DD).
        """
        if car_id in self.maintenance_records:
            if rotation_date:
                self.maintenance_records[car_id]['last_rotation_date'] = rotation_date
            if alignment_date:
                self.maintenance_records[car_id]['last_alignment_date'] = alignment_date
            self.save_records()
        else:
            raise ValueError(f"Car ID {car_id} not found in records.")

if __name__ == "__main__":
    # Example usage of the CarMaintenanceScheduler
    scheduler = CarMaintenanceScheduler()

    # Adding cars to the maintenance schedule
    scheduler.add_car('ABC123', '2023-01-15', '2023-03-10')
    scheduler.add_car('XYZ789', '2022-11-20', '2023-02-05')

    # Checking for reminders
    reminders = scheduler.check_reminders()
    for reminder in reminders:
        print(reminder)

    # Updating maintenance records
    try:
        scheduler.update_maintenance('ABC123', rotation_date='2023-07-15')
    except ValueError as e:
        print(e)
```
