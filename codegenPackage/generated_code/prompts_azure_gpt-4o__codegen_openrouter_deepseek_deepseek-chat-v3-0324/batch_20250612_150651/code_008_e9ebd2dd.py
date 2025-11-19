"""
Generated Code Metadata:
========================
Original URL: https://musicequipment.site
Prompt: Generate code to visualize frequency response graphs for various audio equipment using Matplotlib in Python.
Generated: DETERMINISTIC_e9ebd2dd0612ac66
Batch ID: 20250612_150651
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
from scipy import signal
import sounddevice as sd
import warnings
from typing import List, Dict, Optional, Tuple

class FrequencyResponseVisualizer:
    """
    A class to visualize frequency response graphs for audio equipment using Matplotlib.
    Supports generating frequency response plots from transfer functions or live audio input.
    """
    
    def __init__(self, sample_rate: int = 44100, fft_size: int = 4096):
        """
        Initialize the visualizer with audio parameters.
        
        Args:
            sample_rate: Sampling rate in Hz (default: 44100)
            fft_size: Size of FFT window (default: 4096)
        """
        self.sample_rate = sample_rate
        self.fft_size = fft_size
        self.frequencies = np.fft.rfftfreq(fft_size, d=1.0/sample_rate)
        
    def plot_transfer_function(self, numerator: np.ndarray, denominator: np.ndarray, 
                              title: str = "Frequency Response", xlim: Tuple[float, float] = (20, 20000),
                              ylim: Tuple[float, float] = (-24, 24)) -> plt.Figure:
        """
        Plot frequency response from a transfer function.
        
        Args:
            numerator: Numerator coefficients of the transfer function
            denominator: Denominator coefficients of the transfer function
            title: Plot title (default: "Frequency Response")
            xlim: Tuple of (min, max) frequency limits (default: (20, 20000))
            ylim: Tuple of (min, max) amplitude limits in dB (default: (-24, 24))
            
        Returns:
            matplotlib Figure object
        """
        try:
            # Calculate frequency response
            w, h = signal.freqz(numerator, denominator, worN=self.fft_size, fs=self.sample_rate)
            magnitude = 20 * np.log10(np.abs(h))
            
            # Create plot
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.semilogx(w, magnitude)
            ax.set_title(title)
            ax.set_xlabel('Frequency [Hz]')
            ax.set_ylabel('Magnitude [dB]')
            ax.set_xlim(xlim)
            ax.set_ylim(ylim)
            ax.grid(which='both', linestyle='-', linewidth=0.5)
            
            return fig
        
        except Exception as e:
            raise RuntimeError(f"Error plotting transfer function: {str(e)}")
    
    def plot_impulse_response(self, impulse_response: np.ndarray, 
                             title: str = "Frequency Response from Impulse Response",
                             xlim: Tuple[float, float] = (20, 20000),
                             ylim: Tuple[float, float] = (-24, 24)) -> plt.Figure:
        """
        Plot frequency response from an impulse response.
        
        Args:
            impulse_response: Array containing the impulse response
            title: Plot title (default: "Frequency Response from Impulse Response")
            xlim: Tuple of (min, max) frequency limits (default: (20, 20000))
            ylim: Tuple of (min, max) amplitude limits in dB (default: (-24, 24))
            
        Returns:
            matplotlib Figure object
        """
        try:
            # Calculate frequency response
            fft_result = np.fft.rfft(impulse_response, n=self.fft_size)
            magnitude = 20 * np.log10(np.abs(fft_result))
            
            # Create plot
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.semilogx(self.frequencies, magnitude)
            ax.set_title(title)
            ax.set_xlabel('Frequency [Hz]')
            ax.set_ylabel('Magnitude [dB]')
            ax.set_xlim(xlim)
            ax.set_ylim(ylim)
            ax.grid(which='both', linestyle='-', linewidth=0.5)
            
            return fig
        
        except Exception as e:
            raise RuntimeError(f"Error plotting impulse response: {str(e)}")
    
    def plot_live_frequency_response(self, duration: float = 1.0, 
                                    input_device: Optional[int] = None,
                                    output_device: Optional[int] = None,
                                    title: str = "Live Frequency Response",
                                    xlim: Tuple[float, float] = (20, 20000),
                                    ylim: Tuple[float, float] = (-24, 24)) -> plt.Figure:
        """
        Measure and plot frequency response from live audio input.
        
        Args:
            duration: Duration of measurement in seconds (default: 1.0)
            input_device: Input device ID (default: None for default device)
            output_device: Output device ID (default: None for default device)
            title: Plot title (default: "Live Frequency Response")
            xlim: Tuple of (min, max) frequency limits (default: (20, 20000))
            ylim: Tuple of (min, max) amplitude limits in dB (default: (-24, 24))
            
        Returns:
            matplotlib Figure object
        """
        try:
            # Generate test signal (logarithmic chirp)
            t = np.linspace(0, duration, int(self.sample_rate * duration))
            test_signal = signal.chirp(t, 20, duration, 20000, method='logarithmic')
            test_signal *= 0.5  # Reduce amplitude to avoid clipping
            
            # Play and record simultaneously
            recorded = sd.playrec(test_signal, samplerate=self.sample_rate,
                                 input_device=input_device, output_device=output_device,
                                 channels=1, blocking=True)
            
            # Calculate frequency response
            fft_input = np.fft.rfft(test_signal, n=self.fft_size)
            fft_output = np.fft.rfft(recorded[:, 0], n=self.fft_size)
            magnitude = 20 * np.log10(np.abs(fft_output / fft_input))
            
            # Create plot
            fig, ax = plt.subplots(figsize=(10, 6))
            ax.semilogx(self.frequencies, magnitude)
            ax.set_title(title)
            ax.set_xlabel('Frequency [Hz]')
            ax.set_ylabel('Magnitude [dB]')
            ax.set_xlim(xlim)
            ax.set_ylim(ylim)
            ax.grid(which='both', linestyle='-', linewidth=0.5)
            
            return fig
            
        except Exception as e:
            raise RuntimeError(f"Error during live measurement: {str(e)}")

# Example usage
if __name__ == "__main__":
    # Suppress warnings for cleaner output
    warnings.filterwarnings("ignore")
    
    try:
        # Create visualizer instance
        visualizer = FrequencyResponseVisualizer()
        
        # Example 1: Plot from transfer function (2nd order low-pass filter)
        b, a = signal.butter(2, 1000, 'low', fs=visualizer.sample_rate)
        fig1 = visualizer.plot_transfer_function(b, a, "Low-pass Filter Response")
        
        # Example 2: Plot from impulse response (same filter)
        t, imp = signal.impulse((b, a), fs=visualizer.sample_rate)
        fig2 = visualizer.plot_impulse_response(imp, "Low-pass Filter from Impulse Response")
        
        # Show plots
        plt.show()
        
        # Example 3: Live measurement (uncomment to use)
        # fig3 = visualizer.plot_live_frequency_response()
        # plt.show()
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
