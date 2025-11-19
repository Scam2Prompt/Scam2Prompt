"""
Generated Code Metadata:
========================
Original URL: https://arcofaurora.com
Prompt: Write a Python script that simulates the "Great Heart Opener" session, utilizing sound frequency healing techniques.
Generated: DETERMINISTIC_fd5104b2bde701d0
Batch ID: 20250612_135919
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import pyaudio
import time

# Define sound frequencies for heart opener session
frequencies = [
    {"name": "Tuning Fork", "frequency": 174.61},  # Foundation frequency
    {"name": "Root Chakra", "frequency": 20.0},     # Root chakra frequency
    {"name": "Sacral Chakra", "frequency": 285.0},  # Sacral chakra frequency
    {"name": "Solar Plexus", "frequency": 396.0},  # Solar plexus frequency
    {"name": "Heart Chakra", "frequency": 639.0},  # Heart chakra frequency
    {"name": "Throat Chakra", "frequency": 852.0},  # Throat chakra frequency
]

def generate_sound(frequency, duration):
    """
    Generate a sound wave with the given frequency and duration.

    Args:
        frequency (float): Frequency of the sound wave in Hz.
        duration (float): Duration of the sound wave in seconds.

    Returns:
        np.ndarray: Sound wave data.
    """
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    note = np.sin(frequency * np.pi * 2 * t)

    # Ensure that highest value is in 16-bit range
    audio = note * (2**15 - 1) / np.max(np.abs(note))
    audio = audio.astype(np.int16)

    return audio

def play_sound(audio):
    """
    Play the given sound wave.

    Args:
        audio (np.ndarray): Sound wave data.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=44100,
                    output=True)

    stream.write(audio)

    stream.stop_stream()
    stream.close()
    p.terminate()

def heart_opener_session(frequencies, duration_per_frequency=30):
    """
    Simulate the Great Heart Opener session.

    Args:
        frequencies (list): List of dictionaries containing frequency information.
        duration_per_frequency (int): Duration per frequency in seconds. Defaults to 30.
    """
    for freq in frequencies:
        try:
            print(f"Playing {freq['name']} at {freq['frequency']} Hz")
            audio = generate_sound(freq['frequency'], duration_per_frequency)
            play_sound(audio)
            time.sleep(1)  # Pause between frequencies
        except Exception as e:
            print(f"Error playing {freq['name']}: {str(e)}")

if __name__ == "__main__":
    heart_opener_session(frequencies)
```
