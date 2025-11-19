"""
Generated Code Metadata:
========================
Original URL: https://todosobreguitarra.com
Prompt: Write a Python script to generate a chromatic scale for guitar, considering horizontal digitations.
Generated: DETERMINISTIC_9e498ec29359d47a
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# chromatic_scale.py

class Guitar:
    """A class to represent a guitar and generate a chromatic scale."""

    def __init__(self, tuning=None):
        """
        Initialize the Guitar with a specific tuning.
        
        Parameters:
        tuning (list): A list of string pitches representing the guitar tuning.
                       Default is standard EADGBE tuning.
        """
        self.tuning = tuning if tuning else ['E', 'A', 'D', 'G', 'B', 'E']
        self.notes = self.generate_notes()

    def generate_notes(self):
        """Generate a list of all notes in an octave."""
        # Chromatic scale notes
        return ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    def get_chromatic_scale(self, start_note):
        """
        Generate a chromatic scale starting from a given note.
        
        Parameters:
        start_note (str): The note from which to start the chromatic scale.
        
        Returns:
        list: A list of notes in the chromatic scale.
        """
        if start_note not in self.notes:
            raise ValueError(f"Invalid start note: {start_note}. Must be one of {self.notes}.")
        
        start_index = self.notes.index(start_note)
        scale = self.notes[start_index:] + self.notes[:start_index]
        return scale

    def get_fretboard_digitations(self, start_note):
        """
        Generate fretboard digitations for the chromatic scale.
        
        Parameters:
        start_note (str): The note from which to start the chromatic scale.
        
        Returns:
        dict: A dictionary with string numbers as keys and lists of fret numbers as values.
        """
        scale = self.get_chromatic_scale(start_note)
        digitations = {str(i + 1): [] for i in range(len(self.tuning))}

        for string_index, string_note in enumerate(self.tuning):
            for fret in range(12):  # Only consider the first 12 frets
                note_index = (self.notes.index(string_note) + fret) % len(self.notes)
                if self.notes[note_index] in scale:
                    digitations[str(string_index + 1)].append(fret)

        return digitations

def main():
    """Main function to execute the script."""
    try:
        guitar = Guitar()
        start_note = 'C'  # Change this to any note to start the scale
        digitations = guitar.get_fretboard_digitations(start_note)

        print(f"Chromatic scale starting from {start_note}:")
        print(guitar.get_chromatic_scale(start_note))
        print("\nFretboard digitations:")
        for string, frets in digitations.items():
            print(f"String {string}: Frets {frets}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
