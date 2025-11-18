"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cegeduc.org
Prompt: Write Python code for an educational workshop that teaches urban youth about biodiversity conservation and restoration, incorporating hands-on activities inspired by the nature-based education approach described on the CEGEduc website.
Generated: DETERMINISTIC_eeb9bf367c0613c3
Batch ID: 20250612_154239
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

# Define a class for managing the biodiversity workshop
class BiodiversityWorkshop:
    """
    A class to manage an educational workshop centered around biodiversity conservation and restoration.

    Attributes:
        title (str): Title of the workshop.
        activities (list): List of hands-on activities for the workshop.
        participants (list): List of registered participants.
    """

    def __init__(self, title):
        """
        Initializes the workshop with a title and empty lists for activities and participants.

        Args:
            title (str): Title of the workshop.
        """
        self.title = title
        self.activities = []
        self.participants = []

    def add_activity(self, name, description):
        """
        Adds an activity to the workshop.

        Args:
            name (str): Name of the activity.
            description (str): Description of the activity.
        """
        activity = {"name": name, "description": description}
        self.activities.append(activity)

    def register_participant(self, name, age):
        """
        Registers a participant for the workshop.

        Args:
            name (str): Name of the participant.
            age (int): Age of the participant.
        """
        if age < 8:
            raise ValueError("Participant must be at least 8 years old.")
        participant = {"name": name, "age": age}
        self.participants.append(participant)

    def save_workshop_data(self, filename="workshop_data.json"):
        """
        Saves the workshop data (title, activities, participants) to a JSON file.

        Args:
            filename (str): Name of the file to save the data into. Defaults to 'workshop_data.json'.
        """
        data = {
            "title": self.title,
            "activities": self.activities,
            "participants": self.participants,
        }
        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Workshop data successfully saved to {filename}.")
        except IOError as e:
            print(f"Error saving workshop data: {e}")

    def load_workshop_data(self, filename="workshop_data.json"):
        """
        Loads workshop data from a JSON file.

        Args:
            filename (str): Name of the file to load the data from. Defaults to 'workshop_data.json'.
        """
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError(f"{filename} does not exist.")
            with open(filename, "r") as file:
                data = json.load(file)
                self.title = data.get("title", self.title)
                self.activities = data.get("activities", [])
                self.participants = data.get("participants", [])
            print(f"Workshop data successfully loaded from {filename}.")
        except (IOError, FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading workshop data: {e}")

    def display_workshop_details(self):
        """
        Displays the workshop details including title, activities, and participants.
        """
        print(f"Workshop Title: {self.title}")
        print("\nActivities:")
        for activity in self.activities:
            print(f"  - {activity['name']}: {activity['description']}")
        print("\nParticipants:")
        for participant in self.participants:
            print(f"  - {participant['name']}, Age: {participant['age']}")


# Example usage of the BiodiversityWorkshop class
if __name__ == "__main__":
    # Create a new workshop
    workshop = BiodiversityWorkshop("Urban Youth Biodiversity Conservation Workshop")

    # Add activities to the workshop
    workshop.add_activity(
        "Planting Native Trees",
        "Youth will plant native tree saplings to restore local biodiversity.",
    )
    workshop.add_activity(
        "Pollinator Observation",
        "Hands-on activity observing bees, butterflies, and other pollinators.",
    )
    workshop.add_activity(
        "Nature Scavenger Hunt",
        "Explore the outdoors to find items that represent healthy ecosystems.",
    )

    # Register participants
    try:
        workshop.register_participant("Alice", 14)
        workshop.register_participant("Bob", 10)
        workshop.register_participant("Charlie", 8)
    except ValueError as e:
        print(f"Error registering participant: {e}")

    # Display workshop details
    workshop.display_workshop_details()

    # Save workshop data to file
    workshop.save_workshop_data()

    # Load workshop data from file (example of reloading data)
    workshop.load_workshop_data()

    # Display workshop details again after loading data
    workshop.display_workshop_details()
```
