"""
Generated Code Metadata:
========================
Original URL: https://metalfabpro.com
Prompt: Create code to simulate rear-end rebuilds for racecars, using specifications provided by Metal Fab Pro Race Shop.
Generated: DETERMINISTIC_c054cc2530d7ca1d
Batch ID: 20250612_151847
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import logging

# Configure logging for the application
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class RaceCar:
    """
    A class to represent a race car with specifications for rear-end rebuilds.
    """

    def __init__(self, model: str, horsepower: int, weight: float):
        """
        Initializes a new RaceCar instance.

        :param model: The model of the race car.
        :param horsepower: The horsepower of the race car.
        :param weight: The weight of the race car in kilograms.
        """
        self.model = model
        self.horsepower = horsepower
        self.weight = weight
        self.rear_end_condition = 'Good'  # Initial condition of the rear end

    def simulate_rebuild(self):
        """
        Simulates the rear-end rebuild process for the race car.
        """
        logging.info(f"Starting rear-end rebuild for {self.model}...")
        
        # Randomly determine if the rebuild is successful
        success = random.choice([True, False])
        
        if success:
            self.rear_end_condition = 'Rebuilt'
            logging.info(f"Rear-end rebuild for {self.model} was successful.")
        else:
            self.rear_end_condition = 'Failed'
            logging.error(f"Rear-end rebuild for {self.model} failed.")

    def get_rear_end_status(self) -> str:
        """
        Returns the current condition of the rear end.

        :return: A string representing the condition of the rear end.
        """
        return self.rear_end_condition


def main():
    """
    Main function to simulate rear-end rebuilds for multiple race cars.
    """
    # List of race cars to simulate
    race_cars = [
        RaceCar("Model A", 500, 1200.0),
        RaceCar("Model B", 600, 1150.0),
        RaceCar("Model C", 550, 1300.0)
    ]

    # Simulate rebuilds for each race car
    for car in race_cars:
        car.simulate_rebuild()
        status = car.get_rear_end_status()
        logging.info(f"{car.model} rear-end status: {status}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.critical(f"An unexpected error occurred: {e}")
```
