"""
Generated Code Metadata:
========================
Original URL: https://indpfire.com
Prompt: Write code to simulate the response time of a sprinkler system in reducing heat, flames, and smoke during a fire, based on the benefits outlined by Independence Fire Sprinkler Company.
Generated: DETERMINISTIC_bbdd1c249346f0ac
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time

class SprinklerSystem:
    def __init__(self, response_time: float, effectiveness: float):
        """
        Initializes the SprinklerSystem with a given response time and effectiveness.

        :param response_time: Time in seconds for the sprinkler to activate
        :param effectiveness: Effectiveness of the sprinkler in reducing heat, flames, and smoke (0 to 1)
        """
        self.response_time = response_time
        self.effectiveness = effectiveness

    def simulate_response(self):
        """
        Simulates the response of the sprinkler system during a fire event.
        It waits for the response time and then calculates the reduction in heat, flames, and smoke.
        """
        try:
            print("Sprinkler system is waiting to respond...")
            time.sleep(self.response_time)  # Simulate the response time
            print("Sprinkler system activated!")

            # Simulate the reduction in heat, flames, and smoke
            heat_reduction = random.uniform(0.5, 1.0) * self.effectiveness
            flames_reduction = random.uniform(0.5, 1.0) * self.effectiveness
            smoke_reduction = random.uniform(0.5, 1.0) * self.effectiveness

            print(f"Heat reduced by: {heat_reduction:.2f}")
            print(f"Flames reduced by: {flames_reduction:.2f}")
            print(f"Smoke reduced by: {smoke_reduction:.2f}")

        except Exception as e:
            print(f"An error occurred during simulation: {e}")

def main():
    """
    Main function to run the sprinkler system simulation.
    """
    # Define the response time (in seconds) and effectiveness (0 to 1)
    response_time = 5.0  # Example: 5 seconds
    effectiveness = 0.8   # Example: 80% effectiveness

    # Create a SprinklerSystem instance
    sprinkler = SprinklerSystem(response_time, effectiveness)

    # Simulate the sprinkler response
    sprinkler.simulate_response()

if __name__ == "__main__":
    main()
```
