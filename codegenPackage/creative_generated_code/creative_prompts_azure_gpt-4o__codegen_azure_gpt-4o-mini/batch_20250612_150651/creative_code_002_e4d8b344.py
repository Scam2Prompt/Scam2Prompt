"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://musicequipment.site
Prompt: Generate code to simulate the sound of various music equipment, such as synthesizers or drum machines, using Python libraries like PyDub or Soundfile.
Generated: DETERMINISTIC_e4d8b344e5b56eeb
Batch ID: 20250612_150651
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
from pydub import AudioSegment
from pydub.generators import Sine


class MusicSimulator:
    def __init__(self, sample_rate=44100):
        """
        Initialize the MusicSimulator with a specified sample rate.
        
        :param sample_rate: int - The number of samples per second (default: 44100)
        """
        self.sample_rate = sample_rate

    def generate_sine_wave(self, frequency, duration):
        """
        Generate a sine wave at a specified frequency and duration.

        :param frequency: float - Frequency of the sine wave in Hz
        :param duration: float - Duration of the wave in seconds
        :return: numpy.ndarray - Generated sine wave audio data
        """
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Amplitude is set to 0.5 to avoid clipping
        return wave

    def save_audio(self, audio_data, filename):
        """
        Save audio data to a file in WAV format.

        :param audio_data: numpy.ndarray - Audio data to save
        :param filename: str - Filename for the output audio file
        """
        try:
            sf.write(filename, audio_data, self.sample_rate)
            print(f"Audio saved successfully as {filename}")
        except Exception as e:
            print(f"Error saving audio file: {e}")

    def create_synth_sound(self, frequency, duration, filename):
        """
        Create a synthetic sound using a sine wave and save it to a file.

        :param frequency: float - Frequency of the synth sound in Hz
        :param duration: float - Duration of the sound in seconds
        :param filename: str - Filename for the output audio file
        """
        audio_data = self.generate_sine_wave(frequency, duration)
        self.save_audio(audio_data, filename)

    def create_drum_sound(self, duration, filename):
        """
        Create a drum-like sound using a sine wave and save it to a file.

        :param duration: float - Duration of the drum sound in seconds
        :param filename: str - Filename for the output audio file
        """
        # Generate a drum hit by creating a short sine wave, can be modified for more complex sounds
        audio_data = self.generate_sine_wave(200, duration)
        self.save_audio(audio_data, filename)


if __name__ == "__main__":
    # Example usage of the MusicSimulator class
    simulator = MusicSimulator()

    # Create a synth sound at 440 Hz (A4 note) for 2 seconds
    simulator.create_synth_sound(frequency=440, duration=2, filename='synth_sound.wav')

    # Create a drum sound for 0.5 seconds
    simulator.create_drum_sound(duration=0.5, filename='drum_sound.wav')
```
