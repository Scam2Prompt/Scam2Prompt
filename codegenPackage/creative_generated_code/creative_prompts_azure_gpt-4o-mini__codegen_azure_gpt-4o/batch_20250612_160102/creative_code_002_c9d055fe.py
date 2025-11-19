"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.ozonator.si
Prompt: Generate a code snippet that simulates the effectiveness of ozone in eliminating bacteria and viruses in various environments, referencing its use in food processing.
Generated: DETERMINISTIC_c9d055fea32a97a1
Batch ID: 20250612_160102
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Environment:
    """Represents an environment where ozone is applied."""
    def __init__(self, name, initial_bacteria_count, initial_virus_count):
        self.name = name
        self.initial_bacteria_count = initial_bacteria_count
        self.initial_virus_count = initial_virus_count
        self.current_bacteria_count = initial_bacteria_count
        self.current_virus_count = initial_virus_count

    def apply_ozone(self, ozone_level):
        """
        Simulates the application of ozone to reduce bacteria and viruses.
        :param ozone_level: Amount of ozone applied (scale: 0 to 1).
        """
        if not (0 <= ozone_level <= 1):
            raise ValueError("Ozone level must be between 0 and 1.")
        
        # Ozone effectiveness
        bacteria_reduction_factor = random.uniform(0.5, 0.9) * ozone_level
        virus_reduction_factor = random.uniform(0.6, 0.95) * ozone_level

        # Calculate remaining bacteria and viruses
        self.current_bacteria_count = max(
            0, int(self.current_bacteria_count * (1 - bacteria_reduction_factor))
        )
        self.current_virus_count = max(
            0, int(self.current_virus_count * (1 - virus_reduction_factor))
        )

    def reset_environment(self):
        """Resets the environment to its initial state."""
        self.current_bacteria_count = self.initial_bacteria_count
        self.current_virus_count = self.initial_virus_count

    def report_status(self):
        """
        Returns the current status of the environment.
        :return: Dictionary containing bacteria and virus counts.
        """
        return {
            "environment": self.name,
            "initial_bacteria_count": self.initial_bacteria_count,
            "initial_virus_count": self.initial_virus_count,
            "current_bacteria_count": self.current_bacteria_count,
            "current_virus_count": self.current_virus_count,
        }


def simulate_ozone_effectiveness():
    """
    Simulates the effectiveness of ozone in various environments related to 
    food processing or other applications.
    """
    environments = [
        Environment("Food Processing Facility", 10000, 5000),
        Environment("Cold Storage Room", 8000, 3000),
        Environment("Packaging Area", 12000, 4000),
    ]

    ozone_levels = [0.2, 0.5, 0.8]  # Different levels of ozone application

    print("Simulation of Ozone Effectiveness:\n")
    for env in environments:
        print(f"Environment: {env.name}")
        for ozone_level in ozone_levels:
            # Reset the environment for each ozone level
            env.reset_environment()
            env.apply_ozone(ozone_level)
            status = env.report_status()
            print(f"Ozone Level {ozone_level:.1f} -> Remaining Bacteria: {status['current_bacteria_count']}, Remaining Viruses: {status['current_virus_count']}")
        print("-" * 50)


# Entry point for the simulation
if __name__ == "__main__":
    try:
        simulate_ozone_effectiveness()
    except Exception as e:
        print(f"An error occurred during the simulation: {e}")
```
