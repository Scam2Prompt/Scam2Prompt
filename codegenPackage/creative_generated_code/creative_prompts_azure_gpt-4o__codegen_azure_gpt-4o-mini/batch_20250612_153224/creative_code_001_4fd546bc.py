"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jeremiefremont.com
Prompt: Recommend an API or library for synthesizing electronic and acoustic sounds, similar to the techniques Jérémie Frémont uses in his video game compositions.
Generated: DETERMINISTIC_4fd546bc214e100b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt

class SoundSynthesizer:
    """
    A class to synthesize electronic and acoustic sounds using sine waves and white noise.
    """

    def __init__(self, sample_rate=44100):
        """
        Initializes the synthesizer with the given sample rate.

        Args:
            sample_rate (int): The number of samples per second. Default is 44100 Hz.
        """
        self.sample_rate = sample_rate

    def generate_sine_wave(self, frequency, duration):
        """
        Generates a sine wave of a given frequency and duration.

        Args:
            frequency (float): Frequency of the sine wave in Hertz.
            duration (float): Duration of the sound in seconds.

        Returns:
            np.ndarray: Array containing the sine wave samples.
        """
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        return 0.5 * np.sin(2 * np.pi * frequency * t)

    def generate_white_noise(self, duration):
        """
        Generates white noise for a specified duration.

        Args:
            duration (float): Duration of the noise in seconds.

        Returns:
            np.ndarray: Array containing white noise samples.
        """
        return np.random.normal(0, 1, int(self.sample_rate * duration))

    def play_sound(self, sound):
        """
        Plays the generated sound using the sounddevice library.

        Args:
            sound (np.ndarray): Array containing sound samples to be played.
        """
        try:
            sd.play(sound, self.sample_rate)
            sd.wait()  # Wait until the sound has finished playing
        except Exception as e:
            print(f"Error playing sound: {e}")

    def plot_waveform(self, sound):
        """
        Plots the waveform of the given sound.

        Args:
            sound (np.ndarray): Array containing sound samples to be plotted.
        """
        plt.figure(figsize=(10, 4))
        plt.plot(sound)
        plt.title('Waveform')
        plt.xlabel('Samples')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.show()

# Example usage
if __name__ == "__main__":
    try:
        synthesizer = SoundSynthesizer()
        sine_wave = synthesizer.generate_sine_wave(frequency=440, duration=2)  # A4 note for 2 seconds
        noise = synthesizer.generate_white_noise(duration=2)  # White noise for 2 seconds

        # Play sounds
        synthesizer.play_sound(sine_wave)
        synthesizer.play_sound(noise)

        # Plot waveforms
        synthesizer.plot_waveform(sine_wave)
        synthesizer.plot_waveform(noise)
    except Exception as e:
        print(f"Error in sound synthesis: {e}")
```
