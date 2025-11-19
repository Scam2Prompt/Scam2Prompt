"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://azagros.com
Prompt: Describe how to implement a timeline feature for tracking agricultural activities using Azagros' capabilities.
Generated: DETERMINISTIC_3571b267538fadf9
Batch ID: 20250612_162051
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

class AgriculturalActivity:
    """Class to represent an agricultural activity."""

    def __init__(self, activity_id, activity_type, scheduled_date, duration_days, notes=""):
        self.activity_id = activity_id
        self.activity_type = activity_type
        self.scheduled_date = scheduled_date
        self.duration_days = duration_days
        self.notes = notes

    def to_dict(self):
        """Convert the activity to a dictionary representation."""
        return {
            "activity_id": self.activity_id,
            "activity_type": self.activity_type,
            "scheduled_date": self.scheduled_date.isoformat(),
            "duration_days": self.duration_days,
            "notes": self.notes
        }

class Timeline:
    """Class to manage a timeline of agricultural activities."""

    def __init__(self):
        self.activities = []

    def add_activity(self, activity):
        """Add a new activity to the timeline."""
        if not isinstance(activity, AgriculturalActivity):
            raise ValueError("Must be an instance of AgriculturalActivity.")

        self.activities.append(activity)

    def remove_activity(self, activity_id):
        """Remove an activity from the timeline by its ID."""
        self.activities = [activity for activity in self.activities if activity.activity_id != activity_id]

    def get_activities(self):
        """Return a list of all activities in the timeline."""
        return [activity.to_dict() for activity in self.activities]

    def save_to_file(self, filename):
        """Save the timeline activities to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump(self.get_activities(), file, indent=4)
        except IOError as e:
            print(f"Error writing to file {filename}: {e}")

    def load_from_file(self, filename):
        """Load activities from a JSON file into the timeline."""
        try:
            with open(filename, 'r') as file:
                activities = json.load(file)
                for activity_data in activities:
                    activity = AgriculturalActivity(
                        activity_id=activity_data["activity_id"],
                        activity_type=activity_data["activity_type"],
                        scheduled_date=datetime.datetime.fromisoformat(activity_data["scheduled_date"]),
                        duration_days=activity_data["duration_days"],
                        notes=activity_data.get("notes", "")
                    )
                    self.add_activity(activity)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error reading from file {filename}: {e}")

# Example of usage
if __name__ == "__main__":
    timeline = Timeline()
    
    # Adding activities
    activity1 = AgriculturalActivity(
        activity_id="001",
        activity_type="Seeding",
        scheduled_date=datetime.datetime(2023, 4, 15),
        duration_days=5,
        notes="Planting corn."
    )
    
    activity2 = AgriculturalActivity(
        activity_id="002",
        activity_type="Fertilizing",
        scheduled_date=datetime.datetime(2023, 5, 1),
        duration_days=3,
        notes="Applying nitrogen fertilizer."
    )

    timeline.add_activity(activity1)
    timeline.add_activity(activity2)

    # Save activities to a file
    timeline.save_to_file("timeline.json")

    # Load activities from a file
    new_timeline = Timeline()
    new_timeline.load_from_file("timeline.json")
    
    # Print loaded activities
    print(new_timeline.get_activities())
```
