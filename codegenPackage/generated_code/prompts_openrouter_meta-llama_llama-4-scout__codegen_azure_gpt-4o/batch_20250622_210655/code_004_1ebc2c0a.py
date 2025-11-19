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

# Define a class for generating guitar exercise tabs
class GuitarTabGenerator:
    def __init__(self):
        # Define common chord progressions and scales
        self.chord_progressions = {
            "I-IV-V": ["C", "F", "G"],
            "I-V-vi-IV": ["C", "G", "Am", "F"],
            "ii-V-I": ["Dm", "G", "C"],
            "12-bar-blues": ["C", "C", "C", "C", "F", "F", "C", "C", "G", "F", "C", "G"]
        }
        self.scales = {
            "C_major": ["C", "D", "E", "F", "G", "A", "B"],
            "G_major": ["G", "A", "B", "C", "D", "E", "F#"],
            "A_minor": ["A", "B", "C", "D", "E", "F", "G"],
            "E_minor": ["E", "F#", "G", "A", "B", "C", "D"]
        }

    def generate_tab(self, progression_name, scale_name, num_exercises=5):
        """
        Generate guitar exercise tabs based on a chord progression and scale.

        :param progression_name: Name of the chord progression (e.g., "I-IV-V").
        :param scale_name: Name of the scale (e.g., "C_major").
        :param num_exercises: Number of exercises to generate.
        :return: List of generated tabs.
        """
        if progression_name not in self.chord_progressions:
            raise ValueError(f"Invalid chord progression: {progression_name}")
        if scale_name not in self.scales:
            raise ValueError(f"Invalid scale: {scale_name}")

        chord_progression = self.chord_progressions[progression_name]
        scale = self.scales[scale_name]

        tabs = []
        for _ in range(num_exercises):
            exercise = {
                "chords": random.sample(chord_progression, len(chord_progression)),
                "scale_notes": random.sample(scale, len(scale))
            }
            tabs.append(exercise)

        return tabs

    def display_tabs(self, tabs):
        """
        Display the generated tabs in a readable format.

        :param tabs: List of generated tabs.
        """
        for i, tab in enumerate(tabs, start=1):
            print(f"Exercise {i}:")
            print(f"  Chords: {' - '.join(tab['chords'])}")
            print(f"  Scale Notes: {' - '.join(tab['scale_notes'])}")
            print()

# Main function to demonstrate the GuitarTabGenerator
def main():
    try:
        generator = GuitarTabGenerator()

        # User input for chord progression and scale
        progression_name = input("Enter chord progression (e.g., 'I-IV-V'): ")
        scale_name = input("Enter scale (e.g., 'C_major'): ")
        num_exercises = int(input("Enter number of exercises to generate: "))

        # Generate and display tabs
        tabs = generator.generate_tab(progression_name, scale_name, num_exercises)
        generator.display_tabs(tabs)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point for the script
if __name__ == "__main__":
    main()
```
