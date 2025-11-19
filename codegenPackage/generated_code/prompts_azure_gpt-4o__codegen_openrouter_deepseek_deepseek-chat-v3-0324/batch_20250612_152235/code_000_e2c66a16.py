"""
Generated Code Metadata:
========================
Original URL: https://alphatest.com
Prompt: Write Python code to simulate the use of AlphaTest µ HELIX ® fine pitch test probes for ICT/FCT testing with close center spacing, ensuring low signal crosstalk and impedance.
Generated: DETERMINISTIC_e2c66a162a6dfbce
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.signal import convolve
from typing import List, Tuple, Optional

class AlphaTestProbeSimulator:
    """
    Simulates AlphaTest µ HELIX fine pitch test probes for ICT/FCT testing.
    Handles signal propagation, crosstalk, and impedance characteristics.
    """
    
    def __init__(self, 
                 probe_count: int = 32,
                 pitch: float = 0.5,  # in mm
                 impedance: float = 50.0,  # ohms
                 crosstalk_coeff: float = 0.05,
                 sample_rate: float = 1e9):  # 1 GHz
        """
        Initialize the probe simulator with given parameters.
        
        Args:
            probe_count: Number of probes in the array
            pitch: Center-to-center spacing between probes (mm)
            impedance: Characteristic impedance of probes (ohms)
            crosstalk_coeff: Crosstalk coefficient between adjacent probes
            sample_rate: Sampling rate for signal simulation (Hz)
        """
        self.probe_count = probe_count
        self.pitch = pitch
        self.impedance = impedance
        self.crosstalk_coeff = crosstalk_coeff
        self.sample_rate = sample_rate
        
        # Initialize probe state (voltage, current)
        self.probe_states = np.zeros((probe_count, 2))
        
        # Create crosstalk matrix
        self.crosstalk_matrix = self._create_crosstalk_matrix()
        
    def _create_crosstalk_matrix(self) -> np.ndarray:
        """
        Create a crosstalk matrix based on probe spacing and coefficient.
        
        Returns:
            Crosstalk matrix where diagonal is 1.0 and adjacent probes have crosstalk
        """
        matrix = np.eye(self.probe_count)
        for i in range(self.probe_count):
            if i > 0:
                matrix[i, i-1] = self.crosstalk_coeff
            if i < self.probe_count - 1:
                matrix[i, i+1] = self.crosstalk_coeff
        return matrix
    
    def apply_signals(self, signals: np.ndarray) -> None:
        """
        Apply input signals to the probes.
        
        Args:
            signals: Array of signal values (voltage) for each probe
        """
        if signals.shape[0] != self.probe_count:
            raise ValueError(f"Expected {self.probe_count} signals, got {signals.shape[0]}")
            
        # Apply signals with crosstalk
        self.probe_states[:, 0] = np.dot(self.crosstalk_matrix, signals)
        
    def measure_signals(self, duration: float = 1e-6) -> np.ndarray:
        """
        Measure output signals from probes over specified duration.
        
        Args:
            duration: Measurement duration in seconds
            
        Returns:
            Array of measured signals with shape (probe_count, samples)
        """
        samples = int(duration * self.sample_rate)
        time = np.linspace(0, duration, samples)
        
        # Simulate signal propagation with some noise
        measured_signals = np.zeros((self.probe_count, samples))
        for i in range(self.probe_count):
            # Basic signal propagation model with impedance effects
            signal = self.probe_states[i, 0] * np.exp(-time * 1e6 / self.impedance)
            # Add some Gaussian noise
            noise = np.random.normal(0, 0.01, samples)
            measured_signals[i] = signal + noise
            
        return measured_signals
    
    def calculate_impedance(self, voltage: np.ndarray, current: np.ndarray) -> np.ndarray:
        """
        Calculate impedance from voltage and current measurements.
        
        Args:
            voltage: Array of voltage measurements
            current: Array of current measurements
            
        Returns:
            Array of impedance values
        """
        if voltage.shape != current.shape:
            raise ValueError("Voltage and current arrays must have same shape")
            
        # Avoid division by zero
        current_nonzero = np.where(current != 0, current, 1e-12)
        return np.abs(voltage / current_nonzero)
    
    def analyze_crosstalk(self, signals: np.ndarray) -> Tuple[float, np.ndarray]:
        """
        Analyze crosstalk between probes.
        
        Args:
            signals: Measured signals from all probes
            
        Returns:
            Tuple of (worst_case_crosstalk, crosstalk_matrix)
        """
        if signals.shape[0] != self.probe_count:
            raise ValueError(f"Expected {self.probe_count} probe signals, got {signals.shape[0]}")
            
        # Normalize signals
        normalized = signals / np.max(np.abs(signals), axis=1, keepdims=True)
        
        # Calculate crosstalk as correlation between adjacent probes
        crosstalk = np.zeros(self.probe_count - 1)
        for i in range(self.probe_count - 1):
            crosstalk[i] = np.correlate(normalized[i], normalized[i+1])[0]
            
        worst_case = np.max(crosstalk)
        return worst_case, crosstalk

# Example usage
if __name__ == "__main__":
    # Create a probe array with 16 probes, 0.5mm pitch
    probe_sim = AlphaTestProbeSimulator(probe_count=16, pitch=0.5)
    
    # Generate test signals (square waves for example)
    test_signals = np.zeros(16)
    test_signals[::2] = 3.3  # Alternate probes at 3.3V
    
    # Apply signals
    probe_sim.apply_signals(test_signals)
    
    # Measure signals for 1 microsecond
    measured = probe_sim.measure_signals(1e-6)
    
    # Analyze crosstalk
    worst_case, crosstalk = probe_sim.analyze_crosstalk(measured)
    print(f"Worst case crosstalk: {worst_case:.4f}")
    
    # Calculate impedance (example with dummy current data)
    current = np.random.uniform(0.01, 0.1, measured.shape)
    impedance = probe_sim.calculate_impedance(measured, current)
    print(f"Average impedance: {np.mean(impedance):.2f} ohms")
```
