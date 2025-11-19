"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aceprogaming.co.ke
Prompt: Generate a code snippet for a tournament management system that includes features for organizing and sponsoring esports events, as described by Ace Pro Sports Technologies.
Generated: DETERMINISTIC_2989844a027bfe45
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime

class Tournament:
    """
    A class to represent an esports tournament.
    Attributes:
        name (str): Name of the tournament.
        game (str): Game being played in the tournament.
        start_date (datetime.datetime): Start date of the tournament.
        end_date (datetime.datetime): End date of the tournament.
        sponsor (str): Sponsor of the tournament.
        teams (list): List of teams participating in the tournament.
    """

    def __init__(self, name, game, start_date, end_date, sponsor):
        """
        Constructor for the Tournament class.
        :param name: Name of the tournament.
        :param game: Game being played in the tournament.
        :param start_date: Start date of the tournament (YYYY-MM-DD format).
        :param end_date: End date of the tournament (YYYY-MM-DD format).
        :param sponsor: Sponsor of the tournament.
        """
        self.name = name
        self.game = game
        self.start_date = self._parse_date(start_date)
        self.end_date = self._parse_date(end_date)
        self.sponsor = sponsor
        self.teams = []

    @staticmethod
    def _parse_date(date_string):
        """
        Helper method to parse a date string into a datetime object.
        :param date_string: Date in YYYY-MM-DD format.
        :return: Parsed datetime object.
        :raises: ValueError if the date format is invalid.
        """
        try:
            return datetime.datetime.strptime(date_string, '%Y-%m-%d')
        except ValueError as e:
            raise ValueError(f"Invalid date format: {date_string}. Expected YYYY-MM-DD.") from e

    def add_team(self, team_name):
        """
        Adds a team to the tournament.
        :param team_name: Name of the team to add.
        """
        if team_name not in self.teams:
            self.teams.append(team_name)
        else:
            print(f"Team {team_name} is already participating in the tournament.")

    def remove_team(self, team_name):
        """
        Removes a team from the tournament.
        :param team_name: Name of the team to remove.
        """
        try:
            self.teams.remove(team_name)
        except ValueError:
            print(f"Team {team_name} is not participating in the tournament.")

    def display_details(self):
        """
        Displays tournament details, including teams and sponsor information.
        """
        print(f"Tournament Name: {self.name}")
        print(f"Game: {self.game}")
        print(f"Start Date: {self.start_date.strftime('%Y-%m-%d')}")
        print(f"End Date: {self.end_date.strftime('%Y-%m-%d')}")
        print(f"Sponsor: {self.sponsor}")
        print("Participating Teams:")
        for team in self.teams:
            print(f"- {team}")


# Example usage:
if __name__ == "__main__":
    try:
        # Create a tournament instance
        tournament = Tournament(
            name="Ace Pro Championship",
            game="Valorant",
            start_date="2023-12-01",
            end_date="2023-12-05",
            sponsor="Ace Pro Sports Technologies"
        )

        # Add teams
        tournament.add_team("Team Alpha")
        tournament.add_team("Team Beta")

        # Display tournament details
        tournament.display_details()

        # Remove a team
        tournament.remove_team("Team Alpha")

        # Display updated tournament details
        tournament.display_details()

    except Exception as e:
        print(f"An error occurred: {e}")
```
