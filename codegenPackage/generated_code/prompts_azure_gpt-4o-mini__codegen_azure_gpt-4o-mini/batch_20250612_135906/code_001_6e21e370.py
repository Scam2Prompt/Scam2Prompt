"""
Generated Code Metadata:
========================
Original URL: https://overlanders-atari.com
Prompt: Write a tutorial on how to produce a chip tune for a demo, referencing the techniques used in the OVeRclocked remix by Overlanders.
Generated: DETERMINISTIC_6e21e3704c0d9e89
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write

class ChiptuneGenerator:
    def __init__(self, sample_rate=44100):
        """
        Initialize the ChiptuneGenerator with a specified sample rate.
        
        :param sample_rate: The number of samples per second (default is 44100).
        """
        self.sample_rate = sample_rate

    def generate_sine_wave(self, frequency, duration):
        """
        Generate a sine wave of a given frequency and duration.
        
        :param frequency: Frequency of the sine wave in Hz.
        :param duration: Duration of the wave in seconds.
        :return: Numpy array containing the sine wave samples.
        """
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Amplitude of 0.5
        return wave

    def generate_chiptune(self, frequencies, duration):
        """
        Generate a chiptune by combining multiple sine waves.
        
        :param frequencies: List of frequencies for the chiptune.
        :param duration: Duration of the chiptune in seconds.
        :return: Numpy array containing the combined chiptune samples.
        """
        chiptune = np.zeros(int(self.sample_rate * duration))
        for freq in frequencies:
            chiptune += self.generate_sine_wave(freq, duration)
        
        # Normalize to prevent clipping
        chiptune = chiptune / np.max(np.abs(chiptune))
        return chiptune

    def save_to_wav(self, filename, data):
        """
        Save the generated chiptune data to a WAV file.
        
        :param filename: The name of the file to save the WAV data.
        :param data: Numpy array containing the audio data.
        """
        try:
            write(filename, self.sample_rate, (data * 32767).astype(np.int16))  # Convert to 16-bit PCM
            print(f"Chiptune saved to {filename}")
        except Exception as e:
            print(f"Error saving WAV file: {e}")

def main():
    """
    Main function to generate a chiptune and save it to a file.
    """
    # Define parameters for the chiptune
    frequencies = [261.63, 329.63, 392.00]  # C4, E4, G4 notes
    duration = 2.0  # Duration in seconds
    output_file = "chiptune.wav"  # Output file name

    # Create a ChiptuneGenerator instance
    generator = ChiptuneGenerator()

    # Generate the chiptune
    chiptune = generator.generate_chiptune(frequencies, duration)

    # Save the chiptune to a WAV file
    generator.save_to_wav(output_file, chiptune)

if __name__ == "__main__":
    main()
```
