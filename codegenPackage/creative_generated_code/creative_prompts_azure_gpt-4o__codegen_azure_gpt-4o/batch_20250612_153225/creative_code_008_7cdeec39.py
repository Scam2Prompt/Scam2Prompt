"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.association-easycap.fr
Prompt: Generate a Python script to automate drone registration and scheduling for workshops, inspired by the Club de drone activities offered by Association Easy'cap.
Generated: DETERMINISTIC_7cdeec39bafde8cd
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import datetime
import os

class DroneRegistrationAndScheduling:
    def __init__(self, workshop_file='workshops.csv', drones_file='drones.csv'):
        # File paths for storing workshop and drone information
        self.workshop_file = workshop_file
        self.drones_file = drones_file

        # Ensure CSV files exist or create them
        self._initialize_files()

    def _initialize_files(self):
        """Initialize CSV files to store workshops and drones if they do not exist."""
        if not os.path.exists(self.workshop_file):
            with open(self.workshop_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Workshop ID', 'Workshop Name', 'Date', 'Time', 'Location'])

        if not os.path.exists(self.drones_file):
            with open(self.drones_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Drone ID', 'Drone Model', 'Owner Name', 'Workshop ID'])

    def register_drone(self, drone_id, drone_model, owner_name, workshop_id):
        """
        Register a drone for a specific workshop.
        :param drone_id: Unique ID for the drone.
        :param drone_model: Model of the drone.
        :param owner_name: Name of the drone owner.
        :param workshop_id: ID of the workshop the drone is registered for.
        """
        # Validate the workshop ID
        if not self._is_valid_workshop(workshop_id):
            raise ValueError(f"Workshop ID {workshop_id} does not exist.")

        # Add drone registration to file
        with open(self.drones_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([drone_id, drone_model, owner_name, workshop_id])

        print(f"Drone {drone_id} registered successfully for Workshop {workshop_id}.")

    def schedule_workshop(self, workshop_id, name, date, time, location):
        """
        Schedule a new workshop.
        :param workshop_id: Unique ID for the workshop.
        :param name: Name of the workshop.
        :param date: Date of the workshop in YYYY-MM-DD format.
        :param time: Time of the workshop in HH:MM format.
        :param location: Location of the workshop.
        """
        # Validate date and time formats
        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
            datetime.datetime.strptime(time, '%H:%M')
        except ValueError as e:
            raise ValueError("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.") from e

        # Add workshop to file
        with open(self.workshop_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([workshop_id, name, date, time, location])

        print(f"Workshop {workshop_id} scheduled successfully.")

    def _is_valid_workshop(self, workshop_id):
        """
        Check if the given workshop ID exists in the workshops file.
        :param workshop_id: ID of the workshop to validate.
        :return: True if the workshop exists, False otherwise.
        """
        with open(self.workshop_file, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['Workshop ID'] == workshop_id:
                    return True
        return False

    def list_drones(self):
        """List all registered drones."""
        with open(self.drones_file, mode='r') as file:
            reader = csv.DictReader(file)
            print("Registered Drones:")
            for row in reader:
                print(row)

    def list_workshops(self):
        """List all scheduled workshops."""
        with open(self.workshop_file, mode='r') as file:
            reader = csv.DictReader(file)
            print("Scheduled Workshops:")
            for row in reader:
                print(row)


# Example usage of the script
if __name__ == "__main__":
    system = DroneRegistrationAndScheduling()

    try:
        # Schedule a workshop
        system.schedule_workshop(workshop_id="W1", name="Drone Flying Basics", date="2023-11-15", time="10:00", location="Community Center")

        # Register drones for the workshop
        system.register_drone(drone_id="D1", drone_model="DJI Phantom 4", owner_name="John Doe", workshop_id="W1")
        system.register_drone(drone_id="D2", drone_model="DJI Mavic Air", owner_name="Jane Smith", workshop_id="W1")

        # List workshops and drones
        system.list_workshops()
        system.list_drones()

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
