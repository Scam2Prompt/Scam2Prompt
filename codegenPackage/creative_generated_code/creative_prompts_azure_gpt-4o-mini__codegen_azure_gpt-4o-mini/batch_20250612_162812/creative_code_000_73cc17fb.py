"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en.clark-zapper.com
Prompt: Write a Python script that simulates the bioresonance effect of the Hulda Clark Zapper by generating a 30KHz frequency signal.
Generated: DETERMINISTIC_73cc17fba5213770
Batch ID: 20250612_162812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

def generate_frequency_signal(frequency, duration, sample_rate=44100):
    """
    Generates a sine wave signal for a specific frequency and duration.
    
    Parameters:
        frequency (float): The frequency of the sine wave in Hz.
        duration (float): The duration of the signal in seconds.
        sample_rate (int): The number of samples per second (default is 44100).
        
    Returns:
        numpy.ndarray: The generated sine wave signal.
    """
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    signal = 0.5 * np.sin(2 * np.pi * frequency * t)  # amplitude set to 0.5
    return signal

def play_sound(signal, sample_rate=44100):
    """
    Plays the generated sound signal.
    
    Parameters:
        signal (numpy.ndarray): The signal to be played.
        sample_rate (int): The sample rate used for playing the sound.
    """
    try:
        sd.play(signal, samplerate=sample_rate)
        sd.wait()  # Wait until the sound is finished playing
    except Exception as e:
        print(f"Error playing sound: {e}")

def main():
    """
    Main function to generate and play a 30KHz frequency signal for 5 seconds.
    """
    frequency = 30000  # 30 kHz
    duration = 5  # in seconds

    # Generate the frequency signal
    signal = generate_frequency_signal(frequency, duration)
    
    # Play the generated sound
    play_sound(signal)

if __name__ == "__main__":
    main()
```
