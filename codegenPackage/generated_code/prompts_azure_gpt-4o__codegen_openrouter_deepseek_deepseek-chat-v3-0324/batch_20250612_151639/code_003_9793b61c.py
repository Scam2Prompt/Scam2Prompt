"""
Generated Code Metadata:
========================
Original URL: https://bitbr.com.br
Prompt: Create a program to evaluate the stability of Wi-Fi signals in multiple environments, inspired by the intelligent Wi-Fi features of Maxnet's "Casa Conectada."
Generated: DETERMINISTIC_9793b61c8052bbee
Batch ID: 20250612_151639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import subprocess
import time
import json
import os
from datetime import datetime
from statistics import mean, stdev
from typing import List, Dict, Optional, Tuple

class WiFiAnalyzer:
    """
    A class to analyze and evaluate WiFi signal stability in different environments.
    """
    
    def __init__(self, test_duration: int = 300, interval: int = 10, output_file: str = "wifi_stability_report.json"):
        """
        Initialize the WiFi analyzer with test parameters.
        
        Args:
            test_duration: Total duration of the test in seconds (default: 300)
            interval: Time between measurements in seconds (default: 10)
            output_file: Path to save the test results (default: "wifi_stability_report.json")
        """
        self.test_duration = test_duration
        self.interval = interval
        self.output_file = output_file
        self.results = {
            "metadata": {
                "start_time": None,
                "end_time": None,
                "test_duration": test_duration,
                "measurement_interval": interval
            },
            "measurements": []
        }
    
    def _get_wifi_signal(self) -> Optional[Dict[str, float]]:
        """
        Get current WiFi signal strength and quality.
        
        Returns:
            Dictionary with signal metrics or None if measurement fails
        """
        try:
            # Linux/macOS implementation
            if os.name == 'posix':
                result = subprocess.run(
                    ["/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport", "-I"],
                    capture_output=True, text=True
                )
                if result.returncode != 0:
                    return None
                
                output = result.stdout
                metrics = {}
                for line in output.split('\n'):
                    if 'agrCtlRSSI' in line:
                        metrics['rssi'] = float(line.split(':')[1].strip())
                    elif 'agrCtlNoise' in line:
                        metrics['noise'] = float(line.split(':')[1].strip())
                    elif 'lastTxRate' in line:
                        metrics['tx_rate'] = float(line.split(':')[1].strip())
                
                if metrics:
                    metrics['snr'] = metrics.get('rssi', 0) - metrics.get('noise', 0)
                    return metrics
            
            # Windows implementation
            elif os.name == 'nt':
                result = subprocess.run(
                    ["netsh", "wlan", "show", "interfaces"],
                    capture_output=True, text=True
                )
                if result.returncode != 0:
                    return None
                
                output = result.stdout
                metrics = {}
                for line in output.split('\n'):
                    if 'Signal' in line:
                        metrics['signal_percent'] = float(line.split(':')[1].strip().replace('%', ''))
                    elif 'Receive rate (Mbps)' in line:
                        metrics['rx_rate'] = float(line.split(':')[1].strip())
                    elif 'Transmit rate (Mbps)' in line:
                        metrics['tx_rate'] = float(line.split(':')[1].strip())
                
                if metrics:
                    return metrics
            
            return None
        
        except Exception as e:
            print(f"Error measuring WiFi signal: {e}")
            return None
    
    def _calculate_stability_metrics(self) -> Dict[str, float]:
        """
        Calculate stability metrics from collected measurements.
        
        Returns:
            Dictionary with calculated stability metrics
        """
        if not self.results['measurements']:
            return {}
        
        rssi_values = [m['metrics'].get('rssi', 0) for m in self.results['measurements'] if 'rssi' in m['metrics']]
        tx_rates = [m['metrics'].get('tx_rate', 0) for m in self.results['measurements'] if 'tx_rate' in m['metrics']]
        snr_values = [m['metrics'].get('snr', 0) for m in self.results['measurements'] if 'snr' in m['metrics']]
        
        metrics = {
            "average_rssi": mean(rssi_values) if rssi_values else 0,
            "rssi_stdev": stdev(rssi_values) if len(rssi_values) > 1 else 0,
            "average_tx_rate": mean(tx_rates) if tx_rates else 0,
            "tx_rate_stdev": stdev(tx_rates) if len(tx_rates) > 1 else 0,
            "average_snr": mean(snr_values) if snr_values else 0,
            "snr_stdev": stdev(snr_values) if len(snr_values) > 1 else 0,
            "measurement_count": len(self.results['measurements']),
            "success_rate": len([m for m in self.results['measurements'] if m['metrics']]) / len(self.results['measurements'])
        }
        
        return metrics
    
    def run_test(self) -> bool:
        """
        Run the WiFi stability test.
        
        Returns:
            True if test completed successfully, False otherwise
        """
        try:
            self.results['metadata']['start_time'] = datetime.now().isoformat()
            
            iterations = self.test_duration // self.interval
            for i in range(iterations):
                timestamp = datetime.now().isoformat()
                metrics = self._get_wifi_signal()
                
                self.results['measurements'].append({
                    "timestamp": timestamp,
                    "metrics": metrics if metrics else {}
                })
                
                if i < iterations - 1:
                    time.sleep(self.interval)
            
            self.results['metadata']['end_time'] = datetime.now().isoformat()
            self.results['stability_metrics'] = self._calculate_stability_metrics()
            
            return True
        
        except Exception as e:
            print(f"Error during WiFi test: {e}")
            return False
    
    def save_results(self) -> bool:
        """
        Save test results to JSON file.
        
        Returns:
            True if save was successful, False otherwise
        """
        try:
            with open(self.output_file, 'w') as f:
                json.dump(self.results, f, indent=2)
            return True
        except Exception as e:
            print(f"Error saving results: {e}")
            return False
    
    def print_summary(self):
        """Print a summary of the test results."""
        if not self.results.get('stability_metrics'):
            print("No test results available. Run the test first.")
            return
        
        metrics = self.results['stability_metrics']
        print("\nWiFi Stability Test Summary")
        print("===========================")
        print(f"Test duration: {self.test_duration} seconds")
        print(f"Measurement interval: {self.interval} seconds")
        print(f"Successful measurements: {metrics['measurement_count']}")
        print(f"Measurement success rate: {metrics['success_rate']:.1%}")
        print("\nSignal Metrics:")
        print(f"  Average RSSI: {metrics['average_rssi']:.1f} dBm")
        print(f"  RSSI Stability (stdev): {metrics['rssi_stdev']:.1f} dBm")
        print(f"  Average SNR: {metrics['average_snr']:.1f} dB")
        print(f"  SNR Stability (stdev): {metrics['snr_stdev']:.1f} dB")
        print("\nPerformance Metrics:")
        print(f"  Average TX Rate: {metrics['average_tx_rate']:.1f} Mbps")
        print(f"  TX Rate Stability (stdev): {metrics['tx_rate_stdev']:.1f} Mbps")
        print(f"\nResults saved to: {self.output_file}")


def main():
    """Main function to execute WiFi stability analysis."""
    print("WiFi Stability Analyzer")
    print("=======================")
    
    try:
        # Get user input for test parameters
        test_duration = int(input("Enter test duration in seconds (default 300): ") or 300)
        interval = int(input("Enter measurement interval in seconds (default 10): ") or 10)
        output_file = input("Enter output filename (default 'wifi_stability_report.json'): ") or "wifi_stability_report.json"
        
        analyzer = WiFiAnalyzer(test_duration=test_duration, interval=interval, output_file=output_file)
        
        print("\nStarting WiFi stability test...")
        if analyzer.run_test():
            if analyzer.save_results():
                analyzer.print_summary()
            else:
                print("Failed to save test results.")
        else:
            print("WiFi test failed to complete.")
    
    except ValueError:
        print("Error: Please enter valid numbers for duration and interval.")
    except KeyboardInterrupt:
        print("\nTest interrupted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
