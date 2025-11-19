"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getsonicsolutions.com
Prompt: Write a Python script that utilizes ultrasonic cleaning methods to effectively clean industrial parts, referencing the techniques discussed on Sonic Solutions' website.
Generated: DETERMINISTIC_0ceeca8f6447d7bc
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
import logging

# Set up logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UltrasonicCleaner:
    """
    A class to represent an ultrasonic cleaner for industrial parts.
    """

    def __init__(self, frequency: float, power: float, tank_size: float):
        """
        Initialize the UltrasonicCleaner with frequency, power, and tank size.

        :param frequency: Frequency of ultrasonic waves in kHz
        :param power: Power of the ultrasonic cleaner in watts
        :param tank_size: Size of the tank in liters
        """
        self.frequency = frequency
        self.power = power
        self.tank_size = tank_size
        self.is_cleaning = False

    def start_cleaning(self, duration: int):
        """
        Start the ultrasonic cleaning process for a specified duration.

        :param duration: Duration of the cleaning process in seconds
        """
        if self.is_cleaning:
            logging.warning("Cleaning process is already running.")
            return
        
        logging.info(f"Starting cleaning with frequency: {self.frequency} kHz, power: {self.power} W for {duration} seconds.")
        self.is_cleaning = True
        
        try:
            time.sleep(duration)  # Simulate cleaning process
            logging.info("Cleaning process completed successfully.")
        except Exception as e:
            logging.error(f"An error occurred during cleaning: {str(e)}")
        finally:
            self.is_cleaning = False

    def set_parameters(self, frequency: float, power: float, tank_size: float):
        """
        Set the parameters for the ultrasonic cleaner.

        :param frequency: New frequency in kHz
        :param power: New power in watts
        :param tank_size: New tank size in liters
        """
        self.frequency = frequency
        self.power = power
        self.tank_size = tank_size
        logging.info(f"Parameters updated: frequency={frequency} kHz, power={power} W, tank_size={tank_size} L")

    def get_status(self):
        """
        Get the current status of the ultrasonic cleaner.

        :return: A string describing the current state
        """
        status = "Running" if self.is_cleaning else "Idle"
        logging.info(f"Ultrasonic Cleaner Status: {status}")
        return status

if __name__ == "__main__":
    # Example usage of the UltrasonicCleaner class
    try:
        cleaner = UltrasonicCleaner(frequency=40.0, power=150.0, tank_size=10.0)  # 40 kHz, 150 W, 10 L tank
        cleaner.start_cleaning(duration=5)  # Clean for 5 seconds
        cleaner.get_status()
    except Exception as e:
        logging.critical(f"Critical error: {str(e)}")
```
