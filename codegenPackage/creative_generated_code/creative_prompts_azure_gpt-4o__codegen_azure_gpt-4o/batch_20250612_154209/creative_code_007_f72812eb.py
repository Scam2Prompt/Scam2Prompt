"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aktivrorteknikk.no
Prompt: Provide code examples for implementing a 24-hour service scheduling system for water pipeline maintenance, inspired by Aktiv Rørteknikk AS's round-the-clock service model.
Generated: DETERMINISTIC_f72812eb8687f006
Batch ID: 20250612_154209
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


class PipelineMaintenanceScheduler:
    """
    A class to schedule 24-hour water pipeline maintenance service.
    Inspired by Aktiv Rørteknikk AS's service model.
    """

    def __init__(self):
        """
        Initializes the scheduler with an empty schedule.
        """
        self.schedule = {}  # Stores scheduled tasks, keyed by date.

    def add_service_request(self, client_name, date, time, description):
        """
        Adds a service request to the schedule if the date/time is valid.
        :param client_name: str - Name of the client requesting service.
        :param date: str - Date of service in format "YYYY-MM-DD".
        :param time: str - Time of service in format "HH:MM".
        :param description: str - Description of the service request.
        :return: dict - Confirmation of the scheduled service or an error message.
        """
        try:
            # Validate date and time format.
            service_datetime = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")

            # Check if the date/time is in the past.
            if service_datetime < datetime.datetime.now():
                return {"error": "Cannot schedule a service in the past."}

            # Add the service to the schedule.
            self.schedule.setdefault(date, []).append({
                "time": time,
                "client_name": client_name,
                "description": description
            })

            return {"success": "Service request successfully added.", "data": self.schedule[date]}

        except ValueError:
            # Handle invalid date/time format.
            return {"error": "Invalid date or time format. Use 'YYYY-MM-DD' for date and 'HH:MM' for time."}

    def view_schedule(self, date=None):
        """
        Retrieves the schedule for a specific date or the entire schedule if no date is specified.
        :param date: str (optional) - Date in format "YYYY-MM-DD" to view the schedule for.
        :return: dict - The schedule for the specified date or the entire schedule.
        """
        if date:
            return {"date": date, "schedule": self.schedule.get(date, [])}
        return {"full_schedule": self.schedule}

    def cancel_service(self, date, time, client_name):
        """
        Cancels a scheduled service by date, time, and client name.
        :param date: str - Date of the service in format "YYYY-MM-DD".
        :param time: str - Time of the service in format "HH:MM".
        :param client_name: str - Name of the client requesting cancellation.
        :return: dict - Confirmation of cancellation or an error message.
        """
        if date not in self.schedule:
            return {"error": "No services scheduled for the specified date."}

        services = self.schedule[date]
        for service in services:
            if service["time"] == time and service["client_name"] == client_name:
                services.remove(service)
                return {"success": "Service successfully canceled.", "data": self.schedule[date]}

        return {"error": "Service not found for the specified date, time, and client name."}

    def save_schedule_to_file(self, filename="schedule.json"):
        """
        Saves the entire schedule to a JSON file.
        :param filename: str (optional) - Name of the file to save the schedule into.
        :return: dict - Confirmation of successful save or an error message.
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.schedule, file, indent=4)
            return {"success": f"Schedule successfully saved to {filename}."}
        except IOError:
            return {"error": f"Failed to save schedule to {filename}."}

    def load_schedule_from_file(self, filename="schedule.json"):
        """
        Loads the schedule from a JSON file.
        :param filename: str (optional) - Name of the file to load the schedule from.
        :return: dict - Confirmation of successful load or an error message.
        """
        try:
            with open(filename, "r") as file:
                self.schedule = json.load(file)
            return {"success": f"Schedule successfully loaded from {filename}."}
        except (IOError, json.JSONDecodeError):
            return {"error": f"Failed to load schedule from {filename}."}


# Example usage
if __name__ == "__main__":
    scheduler = PipelineMaintenanceScheduler()

    # Adding service requests
    print(scheduler.add_service_request("Client A", "2023-11-01", "14:00", "Repair main pipeline"))
    print(scheduler.add_service_request("Client B", "2023-11-01", "15:00", "Inspect valves"))

    # Viewing schedule
    print(scheduler.view_schedule("2023-11-01"))

    # Canceling a service request
    print(scheduler.cancel_service("2023-11-01", "14:00", "Client A"))

    # Saving schedule to file
    print(scheduler.save_schedule_to_file())

    # Loading schedule from file
    print(scheduler.load_schedule_from_file())
```
