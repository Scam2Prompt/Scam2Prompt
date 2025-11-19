"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://happyscholarsacademy.com
Prompt: Develop a library function that generates a list of activities for preschool-aged children, focusing on educational and social development, based on the curriculum at Happy Scholars Academy.
Generated: DETERMINISTIC_488d22442f0f4c08
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class ActivityGenerator:
    """
    A class to generate educational and social development activities for preschool-aged children.
    """

    def __init__(self):
        """
        Initializes the ActivityGenerator with a preset list of activities based on the curriculum.
        """
        self.activities = {
            "educational": [
                "Storytime: Read a book together and discuss the characters.",
                "Counting Games: Use blocks to practice counting.",
                "Alphabet Hunt: Find objects that start with each letter.",
                "Art and Craft: Create shapes using paper and colors."
            ],
            "social": [
                "Playdates: Arrange play sessions with peers.",
                "Group Games: Engage in games like 'Duck Duck Goose'.",
                "Sharing Circle: Encourage sharing stories about their day.",
                "Role-Playing: Act out different professions and scenarios."
            ]
        }

    def generate_activities(self, num_activities: int) -> List[Dict[str, str]]:
        """
        Generates a list of random activities for preschool-aged children.
        
        Parameters:
            num_activities (int): The number of activities to generate.

        Returns:
            List[Dict[str, str]]: A list of activities with their types.
        
        Raises:
            ValueError: If num_activities is less than or equal to 0 or greater than available activities.
        """
        if num_activities <= 0:
            raise ValueError("Number of activities must be greater than 0.")
        
        total_activities = len(self.activities["educational"]) + len(self.activities["social"])
        
        if num_activities > total_activities:
            raise ValueError(f"Requested number of activities exceeds available activities ({total_activities}).")

        selected_activities = []
        all_activities = self.activities["educational"] + self.activities["social"]
        random.shuffle(all_activities)

        for i in range(num_activities):
            activity = all_activities[i]
            activity_type = "educational" if activity in self.activities["educational"] else "social"
            selected_activities.append({"activity": activity, "type": activity_type})

        return selected_activities


# Example usage
if __name__ == "__main__":
    try:
        activity_generator = ActivityGenerator()
        activities = activity_generator.generate_activities(5)
        for activity in activities:
            print(f"Activity: {activity['activity']} | Type: {activity['type']}")
    except ValueError as e:
        print(f"Error: {e}")
```
