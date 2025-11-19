"""
Generated Code Metadata:
========================
Original URL: https://en.clark-zapper.com
Prompt: What libraries can I use in Python to create a program that controls a frequency generator for therapeutic purposes, similar to the Zapper mentioned on the Clark Zapper site?
Generated: DETERMINISTIC_fac781847d9cb772
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
import sounddevice as sd
import time
import argparse
from typing import Optional, Tuple

class FrequencyGenerator:
    """
    A class to generate and play therapeutic frequency signals similar to a Zapper device.
    """
    
    def __init__(self, sample_rate: int = 44100, duration: float = 1.0):
        """
        Initialize the FrequencyGenerator.
        
        Args:
            sample_rate (int): Sampling rate in Hz. Default is 44100.
            duration (float): Duration of each frequency pulse in seconds. Default is 1.0.
        """
        self.sample_rate = sample_rate
        self.duration = duration
        self.is_playing = False

    def generate_sine_wave(self, frequency: float, amplitude: float = 0.5) -> np.ndarray:
        """
        Generate a sine wave signal of the given frequency and amplitude.
        
        Args:
            frequency (float): Frequency of the sine wave in Hz.
            amplitude (float): Amplitude of the sine wave (0.0 to 1.0). Default is 0.5.
            
        Returns:
            np.ndarray: Generated sine wave signal.
        """
        t = np.linspace(0, self.duration, int(self.sample_rate * self.duration), endpoint=False)
        signal = amplitude * np.sin(2 * np.pi * frequency * t)
        return signal

    def play_frequency(self, frequency: float, amplitude: float = 0.5) -> None:
        """
        Play a single frequency for the specified duration.
        
        Args:
            frequency (float): Frequency to play in Hz.
            amplitude (float): Amplitude of the signal (0.0 to 1.0). Default is 0.5.
        """
        try:
            signal = self.generate_sine_wave(frequency, amplitude)
            self.is_playing = True
            sd.play(signal, self.sample_rate)
            time.sleep(self.duration)
            sd.stop()
            self.is_playing = False
        except Exception as e:
            print(f"Error playing frequency: {e}")
            self.is_playing = False

    def play_frequency_sequence(self, frequencies: list, amplitudes: Optional[list] = None) -> None:
        """
        Play a sequence of frequencies with optional amplitudes.
        
        Args:
            frequencies (list): List of frequencies to play in Hz.
            amplitudes (list, optional): List of amplitudes for each frequency. 
                                        If None, default amplitude (0.5) is used for all.
        """
        if amplitudes is None:
            amplitudes = [0.5] * len(frequencies)
        
        if len(frequencies) != len(amplitudes):
            raise ValueError("Length of frequencies and amplitudes must match.")
        
        for freq, amp in zip(frequencies, amplitudes):
            if not self.is_playing:  # Allow early termination
                break
            self.play_frequency(freq, amp)

def parse_args() -> Tuple[list, list, float]:
    """
    Parse command-line arguments for frequencies, amplitudes, and duration.
    
    Returns:
        Tuple[list, list, float]: Frequencies, amplitudes, and duration.
    """
    parser = argparse.ArgumentParser(description="Therapeutic Frequency Generator")
    parser.add_argument(
        "-f", "--frequencies", 
        nargs="+", 
        type=float, 
        required=True,
        help="List of frequencies in Hz (e.g., 1000 2000 3000)"
    )
    parser.add_argument(
        "-a", "--amplitudes", 
        nargs="+", 
        type=float, 
        help="List of amplitudes (0.0 to 1.0) for each frequency"
    )
    parser.add_argument(
        "-d", "--duration", 
        type=float, 
        default=1.0,
        help="Duration of each frequency pulse in seconds"
    )
    args = parser.parse_args()
    return args.frequencies, args.amplitudes, args.duration

def main():
    """Main function to run the frequency generator."""
    try:
        frequencies, amplitudes, duration = parse_args()
        generator = FrequencyGenerator(duration=duration)
        generator.is_playing = True
        generator.play_frequency_sequence(frequencies, amplitudes)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
