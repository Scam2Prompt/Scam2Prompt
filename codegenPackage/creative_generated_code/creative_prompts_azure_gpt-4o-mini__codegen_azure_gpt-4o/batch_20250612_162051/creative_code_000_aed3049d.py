"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeremiefremont.com
Prompt: Generate a code snippet for a sound design tool that can blend acoustic and electronic sounds, inspired by Jérémie Frémont's unique approach to composition.
Generated: DETERMINISTIC_aed3049d3351a17d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
from scipy.io.wavfile import read, write
import os

class SoundBlendTool:
    """
    A tool for blending acoustic and electronic sounds into unique compositions.
    """

    def __init__(self):
        """
        Initialize the SoundBlendTool with default settings.
        """
        self.acoustic_sound = None
        self.electronic_sound = None
        self.output_sample_rate = None

    def load_sound(self, filepath):
        """
        Load a sound file (WAV format).

        Args:
            filepath (str): Path to the WAV file.

        Returns:
            tuple: Sample rate and audio data as a NumPy array.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")
        sample_rate, data = read(filepath)
        if len(data.shape) > 1:  # Convert stereo to mono if necessary
            data = data.mean(axis=1)
        return sample_rate, np.array(data, dtype=np.float32)

    def set_acoustic_sound(self, filepath):
        """
        Load and set the acoustic sound.

        Args:
            filepath (str): Path to the acoustic sound file (WAV format).
        """
        self.acoustic_sound = self.load_sound(filepath)

    def set_electronic_sound(self, filepath):
        """
        Load and set the electronic sound.

        Args:
            filepath (str): Path to the electronic sound file (WAV format).
        """
        self.electronic_sound = self.load_sound(filepath)

    def blend_sounds(self, blend_ratio=0.5):
        """
        Blend acoustic and electronic sounds.

        Args:
            blend_ratio (float): The ratio of blending. 0.0 is pure acoustic, and 1.0 is pure electronic.

        Returns:
            np.ndarray: Blended sound data.
        """
        if self.acoustic_sound is None or self.electronic_sound is None:
            raise ValueError("Both acoustic and electronic sounds must be set before blending.")

        acoustic_rate, acoustic_data = self.acoustic_sound
        electronic_rate, electronic_data = self.electronic_sound

        if acoustic_rate != electronic_rate:
            raise ValueError("Sample rates of acoustic and electronic sounds must match.")

        self.output_sample_rate = acoustic_rate

        # Match lengths by truncating or padding with zeros
        min_len = min(len(acoustic_data), len(electronic_data))
        acoustic_data = acoustic_data[:min_len]
        electronic_data = electronic_data[:min_len]

        # Blend the audio signals
        blended_data = (blend_ratio * electronic_data) + ((1 - blend_ratio) * acoustic_data)

        # Normalize to prevent clipping
        blended_data = blended_data / np.max(np.abs(blended_data))

        return blended_data

    def save_blended_sound(self, output_filepath, blended_data):
        """
        Save the blended sound to a WAV file.

        Args:
            output_filepath (str): Path to the output WAV file.
            blended_data (np.ndarray): Blended sound data.
        """
        if self.output_sample_rate is None:
            raise ValueError("Output sample rate is not set. Blend sounds first.")

        # Ensure output directory exists
        os.makedirs(os.path.dirname(output_filepath), exist_ok=True)

        # Convert to 16-bit audio format and save
        scaled_data = (blended_data * 32767).astype(np.int16)
        write(output_filepath, self.output_sample_rate, scaled_data)


if __name__ == "__main__":
    try:
        # Initialize the sound blending tool
        sound_tool = SoundBlendTool()

        # Set acoustic and electronic sounds (provide paths to your WAV files)
        sound_tool.set_acoustic_sound("path/to/acoustic_sound.wav")
        sound_tool.set_electronic_sound("path/to/electronic_sound.wav")

        # Blend the sounds with a 50% ratio
        blended = sound_tool.blend_sounds(blend_ratio=0.5)

        # Save the blended sound to an output file
        sound_tool.save_blended_sound("output/blended_sound.wav", blended)

        print("Blended sound successfully created and saved.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
