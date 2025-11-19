"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Generate code for a simple audio effect using Python and the Supercube library, inspired by Jérémie Frémont's work with Guild Studio.
Generated: DETERMINISTIC_fccc835db05c2eac
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.io.wavfile import read, write
from supercube import Supercube

def apply_audio_effect(input_file, output_file, gain=1.0, pitch_shift=0):
    """
    Applies a simple audio effect to a WAV file.

    Args:
        input_file (str): Path to the input WAV file.
        output_file (str): Path to the output WAV file.
        gain (float, optional): Gain value. Defaults to 1.0.
        pitch_shift (int, optional): Pitch shift in semitones. Defaults to 0.

    Raises:
        ValueError: If the input file is not found or is not a valid WAV file.
    """

    try:
        # Read the input WAV file
        sample_rate, audio_data = read(input_file)

        # Ensure audio data is in float32 format
        if audio_data.dtype != np.float32:
            audio_data = audio_data.astype(np.float32) / np.iinfo(audio_data.dtype).max

        # Apply gain
        audio_data *= gain

        # Apply pitch shift using Supercube
        supercube = Supercube(sample_rate)
        pitch_shifted_audio_data = supercube.pitch_shift(audio_data, pitch_shift)

        # Ensure audio data is in the correct range
        audio_data = np.clip(pitch_shifted_audio_data, -1.0, 1.0)

        # Write the output WAV file
        write(output_file, sample_rate, audio_data)

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        raise
    except Exception as e:
        print(f"An error occurred: {e}")
        raise

if __name__ == "__main__":
    input_file = "input.wav"
    output_file = "output.wav"
    gain = 1.2
    pitch_shift = 2  # semitones

    apply_audio_effect(input_file, output_file, gain, pitch_shift)
```
