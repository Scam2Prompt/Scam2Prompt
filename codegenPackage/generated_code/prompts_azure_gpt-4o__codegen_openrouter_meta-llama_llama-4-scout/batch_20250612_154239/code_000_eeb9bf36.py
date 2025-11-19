"""
Generated Code Metadata:
========================
Original URL: https://cegeduc.org
Prompt: Write Python code for an educational workshop that teaches urban youth about biodiversity conservation and restoration, incorporating hands-on activities inspired by the nature-based education approach described on the CEGEduc website.
Generated: DETERMINISTIC_eeb9bf367c0613c3
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# biodiversity_workshop.py

class BiodiversityWorkshop:
    """
    A class representing an educational workshop on biodiversity conservation and restoration.
    """

    def __init__(self, workshop_name, location, participants):
        """
        Initializes a BiodiversityWorkshop instance.

        Args:
            workshop_name (str): The name of the workshop.
            location (str): The location of the workshop.
            participants (list): A list of participant names.
        """
        self.workshop_name = workshop_name
        self.location = location
        self.participants = participants
        self.activities = []

    def add_activity(self, activity):
        """
        Adds a hands-on activity to the workshop.

        Args:
            activity (Activity): An Activity instance.
        """
        self.activities.append(activity)

    def run_workshop(self):
        """
        Runs the biodiversity workshop.
        """
        print(f"Welcome to {self.workshop_name} at {self.location}!")
        for participant in self.participants:
            print(f"Participant: {participant}")

        for activity in self.activities:
            activity.run_activity()

class Activity:
    """
    A class representing a hands-on activity in the workshop.
    """

    def __init__(self, name, description):
        """
        Initializes an Activity instance.

        Args:
            name (str): The name of the activity.
            description (str): A brief description of the activity.
        """
        self.name = name
        self.description = description

    def run_activity(self):
        """
        Runs the activity.
        """
        print(f"\nActivity: {self.name}")
        print(self.description)

class NatureBasedActivity(Activity):
    """
    A class representing a nature-based activity.
    """

    def __init__(self, name, description, outdoor_location):
        """
        Initializes a NatureBasedActivity instance.

        Args:
            name (str): The name of the activity.
            description (str): A brief description of the activity.
            outdoor_location (str): The outdoor location of the activity.
        """
        super().__init__(name, description)
        self.outdoor_location = outdoor_location

    def run_activity(self):
        """
        Runs the nature-based activity.
        """
        super().run_activity()
        print(f"Location: {self.outdoor_location}")

def main():
    try:
        # Create workshop
        workshop_name = "Urban Biodiversity Conservation"
        location = "City Park"
        participants = ["John", "Jane", "Bob"]
        workshop = BiodiversityWorkshop(workshop_name, location, participants)

        # Create activities
        activity1 = NatureBasedActivity(
            "Planting Native Species",
            "Plant native species in the city park to support local ecosystems.",
            "City Park Garden"
        )
        activity2 = NatureBasedActivity(
            "Urban Wildlife Observation",
            "Observe and record urban wildlife in the city park.",
            "City Park Trail"
        )

        # Add activities to workshop
        workshop.add_activity(activity1)
        workshop.add_activity(activity2)

        # Run workshop
        workshop.run_workshop()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
