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
import json
import datetime

class DroneRegistrationError(Exception):
    """Custom exception for drone registration errors."""
    pass

class WorkshopScheduler:
    """Class to handle drone registration and workshop scheduling."""

    def __init__(self, data_file='drone_data.json'):
        """
        Initialize WorkshopScheduler with a data file for storing drone registrations.

        Args:
            data_file (str): The path to the JSON file for storing drone data.
        """
        self.data_file = data_file
        self.drones = self.load_drones()

    def load_drones(self):
        """Load drone registrations from a JSON file."""
        try:
            with open(self.data_file, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_drones(self):
        """Save drone registrations to a JSON file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.drones, file, indent=4)

    def register_drone(self, owner_name, drone_id, registration_date=None):
        """
        Register a new drone.

        Args:
            owner_name (str): The name of the drone owner.
            drone_id (str): The unique identifier for the drone.
            registration_date (str): The date of registration in YYYY-MM-DD format. Defaults to today.

        Raises:
            DroneRegistrationError: If the drone is already registered.
        """
        registration_date = registration_date or datetime.date.today().isoformat()

        # Check if the drone is already registered
        if any(drone['drone_id'] == drone_id for drone in self.drones):
            raise DroneRegistrationError(f"Drone ID {drone_id} is already registered.")

        # Register the new drone
        self.drones.append({
            'owner_name': owner_name,
            'drone_id': drone_id,
            'registration_date': registration_date
        })
        self.save_drones()
        print(f"Drone ID {drone_id} registered successfully.")

    def schedule_workshop(self, workshop_date, max_participants):
        """
        Schedule a workshop.

        Args:
            workshop_date (str): The date of the workshop in YYYY-MM-DD format.
            max_participants (int): The maximum number of participants for the workshop.

        Returns:
            dict: Workshop details including date and max participants.
        """
        workshop_date = datetime.datetime.strptime(workshop_date, '%Y-%m-%d').date()
        if workshop_date < datetime.date.today():
            raise ValueError("Workshop date cannot be in the past.")

        return {
            'workshop_date': workshop_date,
            'max_participants': max_participants
        }

def main():
    """Main function to execute the drone registration and workshop scheduling."""
    scheduler = WorkshopScheduler()

    # Example of registering a drone
    try:
        scheduler.register_drone("John Doe", "DRONE123")
    except DroneRegistrationError as e:
        print(e)

    # Example of scheduling a workshop
    try:
        workshop = scheduler.schedule_workshop("2023-12-01", 10)
        print("Workshop scheduled:", workshop)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
