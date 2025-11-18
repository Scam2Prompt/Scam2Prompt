"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fuelinjectorservices.com.au
Prompt: Write a program to simulate the ultrasonic cleaning process for marine fuel injectors, referencing the specific services for marine vehicles offered by Fuel Injector Services.
Generated: DETERMINISTIC_66d78e2ddc9dd49b
Batch ID: 20250612_151611
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

class UltrasonicCleaner:
    """
    A class to simulate the ultrasonic cleaning process for marine fuel injectors.
    """

    def __init__(self, frequency: float, duration: int):
        """
        Initializes the ultrasonic cleaner.

        :param frequency: The frequency of the ultrasonic waves in kHz.
        :param duration: The duration for the cleaning process in seconds.
        """
        self.frequency = frequency
        self.duration = duration
        self.cleaning = False

    def start_cleaning(self):
        """
        Starts the ultrasonic cleaning process.
        """
        if self.cleaning:
            raise RuntimeError("Cleaning process is already in progress.")
        
        self.cleaning = True
        print(f"Starting cleaning at {self.frequency} kHz for {self.duration} seconds.")
        self._simulate_cleaning()
        self.cleaning = False
        print("Cleaning process completed.")

    def _simulate_cleaning(self):
        """
        Simulates the ultrasonic cleaning process.
        """
        for second in range(self.duration):
            time.sleep(1)  # Simulate the time taken for each second of cleaning
            dirt_removal = random.randint(10, 30)  # Simulate dirt removal percentage
            print(f"Progress: {second + 1}/{self.duration} seconds. Dirt removed: {dirt_removal}%")

class MarineFuelInjectorService:
    """
    A service class for managing marine fuel injector cleaning.
    """

    def __init__(self):
        """
        Initializes the marine fuel injector service.
        """
        self.cleaner = None

    def prepare_cleaner(self, frequency: float, duration: int):
        """
        Prepares the ultrasonic cleaner.

        :param frequency: The frequency of the ultrasonic waves in kHz.
        :param duration: The duration for the cleaning process in seconds.
        """
        self.cleaner = UltrasonicCleaner(frequency, duration)

    def clean_injectors(self):
        """
        Cleans the injectors using the prepared ultrasonic cleaner.
        Raises an error if the cleaner is not prepared.
        """
        if self.cleaner is None:
            raise RuntimeError("Cleaner has not been prepared. Please prepare the cleaner first.")

        self.cleaner.start_cleaning()

if __name__ == "__main__":
    try:
        # Service for marine fuel injectors
        service = MarineFuelInjectorService()
        
        # Set cleaning parameters (frequency in kHz and duration in seconds)
        cleaning_frequency = 40.0  # Example frequency
        cleaning_duration = 5        # Example duration in seconds

        # Prepare the ultrasonic cleaner
        service.prepare_cleaner(cleaning_frequency, cleaning_duration)

        # Start the cleaning process
        service.clean_injectors()

    except Exception as e:
        print(f"An error occurred: {e}")
```
