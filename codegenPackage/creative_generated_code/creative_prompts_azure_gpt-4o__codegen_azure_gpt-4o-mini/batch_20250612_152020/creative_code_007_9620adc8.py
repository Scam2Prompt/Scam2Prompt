"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geminito.com
Prompt: Write code to generate and display musical intervals (e.g., thirds, fifths) and chords (major, minor, diminished, augmented) as described in Géminito's gameplay.
Generated: DETERMINISTIC_9620adc8a27bb3d5
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import itertools

class MusicalInterval:
    """
    Class to represent and generate musical intervals and chords.
    """

    # Define the intervals based on semitone differences
    INTERVALS = {
        "unison": 0,
        "minor second": 1,
        "major second": 2,
        "minor third": 3,
        "major third": 4,
        "perfect fourth": 5,
        "tritone": 6,
        "perfect fifth": 7,
        "minor sixth": 8,
        "major sixth": 9,
        "minor seventh": 10,
        "major seventh": 11,
        "octave": 12
    }

    # Define the chords based on intervals
    CHORDS = {
        "major": [0, 4, 7],
        "minor": [0, 3, 7],
        "diminished": [0, 3, 6],
        "augmented": [0, 4, 8]
    }

    def __init__(self, root_note):
        """
        Initialize the MusicalInterval with a root note.
        
        :param root_note: The tonic note of the scale (e.g., C, D, E).
        """
        self.root_note = root_note

    def get_interval(self, interval_name):
        """
        Get the interval in semitones for a given interval name.
        
        :param interval_name: Name of the interval.
        :return: Number of semitones for the interval.
        :raises ValueError: If the interval name is not recognized.
        """
        try:
            return self.INTERVALS[interval_name]
        except KeyError:
            raise ValueError(f"Interval '{interval_name}' is not recognized.")

    def generate_chord(self, chord_type):
        """
        Generate the notes for a given chord type based on the root note.
        
        :param chord_type: Type of the chord (major, minor, diminished, augmented).
        :return: List of notes in the chord.
        :raises ValueError: If the chord type is not recognized.
        """
        try:
            intervals = self.CHORDS[chord_type]
            return [self._note_from_interval(interval) for interval in intervals]
        except KeyError:
            raise ValueError(f"Chord type '{chord_type}' is not recognized.")

    def _note_from_interval(self, interval):
        """
        Generate a note from the root note and a given interval in semitones.
        
        :param interval: Interval in semitones.
        :return: The resulting note.
        """
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        root_index = note_names.index(self.root_note)
        note_index = (root_index + interval) % len(note_names)
        return note_names[note_index]

    def display_intervals(self):
        """
        Display all musical intervals and their corresponding semitone values.
        """
        print("Musical Intervals:")
        for interval, semitones in self.INTERVALS.items():
            print(f"{interval}: {semitones} semitones")

    def display_chords(self):
        """
        Display all chord types along with their generated notes based on a fixed root note.
        """
        print(f"Chords based on {self.root_note}:")
        for chord_type in self.CHORDS.keys():
            chord_notes = self.generate_chord(chord_type)
            print(f"{chord_type.capitalize()} chord: {', '.join(chord_notes)}")


# Example Usage
if __name__ == "__main__":
    try:
        root_note = "C"
        musical_interval = MusicalInterval(root_note)
        musical_interval.display_intervals()
        musical_interval.display_chords()
    except ValueError as e:
        print(f"Error: {e}")
```
