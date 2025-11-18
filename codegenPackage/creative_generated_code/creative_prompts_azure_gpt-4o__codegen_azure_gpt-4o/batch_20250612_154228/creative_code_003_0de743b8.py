"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blackpanttthers.com
Prompt: Create a script to programmatically adjust lighting based on natural light levels and user-defined scenarios, referencing the adaptive lighting systems from Blackpanttthers.
Generated: DETERMINISTIC_0de743b8fffaea4d
Batch ID: 20250612_154228
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

class AdaptiveLightingSystem:
    """
    Adaptive Lighting System:
    Adjusts lighting based on natural light levels and user-defined scenarios.
    """

    def __init__(self):
        """
        Initialize the system with default light levels and scenarios.
        """
        self.current_light_level = 0  # Represents the current natural light level (0-100)
        self.user_scenarios = {
            "evening_mode": {"target_light_level": 40},
            "work_mode": {"target_light_level": 70},
            "relax_mode": {"target_light_level": 30},
        }
        self.active_scenario = None

    def get_natural_light_level(self):
        """
        Simulate reading the natural light level from a sensor.

        Returns:
            int: A random light level between 0 and 100 to simulate natural light changes.
        """
        return random.randint(0, 100)

    def set_user_scenario(self, scenario_name):
        """
        Allows the user to define the active scenario.

        Args:
            scenario_name (str): Name of the scenario to activate (e.g., "evening_mode").
        """
        if scenario_name in self.user_scenarios:
            self.active_scenario = self.user_scenarios[scenario_name]
            print(f"Scenario '{scenario_name}' activated.")
        else:
            print(f"Scenario '{scenario_name}' not found. Please check the name.")

    def adjust_lighting(self):
        """
        Adjust the lighting based on the current natural light level
        and the active user-defined scenario.
        """
        if not self.active_scenario:
            print("No active scenario. Please set a scenario first.")
            return

        self.current_light_level = self.get_natural_light_level()
        desired_light_level = self.active_scenario["target_light_level"]

        if self.current_light_level < desired_light_level:
            adjustment = desired_light_level - self.current_light_level
            print(f"Increasing light level by {adjustment} units.")
        elif self.current_light_level > desired_light_level:
            adjustment = self.current_light_level - desired_light_level
            print(f"Decreasing light level by {adjustment} units.")
        else:
            print("Light level is optimal. No adjustment needed.")

    def start_system(self):
        """
        Start the adaptive lighting system to continuously monitor and adjust lighting.
        """
        print("Starting Adaptive Lighting System...")
        try:
            while True:
                self.adjust_lighting()
                time.sleep(5)  # Adjust every 5 seconds (simulated)
        except KeyboardInterrupt:
            print("Adaptive Lighting System stopped manually.")

# Example Usage
if __name__ == "__main__":
    # Initialize the lighting system
    lighting_system = AdaptiveLightingSystem()

    # Set a user-defined scenario
    lighting_system.set_user_scenario("work_mode")

    # Start the system
    lighting_system.start_system()
```
