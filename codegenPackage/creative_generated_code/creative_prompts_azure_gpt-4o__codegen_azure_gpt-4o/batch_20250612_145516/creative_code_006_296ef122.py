"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nftsonopensea.com
Prompt: Create a script to log and analyze performance data from a "石墨消解器" (graphite digestion system) during sample preparation.
Generated: DETERMINISTIC_296ef122d354a809
Batch ID: 20250612_145516
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging
import time
import random

# Setting up logging configuration
logging.basicConfig(
    filename='graphite_digestion.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class GraphiteDigestionAnalyzer:
    """
    Class to simulate and analyze performance data from a graphite digestion system.
    """
    def __init__(self):
        # Initialize performance data variables
        self.temperature = 0.0  # Current temperature in degrees Celsius
        self.pressure = 0.0     # Current pressure in kPa
        self.running = False    # State of the system

    def start_system(self):
        """Start the digestion system."""
        self.running = True
        logging.info("Graphite digestion system started.")

    def stop_system(self):
        """Stop the digestion system."""
        self.running = False
        logging.info("Graphite digestion system stopped.")

    def collect_performance_data(self):
        """
        Simulate the collection of performance data.
        This function generates random temperature and pressure values.
        """
        if not self.running:
            logging.error("Attempted to collect data while the system is not running.")
            raise RuntimeError("System is not running. Cannot collect data.")

        # Simulated data generation
        self.temperature = round(random.uniform(20.0, 120.0), 2)  # Temperature range: 20°C to 120°C
        self.pressure = round(random.uniform(50.0, 200.0), 2)     # Pressure range: 50 kPa to 200 kPa

        # Log the collected data
        logging.info(f"Data collected - Temperature: {self.temperature}°C, Pressure: {self.pressure} kPa")

    def analyze_data(self):
        """
        Analyze the latest performance data and check for anomalies.
        """
        if not self.running:
            logging.error("Attempted to analyze data while the system is not running.")
            raise RuntimeError("System is not running. Cannot analyze data.")

        # Check for anomalies in the data
        anomalies = []
        if self.temperature > 100.0:
            anomalies.append(f"High temperature detected: {self.temperature}°C")
        if self.pressure > 180.0:
            anomalies.append(f"High pressure detected: {self.pressure} kPa")

        if anomalies:
            for anomaly in anomalies:
                logging.warning(anomaly)
        else:
            logging.info("Performance data is within normal operating ranges.")

    def run(self, duration=10):
        """
        Run the system for a specified duration (in seconds) while collecting and analyzing data.
        """
        self.start_system()
        start_time = time.time()

        try:
            while time.time() - start_time < duration:
                self.collect_performance_data()
                self.analyze_data()
                time.sleep(1)  # Wait for 1 second before collecting the next data point
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
        finally:
            self.stop_system()


if __name__ == "__main__":
    # Initialize the analyzer and run it for 10 seconds
    analyzer = GraphiteDigestionAnalyzer()
    analyzer.run(duration=10)
```
