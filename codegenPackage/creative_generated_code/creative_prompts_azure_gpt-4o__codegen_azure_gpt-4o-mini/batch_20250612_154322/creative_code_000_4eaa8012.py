"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://equipeleiafreitas.site
Prompt: Write Python code to simulate signal generation for PGSoft and Pragmatic platforms, incorporating user input for dynamic adjustments.
Generated: DETERMINISTIC_4eaa80128058ad31
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import numpy as np
import matplotlib.pyplot as plt

class SignalGenerator:
    """
    A class to simulate signal generation for PGSoft and Pragmatic platforms.
    This class allows for user-defined parameters to dynamically adjust the signal.
    """
    
    def __init__(self, platform: str, frequency: float, duration: float, amplitude: float):
        """
        Initializes the SignalGenerator with the specified parameters.
        
        Parameters:
        - platform (str): The target platform, either 'PGSoft' or 'Pragmatic'.
        - frequency (float): Frequency of the signal in Hz.
        - duration (float): Duration of the signal in seconds.
        - amplitude (float): Amplitude of the signal.
        """
        self.platform = platform
        self.frequency = frequency
        self.duration = duration
        self.amplitude = amplitude
        self.time = np.linspace(0, self.duration, int(self.duration * 1000))
        self.signal = self.generate_signal()

    def generate_signal(self) -> np.ndarray:
        """
        Generates a simulated signal based on the platform type.
        
        Returns:
        - np.ndarray: The generated signal values.
        """
        if self.platform not in ['PGSoft', 'Pragmatic']:
            raise ValueError("Invalid platform specified. Choose either 'PGSoft' or 'Pragmatic'.")
        
        # Determine the type of signal based on the platform
        if self.platform == 'PGSoft':
            return self.amplitude * np.sin(2 * np.pi * self.frequency * self.time) + self.noise()
        elif self.platform == 'Pragmatic':
            return self.amplitude * np.cos(2 * np.pi * self.frequency * self.time) + self.noise()

    def noise(self) -> np.ndarray:
        """
        Generates random noise to simulate real-world signal variations.
        
        Returns:
        - np.ndarray: Array of noise values.
        """
        noise_level = 0.1 * self.amplitude
        return random.uniform(-noise_level, noise_level) * np.ones_like(self.time)

    def plot_signal(self):
        """
        Plots the generated signal for visualization.
        """
        plt.figure(figsize=(10, 5))
        plt.plot(self.time, self.signal, label=f'Signal ({self.platform})')
        plt.title(f'Signal Generation for {self.platform}')
        plt.xlabel('Time (s)')
        plt.ylabel('Amplitude')
        plt.grid()
        plt.legend()
        plt.show()

def main():
    """
    Main function to run the signal generator based on user input.
    """
    try:
        platform = input("Enter platform (PGSoft/Pragmatic): ").strip()
        frequency = float(input("Enter frequency (Hz): "))
        duration = float(input("Enter duration (seconds): "))
        amplitude = float(input("Enter amplitude: "))

        signal_generator = SignalGenerator(platform, frequency, duration, amplitude)
        signal_generator.plot_signal()
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
