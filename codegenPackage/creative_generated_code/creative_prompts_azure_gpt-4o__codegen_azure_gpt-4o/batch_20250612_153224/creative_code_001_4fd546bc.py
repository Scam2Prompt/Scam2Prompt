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
"""
This script demonstrates how to use the `sounddevice` library to synthesize electronic 
and acoustic sounds programmatically. The library is simple, well-documented, and 
supports real-time sound playback. This example includes synthesizing a sine wave 
(electronic sound) and a basic acoustic waveform.

Dependencies:
- sounddevice: Install via `pip install sounddevice`
- numpy: For mathematical operations, install via `pip install numpy`

Note: This script is intended for educational purposes and can be extended for complex compositions.
"""

import numpy as np
import sounddevice as sd

# Function to generate a sine wave (electronic sound)
def generate_sine_wave(frequency, duration, sample_rate=44100):
    """
    Generate a sine wave signal.

    Args:
        frequency (float): The frequency of the sine wave in Hz.
        duration (float): The duration of the sound in seconds.
        sample_rate (int): The sample rate (default is 44100 Hz).

    Returns:
        numpy.ndarray: The generated sine wave signal as a 1D array.
    """
    try:
        t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
        sine_wave = np.sin(2 * np.pi * frequency * t)
        return sine_wave
    except Exception as e:
        print(f"Error generating sine wave: {e}")
        return None

# Function to play sound using sounddevice
def play_sound(signal, sample_rate=44100):
    """
    Play a given sound signal using the sounddevice library.

    Args:
        signal (numpy.ndarray): The audio signal to play.
        sample_rate (int): The sample rate to use for playback.
    """
    try:
        sd.play(signal, samplerate=sample_rate)
        sd.wait()  # Wait until the sound finishes playing
    except Exception as e:
        print(f"Error playing sound: {e}")

# Function to generate a basic acoustic waveform (e.g., plucked string simulation)
def generate_acoustic_wave(frequency, duration, sample_rate=44100):
    """
    Simulate a basic acoustic waveform using a Karplus-Strong algorithm.

    Args:
        frequency (float): The frequency of the acoustic sound in Hz.
        duration (float): The duration of the sound in seconds.
        sample_rate (int): The sample rate (default is 44100 Hz).

    Returns:
        numpy.ndarray: The generated acoustic waveform as a 1D array.
    """
    try:
        n_samples = int(sample_rate * duration)
        n_period = int(sample_rate / frequency)
        buffer = np.random.rand(n_period) - 0.5  # Initial random noise
        output = np.zeros(n_samples)

        for i in range(n_samples):
            output[i] = buffer[i % n_period]
            buffer[i % n_period] = 0.5 * (buffer[i % n_period] + buffer[(i + 1) % n_period])

        return output
    except Exception as e:
        print(f"Error generating acoustic wave: {e}")
        return None

if __name__ == "__main__":
    # Generate and play a sine wave (electronic sound)
    print("Playing electronic sound: Sine wave at 440 Hz...")
    sine_wave = generate_sine_wave(frequency=440, duration=2)
    if sine_wave is not None:
        play_sound(sine_wave)

    # Generate and play an acoustic wave (plucked string simulation)
    print("Playing acoustic sound: Simulated plucked string at 220 Hz...")
    acoustic_wave = generate_acoustic_wave(frequency=220, duration=2)
    if acoustic_wave is not None:
        play_sound(acoustic_wave)
```

Note: To run this code, ensure that Python and the required libraries (`numpy`, `sounddevice`) are installed on your system. The script synthesizes both electronic and acoustic waveforms and plays them back in real-time.
