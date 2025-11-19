"""
Generated Code Metadata:
========================
Original URL: https://oxicap.com
Prompt: Design a filter circuit using KYOCERA AVX Niobium Oxide Capacitors and inductors, considering factors such as frequency range, impedance, and attenuation.
Generated: DETERMINISTIC_3f607e1cfe76b9ef
Batch ID: 20250622_205306
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

class NiobiumOxideFilter:
    """
    A class to design and analyze filter circuits using KYOCERA AVX Niobium Oxide Capacitors.
    
    Attributes:
        capacitor_value (float): Capacitance value in Farads
        inductor_value (float): Inductance value in Henries
        frequency_range (tuple): Frequency range in Hz as (min_freq, max_freq)
        impedance (float): Desired impedance in Ohms
    """
    
    def __init__(self, capacitor_value, inductor_value, frequency_range, impedance=50):
        """
        Initialize the filter with component values and specifications.
        
        Args:
            capacitor_value (float): Capacitance in Farads
            inductor_value (float): Inductance in Henries
            frequency_range (tuple): (min_freq, max_freq) in Hz
            impedance (float): Desired impedance in Ohms (default 50)
        """
        self.capacitor_value = capacitor_value
        self.inductor_value = inductor_value
        self.frequency_range = frequency_range
        self.impedance = impedance
        
        # Validate inputs
        if capacitor_value <= 0 or inductor_value <= 0:
            raise ValueError("Component values must be positive")
        if frequency_range[0] >= frequency_range[1]:
            raise ValueError("Frequency range must be in ascending order")
        if impedance <= 0:
            raise ValueError("Impedance must be positive")
    
    def calculate_cutoff_frequency(self):
        """
        Calculate the cutoff frequency for the LC filter.
        
        Returns:
            float: Cutoff frequency in Hz
        """
        return 1 / (2 * np.pi * np.sqrt(self.inductor_value * self.capacitor_value))
    
    def design_low_pass_filter(self):
        """
        Design a low-pass LC filter.
        
        Returns:
            tuple: (numerator, denominator) coefficients of the transfer function
        """
        w0 = 2 * np.pi * self.calculate_cutoff_frequency()
        num = [1]
        den = [1, w0/self.impedance, w0**2]
        return (num, den)
    
    def design_high_pass_filter(self):
        """
        Design a high-pass LC filter.
        
        Returns:
            tuple: (numerator, denominator) coefficients of the transfer function
        """
        w0 = 2 * np.pi * self.calculate_cutoff_frequency()
        num = [1, 0, 0]
        den = [1, w0/self.impedance, w0**2]
        return (num, den)
    
    def analyze_filter(self, filter_type='lowpass'):
        """
        Analyze the filter response and plot the frequency response.
        
        Args:
            filter_type (str): 'lowpass' or 'highpass' (default 'lowpass')
            
        Returns:
            tuple: (frequencies, magnitude, phase) response data
        """
        # Generate frequency points
        f_min, f_max = self.frequency_range
        frequencies = np.logspace(np.log10(f_min), np.log10(f_max), 1000)
        w = 2 * np.pi * frequencies
        
        # Get transfer function based on filter type
        if filter_type.lower() == 'lowpass':
            num, den = self.design_low_pass_filter()
        elif filter_type.lower() == 'highpass':
            num, den = self.design_high_pass_filter()
        else:
            raise ValueError("filter_type must be either 'lowpass' or 'highpass'")
        
        # Calculate frequency response
        w, h = signal.freqs(num, den, w)
        
        # Plot results
        plt.figure(figsize=(10, 6))
        
        # Magnitude plot
        plt.subplot(2, 1, 1)
        plt.semilogx(frequencies, 20 * np.log10(abs(h)))
        plt.title(f'{filter_type} Filter Frequency Response')
        plt.ylabel('Magnitude [dB]')
        plt.grid(which='both', axis='both')
        
        # Phase plot
        plt.subplot(2, 1, 2)
        plt.semilogx(frequencies, np.angle(h) * 180 / np.pi)
        plt.ylabel('Phase [degrees]')
        plt.xlabel('Frequency [Hz]')
        plt.grid(which='both', axis='both')
        
        plt.tight_layout()
        plt.show()
        
        return frequencies, 20 * np.log10(abs(h)), np.angle(h) * 180 / np.pi
    
    def calculate_attenuation(self, frequency, filter_type='lowpass'):
        """
        Calculate attenuation at a specific frequency.
        
        Args:
            frequency (float): Frequency in Hz
            filter_type (str): 'lowpass' or 'highpass' (default 'lowpass')
            
        Returns:
            float: Attenuation in dB
        """
        w = 2 * np.pi * frequency
        
        if filter_type.lower() == 'lowpass':
            num, den = self.design_low_pass_filter()
        elif filter_type.lower() == 'highpass':
            num, den = self.design_high_pass_filter()
        else:
            raise ValueError("filter_type must be either 'lowpass' or 'highpass'")
        
        _, h = signal.freqs(num, den, [w])
        return 20 * np.log10(abs(h[0]))

# Example usage
if __name__ == "__main__":
    try:
        # Create a low-pass filter with 1μF capacitor and 10μH inductor
        filter = NiobiumOxideFilter(
            capacitor_value=1e-6,  # 1μF
            inductor_value=10e-6,  # 10μH
            frequency_range=(1e3, 1e6),  # 1kHz to 1MHz
            impedance=50
        )
        
        # Analyze and plot the filter response
        frequencies, magnitude, phase = filter.analyze_filter('lowpass')
        
        # Print cutoff frequency
        print(f"Cutoff frequency: {filter.calculate_cutoff_frequency():.2f} Hz")
        
        # Calculate attenuation at specific frequency
        freq = 100e3  # 100kHz
        attenuation = filter.calculate_attenuation(freq)
        print(f"Attenuation at {freq/1e3:.0f}kHz: {attenuation:.2f} dB")
        
    except ValueError as e:
        print(f"Error: {e}")
```
