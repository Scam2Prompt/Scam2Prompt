"""
Generated Code Metadata:
========================
Original URL: https://masterclicsolutions.com
Prompt: How can I implement gamification techniques in an e-learning course to enhance engagement, based on the recommendations from MasterClic Solutions?
Generated: DETERMINISTIC_f71eb8d7d913a967
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class GamificationElement:
    """Base class for gamification elements in the e-learning course."""
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display(self):
        """Display the gamification element."""
        return f"{self.name}: {self.description}"


class Badge(GamificationElement):
    """Class representing a badge that can be earned by users."""
    
    def __init__(self, name, description, criteria):
        super().__init__(name, description)
        self.criteria = criteria

    def check_criteria(self, user):
        """Check if the user meets the criteria to earn the badge."""
        return user.points >= self.criteria


class Leaderboard:
    """Class to manage the leaderboard for users."""
    
    def __init__(self):
        self.scores = {}

    def update_score(self, user, points):
        """Update the user's score in the leaderboard."""
        if user.name in self.scores:
            self.scores[user.name] += points
        else:
            self.scores[user.name] = points

    def get_leaderboard(self):
        """Return the leaderboard sorted by scores."""
        return sorted(self.scores.items(), key=lambda x: x[1], reverse=True)


class User:
    """Class representing a user in the e-learning course."""
    
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.badges = []

    def earn_points(self, points):
        """Add points to the user's score."""
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.points += points

    def earn_badge(self, badge):
        """Award a badge to the user if criteria are met."""
        if badge.check_criteria(self):
            self.badges.append(badge)
            return f"{self.name} earned the badge: {badge.name}"
        return f"{self.name} did not meet the criteria for the badge: {badge.name}"


def main():
    """Main function to demonstrate gamification in an e-learning course."""
    # Create users
    user1 = User("Alice")
    user2 = User("Bob")

    # Create badges
    badge1 = Badge("Completionist", "Awarded for completing all modules.", criteria=100)
    badge2 = Badge("Top Scorer", "Awarded for being in the top 10% of scores.", criteria=200)

    # Create leaderboard
    leaderboard = Leaderboard()

    # Simulate user earning points
    try:
        user1.earn_points(120)
        user2.earn_points(80)

        # Update leaderboard
        leaderboard.update_score(user1, user1.points)
        leaderboard.update_score(user2, user2.points)

        # Check for badges
        print(user1.earn_badge(badge1))
        print(user2.earn_badge(badge1))

        # Display leaderboard
        print("Leaderboard:")
        for name, score in leaderboard.get_leaderboard():
            print(f"{name}: {score} points")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
