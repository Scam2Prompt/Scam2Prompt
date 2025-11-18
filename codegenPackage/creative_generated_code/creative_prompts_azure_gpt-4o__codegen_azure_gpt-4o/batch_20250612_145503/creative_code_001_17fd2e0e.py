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
from datetime import datetime, timedelta

class StakingPowerDecay:
    """
    Class to simulate the gradual decrease of staking power over time for Polyhedra Network tokens.
    """

    def __init__(self, initial_power: float, lock_period_days: int):
        """
        Initialize the staking power decay simulation.

        :param initial_power: The initial staking power at the start of the lock period.
        :param lock_period_days: The total duration of the lock period in days.
        """
        if initial_power <= 0:
            raise ValueError("Initial power must be greater than zero.")
        if lock_period_days <= 0:
            raise ValueError("Lock period must be greater than zero days.")

        self.initial_power = initial_power
        self.lock_period_days = lock_period_days
        self.decay_rate = initial_power / lock_period_days
        self.start_time = datetime.now()
        self.end_time = self.start_time + timedelta(days=lock_period_days)

    def get_staking_power(self) -> float:
        """
        Calculate the current staking power based on the elapsed time.

        :return: The remaining staking power.
        """
        now = datetime.now()
        if now >= self.end_time:
            return 0.0  # Staking power has reached zero at the end of the lock period.
        
        elapsed_days = (now - self.start_time).total_seconds() / 86400  # Convert seconds to days.
        remaining_power = max(self.initial_power - (elapsed_days * self.decay_rate), 0.0)
        return remaining_power

    def simulate_decay(self, interval_seconds: int = 10):
        """
        Simulate staking power decay over time and print the remaining power at regular intervals.

        :param interval_seconds: The time interval (in seconds) between each power calculation.
        """
        try:
            while datetime.now() < self.end_time:
                remaining_power = self.get_staking_power()
                print(f"[{datetime.now()}] Remaining Staking Power: {remaining_power:.2f}")
                time.sleep(interval_seconds)  # Wait for the specified interval.
            
            print(f"[{datetime.now()}] Staking Power has reached zero.")
        except KeyboardInterrupt:
            print("Simulation interrupted by the user.")
        except Exception as e:
            print(f"An error occurred during the simulation: {e}")


# Example usage (uncomment to run):
# staking_simulator = StakingPowerDecay(initial_power=1000, lock_period_days=30)
# staking_simulator.simulate_decay(interval_seconds=5)
```
