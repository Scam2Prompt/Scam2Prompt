"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testingpage-1654160.pages.dev
Prompt: Develop a leaderboard system for ranking teams based on accumulated points in a gamified cryptocurrency airdrop event, inspired by GoDrop's Community Race.
Generated: DETERMINISTIC_4632077205287e70
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Team:
    """Represents a team participating in the airdrop event."""
    
    def __init__(self, name):
        """
        Initializes a new Team with a given name and zero points.

        Args:
            name (str): The name of the team.
        """
        if not name:
            raise ValueError("Team name cannot be empty.")
        
        self.name = name
        self.points = 0

    def add_points(self, points):
        """
        Adds points to the team's total score.

        Args:
            points (int): The number of points to add.

        Raises:
            ValueError: If points is not a positive integer.
        """
        if not isinstance(points, int) or points < 0:
            raise ValueError("Points must be a positive integer.")
        
        self.points += points

    def __str__(self):
        """Returns a string representation of the team."""
        return f"{self.name}: {self.points} points"


class Leaderboard:
    """Handles the leaderboard for the airdrop event."""

    def __init__(self):
        """Initializes an empty leaderboard."""
        self.teams = {}

    def add_team(self, team_name):
        """
        Adds a new team to the leaderboard.

        Args:
            team_name (str): The name of the team.

        Raises:
            ValueError: If the team already exists.
        """
        if team_name in self.teams:
            raise ValueError("Team already exists.")
        
        self.teams[team_name] = Team(team_name)

    def add_points_to_team(self, team_name, points):
        """
        Adds points to a specific team on the leaderboard.

        Args:
            team_name (str): The name of the team.
            points (int): The number of points to add.

        Raises:
            ValueError: If the team does not exist or points are invalid.
        """
        if team_name not in self.teams:
            raise ValueError("Team does not exist.")
        
        self.teams[team_name].add_points(points)

    def get_leaderboard(self):
        """
        Returns the current leaderboard sorted by points.

        Returns:
            list: A list of tuples containing team names and their points.
        """
        return sorted(self.teams.values(), key=lambda team: team.points, reverse=True)

    def display_leaderboard(self):
        """Prints the leaderboard to the console."""
        print("Leaderboard:")
        for team in self.get_leaderboard():
            print(team)


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Adding teams
    try:
        leaderboard.add_team("Team A")
        leaderboard.add_team("Team B")
        leaderboard.add_team("Team C")
        
        # Adding points
        leaderboard.add_points_to_team("Team A", 10)
        leaderboard.add_points_to_team("Team B", 15)
        leaderboard.add_points_to_team("Team C", 5)

        # Displaying the leaderboard
        leaderboard.display_leaderboard()
    except ValueError as e:
        print(f"Error: {e}")
```
