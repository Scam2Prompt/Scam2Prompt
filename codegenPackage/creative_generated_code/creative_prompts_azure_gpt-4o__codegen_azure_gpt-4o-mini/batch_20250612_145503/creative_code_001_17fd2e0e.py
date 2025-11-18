"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polyhedra-foundation-web.pages.dev
Prompt: Generate code to simulate the gradual decrease of staking power over time for Polyhedra Network tokens, ensuring it reaches zero at the end of the lock period.
Generated: DETERMINISTIC_17fd2e0e827044de
Batch ID: 20250612_145503
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time

class StakingSimulation:
    """
    A class to simulate the gradual decrease of staking power over time for Polyhedra Network tokens.
    """

    def __init__(self, initial_staking_power, lock_period):
        """
        Initializes the StakingSimulation with given parameters.

        :param initial_staking_power: The initial amount of staking power.
        :param lock_period: The duration (in seconds) over which the staking power decreases to zero.
        """
        self.initial_staking_power = initial_staking_power
        self.lock_period = lock_period
        self.remaining_power = initial_staking_power
        self.start_time = None

    def start_staking(self):
        """
        Starts the staking process, simulating the gradual decrease of staking power.
        """
        self.start_time = time.time()
        print(f"Staking started with an initial power of {self.initial_staking_power}.")

        try:
            while self.remaining_power > 0:
                elapsed_time = time.time() - self.start_time
                self.update_staking_power(elapsed_time)
                print(f"Remaining staking power: {self.remaining_power:.2f}")
                time.sleep(1)  # Update every second

        except KeyboardInterrupt:
            print("\nStaking simulation interrupted.")
        except Exception as e:
            print(f"An error occurred during the staking simulation: {e}")

        self.remaining_power = 0
        print("Staking period completed. Remaining power has reached zero.")

    def update_staking_power(self, elapsed_time):
        """
        Updates the remaining staking power based on elapsed time.

        :param elapsed_time: The amount of time (in seconds) that has passed since staking started.
        """
        # Calculate the fraction of the lock period that has elapsed
        fraction_elapsed = elapsed_time / self.lock_period
        # Ensure it does not exceed 1
        fraction_elapsed = min(fraction_elapsed, 1)
        # Update remaining power
        self.remaining_power = self.initial_staking_power * (1 - fraction_elapsed)

if __name__ == "__main__":
    # Example usage
    initial_power = 1000  # Initial staking power
    lock_duration = 10    # Lock period in seconds

    staking_simulation = StakingSimulation(initial_power, lock_duration)
    staking_simulation.start_staking()
```
