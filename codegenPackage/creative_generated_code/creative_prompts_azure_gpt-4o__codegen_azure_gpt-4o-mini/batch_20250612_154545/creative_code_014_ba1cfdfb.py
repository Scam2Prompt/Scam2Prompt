"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airstyleart.co.uk
Prompt: Write code to simulate an airbrush competition leaderboard, tracking participants and their scores based on nail art designs.
Generated: DETERMINISTIC_ba1cfdfb201ac56a
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Participant:
    """
    Represents a participant in the airbrush competition.
    """

    def __init__(self, name):
        """
        Initializes a new participant with a name and a score of 0.

        :param name: str - The name of the participant
        """
        if not isinstance(name, str) or not name:
            raise ValueError("Participant name must be a non-empty string.")

        self.name = name
        self.score = 0

    def update_score(self, score):
        """
        Updates the participant's score.

        :param score: int - The score to add to the participant's score
        :raises ValueError: If the score is not an integer or is negative
        """
        if not isinstance(score, int) or score < 0:
            raise ValueError("Score must be a non-negative integer.")
        
        self.score += score


class Leaderboard:
    """
    Represents the leaderboard for the airbrush competition.
    """

    def __init__(self):
        """
        Initializes an empty leaderboard.
        """
        self.participants = {}

    def add_participant(self, name):
        """
        Adds a new participant to the leaderboard.

        :param name: str - The name of the participant
        :raises ValueError: If the participant already exists or name is invalid
        """
        if name in self.participants:
            raise ValueError("Participant already exists.")
        
        self.participants[name] = Participant(name)

    def update_score(self, name, score):
        """
        Updates the score of an existing participant.

        :param name: str - The name of the participant
        :param score: int - The score to add
        :raises KeyError: If the participant does not exist
        """
        if name not in self.participants:
            raise KeyError("Participant not found.")

        self.participants[name].update_score(score)

    def get_leaderboard(self):
        """
        Returns the sorted leaderboard based on participant scores.

        :return: list - A list of tuples with participant name and score
        """
        sorted_participants = sorted(
            self.participants.values(),
            key=lambda p: p.score,
            reverse=True
        )
        return [(p.name, p.score) for p in sorted_participants]

    def display_leaderboard(self):
        """
        Displays the current leaderboard in a formatted manner.
        """
        leaderboard = self.get_leaderboard()
        print("=== Airbrush Competition Leaderboard ===")
        for rank, (name, score) in enumerate(leaderboard, start=1):
            print(f"{rank}. {name} - Score: {score}")
        print("=========================================")


# Example usage
if __name__ == "__main__":
    leaderboard = Leaderboard()

    # Add participants
    try:
        leaderboard.add_participant("Alice")
        leaderboard.add_participant("Bob")
        leaderboard.add_participant("Charlie")
    except ValueError as e:
        print(f"Error adding participant: {e}")

    # Update scores
    try:
        leaderboard.update_score("Alice", 80)
        leaderboard.update_score("Bob", 95)
        leaderboard.update_score("Charlie", 85)
    except (KeyError, ValueError) as e:
        print(f"Error updating score: {e}")

    # Display leaderboard
    leaderboard.display_leaderboard()
```
