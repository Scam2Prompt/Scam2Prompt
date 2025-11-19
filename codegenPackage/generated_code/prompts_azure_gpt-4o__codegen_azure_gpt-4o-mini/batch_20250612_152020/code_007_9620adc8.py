"""
Generated Code Metadata:
========================
Original URL: https://geminito.com
Prompt: Write code to generate and display musical intervals (e.g., thirds, fifths) and chords (major, minor, diminished, augmented) as described in Géminito's gameplay.
Generated: DETERMINISTIC_9620adc8a27bb3d5
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt

class MusicalInterval:
    """Class to represent musical intervals and chords."""

    INTERVALS = {
        'unison': 0,
        'minor second': 1,
        'major second': 2,
        'minor third': 3,
        'major third': 4,
        'perfect fourth': 5,
        'tritone': 6,
        'perfect fifth': 7,
        'minor sixth': 8,
        'major sixth': 9,
        'minor seventh': 10,
        'major seventh': 11,
        'octave': 12
    }

    CHORDS = {
        'major': [0, 4, 7],
        'minor': [0, 3, 7],
        'diminished': [0, 3, 6],
        'augmented': [0, 4, 8]
    }

    def __init__(self, root_note):
        """Initialize with a root note (0-11 representing C-B)."""
        if not (0 <= root_note <= 11):
            raise ValueError("Root note must be between 0 (C) and 11 (B).")
        self.root_note = root_note

    def get_interval(self, interval_name):
        """Get the pitch class of a given interval from the root note."""
        if interval_name not in self.INTERVALS:
            raise ValueError(f"Invalid interval name: {interval_name}")
        return (self.root_note + self.INTERVALS[interval_name]) % 12

    def get_chord(self, chord_name):
        """Get the pitch classes of a given chord from the root note."""
        if chord_name not in self.CHORDS:
            raise ValueError(f"Invalid chord name: {chord_name}")
        return [(self.root_note + step) % 12 for step in self.CHORDS[chord_name]]

    def display_intervals(self):
        """Display all intervals from the root note."""
        print(f"Intervals from root note {self.root_note}:")
        for interval in self.INTERVALS:
            note = self.get_interval(interval)
            print(f"{interval}: {note}")

    def display_chords(self):
        """Display all chords from the root note."""
        print(f"Chords from root note {self.root_note}:")
        for chord in self.CHORDS:
            notes = self.get_chord(chord)
            print(f"{chord}: {notes}")

def main():
    """Main function to demonstrate musical intervals and chords."""
    try:
        root_note = int(input("Enter a root note (0-11, where 0=C and 11=B): "))
        musical_interval = MusicalInterval(root_note)

        musical_interval.display_intervals()
        musical_interval.display_chords()

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
