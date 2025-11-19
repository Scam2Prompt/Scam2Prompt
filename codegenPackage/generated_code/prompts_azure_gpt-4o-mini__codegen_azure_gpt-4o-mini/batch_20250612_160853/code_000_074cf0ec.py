"""
Generated Code Metadata:
========================
Original URL: https://utkutantoglu.com
Prompt: Generate a Python function that simulates the process of a gastric sleeve surgery, focusing on the reduction of stomach size and its effects on appetite.
Generated: DETERMINISTIC_074cf0ec40f4b35b
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class GastricSleeveSurgery:
    """
    A class to simulate the effects of gastric sleeve surgery on stomach size and appetite.
    """

    def __init__(self, initial_stomach_size: float):
        """
        Initializes the GastricSleeveSurgery instance.

        :param initial_stomach_size: The initial size of the stomach in milliliters.
        """
        if initial_stomach_size <= 0:
            raise ValueError("Initial stomach size must be a positive value.")
        
        self.initial_stomach_size = initial_stomach_size
        self.current_stomach_size = initial_stomach_size
        self.appetite_level = 100  # Scale from 0 (no appetite) to 100 (normal appetite)

    def perform_surgery(self):
        """
        Simulates the gastric sleeve surgery by reducing the stomach size.
        The stomach size is reduced to approximately 25% of its original size.
        """
        self.current_stomach_size = self.initial_stomach_size * 0.25
        self.adjust_appetite()

    def adjust_appetite(self):
        """
        Adjusts the appetite level based on the new stomach size.
        The appetite level is reduced to simulate the effects of surgery.
        """
        # Assuming appetite decreases by 50% after surgery
        self.appetite_level *= 0.5

    def get_stomach_size(self) -> float:
        """
        Returns the current stomach size.

        :return: Current stomach size in milliliters.
        """
        return self.current_stomach_size

    def get_appetite_level(self) -> float:
        """
        Returns the current appetite level.

        :return: Current appetite level on a scale from 0 to 100.
        """
        return self.appetite_level

    def simulate_post_surgery(self, days: int):
        """
        Simulates the post-surgery recovery process over a number of days.

        :param days: Number of days to simulate post-surgery recovery.
        :raises ValueError: If days is not a positive integer.
        """
        if days <= 0:
            raise ValueError("Number of days must be a positive integer.")

        for day in range(1, days + 1):
            # Simulate gradual recovery and appetite adjustment
            self.appetite_level += (100 - self.appetite_level) * 0.1  # Gradual increase in appetite
            print(f"Day {day}: Stomach Size = {self.get_stomach_size()} ml, Appetite Level = {self.get_appetite_level()}")

# Example usage:
if __name__ == "__main__":
    try:
        initial_size = 1000  # Initial stomach size in milliliters
        surgery = GastricSleeveSurgery(initial_size)
        surgery.perform_surgery()
        surgery.simulate_post_surgery(10)  # Simulate 10 days of recovery
    except ValueError as e:
        print(f"Error: {e}")
```
