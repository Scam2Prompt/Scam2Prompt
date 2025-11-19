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
import random
from dataclasses import dataclass
from typing import List, Dict, Optional
from enum import Enum, auto


class JudgingCriteria(Enum):
    """Enum representing the criteria for judging the nail art designs."""
    CREATIVITY = auto()
    TECHNIQUE = auto()
    COLOR_USAGE = auto()
    OVERALL_IMPACT = auto()


@dataclass
class Participant:
    """Class representing a participant in the competition."""
    id: int
    name: str
    age: int
    country: str


@dataclass
class Score:
    """Class representing a score for a participant's design."""
    participant_id: int
    creativity: int
    technique: int
    color_usage: int
    overall_impact: int

    @property
    def total_score(self) -> int:
        """Calculate the total score from all criteria."""
        return self.creativity + self.technique + self.color_usage + self.overall_impact


class Leaderboard:
    """Class representing the competition leaderboard."""
    
    def __init__(self):
        self.participants: Dict[int, Participant] = {}
        self.scores: Dict[int, Score] = {}
    
    def add_participant(self, participant: Participant) -> None:
        """Add a participant to the competition."""
        if participant.id in self.participants:
            raise ValueError(f"Participant with ID {participant.id} already exists")
        self.participants[participant.id] = participant
    
    def remove_participant(self, participant_id: int) -> None:
        """Remove a participant from the competition."""
        if participant_id not in self.participants:
            raise ValueError(f"Participant with ID {participant_id} not found")
        del self.participants[participant_id]
        if participant_id in self.scores:
            del self.scores[participant_id]
    
    def add_score(self, score: Score) -> None:
        """Add a score for a participant's design."""
        if score.participant_id not in self.participants:
            raise ValueError(f"Participant with ID {score.participant_id} not found")
        self.scores[score.participant_id] = score
    
    def get_participant_score(self, participant_id: int) -> Optional[Score]:
        """Get the score for a participant."""
        return self.scores.get(participant_id)
    
    def get_leaderboard(self) -> List[Dict]:
        """Get the current leaderboard sorted by total score."""
        leaderboard = []
        for participant_id, score in self.scores.items():
            participant = self.participants[participant_id]
            leaderboard.append({
                "id": participant.id,
                "name": participant.name,
                "country": participant.country,
                "total_score": score.total_score,
                "creativity": score.creativity,
                "technique": score.technique,
                "color_usage": score.color_usage,
                "overall_impact": score.overall_impact
            })
        
        # Sort by total score in descending order
        leaderboard.sort(key=lambda x: x["total_score"], reverse=True)
        return leaderboard
    
    def generate_random_scores(self) -> None:
        """Generate random scores for all participants (for simulation purposes)."""
        for participant_id in self.participants:
            self.scores[participant_id] = Score(
                participant_id=participant_id,
                creativity=random.randint(1, 10),
                technique=random.randint(1, 10),
                color_usage=random.randint(1, 10),
                overall_impact=random.randint(1, 10)
            )


# Example usage
if __name__ == "__main__":
    # Create leaderboard
    leaderboard = Leaderboard()

    # Add participants
    participants = [
        Participant(1, "Alice", 25, "USA"),
        Participant(2, "Bob", 30, "Canada"),
        Participant(3, "Charlie", 22, "UK"),
        Participant(4, "Diana", 28, "Australia"),
    ]

    for participant in participants:
        leaderboard.add_participant(participant)

    # Generate random scores
    leaderboard.generate_random_scores()

    # Display leaderboard
    print("Current Leaderboard:")
    print("Rank | ID | Name     | Country   | Total Score")
    print("----------------------------------------------")
    for rank, entry in enumerate(leaderboard.get_leaderboard(), start=1):
        print(f"{rank:4} | {entry['id']:2} | {entry['name']:8} | {entry['country']:9} | {entry['total_score']:11}")
```
