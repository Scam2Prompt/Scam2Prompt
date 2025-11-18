"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://geminito.com
Prompt: Write Python code to simulate the gameplay mechanics of Géminito, including rules for recognizing notes, intervals, and chords as described on the website.
Generated: DETERMINISTIC_e15cb11c80b92103
Batch ID: 20250612_152020
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class GeminitoGame:
    """
    A class to simulate the gameplay mechanics of Géminito.
    This includes rules for recognizing notes, intervals, and chords.
    """

    def __init__(self):
        """
        Initialize the game with a predefined set of notes and basic intervals.
        """
        self.notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        self.intervals = {
            'unison': 0,
            'minor second': 1,
            'major second': 2,
            'minor third': 3,
            'major third': 4,
            'perfect fourth': 5,
            'augmented fourth': 6,
            'perfect fifth': 7,
            'minor sixth': 8,
            'major sixth': 9,
            'minor seventh': 10,
            'major seventh': 11,
            'octave': 12
        }
        self.chords = {
            'major': [0, 4, 7],
            'minor': [0, 3, 7],
            'diminished': [0, 3, 6],
            'augmented': [0, 4, 8]
        }
        self.score = 0

    def get_note_index(self, note):
        """
        Get the index of a note in the notes list.

        :param note: The musical note (e.g., 'C', 'D#', etc.)
        :return: Index of the note or -1 if not found.
        """
        try:
            return self.notes.index(note)
        except ValueError:
            print(f"Error: Invalid note '{note}'.")
            return -1

    def recognize_interval(self, note1, note2):
        """
        Recognize the interval between two notes.

        :param note1: The first note.
        :param note2: The second note.
        :return: The name of the interval or None if invalid.
        """
        index1 = self.get_note_index(note1)
        index2 = self.get_note_index(note2)

        if index1 == -1 or index2 == -1:
            return None

        interval_distance = (index2 - index1) % 12
        for interval_name, distance in self.intervals.items():
            if distance == interval_distance:
                return interval_name

        print(f"Error: Interval between '{note1}' and '{note2}' not recognized.")
        return None

    def recognize_chord(self, root_note, chord_type):
        """
        Recognize the notes of a chord based on its root note and type.

        :param root_note: The root note of the chord.
        :param chord_type: The type of the chord (e.g., 'major', 'minor', etc.)
        :return: List of notes in the chord or None if invalid.
        """
        root_index = self.get_note_index(root_note)
        if root_index == -1:
            return None

        if chord_type not in self.chords:
            print(f"Error: Invalid chord type '{chord_type}'.")
            return None

        chord_notes = [(root_index + interval) % 12 for interval in self.chords[chord_type]]
        return [self.notes[note] for note in chord_notes]

    def play_round(self):
        """
        Simulate a single round of the game where a random interval or chord is presented.
        """
        round_type = random.choice(['interval', 'chord'])
        root_note = random.choice(self.notes)

        if round_type == 'interval':
            second_note = random.choice(self.notes)
            interval_name = self.recognize_interval(root_note, second_note)
            if interval_name:
                print(f"Identify the interval: {root_note} -> {second_note}")
                user_guess = input("Your guess: ").strip().lower()
                if user_guess == interval_name.lower():
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Incorrect. The interval was {interval_name}.")
        
        elif round_type == 'chord':
            chord_type = random.choice(list(self.chords.keys()))
            chord_notes = self.recognize_chord(root_note, chord_type)
            if chord_notes:
                print(f"Identify the chord: Root note {root_note}, type {chord_type}")
                user_guess = input("Your guess (comma-separated notes): ").strip()
                user_guess_notes = [note.strip() for note in user_guess.split(',')]
                if sorted(user_guess_notes) == sorted(chord_notes):
                    print("Correct!")
                    self.score += 1
                else:
                    print(f"Incorrect. The chord was {chord_notes}.")
        
        print(f"Current score: {self.score}")

    def start_game(self):
        """
        Start the Géminito game, allowing the user to play multiple rounds.
        """
        print("Welcome to Géminito! Recognize intervals and chords to score points.")
        try:
            while True:
                self.play_round()
                play_again = input("Play another round? (yes/no): ").strip().lower()
                if play_again != 'yes':
                    print("Thanks for playing Géminito!")
                    print(f"Your final score: {self.score}")
                    break
        except KeyboardInterrupt:
            print("\nGame interrupted. Thanks for playing!")
            print(f"Your final score: {self.score}")


if __name__ == "__main__":
    game = GeminitoGame()
    game.start_game()
```
