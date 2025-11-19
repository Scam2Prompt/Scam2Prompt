"""
Generated Code Metadata:
========================
Original URL: https://phantom-ss.com
Prompt: Write a code snippet that simulates the performance metrics of a Chevrolet Cobalt SS/TC, including its lap time at Nürburgring and modifications like the Borg Wagner Turbo and K&N Cold Air Intake.
Generated: DETERMINISTIC_94e54006626f55f6
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

class Car:
    """
    A class to represent a car and its performance metrics.
    """

    def __init__(self, model, base_lap_time):
        """
        Initializes the car with a model name and a base lap time.

        :param model: str - The model of the car
        :param base_lap_time: float - The base lap time in seconds
        """
        self.model = model
        self.base_lap_time = base_lap_time
        self.modifications = []

    def add_modification(self, modification):
        """
        Adds a modification to the car.

        :param modification: str - The name of the modification
        """
        self.modifications.append(modification)

    def calculate_lap_time(self):
        """
        Calculates the lap time based on modifications.

        :return: float - The modified lap time in seconds
        """
        lap_time = self.base_lap_time

        # Simulate performance improvement from modifications
        for mod in self.modifications:
            if mod == "Borg Wagner Turbo":
                lap_time *= 0.95  # 5% improvement
            elif mod == "K&N Cold Air Intake":
                lap_time *= 0.98  # 2% improvement

        return round(lap_time, 2)

    def display_performance_metrics(self):
        """
        Displays the performance metrics of the car.
        """
        print(f"Model: {self.model}")
        print(f"Base Lap Time: {self.base_lap_time} seconds")
        print(f"Modifications: {', '.join(self.modifications) if self.modifications else 'None'}")
        print(f"Modified Lap Time: {self.calculate_lap_time()} seconds")


def main():
    """
    Main function to simulate the performance metrics of a Chevrolet Cobalt SS/TC.
    """
    try:
        # Create an instance of the Chevrolet Cobalt SS/TC
        cobalt_ss_tc = Car("Chevrolet Cobalt SS/TC", 8.5)  # Base lap time at Nürburgring in seconds

        # Add modifications
        cobalt_ss_tc.add_modification("Borg Wagner Turbo")
        cobalt_ss_tc.add_modification("K&N Cold Air Intake")

        # Display performance metrics
        cobalt_ss_tc.display_performance_metrics()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
