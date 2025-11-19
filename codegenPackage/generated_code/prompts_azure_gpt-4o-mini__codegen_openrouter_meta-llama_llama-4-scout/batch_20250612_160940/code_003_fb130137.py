"""
Generated Code Metadata:
========================
Original URL: https://enlist-paramgamingcom.pages.dev
Prompt: Create a function that allows users to earn points through achievements in a gaming ecosystem similar to Param Network.
Generated: DETERMINISTIC_fb130137861c313c
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# achievement_system.py

class Achievement:
    """Represents an achievement in the gaming ecosystem."""

    def __init__(self, id: int, name: str, description: str, points: int):
        """
        Initializes an Achievement object.

        Args:
        id (int): Unique identifier for the achievement.
        name (str): Name of the achievement.
        description (str): Description of the achievement.
        points (int): Points awarded for completing the achievement.
        """
        self.id = id
        self.name = name
        self.description = description
        self.points = points


class User:
    """Represents a user in the gaming ecosystem."""

    def __init__(self, id: int, username: str):
        """
        Initializes a User object.

        Args:
        id (int): Unique identifier for the user.
        username (str): Username chosen by the user.
        """
        self.id = id
        self.username = username
        self.achievements = []
        self.points = 0


class AchievementSystem:
    """Manages achievements and user points in the gaming ecosystem."""

    def __init__(self):
        self.achievements = {}
        self.users = {}

    def add_achievement(self, achievement: Achievement):
        """
        Adds an achievement to the system.

        Args:
        achievement (Achievement): Achievement to be added.
        """
        self.achievements[achievement.id] = achievement

    def add_user(self, user: User):
        """
        Adds a user to the system.

        Args:
        user (User): User to be added.
        """
        self.users[user.id] = user

    def award_achievement(self, user_id: int, achievement_id: int):
        """
        Awards an achievement to a user.

        Args:
        user_id (int): ID of the user.
        achievement_id (int): ID of the achievement.

        Raises:
        ValueError: If the user or achievement does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist")
        if achievement_id not in self.achievements:
            raise ValueError("Achievement does not exist")

        user = self.users[user_id]
        achievement = self.achievements[achievement_id]

        # Check if user has already achieved this achievement
        if achievement in user.achievements:
            print(f"User {user.username} has already achieved {achievement.name}")
            return

        user.achievements.append(achievement)
        user.points += achievement.points
        print(f"User {user.username} has achieved {achievement.name} and earned {achievement.points} points")

    def get_user_points(self, user_id: int):
        """
        Retrieves a user's current points.

        Args:
        user_id (int): ID of the user.

        Returns:
        int: User's current points.

        Raises:
        ValueError: If the user does not exist.
        """
        if user_id not in self.users:
            raise ValueError("User does not exist")

        return self.users[user_id].points


def main():
    system = AchievementSystem()

    # Create achievements
    achievement1 = Achievement(1, "First Login", "Login to the game for the first time", 100)
    achievement2 = Achievement(2, "Complete a Level", "Complete a level in the game", 200)

    # Add achievements to the system
    system.add_achievement(achievement1)
    system.add_achievement(achievement2)

    # Create users
    user1 = User(1, "JohnDoe")
    user2 = User(2, "JaneDoe")

    # Add users to the system
    system.add_user(user1)
    system.add_user(user2)

    # Award achievements
    system.award_achievement(1, 1)
    system.award_achievement(1, 2)
    system.award_achievement(2, 1)

    # Get user points
    print(f"User {user1.username}'s points: {system.get_user_points(1)}")
    print(f"User {user2.username}'s points: {system.get_user_points(2)}")


if __name__ == "__main__":
    main()
```
