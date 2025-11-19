"""
Generated Code Metadata:
========================
Original URL: https://bangzoomonline.com
Prompt: "Generate code to simulate room acoustics for a home studio, considering factors mentioned in Bangzoom's acoustic design research."
Generated: DETERMINISTIC_8021769741d2ed6c
Batch ID: 20250622_212254
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
from scipy.io import wavfile

class RoomAcousticsSimulator:
    """
    Simulates room acoustics for a home studio based on Bangzoom's acoustic design research.
    Handles reflection, absorption, reverberation, and frequency response.
    """
    
    def __init__(self, room_dimensions, absorption_coefficients, sample_rate=44100):
        """
        Initialize the simulator with room parameters.
        
        Args:
            room_dimensions (tuple): (length, width, height) in meters
            absorption_coefficients (dict): Material absorption coefficients by frequency band
            sample_rate (int): Audio sample rate in Hz
        """
        self.length, self.width, self.height = room_dimensions
        self.absorption = absorption_coefficients
        self.sample_rate = sample_rate
        self.rt60 = self._calculate_rt60()
        
    def _calculate_rt60(self):
        """
        Calculate RT60 (reverberation time) using Sabine's formula.
        
        Returns:
            float: RT60 time in seconds
        """
        volume = self.length * self.width * self.height
        surface_area = 2 * (self.length*self.width + self.length*self.height + self.width*self.height)
        
        # Average absorption coefficient across frequency bands
        avg_absorption = np.mean(list(self.absorption.values()))
        
        # Sabine's formula
        rt60 = (0.161 * volume) / (surface_area * avg_absorption)
        return rt60
    
    def _generate_ir(self, duration=3.0):
        """
        Generate impulse response based on room acoustics.
        
        Args:
            duration (float): Duration of impulse response in seconds
            
        Returns:
            numpy.ndarray: Impulse response
        """
        t = np.linspace(0, duration, int(duration * self.sample_rate), False)
        
        # Early reflections (first 50ms)
        early_reflections = np.zeros_like(t)
        early_times = [0.005, 0.010, 0.015, 0.020, 0.025, 0.030, 0.035, 0.040, 0.045]
        early_gains = [0.8, 0.6, 0.5, 0.4, 0.3, 0.25, 0.2, 0.15, 0.1]
        
        for time, gain in zip(early_times, early_gains):
            idx = int(time * self.sample_rate)
            if idx < len(early_reflections):
                early_reflections[idx] = gain
        
        # Late reverberation (exponential decay)
        decay = np.exp(-t / (self.rt60 / 6.91))  # 6.91 ≈ ln(1000)
        noise = np.random.normal(0, 1, len(t)) * 0.1
        late_reverb = noise * decay
        
        # Combine components
        impulse_response = early_reflections + late_reverb
        return impulse_response / np.max(np.abs(impulse_response))
    
    def apply_room_acoustics(self, input_signal):
        """
        Apply room acoustics to an input audio signal.
        
        Args:
            input_signal (numpy.ndarray): Input audio signal
            
        Returns:
            numpy.ndarray: Processed audio signal with room acoustics
        """
        if len(input_signal.shape) > 1:
            input_signal = np.mean(input_signal, axis=1)  # Convert to mono
            
        impulse_response = self._generate_ir()
        processed_signal = signal.fftconvolve(input_signal, impulse_response, mode='same')
        
        # Apply frequency-dependent absorption
        freqs = np.fft.rfftfreq(len(processed_signal), 1/self.sample_rate)
        fft_signal = np.fft.rfft(processed_signal)
        
        # Interpolate absorption coefficients for all frequencies
        absorption_freqs = np.array(list(self.absorption.keys()))
        absorption_vals = np.array(list(self.absorption.values()))
        absorption_interp = np.interp(freqs, absorption_freqs, absorption_vals)
        
        # Apply absorption
        fft_signal *= (1 - absorption_interp)
        processed_signal = np.fft.irfft(fft_signal)
        
        return processed_signal / np.max(np.abs(processed_signal))
    
    def plot_frequency_response(self):
        """Plot the frequency response of the room."""
        impulse_response = self._generate_ir()
        freqs, response = signal.freqz(impulse_response, fs=self.sample_rate)
        
        plt.figure(figsize=(10, 4))
        plt.semilogx(freqs, 20 * np.log10(np.abs(response)))
        plt.title('Room Frequency Response')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Amplitude (dB)')
        plt.grid(True)
        plt.show()
    
    def save_processed_audio(self, input_file, output_file):
        """
        Process an audio file and save the result.
        
        Args:
            input_file (str): Path to input audio file
            output_file (str): Path to save processed audio
        """
        try:
            rate, data = wavfile.read(input_file)
            if rate != self.sample_rate:
                raise ValueError(f"Sample rate mismatch: expected {self.sample_rate}, got {rate}")
                
            processed = self.apply_room_acoustics(data)
            wavfile.write(output_file, self.sample_rate, processed)
        except Exception as e:
            print(f"Error processing audio file: {str(e)}")


# Example usage
if __name__ == "__main__":
    # Room dimensions (length, width, height) in meters
    room_dims = (5.0, 4.0, 2.8)
    
    # Absorption coefficients by frequency band (Hz)
    absorption_coeffs = {
        125: 0.1,
        250: 0.2,
        500: 0.3,
        1000: 0.4,
        2000: 0.5,
        4000: 0.6
    }
    
    # Create simulator
    simulator = RoomAcousticsSimulator(room_dims, absorption_coeffs)
    
    # Generate a test signal (1 second of white noise)
    test_signal = np.random.normal(0, 0.1, simulator.sample_rate)
    
    # Process the signal
    processed_signal = simulator.apply_room_acoustics(test_signal)
    
    # Plot frequency response
    simulator.plot_frequency_response()
    
    # Save processed audio (uncomment to use with real files)
    # simulator.save_processed_audio("input.wav", "output.wav")
```
