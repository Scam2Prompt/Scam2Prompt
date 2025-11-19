"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: Create a code snippet that simulates an immersive audio experience for an event, inspired by the projects showcased in Sound Source's portfolio.
Generated: DETERMINISTIC_09f63b69de3d95c4
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

class ImmersiveAudioExperience:
    def __init__(self, sample_rate=44100, duration=10):
        """
        Initializes the immersive audio experience.

        :param sample_rate: The sample rate for audio playback (default is 44100 Hz).
        :param duration: The duration of the audio experience in seconds (default is 10 seconds).
        """
        self.sample_rate = sample_rate
        self.duration = duration
        self.time = np.linspace(0, self.duration, int(self.sample_rate * self.duration), endpoint=False)

    def generate_sound_wave(self, frequency, amplitude=0.5):
        """
        Generates a sine wave sound.

        :param frequency: Frequency of the sine wave in Hz.
        :param amplitude: Amplitude of the sound wave (default is 0.5).
        :return: Numpy array containing the sound wave.
        """
        return amplitude * np.sin(2 * np.pi * frequency * self.time)

    def play_audio(self, sound_wave):
        """
        Plays the generated sound wave.

        :param sound_wave: Numpy array containing the sound wave to be played.
        """
        try:
            sd.play(sound_wave, self.sample_rate)
            sd.wait()  # Wait until sound has finished playing
        except Exception as e:
            print(f"Error playing audio: {e}")

    def create_immersive_experience(self):
        """
        Creates and plays an immersive audio experience by layering multiple sound waves.
        """
        try:
            # Generate multiple sound waves at different frequencies
            frequencies = [440, 554.37, 659.25, 739.99]  # A4, C#5, E5, F#5
            sound_wave = sum(self.generate_sound_wave(freq) for freq in frequencies)

            # Normalize the sound wave to prevent clipping
            sound_wave /= np.max(np.abs(sound_wave))

            # Play the immersive audio experience
            self.play_audio(sound_wave)

        except Exception as e:
            print(f"Error creating immersive experience: {e}")

if __name__ == "__main__":
    immersive_audio = ImmersiveAudioExperience()
    immersive_audio.create_immersive_experience()
```
