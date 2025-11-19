"""
Generated Code Metadata:
========================
Original URL: https://www.association-easycap.fr
Prompt: Generate a Python script to automate drone registration and scheduling for workshops, inspired by the Club de drone activities offered by Association Easy'cap.
Generated: DETERMINISTIC_7cdeec39bafde8cd
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from datetime import datetime, timedelta

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Drone:
    """Class representing a drone with registration details."""
    
    def __init__(self, registration_number, owner_name):
        self.registration_number = registration_number
        self.owner_name = owner_name

    def __repr__(self):
        return f"Drone(registration_number={self.registration_number}, owner_name={self.owner_name})"


class Workshop:
    """Class representing a workshop for drone activities."""
    
    def __init__(self, title, date, duration_hours):
        self.title = title
        self.date = date
        self.duration = timedelta(hours=duration_hours)

    def __repr__(self):
        return f"Workshop(title={self.title}, date={self.date}, duration={self.duration})"


class DroneRegistry:
    """Class to manage drone registrations and workshop scheduling."""
    
    def __init__(self):
        self.drones = []
        self.workshops = []

    def register_drone(self, registration_number, owner_name):
        """Register a new drone."""
        if any(drone.registration_number == registration_number for drone in self.drones):
            logging.error(f"Drone with registration number {registration_number} is already registered.")
            raise ValueError("Drone already registered.")
        
        new_drone = Drone(registration_number, owner_name)
        self.drones.append(new_drone)
        logging.info(f"Registered drone: {new_drone}")

    def schedule_workshop(self, title, date_str, duration_hours):
        """Schedule a new workshop."""
        try:
            workshop_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        except ValueError as e:
            logging.error("Invalid date format. Please use 'YYYY-MM-DD HH:MM'.")
            raise e
        
        new_workshop = Workshop(title, workshop_date, duration_hours)
        self.workshops.append(new_workshop)
        logging.info(f"Scheduled workshop: {new_workshop}")

    def save_registry(self, filename):
        """Save the drone registry and workshops to a JSON file."""
        data = {
            "drones": [drone.__dict__ for drone in self.drones],
            "workshops": [workshop.__dict__ for workshop in self.workshops]
        }
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, default=str, indent=4)
            logging.info(f"Registry saved to {filename}")
        except IOError as e:
            logging.error(f"Failed to save registry: {e}")
            raise e

    def load_registry(self, filename):
        """Load the drone registry and workshops from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            self.drones = [Drone(**drone) for drone in data.get("drones", [])]
            self.workshops = [Workshop(**workshop) for workshop in data.get("workshops", [])]
            logging.info(f"Registry loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Failed to load registry: {e}")
            raise e


if __name__ == "__main__":
    registry = DroneRegistry()

    # Example usage
    try:
        registry.register_drone("ABC123", "John Doe")
        registry.schedule_workshop("Drone Basics", "2023-11-15 10:00", 2)
        registry.save_registry("drone_registry.json")
        registry.load_registry("drone_registry.json")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
