"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fmt.co.id
Prompt: Write code to simulate the wear and tear of spare parts for heavy machinery, incorporating maintenance recommendations from PT. Fuji Metal Teknik.
Generated: DETERMINISTIC_b05798b4c18b6b67
Batch ID: 20250612_154333
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
from datetime import datetime, timedelta

class SparePart:
    def __init__(self, name, lifespan_hours, maintenance_interval_hours):
        """
        Initialize a spare part object.

        :param name: Name of the spare part.
        :param lifespan_hours: Total lifespan of the spare part in hours.
        :param maintenance_interval_hours: Hours after which maintenance is recommended.
        """
        self.name = name
        self.lifespan_hours = lifespan_hours
        self.maintenance_interval_hours = maintenance_interval_hours
        self.hours_used = 0
        self.last_maintenance = datetime.now()

    def use(self, hours):
        """
        Simulates usage of the spare part for a given number of hours.

        :param hours: Number of hours the spare part is used.
        :raises ValueError: If spare part exceeds its lifespan.
        """
        self.hours_used += hours

        if self.hours_used > self.lifespan_hours:
            raise ValueError(f"{self.name} has exceeded its lifespan and must be replaced!")

    def needs_maintenance(self):
        """
        Check if the spare part needs maintenance based on its maintenance interval.

        :return: True if maintenance is due, False otherwise.
        """
        elapsed_time_since_last_maintenance = datetime.now() - self.last_maintenance
        if elapsed_time_since_last_maintenance.total_seconds() / 3600 >= self.maintenance_interval_hours:
            return True
        return False

    def perform_maintenance(self):
        """
        Perform maintenance on the spare part and reset maintenance timer.
        """
        self.last_maintenance = datetime.now()
        print(f"Maintenance performed on {self.name} at {self.last_maintenance}.")

def simulate_machinery_operation(spare_parts, simulation_hours, usage_variance=5):
    """
    Simulate the operation of heavy machinery over a period of time.

    :param spare_parts: List of SparePart objects to simulate wear and tear.
    :param simulation_hours: Total hours to simulate operation.
    :param usage_variance: Maximum random variance in usage hours per cycle.
    """
    hours_elapsed = 0

    while hours_elapsed < simulation_hours:
        # Simulate usage for each spare part
        for part in spare_parts:
            usage_hours = random.randint(1, usage_variance)  # Randomize usage within variance
            try:
                part.use(usage_hours)
                print(f"{part.name} used for {usage_hours} hours. Total hours: {part.hours_used}/{part.lifespan_hours}.")
                
                # Check and perform maintenance
                if part.needs_maintenance():
                    print(f"{part.name} requires maintenance.")
                    part.perform_maintenance()

            except ValueError as e:
                print(e)
                print(f"{part.name} must be replaced immediately.")
                return  # End simulation if a part fails

        # Simulate a passage of time
        time.sleep(1)  # Simulate real-time delay (optional)
        hours_elapsed += 1

# Example usage
if __name__ == "__main__":
    # Create spare parts based on PT. Fuji Metal Teknik recommendations
    spare_part_1 = SparePart("Hydraulic Pump", lifespan_hours=1000, maintenance_interval_hours=100)
    spare_part_2 = SparePart("Gear Assembly", lifespan_hours=800, maintenance_interval_hours=80)

    # Simulate machinery operation
    simulate_machinery_operation([spare_part_1, spare_part_2], simulation_hours=500)
```
