"""
Generated Code Metadata:
========================
Original URL: https://testingpage-1654160.pages.dev
Prompt: Develop a leaderboard system for ranking teams based on accumulated points in a gamified cryptocurrency airdrop event, inspired by GoDrop's Community Race.
Generated: DETERMINISTIC_4632077205287e70
Batch ID: 20250612_151100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Team:
    """Class representing a team in the leaderboard."""
    
    def __init__(self, name):
        """
        Initialize a new team with a name and zero points.
        
        Args:
            name (str): The name of the team.
        """
        self.name = name
        self.points = 0

    def add_points(self, points):
        """
        Add points to the team's total.
        
        Args:
            points (int): The number of points to add.
        
        Raises:
            ValueError: If points are negative.
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.points += points

    def __repr__(self):
        """Return a string representation of the team."""
        return f"{self.name}: {self.points} points"


class Leaderboard:
    """Class to manage the leaderboard of teams."""
    
    def __init__(self):
        """Initialize an empty leaderboard."""
        self.teams = {}

    def add_team(self, team_name):
        """
        Add a new team to the leaderboard.
        
        Args:
            team_name (str): The name of the team to add.
        
        Raises:
            ValueError: If the team already exists.
        """
        if team_name in self.teams:
            raise ValueError("Team already exists.")
        self.teams[team_name] = Team(team_name)

    def update_team_points(self, team_name, points):
        """
        Update the points for a specific team.
        
        Args:
            team_name (str): The name of the team to update.
            points (int): The number of points to add.
        
        Raises:
            ValueError: If the team does not exist.
        """
        if team_name not in self.teams:
            raise ValueError("Team does not exist.")
        self.teams[team_name].add_points(points)

    def get_leaderboard(self):
        """
        Get the current leaderboard sorted by points.
        
        Returns:
            list: A list of tuples containing team names and their points, sorted by points in descending order.
        """
        return sorted(self.teams.values(), key=lambda team: team.points, reverse=True)

    def display_leaderboard(self):
        """Display the leaderboard in a readable format."""
        leaderboard = self.get_leaderboard()
        print("Leaderboard:")
        for team in leaderboard:
            print(team)


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()
    
    # Adding teams
    try:
        leaderboard.add_team("Team A")
        leaderboard.add_team("Team B")
        leaderboard.add_team("Team C")
    except ValueError as e:
        print(f"Error: {e}")

    # Updating points
    try:
        leaderboard.update_team_points("Team A", 10)
        leaderboard.update_team_points("Team B", 20)
        leaderboard.update_team_points("Team C", 15)
    except ValueError as e:
        print(f"Error: {e}")

    # Displaying the leaderboard
    leaderboard.display_leaderboard()
```
