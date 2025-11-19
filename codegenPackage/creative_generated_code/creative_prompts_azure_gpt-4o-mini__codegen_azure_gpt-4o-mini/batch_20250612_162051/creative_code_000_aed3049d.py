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
import soundfile as sf
import librosa

class SoundBlender:
    """
    A class to blend acoustic and electronic sounds using various techniques.
    """

    def __init__(self, acoustic_file, electronic_file):
        """
        Initializes the SoundBlender with paths to the acoustic and electronic sound files.

        :param acoustic_file: Path to the acoustic sound file (e.g., WAV, FLAC)
        :param electronic_file: Path to the electronic sound file (e.g., WAV, FLAC)
        """
        self.acoustic_file = acoustic_file
        self.electronic_file = electronic_file
        self.acoustic_signal = None
        self.electronic_signal = None

    def load_sounds(self):
        """
        Loads acoustic and electronic sound files into the instance.

        Raises:
            FileNotFoundError: If the sound files cannot be found.
            ValueError: If the sound files are not compatible (different sample rates).
        """
        try:
            self.acoustic_signal, self.acoustic_sr = sf.read(self.acoustic_file)
            self.electronic_signal, self.electronic_sr = sf.read(self.electronic_file)

            # Check for sample rate compatibility
            if self.acoustic_sr != self.electronic_sr:
                raise ValueError("Sample rates of acoustic and electronic sounds must match.")
        except FileNotFoundError as e:
            print(f"Error loading sound files: {e}")
            raise

    def blend_sounds(self, blend_ratio=0.5):
        """
        Blend the acoustic and electronic sounds based on a specified ratio.

        :param blend_ratio: Ratio of acoustic sound to electronic sound (0.0 to 1.0).
        :return: Blended sound array.
        """
        if self.acoustic_signal is None or self.electronic_signal is None:
            raise ValueError("Sound files must be loaded before blending.")

        # Ensure both signals are the same length
        min_length = min(len(self.acoustic_signal), len(self.electronic_signal))
        blended_signal = (blend_ratio * self.acoustic_signal[:min_length] +
                          (1 - blend_ratio) * self.electronic_signal[:min_length])

        return blended_signal

    def save_blended_sound(self, output_file, blended_signal):
        """
        Saves the blended sound to a specified output file.

        :param output_file: Path to save the blended sound (e.g., output.wav).
        :param blended_signal: The mixed sound array to save.
        """
        try:
            sf.write(output_file, blended_signal, self.acoustic_sr)
            print(f"Blended sound saved to: {output_file}")
        except Exception as e:
            print(f"Error saving blended sound: {e}")
            raise


# Example usage
if __name__ == "__main__":
    acoustic_path = "acoustic_sound.wav"
    electronic_path = "electronic_sound.wav"
    output_path = "blended_sound.wav"

    # Create an instance of SoundBlender
    blender = SoundBlender(acoustic_path, electronic_path)

    # Load sounds, blend them, and then save the result
    try:
        blender.load_sounds()
        blended = blender.blend_sounds(blend_ratio=0.6)
        blender.save_blended_sound(output_path, blended)
    except Exception as error:
        print(f"An error occurred: {error}")
```
