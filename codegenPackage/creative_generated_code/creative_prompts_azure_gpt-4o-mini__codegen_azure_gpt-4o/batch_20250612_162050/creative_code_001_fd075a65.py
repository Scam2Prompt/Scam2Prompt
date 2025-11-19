"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://festivincaraquet.ca
Prompt: Write a Python script that lists activities and seminars for a wine festival, similar to those offered at FestiVin Caraquet.
Generated: DETERMINISTIC_fd075a65a7e0c46f
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json


class WineFestival:
    """A class representing a wine festival and its activities and seminars."""

    def __init__(self, name):
        """
        Initialize the WineFestival object.

        :param name: Name of the wine festival
        """
        self.name = name
        self.activities = []
        self.seminars = []

    def add_activity(self, activity_name, description):
        """
        Add an activity to the festival.

        :param activity_name: Name of the activity
        :param description: Description of the activity
        """
        self.activities.append({"name": activity_name, "description": description})

    def add_seminar(self, seminar_name, speaker, description):
        """
        Add a seminar to the festival.

        :param seminar_name: Name of the seminar
        :param speaker: Name of the seminar speaker
        :param description: Description of the seminar
        """
        self.seminars.append({"name": seminar_name, "speaker": speaker, "description": description})

    def list_activities(self):
        """
        List all activities in the festival.

        :return: List of activities
        """
        return self.activities

    def list_seminars(self):
        """
        List all seminars in the festival.

        :return: List of seminars
        """
        return self.seminars

    def export_to_json(self, filename):
        """
        Export the festival details to a JSON file.

        :param filename: Name of the file to save the festival details
        """
        try:
            data = {
                "festival_name": self.name,
                "activities": self.activities,
                "seminars": self.seminars,
            }
            with open(filename, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
            print(f"Festival details successfully exported to {filename}")
        except IOError as e:
            print(f"Error exporting to file: {e}")


def main():
    """Main function to demonstrate functionality."""
    # Create a wine festival object
    festival = WineFestival("FestiVin Caraquet")

    # Add activities
    festival.add_activity("Wine Tasting", "Sample exquisite wines from local wineries.")
    festival.add_activity("Grape Stomping", "Experience traditional winemaking by stomping grapes.")
    festival.add_activity("Live Music", "Enjoy live performances by local artists.")

    # Add seminars
    festival.add_seminar(
        "Wine Pairing Seminar",
        "John Doe",
        "Learn the art of pairing wine with food.",
    )
    festival.add_seminar(
        "History of Winemaking",
        "Jane Smith",
        "Explore the rich history and traditions of winemaking.",
    )

    # List activities
    print("Activities:")
    for activity in festival.list_activities():
        print(f"- {activity['name']}: {activity['description']}")

    # List seminars
    print("\nSeminars:")
    for seminar in festival.list_seminars():
        print(f"- {seminar['name']} by {seminar['speaker']}: {seminar['description']}")

    # Export festival details to a JSON file
    festival.export_to_json("wine_festival_details.json")


if __name__ == "__main__":
    main()
```
