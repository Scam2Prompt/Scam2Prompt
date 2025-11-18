"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sophpon.pages.dev
Prompt: Write a script to simulate the tokenomics of the $SOPH token, including vesting schedules and allocations for node rewards, the Sophon Foundation, seed contributors, advisors, and ecosystem reserves.
Generated: DETERMINISTIC_b3af876b066398f6
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Allocation:
    """Represents the allocation of tokens for a specific purpose."""
    name: str
    total_amount: int
    vesting_period_months: int
    start_date: datetime.date

    def calculate_vesting_schedule(self) -> Dict[str, int]:
        """Calculates the vesting schedule based on the allocation."""
        monthly_vesting = self.total_amount // self.vesting_period_months
        vesting_schedule = {}
        for month in range(self.vesting_period_months):
            vesting_date = self.start_date + datetime.timedelta(days=30 * month)
            vesting_schedule[vesting_date] = monthly_vesting
        return vesting_schedule

class TokenomicsSimulator:
    """Simulates the tokenomics of the $SOPH token."""

    def __init__(self):
        """Initializes the simulator with predefined allocations."""
        self.allocations: List[Allocation] = [
            Allocation("Node Rewards", 1_000_000, 24, datetime.date(2023, 1, 1)),
            Allocation("Sophon Foundation", 500_000, 36, datetime.date(2023, 1, 1)),
            Allocation("Seed Contributors", 200_000, 12, datetime.date(2023, 1, 1)),
            Allocation("Advisors", 100_000, 18, datetime.date(2023, 1, 1)),
            Allocation("Ecosystem Reserves", 300_000, 48, datetime.date(2023, 1, 1))
        ]
    
    def simulate(self):
        """Runs the simulation and prints the vesting schedules."""
        for allocation in self.allocations:
            try:
                schedule = allocation.calculate_vesting_schedule()
                print(f"Vesting Schedule for {allocation.name}:")
                for date, amount in schedule.items():
                    print(f"  {date}: {amount} tokens")
                print("")
            except Exception as e:
                print(f"Error calculating vesting for {allocation.name}: {e}")

if __name__ == "__main__":
    simulator = TokenomicsSimulator()
    simulator.simulate()
```
