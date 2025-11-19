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

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("conductor_monitor.log"),
        logging.StreamHandler()
    ]
)

class Conductor:
    """
    Class to represent an electrical conductor.
    Each conductor has a name and a monitored voltage level.
    """

    def __init__(self, name: str, nominal_voltage: float, tolerance: float):
        """
        Initialize a conductor with a name, nominal voltage, and tolerance.
        
        :param name: Name of the conductor
        :param nominal_voltage: Expected voltage level (in volts)
        :param tolerance: Allowable deviation from the nominal voltage
        """
        self.name = name
        self.nominal_voltage = nominal_voltage
        self.tolerance = tolerance

    def read_voltage(self) -> float:
        """
        Simulate reading the voltage of the conductor.
        
        :return: A simulated voltage value (randomly generated)
        """
        # Introduce random variation to simulate real-world voltage readings
        variation = random.uniform(-self.tolerance, self.tolerance)
        return self.nominal_voltage + variation

    def is_voltage_normal(self, voltage: float) -> bool:
        """
        Check if the given voltage is within the acceptable range.
        
        :param voltage: The voltage level to check
        :return: True if voltage is within the acceptable range, else False
        """
        return (self.nominal_voltage - self.tolerance) <= voltage <= (self.nominal_voltage + self.tolerance)

class Monitor:
    """
    Class to monitor multiple conductors and alert for any variations.
    """

    def __init__(self, conductors: list):
        """
        Initialize the monitor with a list of conductors.

        :param conductors: List of Conductor objects to monitor
        """
        self.conductors = conductors

    def monitor_conductors(self):
        """
        Continuously monitor the conductors and log any variations outside the acceptable range.
        """
        try:
            while True:
                for conductor in self.conductors:
                    voltage = conductor.read_voltage()
                    logging.info(f'{conductor.name} - Current Voltage: {voltage:.2f} V')
                    
                    if not conductor.is_voltage_normal(voltage):
                        logging.warning(f'ALERT: {conductor.name} voltage out of range: {voltage:.2f} V')
                
                # Wait for a specified interval before the next reading
                time.sleep(5)  # Monitor every 5 seconds

        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
        except Exception as e:
            logging.error(f"An error occurred during monitoring: {e}")

if __name__ == "__main__":
    # Define conductors with nominal voltages and tolerances
    conductors = [
        Conductor("Conductor A", nominal_voltage=230.0, tolerance=5.0),
        Conductor("Conductor B", nominal_voltage=110.0, tolerance=3.0),
        Conductor("Conductor C", nominal_voltage=400.0, tolerance=10.0),
    ]

    # Initialize the monitor with the specified conductors
    monitor = Monitor(conductors)

    # Start monitoring the conductors
    monitor.monitor_conductors()
```
