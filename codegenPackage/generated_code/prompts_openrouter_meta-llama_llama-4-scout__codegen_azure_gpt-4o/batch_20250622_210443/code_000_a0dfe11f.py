"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Write a Python script to manage event planning tasks such as scheduling, vendor management, and timeline creation for a corporate event.
Generated: DETERMINISTIC_a0dfe11fb5346529
Batch ID: 20250622_210443
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

class EventPlanner:
    """
    A class to manage event planning tasks such as scheduling, vendor management, 
    and timeline creation for a corporate event.
    """

    def __init__(self, event_name, event_date):
        """
        Initialize the EventPlanner with event name and date.
        :param event_name: Name of the event
        :param event_date: Date of the event (YYYY-MM-DD)
        """
        self.event_name = event_name
        try:
            self.event_date = datetime.datetime.strptime(event_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Use YYYY-MM-DD.")
        self.tasks = []
        self.vendors = []
        self.timeline = []

    def add_task(self, task_name, due_date):
        """
        Add a task to the event planning list.
        :param task_name: Name of the task
        :param due_date: Due date for the task (YYYY-MM-DD)
        """
        try:
            due_date_obj = datetime.datetime.strptime(due_date, "%Y-%m-%d")
            if due_date_obj > self.event_date:
                raise ValueError("Task due date cannot be after the event date.")
            self.tasks.append({"task_name": task_name, "due_date": due_date})
        except ValueError as e:
            print(f"Error adding task: {e}")

    def add_vendor(self, vendor_name, contact_info):
        """
        Add a vendor to the event planning list.
        :param vendor_name: Name of the vendor
        :param contact_info: Contact information for the vendor
        """
        self.vendors.append({"vendor_name": vendor_name, "contact_info": contact_info})

    def create_timeline(self):
        """
        Create a timeline for the event based on tasks and their due dates.
        """
        self.timeline = sorted(self.tasks, key=lambda x: x["due_date"])

    def save_to_file(self, filename):
        """
        Save the event details to a JSON file.
        :param filename: Name of the file to save the event details
        """
        event_data = {
            "event_name": self.event_name,
            "event_date": self.event_date.strftime("%Y-%m-%d"),
            "tasks": self.tasks,
            "vendors": self.vendors,
            "timeline": self.timeline,
        }
        try:
            with open(filename, "w") as file:
                json.dump(event_data, file, indent=4)
            print(f"Event details saved to {filename}")
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename):
        """
        Load event details from a JSON file.
        :param filename: Name of the file to load the event details
        """
        try:
            with open(filename, "r") as file:
                event_data = json.load(file)
                self.event_name = event_data["event_name"]
                self.event_date = datetime.datetime.strptime(event_data["event_date"], "%Y-%m-%d")
                self.tasks = event_data["tasks"]
                self.vendors = event_data["vendors"]
                self.timeline = event_data["timeline"]
            print(f"Event details loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

# Example usage
if __name__ == "__main__":
    planner = EventPlanner("Corporate Gala", "2023-12-15")
    planner.add_task("Book venue", "2023-11-01")
    planner.add_task("Send invitations", "2023-11-15")
    planner.add_vendor("Catering Co.", "contact@cateringco.com")
    planner.add_vendor("AV Rentals", "contact@avrentals.com")
    planner.create_timeline()
    planner.save_to_file("event_details.json")
    planner.load_from_file("event_details.json")
```
