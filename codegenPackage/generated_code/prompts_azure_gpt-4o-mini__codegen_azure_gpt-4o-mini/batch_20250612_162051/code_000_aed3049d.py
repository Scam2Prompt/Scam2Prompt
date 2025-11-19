"""
Generated Code Metadata:
========================
Original URL: https://jeremiefremont.com
Prompt: Generate a code snippet for a sound design tool that can blend acoustic and electronic sounds, inspired by Jérémie Frémont's unique approach to composition.
Generated: DETERMINISTIC_aed3049d3351a17d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import soundfile as sf
import librosa

class SoundBlender:
    """
    A class to blend acoustic and electronic sounds.
    """

    def __init__(self, acoustic_file: str, electronic_file: str):
        """
        Initializes the SoundBlender with paths to the acoustic and electronic sound files.

        :param acoustic_file: Path to the acoustic sound file (WAV format).
        :param electronic_file: Path to the electronic sound file (WAV format).
        """
        self.acoustic_file = acoustic_file
        self.electronic_file = electronic_file
        self.acoustic_data = None
        self.electronic_data = None

    def load_sounds(self):
        """
        Loads the acoustic and electronic sound files into memory.
        """
        try:
            self.acoustic_data, self.acoustic_sr = sf.read(self.acoustic_file)
            self.electronic_data, self.electronic_sr = sf.read(self.electronic_file)

            # Ensure both sounds have the same sample rate
            if self.acoustic_sr != self.electronic_sr:
                raise ValueError("Sample rates of the two files do not match.")
        except Exception as e:
            print(f"Error loading sound files: {e}")

    def blend_sounds(self, blend_ratio: float = 0.5) -> np.ndarray:
        """
        Blends the acoustic and electronic sounds based on the specified blend ratio.

        :param blend_ratio: A float between 0 and 1 indicating the blend ratio.
                            0 means only acoustic, 1 means only electronic.
        :return: Blended sound as a NumPy array.
        """
        if self.acoustic_data is None or self.electronic_data is None:
            raise ValueError("Sound files must be loaded before blending.")

        # Ensure blend_ratio is within valid range
        if not (0 <= blend_ratio <= 1):
            raise ValueError("Blend ratio must be between 0 and 1.")

        # Normalize the lengths of the two audio signals
        max_length = max(len(self.acoustic_data), len(self.electronic_data))
        acoustic_resampled = np.pad(self.acoustic_data, (0, max_length - len(self.acoustic_data)), 'constant')
        electronic_resampled = np.pad(self.electronic_data, (0, max_length - len(self.electronic_data)), 'constant')

        # Blend the sounds
        blended_sound = (1 - blend_ratio) * acoustic_resampled + blend_ratio * electronic_resampled
        return blended_sound

    def save_blended_sound(self, output_file: str, blended_sound: np.ndarray):
        """
        Saves the blended sound to a specified output file.

        :param output_file: Path to the output file (WAV format).
        :param blended_sound: The blended sound to save.
        """
        try:
            sf.write(output_file, blended_sound, self.acoustic_sr)
            print(f"Blended sound saved to {output_file}")
        except Exception as e:
            print(f"Error saving blended sound: {e}")

# Example usage
if __name__ == "__main__":
    acoustic_path = "path/to/acoustic.wav"
    electronic_path = "path/to/electronic.wav"
    output_path = "path/to/blended_output.wav"

    blender = SoundBlender(acoustic_path, electronic_path)
    blender.load_sounds()
    blended = blender.blend_sounds(blend_ratio=0.5)
    blender.save_blended_sound(output_path, blended)
```
