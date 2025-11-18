"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poolpalplatform.com
Prompt: Write a script to track bather count and movement across water zones using IoT sensors, inspired by PoolPal™ RoboGuard's safety monitoring features.
Generated: DETERMINISTIC_975121432ee9332a
Batch ID: 20250612_151811
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
import json
from typing import List, Dict

class Bather:
    """Class to represent a bather in the pool."""
    def __init__(self, id: int, zone: str):
        self.id = id
        self.zone = zone
        self.entry_time = time.time()

    def update_zone(self, new_zone: str):
        """Update the bather's zone."""
        self.zone = new_zone
        self.entry_time = time.time()


class PoolZone:
    """Class to represent a zone in the pool."""
    def __init__(self, name: str):
        self.name = name
        self.bathers: List[Bather] = []

    def add_bather(self, bather: Bather):
        """Add a bather to this zone."""
        self.bathers.append(bather)

    def remove_bather(self, bather_id: int):
        """Remove a bather from this zone by ID."""
        self.bathers = [b for b in self.bathers if b.id != bather_id]

    def get_bather_count(self) -> int:
        """Get the current number of bathers in this zone."""
        return len(self.bathers)

    def get_bather_info(self) -> List[Dict]:
        """Get information of all bathers in this zone."""
        return [{'id': bather.id, 'entry_time': bather.entry_time} for bather in self.bathers]


class PoolMonitor:
    """Class to monitor the pool zones and track bathers."""
    def __init__(self):
        self.zones: Dict[str, PoolZone] = {
            'Shallow End': PoolZone('Shallow End'),
            'Deep End': PoolZone('Deep End'),
            'Spa Area': PoolZone('Spa Area')
        }

    def track_bather(self, bather_id: int, zone_name: str):
        """Track a bather's movement across zones."""
        if zone_name not in self.zones:
            raise ValueError(f"Zone '{zone_name}' does not exist.")

        # Check if the bather is already in another zone
        for zone in self.zones.values():
            if any(bather.id == bather_id for bather in zone.bathers):
                zone.remove_bather(bather_id)

        # Add the bather to the new zone
        new_bather = Bather(bather_id, zone_name)
        self.zones[zone_name].add_bather(new_bather)

    def get_zone_statistics(self) -> Dict[str, int]:
        """Get statistics of bathers in all zones."""
        return {zone_name: zone.get_bather_count() for zone_name, zone in self.zones.items()}

    def log_bather_data(self):
        """Log the current state of bathed data in JSON format."""
        log_data = {zone_name: zone.get_bather_info() for zone_name, zone in self.zones.items()}
        with open('bather_log.json', 'w') as log_file:
            json.dump(log_data, log_file, indent=4)


def simulate_pool_activity(monitor: PoolMonitor):
    """Simulate the bathers' activity in the pool."""
    try:
        for _ in range(10):
            bather_id = random.randint(1, 5)  # Simulate 5 bathers with IDs from 1 to 5
            zone = random.choice(list(monitor.zones.keys()))
            monitor.track_bather(bather_id, zone)
            print(f"Bather {bather_id} moved to {zone}.")
            time.sleep(1)  # Simulate time delay between movements

        # Log the bather data after simulation
        monitor.log_bather_data()
        print("Bather data logged successfully.")

    except Exception as e:
        print(f"Error during simulation: {e}")


if __name__ == "__main__":
    pool_monitor = PoolMonitor()
    simulate_pool_activity(pool_monitor)
```
