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
import random
import json
from typing import List, Dict

class BiodiversityWorkshop:
    def __init__(self, participants: List[str]):
        """
        Initializes the Biodiversity Workshop with a list of participants.

        :param participants: List of participant names
        """
        self.participants = participants
        self.activities = self.load_activities()

    def load_activities(self) -> List[Dict]:
        """
        Loads activities from a JSON file.

        :return: List of activities
        """
        try:
            with open('activities.json', 'r') as file:
                activities = json.load(file)
                return activities
        except FileNotFoundError:
            print("Error: activities.json file not found.")
            return []
        except json.JSONDecodeError:
            print("Error: activities.json file is not a valid JSON.")
            return []

    def select_activity(self) -> Dict:
        """
        Randomly selects an activity from the loaded activities.

        :return: A dictionary representing the selected activity
        """
        if not self.activities:
            print("No activities available to select.")
            return {}
        return random.choice(self.activities)

    def conduct_activity(self, activity: Dict):
        """
        Conducts the selected activity with the participants.

        :param activity: The activity to conduct
        """
        if not activity:
            print("No activity to conduct.")
            return
        
        print(f"Conducting Activity: {activity['name']}")
        print(f"Description: {activity['description']}")
        print("Participants:")
        for participant in self.participants:
            print(f"- {participant}")

    def run_workshop(self):
        """
        Runs the workshop by selecting and conducting an activity.
        """
        print("Welcome to the Biodiversity Workshop!")
        activity = self.select_activity()
        self.conduct_activity(activity)

if __name__ == "__main__":
    # Example participant names
    participants_list = ["Alice", "Bob", "Charlie", "Diana"]
    
    # Create a workshop instance
    workshop = BiodiversityWorkshop(participants_list)
    
    # Run the workshop
    workshop.run_workshop()
```

**activities.json** (Example content for the activities file):
```json
[
    {
        "name": "Planting Native Species",
        "description": "Participants will learn about the importance of native plants and will plant them in a local park."
    },
    {
        "name": "Biodiversity Scavenger Hunt",
        "description": "A fun scavenger hunt where participants will find various species in their local environment."
    },
    {
        "name": "Water Quality Testing",
        "description": "Participants will learn how to test water quality and understand its impact on local ecosystems."
    }
]
```
