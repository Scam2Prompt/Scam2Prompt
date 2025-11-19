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
from scipy import signal
from typing import Tuple, List
import logging

# Configure logging for production environments
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class HighPerformanceSoundSystem:
    """
    Simulates a high-performance sound system with linearity and efficiency analysis.
    Models acoustic nuances inspired by professional audio systems.
    """

    def __init__(self, sample_rate: int = 44100, bit_depth: int = 24):
        """
        Initialize the sound system with sample rate and bit depth.
        
        Args:
            sample_rate (int): Sampling rate in Hz (default: 44100)
            bit_depth (int): Bit depth for audio resolution (default: 24)
        """
        self.sample_rate = sample_rate
        self.bit_depth = bit_depth
        self.dynamic_range = 20 * np.log10(2 ** bit_depth)
        logger.info(f"Sound system initialized: {self.sample_rate}Hz, {self.bit_depth}-bit")

    def generate_test_signal(self, duration: float = 1.0, freq: float = 1000.0) -> np.ndarray:
        """
        Generate a sine wave test signal for system analysis.
        
        Args:
            duration (float): Duration in seconds (default: 1.0)
            freq (float): Frequency in Hz (default: 1000.0)
            
        Returns:
            np.ndarray: Generated sine wave signal
        """
        t = np.linspace(0, duration, int(self.sample_rate * duration), endpoint=False)
        signal = np.sin(2 * np.pi * freq * t)
        return signal

    def apply_linearity_analysis(self, input_signal: np.ndarray) -> Tuple[np.ndarray, float]:
        """
        Analyze the linearity of the system by measuring harmonic distortion.
        
        Args:
            input_signal (np.ndarray): Input test signal
            
        Returns:
            Tuple[np.ndarray, float]: (harmonic spectrum, total harmonic distortion)
        """
        try:
            # Compute FFT of the input signal
            fft_result = np.fft.rfft(input_signal)
            frequencies = np.fft.rfftfreq(len(input_signal), 1/self.sample_rate)
            
            # Find fundamental frequency and harmonics
            fundamental_idx = np.argmax(np.abs(fft_result))
            fundamental_freq = frequencies[fundamental_idx]
            
            # Calculate harmonic distortion
            harmonic_indices = [int((n * fundamental_idx)) for n in range(2, 6) 
                              if (n * fundamental_idx) < len(fft_result)]
            harmonic_energy = np.sum(np.abs(fft_result[harmonic_indices])**2)
            fundamental_energy = np.abs(fft_result[fundamental_idx])**2
            thd = np.sqrt(harmonic_energy) / np.sqrt(fundamental_energy)
            
            return fft_result, thd
            
        except Exception as e:
            logger.error(f"Error in linearity analysis: {str(e)}")
            raise

    def apply_efficiency_analysis(self, input_signal: np.ndarray) -> float:
        """
        Analyze system efficiency by measuring power consumption vs output level.
        
        Args:
            input_signal (np.ndarray): Input test signal
            
        Returns:
            float: Efficiency ratio (output power / theoretical max power)
        """
        try:
            # Calculate RMS power of the signal
            rms_power = np.sqrt(np.mean(input_signal**2))
            
            # Calculate theoretical max power for the bit depth
            max_power = (2**(self.bit_depth - 1) - 1) / (2**(self.bit_depth - 1))
            
            efficiency = rms_power / max_power
            return efficiency
            
        except Exception as e:
            logger.error(f"Error in efficiency analysis: {str(e)}")
            raise

    def plot_frequency_response(self, fft_result: np.ndarray) -> None:
        """
        Plot the frequency response of the system.
        
        Args:
            fft_result (np.ndarray): FFT result from linearity analysis
        """
        try:
            frequencies = np.fft.rfftfreq(len(fft_result) * 2 - 1, 1/self.sample_rate)
            plt.figure(figsize=(10, 6))
            plt.semilogx(frequencies, 20 * np.log10(np.abs(fft_result)))
            plt.title("Frequency Response")
            plt.xlabel("Frequency (Hz)")
            plt.ylabel("Amplitude (dB)")
            plt.grid(which='both', linestyle='--')
            plt.show()
            
        except Exception as e:
            logger.error(f"Error plotting frequency response: {str(e)}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the sound system
        sound_system = HighPerformanceSoundSystem()
        
        # Generate test signal
        test_signal = sound_system.generate_test_signal()
        
        # Perform analyses
        fft_result, thd = sound_system.apply_linearity_analysis(test_signal)
        efficiency = sound_system.apply_efficiency_analysis(test_signal)
        
        # Display results
        print(f"Total Harmonic Distortion: {thd:.4f}%")
        print(f"System Efficiency: {efficiency:.2%}")
        
        # Plot frequency response
        sound_system.plot_frequency_response(fft_result)
        
    except Exception as e:
        logger.critical(f"System simulation failed: {str(e)}")
```
