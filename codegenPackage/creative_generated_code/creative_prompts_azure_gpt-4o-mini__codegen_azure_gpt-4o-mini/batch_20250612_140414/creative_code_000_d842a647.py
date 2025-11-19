"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gosonicsolutions.com
Prompt: How can I implement ultrasonic cleaning for industrial parts, specifically for cleaning anilox rollers and circuit boards, using the techniques described by Sonic Solutions?
Generated: DETERMINISTIC_d842a6473df9e249
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

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UltrasonicCleaner:
    """Class to represent an ultrasonic cleaner for industrial parts."""
    
    def __init__(self, frequency: float, temperature: float):
        """
        Initialize the ultrasonic cleaner parameters.
        
        :param frequency: The frequency of the ultrasonic waves in kHz.
        :param temperature: The cleaning bath temperature in Celsius.
        """
        self.frequency = frequency
        self.temperature = temperature
        self.cleaned_parts = []

    def validate_parameters(self):
        """Validate frequency and temperature for ultrasonic cleaning."""
        if not (20 <= self.frequency <= 400):
            logging.error("Frequency must be between 20 kHz and 400 kHz.")
            raise ValueError("Invalid frequency.")
        if not (20 <= self.temperature <= 80):
            logging.error("Temperature must be between 20°C and 80°C.")
            raise ValueError("Invalid temperature.")

    def clean_part(self, part_name: str):
        """
        Simulate cleaning a part using ultrasonic waves.
        
        :param part_name: The name of the part to be cleaned.
        """
        logging.info(f"Starting cleaning process for {part_name}.")
        
        self.validate_parameters()
        
        # Simulating the cleaning process
        try:
            logging.info(f"Cleaning {part_name} at {self.frequency} kHz and {self.temperature}°C.")
            time.sleep(2)  # Simulating cleaning duration
            self.cleaned_parts.append(part_name)
            logging.info(f"{part_name} cleaned successfully.")
        except Exception as e:
            logging.error(f"Error during cleaning {part_name}: {e}")
            raise

    def display_cleaned_parts(self):
        """Display the list of cleaned parts."""
        if not self.cleaned_parts:
            logging.info("No parts have been cleaned yet.")
        else:
            logging.info("Cleaned parts: " + ", ".join(self.cleaned_parts))


def main():
    """Main function to execute the ultrasonic cleaning process."""
    # Set up ultrasonic cleaner with defined parameters
    cleaner = UltrasonicCleaner(frequency=40.0, temperature=50.0)
    
    try:
        # Clean specific parts
        cleaner.clean_part("Anilox Roller")
        cleaner.clean_part("Circuit Board")
        
        # Display cleaned parts
        cleaner.display_cleaned_parts()
        
    except ValueError as ve:
        logging.error(f"Validation error: {ve}")
    except Exception as e:
        logging.error(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
