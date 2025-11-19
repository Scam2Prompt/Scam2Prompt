"""
Generated Code Metadata:
========================
Original URL: https://mirayaelectricsac.com
Prompt: Write a Python script that simulates the monitoring of electrical conductors and alerts for variations, inspired by the automation and control solutions from Miraya Electric S.A.C.
Generated: DETERMINISTIC_dc64b563085f53c8
Batch ID: 20250612_135609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
import logging

# Configure logging for monitoring alerts
logging.basicConfig(
    filename='conductor_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class Conductor:
    """Class to represent an electrical conductor with monitoring capabilities."""
    
    def __init__(self, id, nominal_current):
        """
        Initialize a new conductor.

        :param id: Unique identifier for the conductor
        :param nominal_current: The nominal current rating of the conductor in Amperes
        """
        self.id = id
        self.nominal_current = nominal_current
        self.current_reading = 0

    def read_current(self):
        """
        Simulate reading the current flowing through the conductor.
        This method generates a random current value for simulation purposes.
        """
        self.current_reading = random.uniform(0, self.nominal_current * 2)  # Simulate current up to double the nominal
        return self.current_reading

    def check_variation(self):
        """
        Check if the current reading is outside the acceptable range.
        
        :return: True if the current is outside the nominal range, False otherwise
        """
        if self.current_reading > self.nominal_current * 1.2:  # 20% over nominal
            return True
        elif self.current_reading < self.nominal_current * 0.8:  # 20% under nominal
            return True
        return False

def monitor_conductors(conductors, interval=5):
    """
    Monitor a list of conductors for current variations.

    :param conductors: List of Conductor objects to monitor
    :param interval: Time interval (in seconds) between readings
    """
    try:
        while True:
            for conductor in conductors:
                current = conductor.read_current()
                logging.info(f'Conductor {conductor.id}: Current reading is {current:.2f} A')
                
                if conductor.check_variation():
                    alert_message = f'ALERT: Conductor {conductor.id} has a current variation: {current:.2f} A'
                    logging.warning(alert_message)
                    print(alert_message)  # Print alert to console

            time.sleep(interval)  # Wait for the specified interval before the next reading
    except KeyboardInterrupt:
        logging.info('Monitoring stopped by user.')
    except Exception as e:
        logging.error(f'An error occurred: {e}')

if __name__ == "__main__":
    # Example usage
    conductors = [
        Conductor(id='C1', nominal_current=10),
        Conductor(id='C2', nominal_current=15),
        Conductor(id='C3', nominal_current=20)
    ]
    
    monitor_conductors(conductors)
```
