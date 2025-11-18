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


class MusicTheory:
    """
    A class to handle musical intervals and chords generation and display.
    """

    def __init__(self):
        # List of all notes in Western music, considering a 12-tone system.
        self.notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def get_interval(self, root_note, interval):
        """
        Get the note at a specific interval from the root note.
        :param root_note: The starting note (string).
        :param interval: The interval in semitones (integer).
        :return: Note at the specified interval (string).
        """
        try:
            root_index = self.notes.index(root_note)
        except ValueError:
            raise ValueError(f"Invalid root note: {root_note}. Use one of {self.notes}.")

        interval_index = (root_index + interval) % len(self.notes)
        return self.notes[interval_index]

    def generate_chord(self, root_note, chord_type):
        """
        Generate a chord based on the root note and chord type.
        :param root_note: The starting note (string).
        :param chord_type: Type of chord ('major', 'minor', 'diminished', 'augmented').
        :return: List of notes in the chord.
        """
        # Intervals for different chord types based on their semitonic structure.
        chord_intervals = {
            'major': [0, 4, 7],       # Root, Major Third, Perfect Fifth
            'minor': [0, 3, 7],       # Root, Minor Third, Perfect Fifth
            'diminished': [0, 3, 6],  # Root, Minor Third, Diminished Fifth
            'augmented': [0, 4, 8]    # Root, Major Third, Augmented Fifth
        }

        if chord_type not in chord_intervals:
            raise ValueError(f"Invalid chord type: {chord_type}. Choose from {list(chord_intervals.keys())}.")

        try:
            chord_notes = [self.get_interval(root_note, interval) for interval in chord_intervals[chord_type]]
        except ValueError as e:
            raise ValueError(f"Error generating chord: {e}")

        return chord_notes

    def display_intervals_and_chords(self):
        """
        Display musical intervals and chords for all notes.
        """
        print("Musical Intervals:")
        for note in self.notes:
            print(f"Root Note: {note}")
            print(f"  Major Third: {self.get_interval(note, 4)}")
            print(f"  Perfect Fifth: {self.get_interval(note, 7)}")
            print()

        print("Chords:")
        for note in self.notes:
            print(f"Root Note: {note}")
            for chord_type in ['major', 'minor', 'diminished', 'augmented']:
                chord = self.generate_chord(note, chord_type)
                print(f"  {chord_type.capitalize()} Chord: {chord}")
            print()


if __name__ == "__main__":
    try:
        music_theory = MusicTheory()
        music_theory.display_intervals_and_chords()
    except Exception as e:
        print(f"An error occurred: {e}")
```
