"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trialsonicsolutions.com
Prompt: Describe the process of ultrasonic cleaning and how it can be applied to plastic and polymer extrusion filters.
Generated: DETERMINISTIC_77268d7b972f0742
Batch ID: 20250612_140414
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class UltrasonicCleaner:
    """
    A class to represent an ultrasonic cleaner for plastic and polymer extrusion filters.

    Attributes:
        frequency (float): The frequency of the ultrasonic waves in kHz.
        duration (int): The duration of the cleaning process in seconds.
        temperature (float): The temperature of the cleaning solution in degrees Celsius.
    """

    def __init__(self, frequency: float, duration: int, temperature: float):
        """
        Initializes an UltrasonicCleaner instance.

        Parameters:
            frequency (float): The frequency of the ultrasonic waves.
            duration (int): The duration for which cleaning will occur.
            temperature (float): The temperature of the cleaning solution.
        """
        self.frequency = frequency
        self.duration = duration
        self.temperature = temperature
    
    def validate_parameters(self):
        """
        Validates the parameters provided for the ultrasonic cleaner.
        
        Raises:
            ValueError: If any parameter is outside the acceptable range.
        """
        if not (20 <= self.frequency <= 400):
            raise ValueError("Frequency must be between 20 kHz and 400 kHz.")
        if not (1 <= self.duration <= 120):
            raise ValueError("Duration must be between 1 and 120 seconds.")
        if not (0 <= self.temperature <= 100):
            raise ValueError("Temperature must be between 0°C and 100°C.")

    def clean_filter(self):
        """
        Performs the cleaning process on the extrusion filter using ultrasonic waves.
        
        Raises:
            RuntimeError: If the cleaning process cannot be started.
        """
        try:
            # Validate the parameters before starting the cleaning process
            self.validate_parameters()

            # Simulate the cleaning process
            print(f"Starting ultrasonic cleaning at {self.frequency} kHz.")
            print(f"Cleaning duration: {self.duration} seconds.")
            print(f"Cleaning temperature: {self.temperature}°C.")
            
            # Implement cleaning logic (placeholder for actual ultrasonic cleaning process)
            # In real implementation, this would interface with the ultrasonic cleaning hardware.
            print("Cleaning in progress...")
            import time
            time.sleep(self.duration)  # Simulating the delay for cleaning
            print("Cleaning completed successfully.")

        except Exception as e:
            raise RuntimeError("An error occurred during the cleaning process: " + str(e))


if __name__ == "__main__":
    # Example usage of the UltrasonicCleaner class
    try:
        cleaner = UltrasonicCleaner(frequency=40, duration=30, temperature=60)
        cleaner.clean_filter()
    except ValueError as ve:
        print(f"Parameter error: {ve}")
    except RuntimeError as re:
        print(f"Runtime error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
