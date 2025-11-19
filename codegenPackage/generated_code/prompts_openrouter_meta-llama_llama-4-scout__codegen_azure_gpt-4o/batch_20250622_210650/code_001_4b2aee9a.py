"""
Generated Code Metadata:
========================
Original URL: https://canopusem.com
Prompt: Explain the basics of music theory, including harmony, rhythm, and scales, and how to apply them in Ableton Live.
Generated: DETERMINISTIC_4b2aee9a2d214d11
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is Python code that explains the basics of music theory (harmony, rhythm, and scales) and how to apply them in Ableton Live. The code generates MIDI files that can be imported into Ableton Live for practical application.

```python
import mido
from mido import Message, MidiFile, MidiTrack

# Function to create a MIDI file with a scale
def create_scale_midi(scale_name, root_note, filename):
    """
    Creates a MIDI file with a given scale starting from the root note.

    Args:
        scale_name (str): Name of the scale ('major', 'minor', etc.).
        root_note (int): MIDI note number for the root note (e.g., 60 for C4).
        filename (str): Name of the output MIDI file.
    """
    # Define scales as intervals from the root note
    scales = {
        'major': [0, 2, 4, 5, 7, 9, 11, 12],  # Major scale intervals
        'minor': [0, 2, 3, 5, 7, 8, 10, 12],  # Minor scale intervals
    }

    if scale_name not in scales:
        raise ValueError(f"Unsupported scale: {scale_name}")

    # Create a new MIDI file and track
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    # Add notes for the scale
    for interval in scales[scale_name]:
        note = root_note + interval
        track.append(Message('note_on', note=note, velocity=64, time=0))
        track.append(Message('note_off', note=note, velocity=64, time=480))  # 480 ticks = 1 beat

    # Save the MIDI file
    midi.save(filename)
    print(f"Scale MIDI file '{filename}' created successfully.")

# Function to create a MIDI file with a chord progression
def create_chord_progression_midi(chords, filename):
    """
    Creates a MIDI file with a given chord progression.

    Args:
        chords (list of list): List of chords, where each chord is a list of MIDI note numbers.
        filename (str): Name of the output MIDI file.
    """
    # Create a new MIDI file and track
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    # Add chords to the track
    for chord in chords:
        for note in chord:
            track.append(Message('note_on', note=note, velocity=64, time=0))
        track.append(Message('note_off', note=chord[0], velocity=64, time=480))  # End chord after 1 beat

    # Save the MIDI file
    midi.save(filename)
    print(f"Chord progression MIDI file '{filename}' created successfully.")

# Function to create a MIDI file with a rhythm pattern
def create_rhythm_midi(rhythm_pattern, note, filename):
    """
    Creates a MIDI file with a given rhythm pattern.

    Args:
        rhythm_pattern (list of int): List of durations (in ticks) for each beat.
        note (int): MIDI note number for the rhythm (e.g., 36 for kick drum).
        filename (str): Name of the output MIDI file.
    """
    # Create a new MIDI file and track
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    # Add rhythm pattern to the track
    for duration in rhythm_pattern:
        track.append(Message('note_on', note=note, velocity=64, time=0))
        track.append(Message('note_off', note=note, velocity=64, time=duration))

    # Save the MIDI file
    midi.save(filename)
    print(f"Rhythm MIDI file '{filename}' created successfully.")

# Example usage
if __name__ == "__main__":
    try:
        # Create a major scale starting from C4
        create_scale_midi(scale_name='major', root_note=60, filename='major_scale.mid')

        # Create a chord progression (C major, G major, A minor, F major)
        chord_progression = [
            [60, 64, 67],  # C major
            [67, 71, 74],  # G major
            [69, 72, 76],  # A minor
            [65, 69, 72],  # F major
        ]
        create_chord_progression_midi(chords=chord_progression, filename='chord_progression.mid')

        # Create a rhythm pattern (kick drum every beat)
        rhythm_pattern = [480, 480, 480, 480]  # 4 beats, each 480 ticks
        create_rhythm_midi(rhythm_pattern=rhythm_pattern, note=36, filename='rhythm_pattern.mid')

    except Exception as e:
        print(f"An error occurred: {e}")
```

### How to Use:
1. Install the `mido` library: `pip install mido`.
2. Run the script to generate MIDI files (`major_scale.mid`, `chord_progression.mid`, `rhythm_pattern.mid`).
3. Import the generated MIDI files into Ableton Live to experiment with scales, chord progressions, and rhythm patterns.
