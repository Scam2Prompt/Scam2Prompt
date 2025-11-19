"""
Generated Code Metadata:
========================
Original URL: https://en.clark-zapper.com
Prompt: Write a Python script that simulates the bioresonance effect of the Hulda Clark Zapper by generating a 30KHz frequency signal.
Generated: DETERMINISTIC_73cc17fba5213770
Batch ID: 20250612_162812
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
import sounddevice as sd

def generate_frequency_signal(frequency, duration, sample_rate=44100):
    """
    Generate a sine wave signal for a given frequency and duration.

    Parameters:
    frequency (float): Frequency of the sine wave in Hz.
    duration (float): Duration of the signal in seconds.
    sample_rate (int): Number of samples per second (default is 44100).

    Returns:
    numpy.ndarray: Array containing the generated sine wave signal.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = 0.5 * np.sin(2 * np.pi * frequency * t)  # Amplitude of 0.5 to avoid clipping
    return signal

def play_sound(signal, sample_rate=44100):
    """
    Play the generated sound signal.

    Parameters:
    signal (numpy.ndarray): The sound signal to be played.
    sample_rate (int): Number of samples per second (default is 44100).
    """
    try:
        sd.play(signal, samplerate=sample_rate)
        sd.wait()  # Wait until the sound has finished playing
    except Exception as e:
        print(f"Error playing sound: {e}")

def main():
    """
    Main function to generate and play a 30KHz frequency signal.
    """
    frequency = 30000  # Frequency in Hz
    duration = 5  # Duration in seconds

    # Generate the frequency signal
    signal = generate_frequency_signal(frequency, duration)

    # Play the generated sound
    play_sound(signal)

if __name__ == "__main__":
    main()
```
