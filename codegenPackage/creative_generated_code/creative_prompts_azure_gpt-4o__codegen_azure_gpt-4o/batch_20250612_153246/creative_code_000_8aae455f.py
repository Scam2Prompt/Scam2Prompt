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
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class RefrigeratedVan:
    """
    A class to simulate a refrigerated van with GPS tracking and temperature monitoring.
    """
    def __init__(self, van_id):
        """
        Initializes a RefrigeratedVan instance.
        
        Args:
            van_id (str): Unique identifier for the van.
        """
        self.van_id = van_id
        self.latitude = random.uniform(-90, 90)  # Random initial latitude
        self.longitude = random.uniform(-180, 180)  # Random initial longitude
        self.temperature = random.uniform(-20, 5)  # Random initial temperature (in Celsius)
    
    def update_location(self):
        """
        Updates the van's GPS location with simulated movement.
        """
        self.latitude += random.uniform(-0.05, 0.05)  # Simulate latitude movement
        self.longitude += random.uniform(-0.05, 0.05)  # Simulate longitude movement
    
    def update_temperature(self):
        """
        Updates the van's temperature with simulated fluctuation.
        """
        self.temperature += random.uniform(-0.5, 0.5)  # Simulate temperature fluctuation
        
        # Ensure temperature stays within realistic bounds
        if self.temperature < -20:
            self.temperature = -20
        elif self.temperature > 5:
            self.temperature = 5
    
    def get_status(self):
        """
        Retrieves the current status of the van.
        
        Returns:
            dict: A dictionary containing the van's ID, GPS location, and temperature.
        """
        return {
            'van_id': self.van_id,
            'latitude': round(self.latitude, 6),
            'longitude': round(self.longitude, 6),
            'temperature': round(self.temperature, 2)
        }

def simulate_fleet_tracking(vans, simulation_duration=60, update_interval=5):
    """
    Simulates GPS tracking and temperature monitoring for a fleet of vans.
    
    Args:
        vans (list): List of RefrigeratedVan objects.
        simulation_duration (int): Total duration of the simulation in seconds.
        update_interval (int): Interval in seconds between updates.
    """
    start_time = time.time()
    while time.time() - start_time < simulation_duration:
        for van in vans:
            try:
                van.update_location()
                van.update_temperature()
                status = van.get_status()
                logging.info(f"Van {status['van_id']}: Location ({status['latitude']}, {status['longitude']}), "
                             f"Temperature: {status['temperature']}°C")
            except Exception as e:
                # Log and continue simulation in case of an error
                logging.error(f"Error updating van {van.van_id}: {str(e)}")
        
        time.sleep(update_interval)

# Create a fleet of refrigerated vans
fleet = [RefrigeratedVan(van_id=f"Van_{i+1}") for i in range(10)]

# Simulate fleet tracking and monitoring for 1 minute (60 seconds)
simulate_fleet_tracking(fleet, simulation_duration=60, update_interval=5)
```
