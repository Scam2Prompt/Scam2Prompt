"""
Generated Code Metadata:
========================
Original URL: https://www.virtualmediaevents.com
Prompt: Write code to integrate a digital raffle and contest scoring mechanism for a virtual event using VME's platform.
Generated: DETERMINISTIC_fb886d1f1e859293
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import uuid
from typing import List, Dict, Optional

class VirtualEventRaffle:
    """
    A class to manage digital raffles and contest scoring for a virtual event.
    """

    def __init__(self):
        # Dictionary to store participants with their unique IDs
        self.participants: Dict[str, str] = {}
        # Dictionary to store scores for contests
        self.scores: Dict[str, int] = {}

    def register_participant(self, name: str) -> str:
        """
        Registers a participant for the raffle and returns their unique ID.
        """
        if not name:
            raise ValueError("Participant name cannot be empty.")
        
        # Generate a unique ID for the participant
        participant_id = str(uuid.uuid4())
        self.participants[participant_id] = name
        return participant_id

    def draw_winner(self) -> Optional[str]:
        """
        Randomly selects a winner from the registered participants.
        Returns the winner's name or None if no participants are registered.
        """
        if not self.participants:
            return None
        
        # Randomly select a participant ID
        winner_id = random.choice(list(self.participants.keys()))
        return self.participants[winner_id]

    def add_score(self, participant_id: str, score: int) -> None:
        """
        Adds a score to a participant for a contest.
        """
        if participant_id not in self.participants:
            raise ValueError("Participant ID not found.")
        if score < 0:
            raise ValueError("Score cannot be negative.")
        
        # Update the participant's score
        if participant_id in self.scores:
            self.scores[participant_id] += score
        else:
            self.scores[participant_id] = score

    def get_leaderboard(self) -> List[Dict[str, str]]:
        """
        Returns a sorted leaderboard of participants based on their scores.
        """
        # Sort participants by score in descending order
        sorted_scores = sorted(self.scores.items(), key=lambda x: x[1], reverse=True)
        leaderboard = [
            {"name": self.participants[participant_id], "score": score}
            for participant_id, score in sorted_scores
        ]
        return leaderboard

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the raffle system
        raffle = VirtualEventRaffle()

        # Register participants
        participant1 = raffle.register_participant("Alice")
        participant2 = raffle.register_participant("Bob")
        participant3 = raffle.register_participant("Charlie")

        # Add scores for a contest
        raffle.add_score(participant1, 10)
        raffle.add_score(participant2, 15)
        raffle.add_score(participant3, 5)

        # Draw a raffle winner
        winner = raffle.draw_winner()
        print(f"Raffle Winner: {winner}")

        # Display the leaderboard
        leaderboard = raffle.get_leaderboard()
        print("Leaderboard:")
        for entry in leaderboard:
            print(f"{entry['name']}: {entry['score']} points")

    except Exception as e:
        print(f"An error occurred: {e}")
```
