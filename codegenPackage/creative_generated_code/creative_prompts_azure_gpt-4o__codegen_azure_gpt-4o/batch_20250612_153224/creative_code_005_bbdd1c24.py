"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://indpfire.com
Prompt: Write code to simulate the response time of a sprinkler system in reducing heat, flames, and smoke during a fire, based on the benefits outlined by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_bbdd1c249346f0ac
Batch ID: 20250612_153224
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


class FireSimulation:
    """
    Class to simulate the response of a sprinkler system during a fire.
    This simulation tracks heat, flames, and smoke levels and demonstrates how sprinklers mitigate them over time.
    """

    def __init__(self, initial_heat: int, initial_flames: int, initial_smoke: int):
        """
        Initialize the fire simulation with starting levels for heat, flames, and smoke.

        :param initial_heat: Initial heat level (0-100).
        :param initial_flames: Initial flames level (0-100).
        :param initial_smoke: Initial smoke level (0-100).
        """
        self.heat = initial_heat  # Heat intensity, 0-100
        self.flames = initial_flames  # Flames intensity, 0-100
        self.smoke = initial_smoke  # Smoke intensity, 0-100
        self.sprinkler_active = False  # Sprinkler activation status

    def activate_sprinkler(self):
        """
        Activate the sprinkler system.
        """
        self.sprinkler_active = True
        print("Sprinkler system activated.")

    def simulate_fire(self):
        """
        Simulate fire conditions worsening over time.
        """
        self.heat = min(self.heat + random.randint(5, 15), 100)
        self.flames = min(self.flames + random.randint(5, 10), 100)
        self.smoke = min(self.smoke + random.randint(3, 8), 100)

    def reduce_fire(self):
        """
        Simulate the sprinkler system reducing heat, flames, and smoke.
        """
        self.heat = max(self.heat - random.randint(10, 20), 0)
        self.flames = max(self.flames - random.randint(8, 15), 0)
        self.smoke = max(self.smoke - random.randint(5, 12), 0)

    def display_status(self):
        """
        Display the current fire conditions.
        """
        print(f"Heat Level: {self.heat}")
        print(f"Flames Level: {self.flames}")
        print(f"Smoke Level: {self.smoke}")

    def run_simulation(self, duration: int):
        """
        Run the fire simulation for a given duration.

        :param duration: Duration of the simulation in seconds.
        """
        print("Starting fire simulation...")
        for second in range(1, duration + 1):
            print(f"--- Time: {second} seconds ---")
            if self.sprinkler_active:
                self.reduce_fire()
            else:
                self.simulate_fire()

            self.display_status()

            # Automatically activate sprinklers if conditions reach critical levels
            if not self.sprinkler_active and (self.heat > 75 or self.flames > 50 or self.smoke > 60):
                print("Critical levels detected! Activating sprinkler system...")
                self.activate_sprinkler()

            # End simulation early if fire conditions are completely mitigated
            if self.heat == 0 and self.flames == 0 and self.smoke == 0:
                print("Fire completely mitigated. Ending simulation.")
                break

            time.sleep(1)  # Simulate real-time progression


# Example usage
if __name__ == "__main__":
    # Initialize the fire simulation with moderate fire conditions
    fire_sim = FireSimulation(initial_heat=40, initial_flames=30, initial_smoke=20)

    try:
        # Run the simulation for a maximum of 30 seconds
        fire_sim.run_simulation(duration=30)
    except KeyboardInterrupt:
        print("\nSimulation interrupted by user.")
    except Exception as e:
        print(f"\nAn error occurred during the simulation: {e}")
```
