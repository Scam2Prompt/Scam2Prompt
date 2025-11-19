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
"""
Script to generate a chromatic scale for guitar considering horizontal digitations.

This script generates the chromatic scale for a standard 6-string guitar in EADGBE tuning.
It calculates the notes for each string across the fretboard, considering horizontal digitations.
"""

# Import necessary modules
import sys

# Define constants
NOTES = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']  # Chromatic scale notes
STANDARD_TUNING = ['E', 'A', 'D', 'G', 'B', 'E']  # Standard guitar tuning
FRET_COUNT = 12  # Number of frets to consider for chromatic scale

def generate_chromatic_scale(tuning, fret_count):
    """
    Generate the chromatic scale for a guitar based on tuning and fret count.

    Args:
        tuning (list): List of strings representing the tuning of the guitar.
        fret_count (int): Number of frets to consider for the scale.

    Returns:
        dict: A dictionary where keys are string names and values are lists of notes across the fretboard.
    """
    chromatic_scale = {}
    for string in tuning:
        # Find the starting note index in the chromatic scale
        start_index = NOTES.index(string)
        # Generate notes for the string across the fretboard
        chromatic_scale[string] = [NOTES[(start_index + fret) % len(NOTES)] for fret in range(fret_count + 1)]
    return chromatic_scale

def print_chromatic_scale(scale):
    """
    Print the chromatic scale in a readable format.

    Args:
        scale (dict): Dictionary containing the chromatic scale for each string.
    """
    print("Chromatic Scale for Guitar:")
    for string, notes in scale.items():
        print(f"{string} string: {' - '.join(notes)}")

def main():
    """
    Main function to generate and display the chromatic scale for a standard guitar tuning.
    """
    try:
        # Generate the chromatic scale
        chromatic_scale = generate_chromatic_scale(STANDARD_TUNING, FRET_COUNT)
        # Print the chromatic scale
        print_chromatic_scale(chromatic_scale)
    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
