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
from typing import List, Tuple

# Define note values and their corresponding pitch class
NOTE_VALUES = {
    'C': 0, 'C#': 1, 'Db': 1, 'D': 2, 'D#': 3, 'Eb': 3,
    'E': 4, 'F': 5, 'F#': 6, 'Gb': 6, 'G': 7, 'G#': 8,
    'Ab': 8, 'A': 9, 'A#': 10, 'Bb': 10, 'B': 11
}

# Define interval values and their corresponding names
INTERVAL_VALUES = {
    0: 'Unison', 1: 'm2', 2: 'M2', 3: 'm3', 4: 'M3',
    5: 'P4', 6: 'd5', 7: 'P5', 8: 'm6', 9: 'M6',
    10: 'm7', 11: 'M7', 12: 'P8'
}

class Note:
    """Represents a musical note."""
    def __init__(self, name: str):
        self.name = name
        self.value = NOTE_VALUES[name]

    def __repr__(self):
        return f"Note('{self.name}')"

class Interval:
    """Represents a musical interval."""
    def __init__(self, note1: Note, note2: Note):
        self.note1 = note1
        self.note2 = note2
        self.value = (self.note2.value - self.note1.value) % 12

    def __repr__(self):
        return f"Interval({self.note1}, {self.note2})"

    def get_name(self) -> str:
        return INTERVAL_VALUES[self.value]

class Chord:
    """Represents a musical chord."""
    def __init__(self, notes: List[Note]):
        self.notes = notes

    def __repr__(self):
        return f"Chord({self.notes})"

def recognize_note(note_name: str) -> Note:
    """Recognize a note by its name."""
    try:
        return Note(note_name)
    except KeyError:
        raise ValueError(f"Invalid note name: {note_name}")

def recognize_interval(note1_name: str, note2_name: str) -> Interval:
    """Recognize an interval between two notes."""
    note1 = recognize_note(note1_name)
    note2 = recognize_note(note2_name)
    return Interval(note1, note2)

def recognize_chord(note_names: List[str]) -> Chord:
    """Recognize a chord by its notes."""
    try:
        notes = [recognize_note(name) for name in note_names]
        return Chord(notes)
    except ValueError as e:
        raise ValueError(f"Invalid chord notes: {e}")

def generate_random_note() -> Note:
    """Generate a random note."""
    note_names = list(NOTE_VALUES.keys())
    return recognize_note(random.choice(note_names))

def generate_random_interval() -> Interval:
    """Generate a random interval."""
    note1 = generate_random_note()
    note2 = generate_random_note()
    return Interval(note1, note2)

def generate_random_chord() -> Chord:
    """Generate a random chord."""
    note_names = random.sample(list(NOTE_VALUES.keys()), 3)
    return recognize_chord(note_names)

def main():
    # Test note recognition
    note = recognize_note('C')
    print(f"Note: {note}")

    # Test interval recognition
    interval = recognize_interval('C', 'E')
    print(f"Interval: {interval.note1} to {interval.note2} = {interval.get_name()}")

    # Test chord recognition
    chord = recognize_chord(['C', 'E', 'G'])
    print(f"Chord: {chord}")

    # Generate random note, interval, and chord
    random_note = generate_random_note()
    print(f"Random Note: {random_note}")

    random_interval = generate_random_interval()
    print(f"Random Interval: {random_interval.note1} to {random_interval.note2} = {random_interval.get_name()}")

    random_chord = generate_random_chord()
    print(f"Random Chord: {random_chord}")

if __name__ == "__main__":
    main()
```
