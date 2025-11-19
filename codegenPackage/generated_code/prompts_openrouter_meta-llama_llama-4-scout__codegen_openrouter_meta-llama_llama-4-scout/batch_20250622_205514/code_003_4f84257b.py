"""
Generated Code Metadata:
========================
Original URL: https://wonderplanet.ee
Prompt: "Generate a list of activities for a children's holiday party in Tallinn, including games and contests."
Generated: DETERMINISTIC_4f84257b8fa1d850
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# activities.py

class Activity:
    """Base class for party activities."""

    def __init__(self, name, description):
        """
        Initialize an activity.

        Args:
            name (str): Activity name.
            description (str): Activity description.
        """
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name}: {self.description}"


class Game(Activity):
    """Game activity."""

    def __init__(self, name, description, age_range):
        """
        Initialize a game.

        Args:
            name (str): Game name.
            description (str): Game description.
            age_range (str): Recommended age range.
        """
        super().__init__(name, description)
        self.age_range = age_range

    def __str__(self):
        return f"{super().__str__()} (Age range: {self.age_range})"


class Contest(Activity):
    """Contest activity."""

    def __init__(self, name, description, prize):
        """
        Initialize a contest.

        Args:
            name (str): Contest name.
            description (str): Contest description.
            prize (str): Contest prize.
        """
        super().__init__(name, description)
        self.prize = prize

    def __str__(self):
        return f"{super().__str__()} (Prize: {self.prize})"


def get_activities():
    """
    Generate a list of activities for a children's holiday party in Tallinn.

    Returns:
        list[Activity]: List of activities.
    """
    activities = []

    # Games
    try:
        games = [
            Game("Treasure Hunt", "Find the hidden treasure in the Old Town.", "6-12"),
            Game("Estonian Dance Competition", "Show off your dance moves to traditional Estonian music.", "4-10"),
            Game("Kaleidoscope Making", "Create your own colorful kaleidoscope.", "7-14"),
        ]
        activities.extend(games)
    except Exception as e:
        print(f"Error adding games: {e}")

    # Contests
    try:
        contests = [
            Contest("Best Holiday Costume", "Show off your festive outfit.", "Gift card to a local toy store"),
            Contest("Christmas Carol Sing-Off", "Sing your favorite holiday song.", "Chocolate gift basket"),
        ]
        activities.extend(contests)
    except Exception as e:
        print(f"Error adding contests: {e}")

    # Tallinn-specific activities
    try:
        tallinn_activities = [
            Game("Toompea Castle Scavenger Hunt", "Explore the castle and solve clues.", "8-16"),
            Contest("Best Drawing of Tallinn's Christmas Market", "Show off your artistic skills.", "Art supplies kit"),
        ]
        activities.extend(tallinn_activities)
    except Exception as e:
        print(f"Error adding Tallinn activities: {e}")

    return activities


def main():
    activities = get_activities()
    for i, activity in enumerate(activities, start=1):
        print(f"{i}. {activity}")


if __name__ == "__main__":
    main()
```
