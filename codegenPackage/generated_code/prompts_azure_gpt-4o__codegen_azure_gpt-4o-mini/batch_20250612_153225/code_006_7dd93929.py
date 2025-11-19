"""
Generated Code Metadata:
========================
Original URL: https://soundsource.tn
Prompt: Write code to simulate the linearity and efficiency of high-performance sound systems, inspired by Sound Source's emphasis on acoustic nuances.
Generated: DETERMINISTIC_7dd939291ddc3d09
Batch ID: 20250612_153225
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
from scipy.signal import butter, lfilter

class HighPerformanceSoundSystem:
    """
    A class to simulate the linearity and efficiency of high-performance sound systems.
    This class focuses on generating sound waves and applying filters to simulate acoustic nuances.
    """

    def __init__(self, sample_rate=44100):
        """
        Initializes the sound system with a given sample rate.

        :param sample_rate: The number of samples per second (default is 44100 Hz).
        """
        self.sample_rate = sample_rate

    def generate_sine_wave(self, frequency, duration):
        """
        Generates a sine wave of a given frequency and duration.

        :param frequency: Frequency of the sine wave in Hertz.
        :param duration: Duration of the wave in seconds.
        :return: Numpy array containing the sine wave samples.
        """
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # Amplitude of 0.5
        return wave

    def butter_lowpass(self, cutoff, order=5):
        """
        Designs a lowpass Butterworth filter.

        :param cutoff: The cutoff frequency of the filter.
        :param order: The order of the filter (default is 5).
        :return: The filter coefficients (b, a).
        """
        nyquist = 0.5 * self.sample_rate
        normal_cutoff = cutoff / nyquist
        b, a = butter(order, normal_cutoff, btype='low', analog=False)
        return b, a

    def apply_filter(self, data, cutoff, order=5):
        """
        Applies a lowpass filter to the input data.

        :param data: The input signal to be filtered.
        :param cutoff: The cutoff frequency of the filter.
        :param order: The order of the filter (default is 5).
        :return: The filtered signal.
        """
        b, a = self.butter_lowpass(cutoff, order)
        filtered_data = lfilter(b, a, data)
        return filtered_data

    def plot_waveform(self, wave, title='Waveform'):
        """
        Plots the waveform of the given signal.

        :param wave: The signal to be plotted.
        :param title: Title of the plot.
        """
        plt.figure(figsize=(10, 4))
        plt.plot(wave)
        plt.title(title)
        plt.xlabel('Sample')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.show()

def main():
    """
    Main function to demonstrate the functionality of the HighPerformanceSoundSystem class.
    """
    try:
        sound_system = HighPerformanceSoundSystem()

        # Generate a sine wave
        frequency = 440  # A4 note
        duration = 2.0   # 2 seconds
        sine_wave = sound_system.generate_sine_wave(frequency, duration)

        # Apply a lowpass filter
        cutoff_frequency = 1000  # Cutoff frequency in Hz
        filtered_wave = sound_system.apply_filter(sine_wave, cutoff_frequency)

        # Plot the original and filtered waveforms
        sound_system.plot_waveform(sine_wave, title='Original Sine Wave')
        sound_system.plot_waveform(filtered_wave, title='Filtered Sine Wave')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
