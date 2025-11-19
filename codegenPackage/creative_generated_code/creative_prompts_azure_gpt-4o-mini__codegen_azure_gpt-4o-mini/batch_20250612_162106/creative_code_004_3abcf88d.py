"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanosolutions.in
Prompt: Code a simulation for the operation of a paddy dryer, utilizing the specifications of the various components mentioned on Mechano Solutions' webpage.
Generated: DETERMINISTIC_3abcf88d3d5f261f
Batch ID: 20250612_162106
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


class PaddyDryer:
    def __init__(self, initial_moisture_content, target_moisture_content, drying_rate):
        """
        Initialize the PaddyDryer instance.

        :param initial_moisture_content: Initial moisture content of the paddy (percentage).
        :param target_moisture_content: Desired moisture content after drying (percentage).
        :param drying_rate: Rate at which moisture is removed (percentage per hour).
        """
        self.initial_moisture_content = initial_moisture_content
        self.target_moisture_content = target_moisture_content
        self.drying_rate = drying_rate
        self.current_moisture_content = initial_moisture_content
        self.drying_time = 0

    def start_drying(self):
        """Start the drying process and simulate the operation until the target moisture content is reached."""
        print(f"Starting drying process...")
        print(f"Initial moisture content: {self.initial_moisture_content}%")
        print(f"Target moisture content: {self.target_moisture_content}%")
        
        while self.current_moisture_content > self.target_moisture_content:
            self._dry_one_hour()
            self._display_status()
            time.sleep(1)  # Simulate time passing; Replace with time.sleep(3600) for real-time simulation

        print("Drying process completed.")

    def _dry_one_hour(self):
        """Simulate drying for one hour."""
        moisture_loss = min(self.drying_rate, self.current_moisture_content - self.target_moisture_content)
        self.current_moisture_content -= moisture_loss
        self.drying_time += 1

    def _display_status(self):
        """Display the current status of the drying process."""
        print(f"Hour {self.drying_time}: Current moisture content: {self.current_moisture_content:.2f}%")

    def get_drying_time(self):
        """Return the total time taken for drying in hours."""
        return self.drying_time


if __name__ == "__main__":
    # Initialize the paddy dryer with example values
    try:
        initial_moisture_content = 25.0  # Initial moisture content percentage
        target_moisture_content = 14.0    # Target moisture content percentage
        drying_rate = 2.0                  # Drying rate (percentage per hour)

        # Ensure valid moisture content values
        if not (0 <= initial_moisture_content <= 100) or not (0 <= target_moisture_content <= 100):
            raise ValueError("Moisture content must be between 0 and 100 percent.")

        if initial_moisture_content < target_moisture_content:
            raise ValueError("Initial moisture content must be greater than target moisture content.")

        # Create paddy dryer instance and start the drying process
        paddy_dryer = PaddyDryer(initial_moisture_content, target_moisture_content, drying_rate)
        paddy_dryer.start_drying()

    except Exception as e:
        print(f"An error occurred: {e}")
```
