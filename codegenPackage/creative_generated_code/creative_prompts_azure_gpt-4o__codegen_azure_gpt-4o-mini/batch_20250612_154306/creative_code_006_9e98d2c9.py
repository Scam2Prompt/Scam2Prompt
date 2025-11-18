"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jggbbestforyou.com
Prompt: Create a script to simulate the behavior of Medtrum TouchCare® Nano insulin pump under different insulin infusion rates and user-defined glucose targets.
Generated: DETERMINISTIC_9e98d2c9b3bb67c9
Batch ID: 20250612_154306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time

class InsulinPump:
    def __init__(self, glucose_target, infusion_rate):
        """
        Initializes the InsulinPump with a target glucose level and an infusion rate.

        Args:
            glucose_target (float): Desired glucose level in mg/dL.
            infusion_rate (float): Insulin infusion rate in units/hour.
        """
        self.glucose_target = glucose_target
        self.infusion_rate = infusion_rate
        self.current_glucose_level = self.simulate_initial_glucose()

    def simulate_initial_glucose(self):
        """
        Simulates an initial glucose level.

        Returns:
            float: Random initial glucose level between 70 and 180 mg/dL.
        """
        return random.uniform(70, 180)

    def adjust_glucose_level(self):
        """
        Adjusts the current glucose level based on the insulin infusion rate.
        """
        # Simulate the effect of insulin infusion on glucose level
        glucose_change = -self.infusion_rate * random.uniform(0.1, 0.5)  # Random effect of insulin
        self.current_glucose_level += glucose_change
        
        # Ensure glucose level stays within physiological limits
        if self.current_glucose_level < 40:
            self.current_glucose_level = 40
        elif self.current_glucose_level > 400:
            self.current_glucose_level = 400

    def check_glucose(self):
        """
        Checks the current glucose level against the target and prints the status.
        """
        if self.current_glucose_level < self.glucose_target:
            status = "Below target"
        elif self.current_glucose_level > self.glucose_target:
            status = "Above target"
        else:
            status = "On target"

        print(f"Current Glucose Level: {self.current_glucose_level:.2f} mg/dL - Status: {status}")

    def run_simulation(self, duration_hours):
        """
        Runs the glucose level simulation for a specified duration.

        Args:
            duration_hours (int): The number of hours to run the simulation.
        """
        for hour in range(duration_hours):
            self.adjust_glucose_level()
            self.check_glucose()
            time.sleep(1)  # Simulate waiting time as though each iteration represents an hour

# Example usage of the InsulinPump class
if __name__ == "__main__":
    try:
        # User-defined glucose target and infusion rate
        user_glucose_target = 100  # Desired glucose level in mg/dL
        user_inf_rate = 2  # Insulin infusion rate in units/hour

        # Instantiate the insulin pump simulator
        pump = InsulinPump(glucose_target=user_glucose_target, infusion_rate=user_inf_rate)

        # Run the simulation for 5 hours
        pump.run_simulation(duration_hours=5)

    except Exception as e:
        print(f"An error occurred: {e}")
```
