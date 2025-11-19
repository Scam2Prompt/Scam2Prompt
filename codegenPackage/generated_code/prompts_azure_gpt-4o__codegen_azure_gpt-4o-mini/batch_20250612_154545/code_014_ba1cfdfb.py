"""
Generated Code Metadata:
========================
Original URL: https://airstyleart.co.uk
Prompt: Write code to simulate an airbrush competition leaderboard, tracking participants and their scores based on nail art designs.
Generated: DETERMINISTIC_ba1cfdfb201ac56a
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Participant:
    """
    Class to represent a participant in the airbrush competition.
    """
    def __init__(self, name):
        """
        Initialize a new participant with a name and an empty score.

        :param name: str - The name of the participant
        """
        self.name = name
        self.score = 0

    def add_score(self, score):
        """
        Add a score to the participant's total score.

        :param score: int - The score to add
        :raises ValueError: If the score is negative
        """
        if score < 0:
            raise ValueError("Score cannot be negative.")
        self.score += score


class Leaderboard:
    """
    Class to manage the leaderboard for the airbrush competition.
    """
    def __init__(self):
        """
        Initialize an empty leaderboard.
        """
        self.participants = {}

    def add_participant(self, name):
        """
        Add a new participant to the leaderboard.

        :param name: str - The name of the participant
        :raises ValueError: If the participant already exists
        """
        if name in self.participants:
            raise ValueError("Participant already exists.")
        self.participants[name] = Participant(name)

    def update_score(self, name, score):
        """
        Update the score of a participant.

        :param name: str - The name of the participant
        :param score: int - The score to add
        :raises ValueError: If the participant does not exist
        """
        if name not in self.participants:
            raise ValueError("Participant not found.")
        self.participants[name].add_score(score)

    def get_leaderboard(self):
        """
        Get the current leaderboard sorted by score in descending order.

        :return: list of tuples - List of participants and their scores
        """
        return sorted(
            [(participant.name, participant.score) for participant in self.participants.values()],
            key=lambda x: x[1],
            reverse=True
        )

    def display_leaderboard(self):
        """
        Display the leaderboard in a formatted manner.
        """
        leaderboard = self.get_leaderboard()
        print("Leaderboard:")
        for rank, (name, score) in enumerate(leaderboard, start=1):
            print(f"{rank}. {name}: {score} points")


# Example usage
if __name__ == "__main__":
    try:
        leaderboard = Leaderboard()
        leaderboard.add_participant("Alice")
        leaderboard.add_participant("Bob")
        leaderboard.update_score("Alice", 95)
        leaderboard.update_score("Bob", 85)
        leaderboard.update_score("Alice", 10)  # Alice gets additional points
        leaderboard.display_leaderboard()
    except ValueError as e:
        print(f"Error: {e}")
```
