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
# airbrush_competition_leaderboard.py

class Participant:
    """Represents a participant in the airbrush competition."""

    def __init__(self, name):
        """
        Initializes a participant with a name and an empty list of scores.

        Args:
            name (str): The participant's name.
        """
        self.name = name
        self.scores = []

    def add_score(self, score):
        """
        Adds a score to the participant's list of scores.

        Args:
            score (int): The score to add.

        Raises:
            ValueError: If the score is not a non-negative integer.
        """
        if not isinstance(score, int) or score < 0:
            raise ValueError("Score must be a non-negative integer")
        self.scores.append(score)

    def get_average_score(self):
        """
        Calculates the participant's average score.

        Returns:
            float: The participant's average score.
        """
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)


class AirbrushCompetitionLeaderboard:
    """Represents the leaderboard for the airbrush competition."""

    def __init__(self):
        """Initializes an empty leaderboard."""
        self.participants = {}

    def add_participant(self, name):
        """
        Adds a participant to the leaderboard.

        Args:
            name (str): The participant's name.

        Raises:
            ValueError: If a participant with the same name already exists.
        """
        if name in self.participants:
            raise ValueError("Participant with the same name already exists")
        self.participants[name] = Participant(name)

    def add_score(self, name, score):
        """
        Adds a score to a participant's list of scores.

        Args:
            name (str): The participant's name.
            score (int): The score to add.

        Raises:
            ValueError: If the participant does not exist.
        """
        if name not in self.participants:
            raise ValueError("Participant does not exist")
        self.participants[name].add_score(score)

    def get_leaderboard(self):
        """
        Generates the leaderboard.

        Returns:
            list: A list of tuples containing the participant's name and average score.
        """
        leaderboard = []
        for participant in self.participants.values():
            average_score = participant.get_average_score()
            leaderboard.append((participant.name, average_score))
        leaderboard.sort(key=lambda x: x[1], reverse=True)
        return leaderboard


def main():
    leaderboard = AirbrushCompetitionLeaderboard()

    while True:
        print("\nAirbrush Competition Leaderboard")
        print("1. Add participant")
        print("2. Add score")
        print("3. View leaderboard")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter participant's name: ")
            try:
                leaderboard.add_participant(name)
                print(f"Participant '{name}' added successfully.")
            except ValueError as e:
                print(str(e))
        elif choice == "2":
            name = input("Enter participant's name: ")
            try:
                score = int(input("Enter score: "))
                leaderboard.add_score(name, score)
                print(f"Score added successfully for '{name}'.")
            except ValueError as e:
                print(str(e))
        elif choice == "3":
            leaderboard_data = leaderboard.get_leaderboard()
            print("\nLeaderboard:")
            for i, (name, average_score) in enumerate(leaderboard_data, start=1):
                print(f"{i}. {name}: {average_score:.2f}")
        elif choice == "4":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
