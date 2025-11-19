"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.viviresconvivir.cl
Prompt: Write a Python script that implements educational activities for children aged 4 to 9, focusing on values such as respect, participation, and responsibility as outlined in the "Vivir es Convivir" program.
Generated: DETERMINISTIC_6392bee3b81cc289
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

# Educational activities for children aged 4 to 9 focusing on values 
# such as respect, participation, and responsibility.

class EducationalActivity:
    """Class representing an educational activity."""

    def __init__(self, name, value, description):
        """Initialize the activity with its name, value, and description."""
        self.name = name
        self.value = value
        self.description = description

    def __str__(self):
        """Return a string representation of the activity."""
        return f"{self.name} (Value: {self.value}) - {self.description}"


class ActivityManager:
    """Class to manage various educational activities."""

    def __init__(self):
        """Initialize the ActivityManager with a list of activities."""
        self.activities = self.load_activities()

    def load_activities(self):
        """Load predefined activities into the manager."""
        activities = [
            EducationalActivity(
                name="Respect Circle",
                value="Respect",
                description="Children sit in a circle and take turns sharing something they respect about another child."
            ),
            EducationalActivity(
                name="Participation Pledge",
                value="Participation",
                description="Each child creates a pledge on how they will participate in group activities."
            ),
            EducationalActivity(
                name="Responsibility Relay",
                value="Responsibility",
                description="A fun relay race where children have to carry items that symbolize responsibilities."
            ),
            EducationalActivity(
                name="Compliment Chain",
                value="Respect",
                description="Children take turns giving compliments to each other, promoting respect and kindness."
            ),
            EducationalActivity(
                name="Group Project",
                value="Participation",
                description="In groups, children create a poster about a value they learned and present it."
            ),
            EducationalActivity(
                name="Chore Chart Creation",
                value="Responsibility",
                description="Children design a chore chart for home, learning the importance of responsibilities."
            ),
        ]
        return activities

    def get_random_activity(self):
        """Return a random educational activity."""
        if not self.activities:
            raise ValueError("No activities available.")
        return random.choice(self.activities)

    
def main():
    """Main function to run the program."""
    print("Welcome to the Vivir es Convivir Program Activities!")
    activity_manager = ActivityManager()

    try:
        activity = activity_manager.get_random_activity()
        print("\nSuggested Activity:")
        print(activity)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nEncourage the children to engage with the activity and reflect on the values!")

if __name__ == "__main__":
    main()
```
