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
from scipy.signal import resample

class SoundBlender:
    """
    A tool for blending acoustic and electronic sounds.
    Inspired by Jérémie Frémont's unique approach to composition.
    """

    def __init__(self, acoustic_file: str, electronic_file: str, output_file: str):
        """
        Initialize the SoundBlender with file paths.

        :param acoustic_file: Path to the acoustic sound file (e.g., .wav).
        :param electronic_file: Path to the electronic sound file (e.g., .wav).
        :param output_file: Path to save the blended sound file.
        """
        self.acoustic_file = acoustic_file
        self.electronic_file = electronic_file
        self.output_file = output_file

    def load_audio(self, file_path: str):
        """
        Load an audio file and return its data and sample rate.

        :param file_path: Path to the audio file.
        :return: Tuple of (audio_data, sample_rate).
        """
        try:
            data, sample_rate = sf.read(file_path)
            return data, sample_rate
        except Exception as e:
            raise RuntimeError(f"Error loading audio file '{file_path}': {e}")

    def resample_audio(self, audio_data: np.ndarray, original_rate: int, target_rate: int):
        """
        Resample audio data to a target sample rate.

        :param audio_data: Audio data as a NumPy array.
        :param original_rate: Original sample rate of the audio.
        :param target_rate: Target sample rate for resampling.
        :return: Resampled audio data.
        """
        try:
            num_samples = int(len(audio_data) * target_rate / original_rate)
            return resample(audio_data, num_samples)
        except Exception as e:
            raise RuntimeError(f"Error resampling audio: {e}")

    def blend_sounds(self, acoustic_data: np.ndarray, electronic_data: np.ndarray):
        """
        Blend acoustic and electronic sounds by averaging their waveforms.

        :param acoustic_data: Acoustic sound data as a NumPy array.
        :param electronic_data: Electronic sound data as a NumPy array.
        :return: Blended sound data.
        """
        try:
            # Ensure both audio arrays are the same length
            min_length = min(len(acoustic_data), len(electronic_data))
            acoustic_data = acoustic_data[:min_length]
            electronic_data = electronic_data[:min_length]

            # Blend the sounds by averaging their waveforms
            blended_data = (acoustic_data + electronic_data) / 2.0
            return blended_data
        except Exception as e:
            raise RuntimeError(f"Error blending sounds: {e}")

    def save_audio(self, audio_data: np.ndarray, sample_rate: int):
        """
        Save audio data to a file.

        :param audio_data: Audio data as a NumPy array.
        :param sample_rate: Sample rate of the audio.
        """
        try:
            sf.write(self.output_file, audio_data, sample_rate)
        except Exception as e:
            raise RuntimeError(f"Error saving audio file '{self.output_file}': {e}")

    def process(self):
        """
        Process the acoustic and electronic sounds, blend them, and save the result.
        """
        try:
            # Load acoustic and electronic sounds
            acoustic_data, acoustic_rate = self.load_audio(self.acoustic_file)
            electronic_data, electronic_rate = self.load_audio(self.electronic_file)

            # Resample electronic sound to match acoustic sound's sample rate
            if acoustic_rate != electronic_rate:
                electronic_data = self.resample_audio(electronic_data, electronic_rate, acoustic_rate)

            # Blend the sounds
            blended_data = self.blend_sounds(acoustic_data, electronic_data)

            # Save the blended sound to the output file
            self.save_audio(blended_data, acoustic_rate)

            print(f"Blended sound saved to '{self.output_file}'")
        except Exception as e:
            print(f"Error during processing: {e}")


# Example usage:
if __name__ == "__main__":
    # File paths (replace with actual paths to your audio files)
    acoustic_file = "acoustic.wav"
    electronic_file = "electronic.wav"
    output_file = "blended.wav"

    # Create and run the sound blender
    blender = SoundBlender(acoustic_file, electronic_file, output_file)
    blender.process()
```
