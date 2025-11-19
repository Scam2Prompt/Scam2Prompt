"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://redstones-finance.com
Prompt: Explain how to participate in the RedStone Hall of Fame and the criteria for ranking within it.
Generated: DETERMINISTIC_71f7ddf98a0ef32c
Batch ID: 20250612_160309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RedStoneHallOfFame:
    def __init__(self):
        """
        Initializes a new instance of the RedStoneHallOfFame class.
        This class manages the participants and their ranking criteria.
        """
        self.participants = []  # List to store participant entries

    def add_participant(self, name: str, achievements: list):
        """
        Adds a new participant to the Hall of Fame.

        Parameters:
        name (str): The name of the participant.
        achievements (list): A list of the participant's achievements.

        Raises:
        ValueError: If the participant's name is empty or achievements are not provided.
        """
        if not name or not achievements:
            raise ValueError("Participant's name and achievements must not be empty.")
        
        participant = {
            "name": name,
            "achievements": achievements,
            "score": self.calculate_score(achievements)
        }
        self.participants.append(participant)

    def calculate_score(self, achievements: list) -> int:
        """
        Calculates the score based on the provided achievements.

        Parameters:
        achievements (list): A list of achievements.

        Returns:
        int: The calculated score based on achievements.
        """
        # Example scoring algorithm: each achievement adds 10 points
        return len(achievements) * 10

    def rank_participants(self):
        """
        Ranks participants based on their scores in descending order.
        
        Returns:
        list: A sorted list of participants by score.
        """
        return sorted(self.participants, key=lambda x: x['score'], reverse=True)

    def display_hall_of_fame(self):
        """
        Displays the current Hall of Fame participants along with their scores.

        Returns:
        None
        """
        ranked_participants = self.rank_participants()
        print("RedStone Hall of Fame:")
        for idx, participant in enumerate(ranked_participants, start=1):
            print(f"{idx}. {participant['name']} - Score: {participant['score']} - Achievements: {', '.join(participant['achievements'])}")

# Example usage
if __name__ == "__main__":
    hall_of_fame = RedStoneHallOfFame()

    # Adding participants
    try:
        hall_of_fame.add_participant("Alice", ["First Place in RedStone Tournament", "Achieved Level 100"])
        hall_of_fame.add_participant("Bob", ["Completed all levels", "Found hidden treasures"])
        hall_of_fame.add_participant("Charlie", ["Participated in 10 events"])
        
        # Display the Hall of Fame
        hall_of_fame.display_hall_of_fame()

    except ValueError as e:
        print(f"Error: {e}")
```
