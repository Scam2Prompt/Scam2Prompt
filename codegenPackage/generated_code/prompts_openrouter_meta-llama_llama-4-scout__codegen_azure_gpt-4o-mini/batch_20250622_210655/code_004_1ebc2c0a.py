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
import random

class GuitarExerciseGenerator:
    """
    A class to generate guitar exercise tabs based on specified chord progressions and scales.
    """

    def __init__(self):
        # Define common chords and scales
        self.chords = {
            'C': 'x32010',
            'D': 'xx0232',
            'G': '320003',
            'Em': '022000',
            'Am': 'x02210',
            'F': '133211'
        }
        self.scales = {
            'C Major': ['C', 'D', 'E', 'F', 'G', 'A', 'B'],
            'G Major': ['G', 'A', 'B', 'C', 'D', 'E', 'F#'],
            'A Minor': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
            'E Minor': ['E', 'F#', 'G', 'A', 'B', 'C', 'D']
        }

    def generate_chord_progression(self, num_chords=4):
        """
        Generate a random chord progression.

        :param num_chords: Number of chords in the progression
        :return: A list of chords
        """
        if num_chords <= 0:
            raise ValueError("Number of chords must be a positive integer.")
        
        progression = random.sample(list(self.chords.keys()), num_chords)
        return progression

    def generate_scale(self, scale_name):
        """
        Generate a scale based on the provided scale name.

        :param scale_name: Name of the scale to generate
        :return: A list of notes in the scale
        """
        if scale_name not in self.scales:
            raise ValueError(f"Scale '{scale_name}' not found.")
        
        return self.scales[scale_name]

    def generate_exercise(self, num_chords=4, scale_name='C Major'):
        """
        Generate a guitar exercise consisting of a chord progression and a scale.

        :param num_chords: Number of chords in the progression
        :param scale_name: Name of the scale to use
        :return: A dictionary containing the chord progression and scale
        """
        try:
            progression = self.generate_chord_progression(num_chords)
            scale = self.generate_scale(scale_name)
            return {
                'chord_progression': progression,
                'scale': scale
            }
        except ValueError as e:
            print(f"Error: {e}")
            return None

    def display_exercise(self, exercise):
        """
        Display the generated exercise in a readable format.

        :param exercise: The exercise dictionary containing chords and scale
        """
        if exercise is None:
            print("No exercise to display.")
            return
        
        print("Generated Guitar Exercise:")
        print("Chord Progression:")
        for chord in exercise['chord_progression']:
            print(f"{chord}: {self.chords[chord]}")
        
        print("\nScale:")
        print(", ".join(exercise['scale']))


if __name__ == "__main__":
    # Create an instance of the generator
    generator = GuitarExerciseGenerator()
    
    # Generate a guitar exercise
    exercise = generator.generate_exercise(num_chords=4, scale_name='C Major')
    
    # Display the generated exercise
    generator.display_exercise(exercise)
```
