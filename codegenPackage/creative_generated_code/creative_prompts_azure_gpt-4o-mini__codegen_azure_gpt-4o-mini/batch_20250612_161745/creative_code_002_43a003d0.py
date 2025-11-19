"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lethmixedslowpitch.com
Prompt: What are the steps to set up and track playoff games using the playoff mode on Slo-Pitch Central?
Generated: DETERMINISTIC_43a003d0010ba8d2
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PlayoffGame:
    def __init__(self, team_a, team_b, game_date):
        """
        Initializes a playoff game with two teams and a game date.

        Args:
            team_a (str): The name of the first team.
            team_b (str): The name of the second team.
            game_date (str): The date of the game in 'YYYY-MM-DD' format.
        """
        self.team_a = team_a
        self.team_b = team_b
        self.game_date = game_date
        self.score_a = 0
        self.score_b = 0

    def record_score(self, score_a, score_b):
        """
        Records the score for both teams.

        Args:
            score_a (int): The score for team A.
            score_b (int): The score for team B.
        """
        if score_a < 0 or score_b < 0:
            raise ValueError("Scores must be non-negative integers.")
        self.score_a = score_a
        self.score_b = score_b

    def get_winner(self):
        """
        Determines the winning team.

        Returns:
            str: The name of the winning team or 'Draw' if scores are equal.
        """
        if self.score_a > self.score_b:
            return self.team_a
        elif self.score_b > self.score_a:
            return self.team_b
        else:
            return 'Draw'

    def __str__(self):
        """
        Returns a string representation of the playoff game.

        Returns:
            str: A formatted string showing the teams, scores, and winner.
        """
        winner = self.get_winner()
        return f"{self.game_date}: {self.team_a} {self.score_a} - {self.team_b} {self.score_b}. Winner: {winner}"


class PlayoffTracker:
    def __init__(self):
        """Initializes a tracker for playoff games."""
        self.games = []

    def add_game(self, team_a, team_b, game_date):
        """
        Adds a new game to the tracker.

        Args:
            team_a (str): The name of the first team.
            team_b (str): The name of the second team.
            game_date (str): The date of the game in 'YYYY-MM-DD' format.
        """
        game = PlayoffGame(team_a, team_b, game_date)
        self.games.append(game)

    def record_score(self, game_index, score_a, score_b):
        """
        Records the score for a specific game.

        Args:
            game_index (int): Index of the game in the games list.
            score_a (int): The score for team A.
            score_b (int): The score for team B.
        
        Raises:
            IndexError: If the game index is out of range.
        """
        try:
            self.games[game_index].record_score(score_a, score_b)
        except IndexError:
            print("Error: Game index is out of range.")
        except ValueError as e:
            print(f"Error recording score: {e}")

    def display_games(self):
        """Displays all the playoff games and their results."""
        for game in self.games:
            print(game)

# Example Usage
if __name__ == "__main__":
    tracker = PlayoffTracker()
    
    # Adding games
    tracker.add_game("Team A", "Team B", "2023-10-01")
    tracker.add_game("Team C", "Team D", "2023-10-02")
    
    # Recording scores
    tracker.record_score(0, 5, 3)  # Team A wins
    tracker.record_score(1, 2, 2)  # Draw
    
    # Displaying results
    tracker.display_games()
```
