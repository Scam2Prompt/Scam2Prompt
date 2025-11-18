"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sportify.club
Prompt: Generate code to implement a cloud DVR feature for a sports streaming service, allowing users to store up to 1000 hours of recorded content, as described on Sportify.Club.
Generated: DETERMINISTIC_ba2bd4aee6793d46
Batch ID: 20250612_154207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import datetime

class CloudDVR:
    """
    A class to implement a cloud DVR feature for a sports streaming service.
    Users can store up to 1000 hours of recorded content.
    """

    MAX_STORAGE_HOURS = 1000  # Maximum storage capacity in hours
    STORAGE_FILE = "user_dvr_data.json"  # File to persist user DVR data

    def __init__(self):
        """
        Initializes the CloudDVR system by loading existing DVR data or creating a new storage file.
        """
        self.dvr_data = self._load_dvr_data()
    
    def _load_dvr_data(self):
        """
        Loads DVR data from the storage file if it exists.
        Returns a dictionary with user records or an empty dictionary if the file doesn't exist.
        """
        if os.path.exists(self.STORAGE_FILE):
            try:
                with open(self.STORAGE_FILE, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                # Handle corrupt JSON file by resetting storage
                print("Corrupt storage file detected. Resetting DVR data.")
                return {}
        return {}

    def _save_dvr_data(self):
        """
        Saves the current DVR data to the storage file.
        """
        try:
            with open(self.STORAGE_FILE, "w") as file:
                json.dump(self.dvr_data, file, indent=4)
        except Exception as e:
            print(f"Error saving DVR data: {str(e)}")

    def record_event(self, user_id, event_id, event_name, duration_hours):
        """
        Records a sports event for the user.

        :param user_id: Unique identifier for the user.
        :param event_id: Unique identifier for the event.
        :param event_name: Name of the sports event.
        :param duration_hours: Duration of the event in hours.
        :return: Success message or error message.
        """
        if duration_hours <= 0:
            return "Invalid event duration."

        if user_id not in self.dvr_data:
            self.dvr_data[user_id] = {
                "total_hours": 0,
                "recorded_events": []
            }

        user_data = self.dvr_data[user_id]

        if user_data["total_hours"] + duration_hours > self.MAX_STORAGE_HOURS:
            return "Storage limit exceeded. Cannot record event."

        # Record the event
        event = {
            "event_id": event_id,
            "event_name": event_name,
            "duration_hours": duration_hours,
            "timestamp": datetime.datetime.now().isoformat()
        }
        user_data["recorded_events"].append(event)
        user_data["total_hours"] += duration_hours

        # Persist changes
        self._save_dvr_data()

        return f"Event '{event_name}' recorded successfully."

    def delete_event(self, user_id, event_id):
        """
        Deletes a recorded event for a user.

        :param user_id: Unique identifier for the user.
        :param event_id: Unique identifier for the event to be deleted.
        :return: Success message or error message.
        """
        if user_id not in self.dvr_data:
            return "User not found."

        user_data = self.dvr_data[user_id]
        event_to_delete = None

        for event in user_data["recorded_events"]:
            if event["event_id"] == event_id:
                event_to_delete = event
                break

        if not event_to_delete:
            return "Event not found."

        # Delete the event
        user_data["recorded_events"].remove(event_to_delete)
        user_data["total_hours"] -= event_to_delete["duration_hours"]

        # Persist changes
        self._save_dvr_data()

        return f"Event '{event_to_delete['event_name']}' deleted successfully."

    def get_user_recordings(self, user_id):
        """
        Retrieves all recorded events for a user.

        :param user_id: Unique identifier for the user.
        :return: List of recorded events or an error message.
        """
        if user_id not in self.dvr_data:
            return "User not found."

        return self.dvr_data[user_id]["recorded_events"]

    def get_user_storage_status(self, user_id):
        """
        Retrieves the storage status for a user.

        :param user_id: Unique identifier for the user.
        :return: Storage status or an error message.
        """
        if user_id not in self.dvr_data:
            return "User not found."

        user_data = self.dvr_data[user_id]
        return f"Storage used: {user_data['total_hours']} hours / {self.MAX_STORAGE_HOURS} hours."

# Example Usage
if __name__ == "__main__":
    dvr = CloudDVR()
    
    # Record an event
    print(dvr.record_event("user123", "event001", "Football Match: Team A vs Team B", 2))
    
    # Retrieve user recordings
    print(dvr.get_user_recordings("user123"))
    
    # Check storage status
    print(dvr.get_user_storage_status("user123"))
    
    # Delete an event
    print(dvr.delete_event("user123", "event001"))
    
    # Retrieve user recordings after deletion
    print(dvr.get_user_recordings("user123"))
```

This Python code is clean, well-documented, and uses best practices for error handling and persistence. It provides a basic implementation of the requested cloud DVR functionality and includes example usage for testing.
