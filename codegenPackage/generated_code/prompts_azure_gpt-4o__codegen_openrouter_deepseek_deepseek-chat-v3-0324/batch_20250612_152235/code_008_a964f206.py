"""
Generated Code Metadata:
========================
Original URL: https://alphatest.com
Prompt: Generate a Python program to analyze the performance of AlphaTest µ HELIX ® probes in RFID antenna testing, focusing on bandwidth and signal integrity.
Generated: DETERMINISTIC_a964f206df061eea
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
import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fft import fft, fftfreq
import os
import json
from datetime import datetime
from typing import Dict, List, Tuple, Optional

class RFIDProbeAnalyzer:
    """
    Analyzes performance of AlphaTest µ HELIX ® probes in RFID antenna testing.
    Focuses on bandwidth and signal integrity metrics.
    """
    
    def __init__(self, config_path: str = None):
        """
        Initialize analyzer with optional configuration.
        
        Args:
            config_path: Path to JSON configuration file. If None, uses defaults.
        """
        self.default_config = {
            'sample_rate': 1e6,  # Hz
            'bandwidth_threshold': -3,  # dB
            'signal_integrity_threshold': 0.9,  # Correlation coefficient
            'output_dir': 'results'
        }
        
        self.config = self.default_config.copy()
        if config_path:
            self.load_config(config_path)
            
        self._create_output_dir()
    
    def load_config(self, config_path: str) -> None:
        """Load configuration from JSON file."""
        try:
            with open(config_path, 'r') as f:
                user_config = json.load(f)
            self.config.update(user_config)
        except FileNotFoundError:
            print(f"Warning: Config file {config_path} not found. Using defaults.")
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in config file {config_path}. Using defaults.")
    
    def _create_output_dir(self) -> None:
        """Create output directory if it doesn't exist."""
        os.makedirs(self.config['output_dir'], exist_ok=True)
    
    def load_test_data(self, file_path: str) -> np.ndarray:
        """
        Load test data from CSV file.
        
        Args:
            file_path: Path to CSV file containing time series data
            
        Returns:
            Numpy array of signal data
            
        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If data format is invalid
        """
        try:
            df = pd.read_csv(file_path, header=None)
            return df.values.flatten()
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file {file_path} not found")
        except Exception as e:
            raise ValueError(f"Error loading data: {str(e)}")
    
    def calculate_bandwidth(self, signal_data: np.ndarray) -> Tuple[float, float, float]:
        """
        Calculate bandwidth of the signal.
        
        Args:
            signal_data: Time series signal data
            
        Returns:
            Tuple of (bandwidth (Hz), center frequency (Hz), peak magnitude (dB))
        """
        n = len(signal_data)
        yf = fft(signal_data)
        xf = fftfreq(n, 1 / self.config['sample_rate'])[:n//2]
        
        # Convert to dB scale
        magnitude = 20 * np.log10(np.abs(yf[0:n//2]))
        peak_idx = np.argmax(magnitude)
        peak_freq = xf[peak_idx]
        peak_mag = magnitude[peak_idx]
        
        # Find -3dB points
        threshold = peak_mag + self.config['bandwidth_threshold']
        above_threshold = magnitude >= threshold
        left_idx = np.argmax(above_threshold)
        right_idx = len(above_threshold) - np.argmax(above_threshold[::-1]) - 1
        
        bandwidth = xf[right_idx] - xf[left_idx]
        
        return bandwidth, peak_freq, peak_mag
    
    def calculate_signal_integrity(self, signal_data: np.ndarray, reference_data: np.ndarray) -> float:
        """
        Calculate signal integrity by comparing to reference signal.
        
        Args:
            signal_data: Test signal data
            reference_data: Reference signal data
            
        Returns:
            Correlation coefficient (0-1)
        """
        min_len = min(len(signal_data), len(reference_data))
        signal_data = signal_data[:min_len]
        reference_data = reference_data[:min_len]
        
        correlation = np.corrcoef(signal_data, reference_data)[0, 1]
        return abs(correlation)  # We care about magnitude, not direction
    
    def analyze_probe_performance(self, test_file: str, reference_file: str = None) -> Dict:
        """
        Complete performance analysis of probe test data.
        
        Args:
            test_file: Path to test data CSV
            reference_file: Optional path to reference data CSV
            
        Returns:
            Dictionary containing analysis results
        """
        results = {
            'timestamp': datetime.now().isoformat(),
            'test_file': test_file,
            'reference_file': reference_file,
            'config': self.config
        }
        
        try:
            test_data = self.load_test_data(test_file)
            
            # Bandwidth analysis
            bandwidth, center_freq, peak_mag = self.calculate_bandwidth(test_data)
            results.update({
                'bandwidth_hz': bandwidth,
                'center_frequency_hz': center_freq,
                'peak_magnitude_db': peak_mag
            })
            
            # Signal integrity analysis
            if reference_file:
                ref_data = self.load_test_data(reference_file)
                integrity = self.calculate_signal_integrity(test_data, ref_data)
                results['signal_integrity'] = integrity
                results['integrity_pass'] = integrity >= self.config['signal_integrity_threshold']
            
            # Generate plots
            self._generate_plots(test_data, results)
            
            results['status'] = 'success'
            
        except Exception as e:
            results.update({
                'status': 'error',
                'error_message': str(e)
            })
        
        self._save_results(results)
        return results
    
    def _generate_plots(self, signal_data: np.ndarray, results: Dict) -> None:
        """Generate analysis plots and save to output directory."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = os.path.splitext(os.path.basename(results['test_file']))[0]
        
        # Time domain plot
        plt.figure(figsize=(12, 6))
        plt.plot(signal_data)
        plt.title(f"Time Domain Signal - {base_name}")
        plt.xlabel("Sample")
        plt.ylabel("Amplitude")
        time_plot_path = os.path.join(self.config['output_dir'], f"{base_name}_{timestamp}_time.png")
        plt.savefig(time_plot_path)
        plt.close()
        
        # Frequency domain plot
        n = len(signal_data)
        yf = fft(signal_data)
        xf = fftfreq(n, 1 / self.config['sample_rate'])[:n//2]
        magnitude = 20 * np.log10(np.abs(yf[0:n//2]))
        
        plt.figure(figsize=(12, 6))
        plt.plot(xf, magnitude)
        plt.title(f"Frequency Domain - {base_name}\nBW: {results['bandwidth_hz']/1e6:.2f} MHz")
        plt.xlabel("Frequency (Hz)")
        plt.ylabel("Magnitude (dB)")
        freq_plot_path = os.path.join(self.config['output_dir'], f"{base_name}_{timestamp}_freq.png")
        plt.savefig(freq_plot_path)
        plt.close()
        
        results['plots'] = {
            'time_domain': time_plot_path,
            'frequency_domain': freq_plot_path
        }
    
    def _save_results(self, results: Dict) -> None:
        """Save analysis results to JSON file."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name = os.path.splitext(os.path.basename(results['test_file']))[0]
        output_path = os.path.join(self.config['output_dir'], f"{base_name}_{timestamp}_results.json")
        
        with open(output_path, 'w') as f:
            json.dump(results, f, indent=4)

def main():
    """Example usage of the RFIDProbeAnalyzer."""
    analyzer = RFIDProbeAnalyzer()
    
    # Example paths - replace with actual test data
    test_data_path = "test_data.csv"
    reference_data_path = "reference_data.csv"
    
    try:
        results = analyzer.analyze_probe_performance(test_data_path, reference_data_path)
        print("Analysis completed successfully.")
        print(f"Bandwidth: {results['bandwidth_hz']/1e6:.2f} MHz")
        if 'signal_integrity' in results:
            print(f"Signal Integrity: {results['signal_integrity']:.3f}")
    except Exception as e:
        print(f"Error during analysis: {str(e)}")

if __name__ == "__main__":
    main()
```
