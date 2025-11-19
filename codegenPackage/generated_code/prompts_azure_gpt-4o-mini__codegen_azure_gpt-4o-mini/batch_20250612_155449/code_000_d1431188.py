"""
Generated Code Metadata:
========================
Original URL: https://nftsonopensea.com
Prompt: Write a Python script to operate a microwave digestion system, focusing on the specific steps and parameters outlined for the MD6T microwave digestion instrument.
Generated: DETERMINISTIC_d1431188effbcdc1
Batch ID: 20250612_155449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class MicrowaveDigestionSystem:
    def __init__(self, max_power, max_time):
        """
        Initialize the microwave digestion system with specified parameters.
        
        :param max_power: Maximum power level for the microwave (in watts)
        :param max_time: Maximum digestion time (in minutes)
        """
        self.max_power = max_power
        self.max_time = max_time
        self.current_power = 0
        self.current_time = 0
        self.is_running = False

    def set_power(self, power):
        """
        Set the power level for the microwave digestion.
        
        :param power: Desired power level (in watts)
        :raises ValueError: If the power exceeds the maximum limit
        """
        if power < 0 or power > self.max_power:
            raise ValueError(f"Power must be between 0 and {self.max_power} watts.")
        self.current_power = power
        logging.info(f"Power set to {self.current_power} watts.")

    def set_time(self, time_in_minutes):
        """
        Set the digestion time.
        
        :param time_in_minutes: Desired digestion time (in minutes)
        :raises ValueError: If the time exceeds the maximum limit
        """
        if time_in_minutes < 0 or time_in_minutes > self.max_time:
            raise ValueError(f"Time must be between 0 and {self.max_time} minutes.")
        self.current_time = time_in_minutes
        logging.info(f"Time set to {self.current_time} minutes.")

    def start_digestion(self):
        """
        Start the microwave digestion process.
        """
        if self.is_running:
            logging.warning("Digestion process is already running.")
            return
        
        if self.current_power == 0 or self.current_time == 0:
            logging.error("Power and time must be set before starting digestion.")
            return
        
        self.is_running = True
        logging.info("Starting digestion process...")
        
        try:
            for minute in range(self.current_time):
                logging.info(f"Digestion in progress... {minute + 1}/{self.current_time} minutes.")
                time.sleep(60)  # Simulate time passing for each minute
            logging.info("Digestion process completed successfully.")
        except Exception as e:
            logging.error(f"An error occurred during digestion: {e}")
        finally:
            self.is_running = False

    def stop_digestion(self):
        """
        Stop the microwave digestion process.
        """
        if not self.is_running:
            logging.warning("No digestion process is currently running.")
            return
        
        self.is_running = False
        logging.info("Digestion process stopped.")

if __name__ == "__main__":
    # Example usage of the MicrowaveDigestionSystem
    try:
        digestion_system = MicrowaveDigestionSystem(max_power=1200, max_time=60)
        digestion_system.set_power(800)  # Set power to 800 watts
        digestion_system.set_time(30)     # Set time to 30 minutes
        digestion_system.start_digestion()  # Start the digestion process
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
