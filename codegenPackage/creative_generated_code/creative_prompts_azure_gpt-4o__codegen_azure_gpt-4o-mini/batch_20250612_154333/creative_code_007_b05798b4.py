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
import random
import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SparePart:
    """
    Class to represent a spare part in heavy machinery.
    """
    def __init__(self, name: str, lifespan: int, maintenance_interval: int):
        """
        Initializes a SparePart instance.
        
        :param name: Name of the spare part
        :param lifespan: Total lifespan of the spare part in hours
        :param maintenance_interval: Recommended maintenance interval in hours
        """
        self.name = name
        self.lifespan = lifespan
        self.maintenance_interval = maintenance_interval
        self.current_hours = 0
        self.maintenance_due = 0

    def wear_and_tear(self):
        """
        Simulates the wear and tear on the spare part.
        Increments the current hours based on a random wear factor.
        """
        wear_factor = random.uniform(0.1, 1.0)  # Random wear factor between 0.1 and 1.0
        self.current_hours += wear_factor
        logging.info(f'{self.name}: Current hours increased by {wear_factor:.2f}. Total hours: {self.current_hours:.2f}')

        # Check if maintenance is due
        if self.current_hours >= self.maintenance_due:
            self.recommend_maintenance()

        # Check if replacement is needed
        if self.current_hours >= self.lifespan:
            logging.warning(f'{self.name} has reached end of life and needs to be replaced.')

    def recommend_maintenance(self):
        """
        Recommend maintenance based on current hours and maintenance interval.
        """
        logging.info(f'Maintenance recommended for {self.name} at {self.current_hours:.2f} hours.')
        self.maintenance_due += self.maintenance_interval  # Schedule next maintenance

    def reset(self):
        """
        Resets the current hours and maintenance schedule for the spare part.
        """
        self.current_hours = 0
        self.maintenance_due = self.maintenance_interval
        logging.info(f'{self.name} reset. Current hours: {self.current_hours}, Next maintenance due: {self.maintenance_due} hours.')

def simulate_spare_parts():
    """
    Simulates the wear and tear process for various spare parts.
    """
    # Create spare parts with test parameters
    parts = [
        SparePart("Hydraulic Pump", lifespan=1000, maintenance_interval=200),
        SparePart("Gearbox", lifespan=800, maintenance_interval=150),
        SparePart("Bearings", lifespan=500, maintenance_interval=100)
    ]
    
    # Simulate over a period of time
    for _ in range(50):  # Simulate 50 time intervals
        for part in parts:
            part.wear_and_tear()

if __name__ == "__main__":
    try:
        simulate_spare_parts()
    except Exception as e:
        logging.error(f'An error occurred: {e}')
```
