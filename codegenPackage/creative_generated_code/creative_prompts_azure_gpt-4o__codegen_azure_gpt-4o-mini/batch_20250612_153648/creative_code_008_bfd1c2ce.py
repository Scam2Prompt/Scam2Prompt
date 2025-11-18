"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://raffle-front-beige.vercel.app
Prompt: Write a script to automatically update the status of raffles (active or past) based on their end time in a cryptocurrency raffle system.
Generated: DETERMINISTIC_bfd1c2cedd32d261
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Tuple
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Raffle:
    def __init__(self, raffle_id: int, end_time: datetime.datetime):
        """
        Initialize a Raffle instance.
        
        :param raffle_id: Unique identifier for the raffle.
        :param end_time: The datetime when the raffle ends.
        """
        self.raffle_id = raffle_id
        self.end_time = end_time
        self.status = 'active'  # Default status

    def update_status(self):
        """
        Update the status of the raffle based on the current time.
        """
        current_time = datetime.datetime.now()
        if current_time > self.end_time:
            self.status = 'past'
            logging.info(f"Raffle ID {self.raffle_id} status updated to 'past'.")
        else:
            logging.info(f"Raffle ID {self.raffle_id} is still 'active'.")

def update_raffle_statuses(raffles: List[Raffle]) -> List[Tuple[int, str]]:
    """
    Update statuses for a list of raffles.
    
    :param raffles: List of Raffle instances.
    :return: List of tuples containing raffle_id and its updated status.
    """
    updated_statuses = []
    
    for raffle in raffles:
        try:
            raffle.update_status()
            updated_statuses.append((raffle.raffle_id, raffle.status))
        except Exception as e:
            logging.error(f"Error updating status for Raffle ID {raffle.raffle_id}: {e}")
    
    return updated_statuses

if __name__ == "__main__":
    # Example Raffles with end times
    raffle1 = Raffle(1, datetime.datetime(2023, 10, 25, 12, 0, 0))  # Active raffle
    raffle2 = Raffle(2, datetime.datetime(2023, 10, 20, 12, 0, 0))  # Past raffle
    raffle3 = Raffle(3, datetime.datetime(2023, 10, 30, 12, 0, 0))  # Active raffle

    # List of raffles to update
    raffles = [raffle1, raffle2, raffle3]

    # Update statuses
    updated_statuses = update_raffle_statuses(raffles)

    # Print updated statuses
    for raffle_id, status in updated_statuses:
        print(f"Raffle ID {raffle_id} is now '{status}'.")
```
