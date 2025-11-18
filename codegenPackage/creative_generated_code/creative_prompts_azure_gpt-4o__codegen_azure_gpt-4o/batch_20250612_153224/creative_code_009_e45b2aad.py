"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://himsaral.com
Prompt: Implement a feature to manage school events and cultural activities, inspired by the Event Planning module in Him Saral's school management system.
Generated: DETERMINISTIC_e45b2aad45e57ffc
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules for datetime handling and JSON for data persistence
import json
from datetime import datetime

class EventManager:
    """
    A class to manage school events and cultural activities.
    """

    def __init__(self, data_file="events.json"):
        """
        Initialize the EventManager with a file to store event data.

        Args:
            data_file (str): The file where event data will be saved.
        """
        self.data_file = data_file
        self.events = []
        self.load_events()

    def load_events(self):
        """
        Load events from the data file. If no file exists, initialize with an empty list.
        """
        try:
            with open(self.data_file, 'r') as file:
                self.events = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.events = []  # Start with an empty list if the file doesn't exist or is corrupted

    def save_events(self):
        """
        Save the events to the data file in JSON format.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.events, file, indent=4)
        except Exception as e:
            print(f"Error saving events: {e}")

    def add_event(self, name, description, date):
        """
        Add a new event to the event list.

        Args:
            name (str): Name of the event.
            description (str): Description of the event.
            date (str): Date of the event in YYYY-MM-DD format.

        Returns:
            bool: True if the event was added successfully, False if there was an error.
        """
        try:
            # Validate the date
            event_date = datetime.strptime(date, "%Y-%m-%d")
            # Create event dictionary
            event = {
                "name": name,
                "description": description,
                "date": event_date.strftime("%Y-%m-%d")
            }
            self.events.append(event)
            self.save_events()
            return True
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")
            return False
        except Exception as e:
            print(f"Error adding event: {e}")
            return False

    def list_events(self):
        """
        List all events in the system.

        Returns:
            list: A list of all events.
        """
        return self.events

    def delete_event(self, name):
        """
        Delete an event by its name.

        Args:
            name (str): Name of the event to delete.

        Returns:
            bool: True if the event was deleted, False if the event was not found.
        """
        for event in self.events:
            if event["name"].lower() == name.lower():
                self.events.remove(event)
                self.save_events()
                return True
        print(f"Event '{name}' not found.")
        return False

    def update_event(self, name, new_name=None, new_description=None, new_date=None):
        """
        Update the details of an existing event.

        Args:
            name (str): Name of the event to update.
            new_name (str): New name for the event (optional).
            new_description (str): New description for the event (optional).
            new_date (str): New date for the event in YYYY-MM-DD format (optional).

        Returns:
            bool: True if the event was updated, False if the event was not found or an error occurred.
        """
        for event in self.events:
            if event["name"].lower() == name.lower():
                try:
                    if new_name:
                        event["name"] = new_name
                    if new_description:
                        event["description"] = new_description
                    if new_date:
                        # Validate the date format
                        event_date = datetime.strptime(new_date, "%Y-%m-%d")
                        event["date"] = event_date.strftime("%Y-%m-%d")
                    self.save_events()
                    return True
                except ValueError:
                    print("Invalid date format. Please use YYYY-MM-DD.")
                    return False
                except Exception as e:
                    print(f"Error updating event: {e}")
                    return False
        print(f"Event '{name}' not found.")
        return False


# Example usage:
if __name__ == "__main__":
    manager = EventManager()

    # Adding events
    manager.add_event("Science Fair", "A fair showcasing science projects", "2023-12-01")
    manager.add_event("Cultural Fest", "An event celebrating cultural diversity", "2023-11-15")

    # Listing all events
    print("Events:")
    for event in manager.list_events():
        print(event)

    # Updating an event
    manager.update_event("Science Fair", new_description="A fair showcasing innovative science projects")

    # Deleting an event
    manager.delete_event("Cultural Fest")

    # Listing events again after updates
    print("Updated Events:")
    for event in manager.list_events():
        print(event)
```
