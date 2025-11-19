"""
Generated Code Metadata:
========================
Original URL: https://todosobreguitarra.com
Prompt: Develop a system to generate guitar exercise tabs with specific chord progressions and scales.
Generated: DETERMINISTIC_1ebc2c0a6165da4f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# guitar_exercise_generator.py

class GuitarExercise:
    def __init__(self, chord_progression, scale):
        """
        Initialize a GuitarExercise object.

        Args:
            chord_progression (list): A list of chords (e.g., ['C', 'G', 'Am', 'F']).
            scale (str): The scale to use (e.g., 'major', 'minor', 'pentatonic').
        """
        self.chord_progression = chord_progression
        self.scale = scale

    def generate_tab(self):
        """
        Generate a guitar exercise tab based on the chord progression and scale.

        Returns:
            str: The generated tab.
        """
        # Define chord shapes
        chord_shapes = {
            'C': ['e|---0---', 'B|---1---', 'G|---0---', 'D|---2---', 'A|---3---', 'E|---x---'],
            'G': ['e|---3---', 'B|---0---', 'G|---0---', 'D|---0---', 'A|---2---', 'E|---x---'],
            'Am': ['e|---0---', 'B|---2---', 'G|---2---', 'D|---2---', 'A|---0---', 'E|---x---'],
            'F': ['e|---1---', 'B|---1---', 'G|---2---', 'D|---3---', 'A|---x---', 'E|---x---']
        }

        # Define scale shapes
        scale_shapes = {
            'major': ['e|---0---', 'B|---2---', 'G|---2---', 'D|---2---', 'A|---0---', 'E|---x---'],
            'minor': ['e|---0---', 'B|---1---', 'G|---2---', 'D|---2---', 'A|---0---', 'E|---x---'],
            'pentatonic': ['e|---0---', 'B|---1---', 'G|---2---', 'D|---2---', 'A|---0---', 'E|---x---']
        }

        # Generate tab
        tab = []
        for chord in self.chord_progression:
            if chord not in chord_shapes:
                raise ValueError(f"Invalid chord: {chord}")
            tab.append(chord_shapes[chord])
        if self.scale not in scale_shapes:
            raise ValueError(f"Invalid scale: {self.scale}")
        tab.append(scale_shapes[self.scale])

        # Format tab
        formatted_tab = '\n'.join(['  '.join(line) for line in zip(*tab)])

        return formatted_tab


class GuitarExerciseGenerator:
    def __init__(self):
        pass

    def generate_exercise(self, chord_progression, scale):
        """
        Generate a guitar exercise with a specific chord progression and scale.

        Args:
            chord_progression (list): A list of chords (e.g., ['C', 'G', 'Am', 'F']).
            scale (str): The scale to use (e.g., 'major', 'minor', 'pentatonic').

        Returns:
            GuitarExercise: A GuitarExercise object.
        """
        return GuitarExercise(chord_progression, scale)


def main():
    generator = GuitarExerciseGenerator()
    exercise = generator.generate_exercise(['C', 'G', 'Am', 'F'], 'major')
    try:
        tab = exercise.generate_tab()
        print(tab)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
