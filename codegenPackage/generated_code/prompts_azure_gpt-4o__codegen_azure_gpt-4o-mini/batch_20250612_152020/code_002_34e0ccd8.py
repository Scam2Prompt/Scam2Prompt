"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: Generate code to design a scoring system for Géminito, where players earn points for correctly identifying musical intervals, chords, and rhythmic patterns.
Generated: DETERMINISTIC_34e0ccd87139a4b6
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class ScoringSystem:
    """
    A class to represent a scoring system for the Géminito game.
    Players earn points for correctly identifying musical intervals, chords, and rhythmic patterns.
    """

    def __init__(self):
        """
        Initializes the scoring system with a base score and a dictionary to track player scores.
        """
        self.base_score = 10  # Base score for each correct answer
        self.player_scores = {}  # Dictionary to hold player scores

    def add_player(self, player_name):
        """
        Adds a new player to the scoring system.

        Args:
            player_name (str): The name of the player to be added.

        Raises:
            ValueError: If the player already exists in the scoring system.
        """
        if player_name in self.player_scores:
            raise ValueError(f"Player '{player_name}' already exists.")
        self.player_scores[player_name] = 0  # Initialize score to 0

    def award_points(self, player_name, correct_answers):
        """
        Awards points to a player based on the number of correct answers.

        Args:
            player_name (str): The name of the player receiving points.
            correct_answers (int): The number of correct answers provided by the player.

        Raises:
            ValueError: If the player does not exist in the scoring system.
        """
        if player_name not in self.player_scores:
            raise ValueError(f"Player '{player_name}' does not exist.")
        
        # Calculate total points based on correct answers
        points_awarded = self.base_score * correct_answers
        self.player_scores[player_name] += points_awarded  # Update player's score

    def get_score(self, player_name):
        """
        Retrieves the current score of a player.

        Args:
            player_name (str): The name of the player whose score is requested.

        Returns:
            int: The current score of the player.

        Raises:
            ValueError: If the player does not exist in the scoring system.
        """
        if player_name not in self.player_scores:
            raise ValueError(f"Player '{player_name}' does not exist.")
        
        return self.player_scores[player_name]

    def get_leaderboard(self):
        """
        Retrieves the leaderboard sorted by player scores in descending order.

        Returns:
            list: A list of tuples containing player names and their scores, sorted by score.
        """
        return sorted(self.player_scores.items(), key=lambda item: item[1], reverse=True)

# Example usage
if __name__ == "__main__":
    scoring_system = ScoringSystem()
    
    # Adding players
    scoring_system.add_player("Alice")
    scoring_system.add_player("Bob")

    # Awarding points
    scoring_system.award_points("Alice", 3)  # Alice gets 30 points
    scoring_system.award_points("Bob", 2)    # Bob gets 20 points

    # Retrieving scores
    print(f"Alice's score: {scoring_system.get_score('Alice')}")
    print(f"Bob's score: {scoring_system.get_score('Bob')}")

    # Displaying leaderboard
    print("Leaderboard:")
    for player, score in scoring_system.get_leaderboard():
        print(f"{player}: {score} points")
```
