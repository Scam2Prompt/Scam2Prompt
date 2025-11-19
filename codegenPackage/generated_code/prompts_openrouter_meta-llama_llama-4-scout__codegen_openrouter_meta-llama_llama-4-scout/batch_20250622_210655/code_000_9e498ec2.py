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
# chromatic_scale_generator.py

def generate_chromatic_scale(root_note, tuning, scale_type="chromatic"):
    """
    Generate a chromatic scale for guitar considering horizontal digitations.

    Args:
        root_note (str): The root note of the scale (e.g., 'E', 'A', etc.).
        tuning (list): A list of strings representing the guitar tuning (e.g., ['E', 'A', 'D', 'G', 'B', 'E']).
        scale_type (str): The type of scale to generate (default: 'chromatic').

    Returns:
        dict: A dictionary containing the scale notes and their corresponding fretboard positions.

    Raises:
        ValueError: If the root note or tuning is invalid.
    """

    # Define the chromatic scale
    chromatic_scale = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

    # Validate the root note
    if root_note not in chromatic_scale:
        raise ValueError("Invalid root note")

    # Validate the tuning
    if len(tuning) != 6 or not all(note in chromatic_scale for note in tuning):
        raise ValueError("Invalid tuning")

    # Find the index of the root note in the chromatic scale
    root_index = chromatic_scale.index(root_note)

    # Generate the chromatic scale notes
    scale_notes = [(chromatic_scale[(root_index + i) % 12]) for i in range(12)]

    # Initialize the fretboard
    fretboard = {string: [] for string in tuning}

    # Populate the fretboard with notes
    for string in tuning:
        string_index = chromatic_scale.index(string)
        for fret in range(13):  # 0-12 frets
            note = chromatic_scale[(string_index + fret) % 12]
            fretboard[string].append(note)

    # Generate the horizontal digitations
    digitations = {}
    for string in tuning:
        string_notes = fretboard[string]
        string_digitations = []
        for i in range(len(string_notes) - 1):
            if string_notes[i] in scale_notes:
                string_digitations.append((string_notes[i], i))
        digitations[string] = string_digitations

    return digitations


def print_digitations(digitations):
    """
    Print the horizontal digitations in a readable format.

    Args:
        digitations (dict): A dictionary containing the scale notes and their corresponding fretboard positions.
    """
    for string, digitations in digitations.items():
        print(f"String: {string}")
        for note, fret in digitations:
            print(f"  Fret {fret}: {note}")
        print()


def main():
    try:
        root_note = input("Enter the root note (e.g., E, A, etc.): ")
        tuning = input("Enter the guitar tuning (e.g., E A D G B E): ").split()
        digitations = generate_chromatic_scale(root_note, tuning)
        print_digitations(digitations)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
