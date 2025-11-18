"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.homecareassistancebarrie.ca
Prompt: Write code to implement a memory care activity tracker for seniors, focusing on interventions targeting attention, visual-spatial perception, and executive functioning, inspired by the Cognitive Therapeutics Method™.
Generated: DETERMINISTIC_692fff2ab1cfa4e2
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Activity:
    """
    Represents a single activity in the memory care tracker.
    Attributes:
        name: Name of the activity
        category: Category of cognitive intervention (e.g., attention, visual-spatial perception, executive functioning)
        duration_minutes: Duration of the activity in minutes
        notes: Additional notes about the activity
    """
    def __init__(self, name, category, duration_minutes, notes=""):
        self.name = name
        self.category = category
        self.duration_minutes = duration_minutes
        self.notes = notes
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"{self.timestamp.strftime('%Y-%m-%d %H:%M:%S')} - {self.name} ({self.category}) for {self.duration_minutes} mins. Notes: {self.notes}"


class MemoryCareActivityTracker:
    """
    Tracks memory care activities for seniors.
    Attributes:
        activities: List of tracked activities
    """
    def __init__(self):
        self.activities = []

    def add_activity(self, name, category, duration_minutes, notes=""):
        """
        Adds a new activity to the tracker.
        Args:
            name: Name of the activity
            category: Category of cognitive intervention
            duration_minutes: Duration in minutes
            notes: Optional notes about the activity
        """
        try:
            if duration_minutes <= 0:
                raise ValueError("Duration must be greater than 0 minutes.")
            activity = Activity(name, category, duration_minutes, notes)
            self.activities.append(activity)
        except ValueError as e:
            print(f"Error: {e}")

    def get_activities(self):
        """
        Retrieves a list of all tracked activities.
        Returns:
            List of activity descriptions.
        """
        return [str(activity) for activity in self.activities]

    def filter_activities_by_category(self, category):
        """
        Filters activities by their category.
        Args:
            category: The category to filter by (e.g., "attention")
        Returns:
            List of activity descriptions matching the specified category.
        """
        return [str(activity) for activity in self.activities if activity.category.lower() == category.lower()]

    def export_activities_to_file(self, file_name="activities_log.txt"):
        """
        Exports all tracked activities to a file.
        Args:
            file_name: Name of the file to export to. Defaults to 'activities_log.txt'.
        """
        try:
            with open(file_name, "w") as file:
                file.write("\n".join(self.get_activities()))
            print(f"Activities successfully exported to {file_name}")
        except Exception as e:
            print(f"Error exporting activities to file: {e}")


# Example usage:
if __name__ == "__main__":
    tracker = MemoryCareActivityTracker()

    tracker.add_activity("Puzzle Solving", "attention", 30, "Used a crossword puzzle.")
    tracker.add_activity("Art Therapy", "visual-spatial perception", 45, "Painted a scenic landscape.")
    tracker.add_activity("Planning Exercise", "executive functioning", 20, "Organized a meal plan.")

    print("All Activities:")
    print("\n".join(tracker.get_activities()))

    print("\nFiltered Activities (Attention):")
    print("\n".join(tracker.filter_activities_by_category("attention")))

    tracker.export_activities_to_file()
```
