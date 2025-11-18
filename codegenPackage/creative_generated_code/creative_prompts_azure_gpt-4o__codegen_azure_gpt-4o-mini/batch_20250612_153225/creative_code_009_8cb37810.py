"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deepti.ac.in
Prompt: Develop a script to organize and display school achievements, such as sports medals and academic awards, similar to the "News & Events" section on the Deepti Convent Higher Secondary School website.
Generated: DETERMINISTIC_8cb37810a3223bc2
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# achievements.py

import json
from datetime import datetime

class Achievement:
    """
    A class to represent a school achievement.
    """

    def __init__(self, title, description, date, category):
        """
        Initializes an Achievement instance.

        :param title: Title of the achievement (str)
        :param description: Description of the achievement (str)
        :param date: Date of the achievement (str formatted as 'YYYY-MM-DD')
        :param category: Category of the achievement (str) e.g., 'Sports', 'Academics'
        """
        self.title = title
        self.description = description
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.category = category

    def to_dict(self):
        """Converts the achievement to a dictionary."""
        return {
            'title': self.title,
            'description': self.description,
            'date': self.date.strftime('%Y-%m-%d'),
            'category': self.category
        }


class AchievementManager:
    """
    A class to manage a collection of achievements.
    """

    def __init__(self):
        """Initializes the AchievementManager with an empty achievements list."""
        self.achievements = []

    def add_achievement(self, achievement):
        """
        Adds a new achievement to the collection.

        :param achievement: An instance of Achievement
        """
        if isinstance(achievement, Achievement):
            self.achievements.append(achievement)
        else:
            raise ValueError("Invalid achievement instance.")

    def save_to_file(self, filename):
        """
        Saves achievements to a JSON file.

        :param filename: The name of the file to save to (str)
        """
        try:
            with open(filename, 'w') as f:
                json.dump([ach.to_dict() for ach in self.achievements], f, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename):
        """
        Loads achievements from a JSON file.

        :param filename: The name of the file to load from (str)
        """
        try:
            with open(filename, 'r') as f:
                achievements_data = json.load(f)
                self.achievements = [Achievement(**data) for data in achievements_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

    def display_achievements(self):
        """Displays all achievements in a formatted manner."""
        if not self.achievements:
            print("No achievements to display.")
            return

        for achievement in sorted(self.achievements, key=lambda x: x.date, reverse=True):
            print(f"{achievement.date.strftime('%Y-%m-%d')} - {achievement.title} ({achievement.category})")
            print(f"   {achievement.description}\n")


if __name__ == "__main__":
    manager = AchievementManager()

    # Example achievements
    manager.add_achievement(Achievement("Gold Medal in Science Olympiad", "Achieved first place in national science competition.", "2023-04-10", "Academics"))
    manager.add_achievement(Achievement("District Basketball Champion", "Won the championship with the school basketball team.", "2023-05-15", "Sports"))

    # Save to file
    manager.save_to_file("achievements.json")

    # Load from file
    manager.load_from_file("achievements.json")

    # Display achievements
    manager.display_achievements()
```
