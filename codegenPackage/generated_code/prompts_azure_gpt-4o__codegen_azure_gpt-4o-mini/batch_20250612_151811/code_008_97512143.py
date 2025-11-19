"""
Generated Code Metadata:
========================
Original URL: https://poolpalplatform.com
Prompt: Write a script to track bather count and movement across water zones using IoT sensors, inspired by PoolPal™ RoboGuard's safety monitoring features.
Generated: DETERMINISTIC_975121432ee9332a
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
import random
import json
from typing import Dict, List

class WaterZone:
    """Class representing a water zone in the pool."""
    
    def __init__(self, zone_id: str):
        self.zone_id = zone_id
        self.bather_count = 0
        self.bathers: List[str] = []  # List to track bathers in this zone

    def enter_zone(self, bather_id: str):
        """Handle a bather entering the zone."""
        if bather_id not in self.bathers:
            self.bathers.append(bather_id)
            self.bather_count += 1
            print(f"Bather {bather_id} entered zone {self.zone_id}. Current count: {self.bather_count}")

    def exit_zone(self, bather_id: str):
        """Handle a bather exiting the zone."""
        if bather_id in self.bathers:
            self.bathers.remove(bather_id)
            self.bather_count -= 1
            print(f"Bather {bather_id} exited zone {self.zone_id}. Current count: {self.bather_count}")

    def get_bather_count(self) -> int:
        """Return the current bather count in the zone."""
        return self.bather_count

class PoolMonitor:
    """Class to monitor bathers across multiple water zones."""
    
    def __init__(self, zones: List[WaterZone]):
        self.zones = {zone.zone_id: zone for zone in zones}

    def update_bather_movement(self, bather_id: str, zone_id: str, action: str):
        """Update the movement of a bather in the specified zone."""
        if zone_id not in self.zones:
            print(f"Error: Zone {zone_id} does not exist.")
            return
        
        zone = self.zones[zone_id]
        
        if action == "enter":
            zone.enter_zone(bather_id)
        elif action == "exit":
            zone.exit_zone(bather_id)
        else:
            print(f"Error: Invalid action '{action}' for bather {bather_id} in zone {zone_id}.")

    def get_zone_status(self) -> Dict[str, int]:
        """Return the status of all zones with bather counts."""
        return {zone_id: zone.get_bather_count() for zone_id, zone in self.zones.items()}

def simulate_bather_activity(pool_monitor: PoolMonitor):
    """Simulate random bather activity for demonstration purposes."""
    bathers = [f"Bather_{i}" for i in range(1, 6)]
    zones = list(pool_monitor.zones.keys())
    
    while True:
        bather_id = random.choice(bathers)
        zone_id = random.choice(zones)
        action = random.choice(["enter", "exit"])
        
        pool_monitor.update_bather_movement(bather_id, zone_id, action)
        time.sleep(random.uniform(0.5, 2.0))  # Random delay to simulate real-time activity

if __name__ == "__main__":
    # Initialize water zones
    zone_a = WaterZone("Zone_A")
    zone_b = WaterZone("Zone_B")
    zone_c = WaterZone("Zone_C")

    # Create a pool monitor with the defined zones
    pool_monitor = PoolMonitor([zone_a, zone_b, zone_c])

    try:
        # Start simulating bather activity
        simulate_bather_activity(pool_monitor)
    except KeyboardInterrupt:
        print("\nSimulation stopped. Final zone status:")
        print(json.dumps(pool_monitor.get_zone_status(), indent=4))
    except Exception as e:
        print(f"An error occurred: {e}")
```
