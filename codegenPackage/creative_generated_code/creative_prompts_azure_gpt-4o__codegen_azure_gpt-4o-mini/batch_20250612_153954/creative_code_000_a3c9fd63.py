"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Write Python code to calculate estimated air freight shipping times for Uniair Cargo's routes, using the provided durations for East Asia, Europe & USA, and Southeast Asia.
Generated: DETERMINISTIC_a3c9fd63e7f32c42
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AirFreightCalculator:
    """
    A class to calculate estimated air freight shipping times for Uniair Cargo's routes.
    """

    # Define shipping durations for different routes in hours
    ROUTE_DURATIONS = {
        "East Asia": 24,      # Estimated duration for East Asia
        "Europe": 48,         # Estimated duration for Europe & USA
        "USA": 48,            # Estimated duration for Europe & USA
        "Southeast Asia": 36   # Estimated duration for Southeast Asia
    }

    def __init__(self):
        """
        Initialize the AirFreightCalculator.
        """
        self.routes = self.ROUTE_DURATIONS.keys()

    def get_shipping_duration(self, destination):
        """
        Get the estimated shipping duration for a specified destination.

        Args:
            destination (str): The destination for which to calculate shipping time.

        Returns:
            int: Estimated shipping time in hours.

        Raises:
            ValueError: If the destination is not supported.
        """
        destination = destination.capitalize()  # Normalize input
        if destination in self.ROUTE_DURATIONS:
            duration = self.ROUTE_DURATIONS[destination]
            logging.info(f"Estimated shipping time to {destination}: {duration} hours")
            return duration
        else:
            logging.error(f"Destination '{destination}' is not supported.")
            raise ValueError(f"Destination '{destination}' is not supported. Valid options are: {', '.join(self.routes)}.")

def main():
    """
    Main function to run the air freight shipping time calculation.
    """
    calculator = AirFreightCalculator()
    
    # Example destinations to test the calculator
    destinations = ["East Asia", "Europe", "USA", "Southeast Asia", "Africa"]
    
    for destination in destinations:
        try:
            duration = calculator.get_shipping_duration(destination)
            print(f"Estimated shipping time to {destination}: {duration} hours")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
```
