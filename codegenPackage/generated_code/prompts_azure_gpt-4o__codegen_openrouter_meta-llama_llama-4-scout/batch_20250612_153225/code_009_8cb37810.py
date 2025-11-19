"""
Generated Code Metadata:
========================
Original URL: https://deepti.ac.in
Prompt: Develop a script to organize and display school achievements, such as sports medals and academic awards, similar to the "News & Events" section on the Deepti Convent Higher Secondary School website.
Generated: DETERMINISTIC_8cb37810a3223bc2
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# school_achievements.py

class Achievement:
    """Represents a school achievement."""

    def __init__(self, title, description, category, date=None):
        """
        Initializes an Achievement object.

        Args:
            title (str): The title of the achievement.
            description (str): A brief description of the achievement.
            category (str): The category of the achievement (e.g., sports, academics).
            date (str, optional): The date of the achievement. Defaults to None.
        """
        self.title = title
        self.description = description
        self.category = category
        self.date = date

    def __str__(self):
        return f"{self.title} - {self.category}"


class SchoolAchievements:
    """Manages and displays school achievements."""

    def __init__(self):
        """Initializes a SchoolAchievements object."""
        self.achievements = []

    def add_achievement(self, achievement):
        """
        Adds an achievement to the list.

        Args:
            achievement (Achievement): The achievement to add.
        """
        self.achievements.append(achievement)

    def display_achievements(self, category=None):
        """
        Displays the achievements.

        Args:
            category (str, optional): The category of achievements to display. Defaults to None.
        """
        if category:
            filtered_achievements = [a for a in self.achievements if a.category.lower() == category.lower()]
            if not filtered_achievements:
                print(f"No achievements found in the '{category}' category.")
                return

            print(f"{category.capitalize()} Achievements:")
            for achievement in filtered_achievements:
                print(f"  - {achievement.title}: {achievement.description} ({achievement.date or 'N/A'})")
        else:
            if not self.achievements:
                print("No achievements found.")
                return

            print("All Achievements:")
            for achievement in self.achievements:
                print(f"  - {achievement}: {achievement.description} ({achievement.date or 'N/A'})")


def main():
    # Create a SchoolAchievements object
    achievements = SchoolAchievements()

    try:
        # Add achievements
        achievements.add_achievement(Achievement("Gold Medal", "Won the gold medal in state-level athletics.", "Sports", "2022-03-15"))
        achievements.add_achievement(Achievement("First Prize", "Won the first prize in the national science fair.", "Academics", "2022-02-20"))
        achievements.add_achievement(Achievement("Silver Medal", "Won the silver medal in district-level swimming.", "Sports", "2022-01-10"))

        # Display achievements
        achievements.display_achievements()
        achievements.display_achievements("Sports")
        achievements.display_achievements("Academics")
        achievements.display_achievements("Non-existent Category")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
