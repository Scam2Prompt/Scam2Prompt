"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://overlanders-atari.com
Prompt: Write a tutorial on how to produce a chip tune for a demo, referencing the techniques used in the OVeRclocked remix by Overlanders.
Generated: DETERMINISTIC_6e21e3704c0d9e89
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

# Constants
SAMPLE_RATE = 44100  # Sample rate in Hz
DURATION = 2.0        # Duration in seconds for each note
FREQUENCIES = {
    "C4": 261.63,
    "D4": 293.66,
    "E4": 329.63,
    "F4": 349.23,
    "G4": 392.00,
    "A4": 440.00,
    "B4": 493.88,
}

def generate_sine_wave(frequency, duration, sample_rate):
    """
    Generate a sine wave for a given frequency and duration.
    
    :param frequency: Frequency of the sine wave in Hz
    :param duration: Duration of the sine wave in seconds
    :param sample_rate: Number of samples per second
    :return: Numpy array containing the sine wave samples
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return 0.5 * np.sin(2 * np.pi * frequency * t)

def create_chip_tune(note_sequence, filename):
    """
    Create a chip tune from a sequence of notes and save it as a WAV file.
    
    :param note_sequence: List of tuples containing note names and their durations
    :param filename: Name of the output WAV file
    """
    try:
        audio = np.array([], dtype=np.float32)
        
        for note, duration in note_sequence:
            if note not in FREQUENCIES:
                raise ValueError(f"Note '{note}' is not a valid frequency entry.")
            wave = generate_sine_wave(FREQUENCIES[note], duration, SAMPLE_RATE)
            audio = np.concatenate((audio, wave))
        
        # Normalize audio to avoid distortion
        audio = np.int16(audio / np.max(np.abs(audio)) * 32767)
        
        # Write the audio to a WAV file
        write(filename, SAMPLE_RATE, audio)
        print(f"Chip tune saved as '{filename}'.")
    except Exception as e:
        print(f"An error occurred while creating the chip tune: {e}")

if __name__ == "__main__":
    # Define a sequence of notes for the chiptune
    notes = [
        ("C4", DURATION),
        ("E4", DURATION),
        ("G4", DURATION),
        ("C4", DURATION),
        ("A4", DURATION),
        ("F4", DURATION),
        ("G4", DURATION),
        ("E4", DURATION),
    ]
    
    # Create the chip tune and save it
    create_chip_tune(notes, "chip_tune.wav")
```
