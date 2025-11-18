"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kallimos.com
Prompt: Write a program to simulate meal-sharing schedules in Kallimos Commons, allowing neighbors to opt into community meals while maintaining privacy.
Generated: DETERMINISTIC_99deac6b1215d544
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional


class Neighbor:
    """
    Represents a neighbor in Kallimos Commons.
    """
    def __init__(self, name: str, dietary_preferences: Optional[List[str]] = None):
        """
        Initialize a neighbor with name and optional dietary preferences.
        :param name: Name of the neighbor.
        :param dietary_preferences: List of dietary preferences (e.g., vegetarian, gluten-free).
        """
        self.name = name
        self.dietary_preferences = dietary_preferences or []


class MealSchedule:
    """
    Manages meal-sharing schedules in Kallimos Commons.
    """
    def __init__(self):
        """
        Initializes an empty meal schedule.
        """
        self.schedule: Dict[datetime.date, List[Neighbor]] = {}

    def add_meal_participant(self, date: datetime.date, neighbor: Neighbor) -> None:
        """
        Adds a neighbor to the meal schedule for a specific date.
        :param date: Date of the meal.
        :param neighbor: Neighbor participating in the meal.
        """
        if date not in self.schedule:
            self.schedule[date] = []
        if neighbor not in self.schedule[date]:
            self.schedule[date].append(neighbor)

    def get_participants(self, date: datetime.date) -> List[Neighbor]:
        """
        Retrieves the list of neighbors participating in a meal on a specific date.
        :param date: Date of the meal.
        :return: List of neighbors participating.
        """
        return self.schedule.get(date, [])

    def get_schedule(self) -> Dict[datetime.date, List[str]]:
        """
        Retrieves the entire meal schedule with neighbor names.
        :return: Dictionary containing the schedule.
        """
        return {
            date: [neighbor.name for neighbor in neighbors]
            for date, neighbors in self.schedule.items()
        }


def main():
    """
    Simulates meal-sharing schedules for Kallimos Commons.
    """
    # Initialize the meal schedule system
    meal_schedule = MealSchedule()

    try:
        # Create some neighbors
        alice = Neighbor(name="Alice", dietary_preferences=["vegetarian"])
        bob = Neighbor(name="Bob", dietary_preferences=["gluten-free"])
        charlie = Neighbor(name="Charlie")

        # Add neighbors to meals
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)

        meal_schedule.add_meal_participant(today, alice)
        meal_schedule.add_meal_participant(today, bob)
        meal_schedule.add_meal_participant(tomorrow, charlie)

        # Print today's participants
        print("Today's meal participants:")
        for neighbor in meal_schedule.get_participants(today):
            print(f"- {neighbor.name} ({', '.join(neighbor.dietary_preferences) or 'No preferences'})")

        # Print the full schedule
        print("\nFull Meal Schedule:")
        for date, participants in meal_schedule.get_schedule().items():
            print(f"{date}: {', '.join(participants)}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
