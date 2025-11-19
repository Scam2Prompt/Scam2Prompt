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
# géminito_scoring_system.py

class MusicalElement:
    """Base class for musical elements."""
    def __init__(self, correct_answer):
        """
        Initialize a musical element.

        Args:
            correct_answer (str): The correct answer for the musical element.
        """
        self.correct_answer = correct_answer

class Interval(MusicalElement):
    """Represents a musical interval."""
    def __init__(self, correct_answer, player_answer):
        """
        Initialize an interval.

        Args:
            correct_answer (str): The correct answer for the interval.
            player_answer (str): The player's answer for the interval.
        """
        super().__init__(correct_answer)
        self.player_answer = player_answer

    def score(self):
        """
        Calculate the score for the interval.

        Returns:
            int: 1 if the player's answer is correct, 0 otherwise.
        """
        if self.player_answer == self.correct_answer:
            return 1
        else:
            return 0

class Chord(MusicalElement):
    """Represents a musical chord."""
    def __init__(self, correct_answer, player_answer):
        """
        Initialize a chord.

        Args:
            correct_answer (str): The correct answer for the chord.
            player_answer (str): The player's answer for the chord.
        """
        super().__init__(correct_answer)
        self.player_answer = player_answer

    def score(self):
        """
        Calculate the score for the chord.

        Returns:
            int: 1 if the player's answer is correct, 0 otherwise.
        """
        if self.player_answer == self.correct_answer:
            return 1
        else:
            return 0

class RhythmicPattern(MusicalElement):
    """Represents a rhythmic pattern."""
    def __init__(self, correct_answer, player_answer):
        """
        Initialize a rhythmic pattern.

        Args:
            correct_answer (str): The correct answer for the rhythmic pattern.
            player_answer (str): The player's answer for the rhythmic pattern.
        """
        super().__init__(correct_answer)
        self.player_answer = player_answer

    def score(self):
        """
        Calculate the score for the rhythmic pattern.

        Returns:
            int: 1 if the player's answer is correct, 0 otherwise.
        """
        if self.player_answer == self.correct_answer:
            return 1
        else:
            return 0

class GéminitoScoringSystem:
    """Manages the scoring system for Géminito."""
    def __init__(self):
        """
        Initialize the scoring system.
        """
        self.score = 0
        self.total_questions = 0

    def add_interval(self, interval):
        """
        Add an interval to the scoring system.

        Args:
            interval (Interval): The interval to add.
        """
        self.total_questions += 1
        self.score += interval.score()

    def add_chord(self, chord):
        """
        Add a chord to the scoring system.

        Args:
            chord (Chord): The chord to add.
        """
        self.total_questions += 1
        self.score += chord.score()

    def add_rhythmic_pattern(self, rhythmic_pattern):
        """
        Add a rhythmic pattern to the scoring system.

        Args:
            rhythmic_pattern (RhythmicPattern): The rhythmic pattern to add.
        """
        self.total_questions += 1
        self.score += rhythmic_pattern.score()

    def get_score(self):
        """
        Get the current score.

        Returns:
            float: The current score as a percentage.
        """
        if self.total_questions == 0:
            return 0.0
        else:
            return (self.score / self.total_questions) * 100

def main():
    # Example usage:
    scoring_system = GéminitoScoringSystem()

    interval = Interval("C4", "C4")
    scoring_system.add_interval(interval)

    chord = Chord("C Major", "C Major")
    scoring_system.add_chord(chord)

    rhythmic_pattern = RhythmicPattern("4/4", "4/4")
    scoring_system.add_rhythmic_pattern(rhythmic_pattern)

    print(f"Score: {scoring_system.get_score()}%")

if __name__ == "__main__":
    main()
```
