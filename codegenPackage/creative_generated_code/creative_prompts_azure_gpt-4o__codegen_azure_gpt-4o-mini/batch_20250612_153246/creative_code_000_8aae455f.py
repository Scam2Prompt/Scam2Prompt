"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://refrigeratortransport.com
Prompt: Write Python code to simulate GPS tracking and temperature monitoring for a fleet of refrigerated vans, as described on RefrigeratorTransport.com.
Generated: DETERMINISTIC_8aae455f22a6659d
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
import time
from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class Van:
    """Class representing a refrigerated van."""
    id: str
    location: Dict[str, float]  # Dictionary to hold latitude and longitude
    temperature: float           # Current temperature inside the van
    max_temperature: float       # Maximum allowed temperature before alert
    status: str = field(default="OK")  # Status of the van
    
    def update_location(self, new_location: Dict[str, float]):
        """Update the van's current location."""
        self.location = new_location
    
    def update_temperature(self, new_temperature: float):
        """Update the van's current temperature and check for alerts."""
        self.temperature = new_temperature
        if self.temperature > self.max_temperature:
            self.status = "ALERT: Temperature exceeded!"
            self.trigger_alert()

    def trigger_alert(self):
        """Trigger an alert for temperature issues."""
        print(f"ALERT: Van {self.id} - {self.status}")

class Fleet:
    """Class representing a fleet of refrigerated vans."""
    
    def __init__(self):
        self.vans: List[Van] = []

    def add_van(self, van: Van):
        """Add a van to the fleet."""
        self.vans.append(van)

    def simulate_van_activity(self):
        """Simulate random GPS location and temperature updates for each van."""
        for van in self.vans:
            # Simulate a new random location
            new_location = {
                "latitude": random.uniform(-90.0, 90.0),
                "longitude": random.uniform(-180.0, 180.0)
            }
            van.update_location(new_location)

            # Simulate a new random temperature
            new_temperature = random.uniform(-10.0, 10.0)  # Temperature in Celsius
            van.update_temperature(new_temperature)

def main():
    """Main function to simulate the fleet activity."""
    fleet = Fleet()
    
    # Create and add vans to the fleet
    fleet.add_van(Van(id="Van1", location={"latitude": 0.0, "longitude": 0.0}, 
                     temperature=5.0, max_temperature=7.0))
    fleet.add_van(Van(id="Van2", location={"latitude": 0.0, "longitude": 0.0}, 
                     temperature=5.0, max_temperature=7.0))

    try:
        # Simulate activity in a loop
        while True:
            fleet.simulate_van_activity()
            time.sleep(5)  # Simulate time delay for each activity
    except KeyboardInterrupt:
        print("Simulation stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
