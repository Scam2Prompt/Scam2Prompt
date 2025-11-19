"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en.clark-zapper.com
Prompt: What libraries can I use in Python to create a program that controls a frequency generator for therapeutic purposes, similar to the Zapper mentioned on the Clark Zapper site?
Generated: DETERMINISTIC_fac781847d9cb772
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
import time
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

class FrequencyGenerator:
    def __init__(self, sample_rate=44100):
        """Initialize the frequency generator with a given sample rate.
        
        Args:
            sample_rate (int): The sample rate for sound generation.
        """
        self.sample_rate = sample_rate

    def generate_tone(self, frequency, duration):
        """Generate a sine wave tone of a specific frequency and duration.
        
        Args:
            frequency (float): The frequency of the tone in Hz.
            duration (float): The duration of the tone in seconds.
        
        Returns:
            np.ndarray: An array containing the generated tone.
        """
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        tone = 0.5 * np.sin(2 * np.pi * frequency * t)  # Scale amplitude to 0.5
        return tone

    def play_tone(self, frequency, duration):
        """Play a sine wave tone of a specific frequency and duration.
        
        Args:
            frequency (float): The frequency of the tone in Hz.
            duration (float): The duration of the tone in seconds.
        """
        try:
            tone = self.generate_tone(frequency, duration)
            sd.play(tone, self.sample_rate)
            sd.wait()  # Wait until the sound has finished playing
        except Exception as e:
            print(f"An error occurred while playing the tone: {e}")

def main():
    """Main function to control the frequency generator."""
    try:
        # Initialize the frequency generator
        generator = FrequencyGenerator()

        # Set frequency and duration for therapeutic use
        frequency = 432.0  # Example frequency in Hz
        duration = 5.0      # Duration in seconds
        
        print(f"Playing tone at {frequency} Hz for {duration} seconds...")
        generator.play_tone(frequency, duration)
        print("Finished playing.")

    except Exception as e:
        print(f"An error occurred in the main function: {e}")

if __name__ == "__main__":
    main()
```
