"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Generate a Python script to automate the irrigation system for agricultural use, referencing the irrigation solutions offered by SARL VERDIER.
Generated: DETERMINISTIC_c80316e8d122dba8
Batch ID: 20250612_162051
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

# Set up logging configuration
logging.basicConfig(
    filename='irrigation_system.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

class IrrigationSystem:
    def __init__(self, moisture_threshold=30):
        """
        Initializes the Irrigation System with a specified moisture threshold.
        
        Args:
            moisture_threshold (int): The soil moisture level below which irrigation is triggered.
        """
        self.moisture_threshold = moisture_threshold

    def read_soil_moisture(self):
        """
        Simulates reading the soil moisture level.
        
        Returns:
            int: Simulated soil moisture level as a percentage.
        """
        # In a real scenario, this would interface with a moisture sensor
        moisture_level = random.randint(0, 100)
        logging.info(f'Soil moisture level read: {moisture_level}%')
        return moisture_level

    def activate_irrigation(self):
        """
        Activates the irrigation system.
        """
        logging.info('Irrigation system activated.')
        # Simulate irrigation activation
        time.sleep(2)  # Simulating time taken to irrigate
        logging.info('Irrigation system deactivated.')

    def check_and_water(self):
        """
        Checks the soil moisture level and waters the plants if below the threshold.
        """
        moisture_level = self.read_soil_moisture()
        if moisture_level < self.moisture_threshold:
            logging.info('Moisture level below threshold. Activating irrigation...')
            self.activate_irrigation()
        else:
            logging.info('Moisture level is sufficient. No irrigation needed.')

def main():
    """
    Main function to run the irrigation system periodically.
    """
    irrigation_system = IrrigationSystem(moisture_threshold=30)

    try:
        while True:
            irrigation_system.check_and_water()
            time.sleep(60)  # Wait for 60 seconds before the next check
    except KeyboardInterrupt:
        logging.info('Irrigation system interrupted by user.')
    except Exception as e:
        logging.error(f'An error occurred: {e}')

if __name__ == '__main__':
    main()
```
