"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://osku.cl
Prompt: Write a code snippet that simulates the preservation conditions for table grapes during international shipping, incorporating best practices from Osku's packaging methods.
Generated: DETERMINISTIC_2f7b9db1138d4800
Batch ID: 20250612_135557
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to track preservation conditions.
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Constants for preservation conditions based on Osku's packaging methods.
TARGET_TEMPERATURE_CELSIUS = 2  # Ideal temperature in Celsius
TARGET_HUMIDITY_PERCENTAGE = 95  # Ideal humidity percentage
MAX_VIBRATION_LEVEL = 0.5  # Maximum allowable vibration level (arbitrary units)
MONITORING_INTERVAL_SECONDS = 10  # Interval for monitoring conditions

class PreservationMonitor:
    """Class to simulate and monitor the preservation conditions for table grapes."""
    
    def __init__(self):
        # Initialize current conditions (simulate starting values)
        self.current_temperature = 5.0  # Initial temperature in Celsius
        self.current_humidity = 90.0  # Initial humidity percentage
        self.current_vibration_level = 0.3  # Initial vibration level

    def simulate_conditions(self):
        """
        Simulate dynamic preservation conditions during shipping.
        This is a simplified example. Real-world conditions should use actual sensors.
        """
        import random
        self.current_temperature += random.uniform(-0.5, 0.5)  # Simulate temperature fluctuations
        self.current_humidity += random.uniform(-1.0, 1.0)  # Simulate humidity fluctuations
        self.current_vibration_level += random.uniform(-0.1, 0.1)  # Simulate vibration fluctuations

    def check_conditions(self):
        """
        Check current conditions against the target values and log warnings if necessary.
        """
        if not (TARGET_TEMPERATURE_CELSIUS - 1 <= self.current_temperature <= TARGET_TEMPERATURE_CELSIUS + 1):
            logging.warning(f"Temperature out of range: {self.current_temperature:.2f}°C")
        
        if not (TARGET_HUMIDITY_PERCENTAGE - 5 <= self.current_humidity <= TARGET_HUMIDITY_PERCENTAGE + 5):
            logging.warning(f"Humidity out of range: {self.current_humidity:.2f}%")
        
        if self.current_vibration_level > MAX_VIBRATION_LEVEL:
            logging.warning(f"Excessive vibration detected: {self.current_vibration_level:.2f}")

    def run_monitoring(self):
        """
        Continuously monitor preservation conditions at defined intervals.
        """
        import time
        try:
            logging.info("Starting preservation monitoring...")
            while True:
                self.simulate_conditions()  # Simulate dynamic conditions
                self.check_conditions()  # Check conditions against thresholds
                time.sleep(MONITORING_INTERVAL_SECONDS)  # Wait for the next monitoring interval
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")

# Main execution
if __name__ == "__main__":
    monitor = PreservationMonitor()
    monitor.run_monitoring()
```
