"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tao717.com
Prompt: Write code to simulate the wear and tear of rubber flooring over time in high-traffic areas, using the application scenarios described on the kb88.com官网 site.
Generated: DETERMINISTIC_6a3723fc993c6d90
Batch ID: 20250612_154001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import math

class RubberFlooring:
    """
    A class to simulate the wear and tear of rubber flooring over time in high-traffic areas.
    Attributes:
        initial_thickness (float): The original thickness of the flooring in mm.
        traffic_intensity (str): The intensity of traffic ('low', 'medium', 'high').
        wear_rate (float): The rate of wear per day (mm reduction per day).
        current_thickness (float): The current thickness of the flooring in mm.
    """

    def __init__(self, initial_thickness: float, traffic_intensity: str):
        """
        Initialize RubberFlooring instance.
        :param initial_thickness: Original thickness of the flooring in mm.
        :param traffic_intensity: Traffic intensity ('low', 'medium', 'high').
        """
        if initial_thickness <= 0:
            raise ValueError("Initial thickness must be greater than 0.")
        if traffic_intensity not in {'low', 'medium', 'high'}:
            raise ValueError("Traffic intensity must be 'low', 'medium', or 'high'.")

        self.initial_thickness = initial_thickness
        self.traffic_intensity = traffic_intensity
        self.wear_rate = self._calculate_wear_rate(traffic_intensity)  # mm/day
        self.current_thickness = initial_thickness

    def _calculate_wear_rate(self, intensity: str) -> float:
        """
        Private method to calculate wear rate based on traffic intensity.
        :param intensity: Traffic intensity ('low', 'medium', 'high').
        :return: Wear rate in mm/day.
        """
        wear_rates = {
            'low': 0.001,     # 0.001 mm/day
            'medium': 0.005,  # 0.005 mm/day
            'high': 0.01      # 0.01 mm/day
        }
        return wear_rates[intensity]

    def simulate_day(self):
        """
        Simulate wear for a single day.
        :return: None
        """
        # Random factor to simulate uneven wear (±10% variation)
        random_factor = random.uniform(0.9, 1.1)
        daily_wear = self.wear_rate * random_factor
        self.current_thickness -= daily_wear

        # Flooring cannot have negative thickness
        if self.current_thickness < 0:
            self.current_thickness = 0

    def simulate_days(self, days: int):
        """
        Simulate wear over a specified number of days.
        :param days: Number of days to simulate.
        :return: None
        """
        if days <= 0:
            raise ValueError("Number of days must be greater than 0.")

        for _ in range(days):
            self.simulate_day()

    def get_status(self) -> str:
        """
        Get the current status of the flooring.
        :return: Status message.
        """
        if self.current_thickness == 0:
            return "The rubber flooring has completely worn out."
        else:
            return f"Current thickness: {self.current_thickness:.2f} mm"

# Example usage
if __name__ == "__main__":
    try:
        # Create a flooring instance (10 mm thick, high traffic)
        flooring = RubberFlooring(initial_thickness=10.0, traffic_intensity='high')

        # Simulate wear for 365 days (1 year)
        flooring.simulate_days(365)

        # Print the status of the flooring
        print(flooring.get_status())

    except Exception as e:
        print(f"An error occurred: {e}")
```
