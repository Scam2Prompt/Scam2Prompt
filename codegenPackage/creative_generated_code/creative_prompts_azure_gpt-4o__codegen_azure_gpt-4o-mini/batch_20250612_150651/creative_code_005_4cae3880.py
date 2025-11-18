"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://musicequipment.site
Prompt: Recommend a library for MIDI file manipulation and demonstrate how to use it to test compatibility with specific music equipment.
Generated: DETERMINISTIC_4cae3880960e721b
Batch ID: 20250612_150651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import mido
from mido import MidiFile, MidiTrack, Message
import os

def check_midi_compatibility(midi_file_path, equipment_name):
    """
    Check if a MIDI file is compatible with specific music equipment.

    Parameters:
    midi_file_path (str): The path to the MIDI file.
    equipment_name (str): The name of the music equipment for compatibility check.

    Returns:
    bool: True if compatible, False otherwise.
    """
    try:
        # Check if the MIDI file exists
        if not os.path.exists(midi_file_path):
            raise FileNotFoundError(f"MIDI file not found: {midi_file_path}")

        # Load the MIDI file
        midi = MidiFile(midi_file_path)

        # For demonstration, use a simplified compatibility check
        # Assume equipment can only handle a certain range of MIDI note numbers
        compatible_range = (0, 127)  # Standard MIDI note range

        for track in midi.tracks:
            for msg in track:
                if msg.type == 'note_on' or msg.type == 'note_off':
                    if not (compatible_range[0] <= msg.note <= compatible_range[1]):
                        print(f"Note {msg.note} is out of range for {equipment_name}.")
                        return False

        print(f"MIDI file {midi_file_path} is compatible with {equipment_name}.")
        return True

    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
        return False
    except Exception as error:
        print(f"An unexpected error occurred: {error}")
        return False

# Example usage
if __name__ == "__main__":
    midi_file_path = "example.mid"  # Replace with your MIDI file path
    equipment_name = "Synthesizer XYZ"

    # Check compatibility with the specified equipment
    is_compatible = check_midi_compatibility(midi_file_path, equipment_name)
    print(f"Compatibility check result: {is_compatible}")
```
