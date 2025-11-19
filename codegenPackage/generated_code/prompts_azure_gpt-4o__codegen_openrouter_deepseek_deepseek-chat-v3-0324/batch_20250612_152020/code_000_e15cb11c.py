"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: Write Python code to simulate the gameplay mechanics of Géminito, including rules for recognizing notes, intervals, and chords as described on the website.
Generated: DETERMINISTIC_e15cb11c80b92103
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import List, Dict, Tuple, Optional

class Note(Enum):
    C = 0
    C_SHARP = 1
    D = 2
    D_SHARP = 3
    E = 4
    F = 5
    F_SHARP = 6
    G = 7
    G_SHARP = 8
    A = 9
    A_SHARP = 10
    B = 11

    def __str__(self):
        return self.name.replace('_SHARP', '#')

class IntervalType(Enum):
    UNISON = 0
    MINOR_SECOND = 1
    MAJOR_SECOND = 2
    MINOR_THIRD = 3
    MAJOR_THIRD = 4
    PERFECT_FOURTH = 5
    TRITONE = 6
    PERFECT_FIFTH = 7
    MINOR_SIXTH = 8
    MAJOR_SIXTH = 9
    MINOR_SEVENTH = 10
    MAJOR_SEVENTH = 11
    OCTAVE = 12

    def __str__(self):
        return self.name.replace('_', ' ').title()

class ChordType(Enum):
    MAJOR = [IntervalType.MAJOR_THIRD, IntervalType.PERFECT_FIFTH]
    MINOR = [IntervalType.MINOR_THIRD, IntervalType.PERFECT_FIFTH]
    DIMINISHED = [IntervalType.MINOR_THIRD, IntervalType.TRITONE]
    AUGMENTED = [IntervalType.MAJOR_THIRD, IntervalType.MINOR_SIXTH]
    MAJOR_SEVENTH = [IntervalType.MAJOR_THIRD, IntervalType.PERFECT_FIFTH, IntervalType.MAJOR_SEVENTH]
    MINOR_SEVENTH = [IntervalType.MINOR_THIRD, IntervalType.PERFECT_FIFTH, IntervalType.MINOR_SEVENTH]
    DOMINANT_SEVENTH = [IntervalType.MAJOR_THIRD, IntervalType.PERFECT_FIFTH, IntervalType.MINOR_SEVENTH]

    def __str__(self):
        return self.name.replace('_', ' ').title()

class GameMode(Enum):
    NOTES = 1
    INTERVALS = 2
    CHORDS = 3

class GeminitoGame:
    def __init__(self):
        self.score = 0
        self.current_question = None
        self.current_answer = None
        self.mode = GameMode.NOTES
        self.note_names = [note for note in Note]
        self.interval_types = [interval for interval in IntervalType if interval != IntervalType.UNISON]
        self.chord_types = [chord for chord in ChordType]

    def set_mode(self, mode: GameMode):
        self.mode = mode

    def generate_question(self) -> Tuple[str, str]:
        if self.mode == GameMode.NOTES:
            note = random.choice(self.note_names)
            self.current_question = f"Identify this note: {note}"
            self.current_answer = str(note)
            return (self.current_question, self.current_answer)

        elif self.mode == GameMode.INTERVALS:
            root = random.choice(self.note_names)
            interval_type = random.choice(self.interval_types)
            top_note = Note((root.value + interval_type.value) % 12)
            
            self.current_question = f"Identify the interval between {root} and {top_note}"
            self.current_answer = str(interval_type)
            return (self.current_question, self.current_answer)

        elif self.mode == GameMode.CHORDS:
            root = random.choice(self.note_names)
            chord_type = random.choice(self.chord_types)
            chord_notes = [root]
            
            for interval in chord_type.value:
                next_note = Note((root.value + interval.value) % 12)
                chord_notes.append(next_note)
            
            self.current_question = f"Identify the chord: {' '.join(str(n) for n in chord_notes)}"
            self.current_answer = str(chord_type)
            return (self.current_question, self.current_answer)

        else:
            raise ValueError("Invalid game mode")

    def check_answer(self, user_answer: str) -> bool:
        if not self.current_question or not self.current_answer:
            raise ValueError("No question generated yet")
        
        is_correct = user_answer.upper() == self.current_answer.upper()
        if is_correct:
            self.score += 1
        return is_correct

    def get_score(self) -> int:
        return self.score

    def reset_score(self):
        self.score = 0

# Example usage
if __name__ == "__main__":
    game = GeminitoGame()
    game.set_mode(GameMode.INTERVALS)
    
    question, answer = game.generate_question()
    print("Question:", question)
    
    user_input = input("Your answer: ")
    if game.check_answer(user_input):
        print("Correct!")
    else:
        print(f"Wrong! The correct answer was {answer}")
    
    print("Your score:", game.get_score())
```
