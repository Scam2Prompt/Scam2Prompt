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
"""
Géminito Scoring System

This module implements a scoring system for the Géminito game where players earn points
for correctly identifying musical intervals, chords, and rhythmic patterns.
"""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

class DifficultyLevel(Enum):
    """Difficulty levels for game challenges."""
    EASY = auto()
    MEDIUM = auto()
    HARD = auto()
    EXPERT = auto()

class ChallengeType(Enum):
    """Types of musical challenges."""
    INTERVAL = auto()
    CHORD = auto()
    RHYTHM = auto()

@dataclass
class Challenge:
    """Represents a musical challenge."""
    challenge_type: ChallengeType
    difficulty: DifficultyLevel
    description: str
    correct_answer: str

class ScoringSystem:
    """Handles scoring calculations for Géminito game."""
    
    # Base points for each challenge type
    BASE_POINTS = {
        ChallengeType.INTERVAL: {
            DifficultyLevel.EASY: 10,
            DifficultyLevel.MEDIUM: 20,
            DifficultyLevel.HARD: 30,
            DifficultyLevel.EXPERT: 50
        },
        ChallengeType.CHORD: {
            DifficultyLevel.EASY: 15,
            DifficultyLevel.MEDIUM: 25,
            DifficultyLevel.HARD: 40,
            DifficultyLevel.EXPERT: 60
        },
        ChallengeType.RHYTHM: {
            DifficultyLevel.EASY: 12,
            DifficultyLevel.MEDIUM: 22,
            DifficultyLevel.HARD: 35,
            DifficultyLevel.EXPERT: 55
        }
    }
    
    # Multipliers for consecutive correct answers
    STREAK_MULTIPLIERS = [1.0, 1.1, 1.25, 1.5, 2.0]
    
    def __init__(self):
        self.total_score = 0
        self.current_streak = 0
        self.highest_streak = 0
    
    def calculate_points(self, challenge: Challenge, is_correct: bool, time_taken: float) -> int:
        """
        Calculate points earned for a challenge attempt.
        
        Args:
            challenge: The challenge attempted
            is_correct: Whether the answer was correct
            time_taken: Time taken to answer in seconds
            
        Returns:
            Points earned (0 if incorrect)
        """
        if not is_correct:
            self.current_streak = 0
            return 0
        
        # Get base points for this challenge
        base_points = self.BASE_POINTS[challenge.challenge_type][challenge.difficulty]
        
        # Apply streak multiplier
        streak_multiplier = self.STREAK_MULTIPLIERS[
            min(self.current_streak, len(self.STREAK_MULTIPLIERS) - 1)
        ]
        
        # Time bonus (faster answers get more points)
        max_time = 10.0  # seconds
        time_factor = max(0.5, 1.0 - (min(time_taken, max_time) / max_time))
        
        # Calculate final points
        points = int(base_points * streak_multiplier * time_factor)
        
        # Update streaks and total score
        self.current_streak += 1
        self.highest_streak = max(self.highest_streak, self.current_streak)
        self.total_score += points
        
        return points
    
    def get_total_score(self) -> int:
        """Return the player's total score."""
        return self.total_score
    
    def get_current_streak(self) -> int:
        """Return the current streak of correct answers."""
        return self.current_streak
    
    def get_highest_streak(self) -> int:
        """Return the highest streak achieved."""
        return self.highest_streak
    
    def reset(self) -> None:
        """Reset the scoring system for a new game."""
        self.total_score = 0
        self.current_streak = 0
        self.highest_streak = 0

# Example usage
if __name__ == "__main__":
    scoring = ScoringSystem()
    
    # Sample challenges
    interval_challenge = Challenge(
        challenge_type=ChallengeType.INTERVAL,
        difficulty=DifficultyLevel.MEDIUM,
        description="Identify the interval between C4 and E4",
        correct_answer="Major Third"
    )
    
    chord_challenge = Challenge(
        challenge_type=ChallengeType.CHORD,
        difficulty=DifficultyLevel.HARD,
        description="Identify the chord: C-E-G-Bb",
        correct_answer="Dominant 7th"
    )
    
    # Player attempts
    points1 = scoring.calculate_points(interval_challenge, True, 3.5)
    print(f"Earned {points1} points for correct interval identification")
    
    points2 = scoring.calculate_points(chord_challenge, True, 7.2)
    print(f"Earned {points2} points for correct chord identification")
    
    print(f"Total score: {scoring.get_total_score()}")
    print(f"Current streak: {scoring.get_current_streak()}")
    print(f"Highest streak: {scoring.get_highest_streak()}")
```
