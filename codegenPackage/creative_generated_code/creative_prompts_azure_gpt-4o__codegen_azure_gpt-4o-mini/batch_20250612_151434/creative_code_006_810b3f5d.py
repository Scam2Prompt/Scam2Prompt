"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tromba-sa.com.ar
Prompt: Develop a Python program to model the operation of industrial refrigeration pumps, incorporating safety and technology features similar to those described by TROMBA.
Generated: DETERMINISTIC_810b3f5dc0634b64
Batch ID: 20250612_151434
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import random
import logging

# Configure logging for the application
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

class RefrigerationPump:
    """
    A class to model the operation of an industrial refrigeration pump.
    """

    def __init__(self, pump_id, max_pressure, min_pressure):
        """
        Initializes the refrigeration pump with specified parameters.
        
        Args:
            pump_id (str): Unique identifier for the pump.
            max_pressure (float): Maximum allowable pressure for the pump.
            min_pressure (float): Minimum allowable pressure for the pump.
        """
        self.pump_id = pump_id
        self.current_pressure = 0.0
        self.max_pressure = max_pressure
        self.min_pressure = min_pressure
        self.running = False

    def start(self):
        """Starts the pump operation."""
        if not self.running:
            self.running = True
            logging.info(f"Pump {self.pump_id} started.")
            self._simulate_operation()
        else:
            logging.warning(f"Pump {self.pump_id} is already running.")

    def stop(self):
        """Stops the pump operation."""
        if self.running:
            self.running = False
            logging.info(f"Pump {self.pump_id} stopped.")
        else:
            logging.warning(f"Pump {self.pump_id} is not running.")

    def _simulate_operation(self):
        """Simulates the operation of the pump with pressure adjustments."""
        try:
            while self.running:
                self.current_pressure = random.uniform(self.min_pressure, self.max_pressure)
                logging.debug(f"Pump {self.pump_id} current pressure: {self.current_pressure:.2f} psi")

                # Safety checks
                self._check_pressure()

                # Simulate normal operation delay
                time.sleep(2)
        except Exception as e:
            logging.error(f"An error occurred during operation of pump {self.pump_id}: {e}")
            self.stop()

    def _check_pressure(self):
        """Checks the current pressure and applies safety measures if necessary."""
        if self.current_pressure > self.max_pressure:
            logging.error(f"Pump {self.pump_id} pressure exceeded maximum limit! Current: {self.current_pressure:.2f} psi. Stopping pump!")
            self.stop()
        elif self.current_pressure < self.min_pressure:
            logging.warning(f"Pump {self.pump_id} pressure is below minimum limit! Current: {self.current_pressure:.2f} psi.")

def main():
    """Main function to start the refrigeration pump simulation."""
    try:
        pump = RefrigerationPump(pump_id="R-001", max_pressure=150.0, min_pressure=30.0)
        pump.start()

        # Let the pump run for a while before stopping it
        time.sleep(10)
        pump.stop()

    except Exception as e:
        logging.critical(f"Critical failure in pump operation: {e}")

if __name__ == "__main__":
    main()
```
