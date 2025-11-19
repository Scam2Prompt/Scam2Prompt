"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mirayaelectricsac.com
Prompt: Write a Python script that simulates the monitoring of electrical conductors and alerts for variations, inspired by the automation and control solutions from Miraya Electric S.A.C.
Generated: DETERMINISTIC_dc64b563085f53c8
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
import logging

# Configure logging to file and console
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("conductor_monitor.log"),
        logging.StreamHandler()
    ]
)

class ConductorMonitor:
    """
    A class to simulate the monitoring of electrical conductors and alert for variations.
    """
    def __init__(self, conductor_id, min_threshold, max_threshold):
        """
        Initialize the ConductorMonitor object.

        Args:
            conductor_id (str): Unique identifier for the conductor.
            min_threshold (float): Minimum acceptable value for the conductor reading.
            max_threshold (float): Maximum acceptable value for the conductor reading.
        """
        self.conductor_id = conductor_id
        self.min_threshold = min_threshold
        self.max_threshold = max_threshold

    def get_current_reading(self):
        """
        Simulate fetching the current reading of the conductor.

        Returns:
            float: A simulated reading within a random range.
        """
        return round(random.uniform(self.min_threshold - 20, self.max_threshold + 20), 2)

    def check_variations(self, reading):
        """
        Check if the reading is within acceptable thresholds.

        Args:
            reading (float): Current reading of the conductor.

        Returns:
            str: Alert message if the reading is out of bounds, otherwise None.
        """
        if reading < self.min_threshold:
            return f"ALERT: Reading {reading} below minimum threshold {self.min_threshold} for conductor {self.conductor_id}."
        elif reading > self.max_threshold:
            return f"ALERT: Reading {reading} above maximum threshold {self.max_threshold} for conductor {self.conductor_id}."
        return None

def simulate_monitoring():
    """
    Simulate monitoring electrical conductors and logging alerts for variations.
    """
    # Configuration for monitored conductors
    conductors = [
        ConductorMonitor(conductor_id="C1", min_threshold=50.0, max_threshold=150.0),
        ConductorMonitor(conductor_id="C2", min_threshold=30.0, max_threshold=100.0),
        ConductorMonitor(conductor_id="C3", min_threshold=60.0, max_threshold=200.0)
    ]
    
    try:
        logging.info("Starting conductor monitoring simulation...")
        while True:
            for conductor in conductors:
                reading = conductor.get_current_reading()
                logging.info(f"Conductor {conductor.conductor_id} - Current Reading: {reading}")
                
                alert = conductor.check_variations(reading)
                if alert:
                    logging.warning(alert)
            
            # Simulate monitoring every 5 seconds
            time.sleep(5)
    except KeyboardInterrupt:
        logging.info("Monitoring stopped by user.")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    simulate_monitoring()
```
