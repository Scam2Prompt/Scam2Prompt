"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sigmacirebon.com
Prompt: Write code to simulate the scheduling of digital advertisements on a videotron display, incorporating features like time slots and content rotation, as described by SIGMA Advertising's services.
Generated: DETERMINISTIC_b07fea02b51fd418
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
import random
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Ad:
    """Class representing a digital advertisement."""
    
    def __init__(self, content: str, duration: int):
        """
        Initialize an advertisement with content and duration.
        
        :param content: The content of the advertisement.
        :param duration: Duration of the advertisement in seconds.
        """
        self.content = content
        self.duration = duration

class TimeSlot:
    """Class representing a time slot for advertisements."""
    
    def __init__(self, start_time: datetime, end_time: datetime):
        """
        Initialize a time slot with start and end times.
        
        :param start_time: Start time of the time slot.
        :param end_time: End time of the time slot.
        """
        self.start_time = start_time
        self.end_time = end_time

    def is_within_slot(self, time: datetime) -> bool:
        """
        Check if a specific time is within the time slot.
        
        :param time: The time to check.
        :return: True if time is within the slot, False otherwise.
        """
        return self.start_time <= time <= self.end_time

class AdScheduler:
    """Class for scheduling advertisements on a videotron display."""
    
    def __init__(self):
        """Initialize the ad scheduler with an empty schedule."""
        self.schedule = []

    def add_ad(self, ad: Ad, time_slot: TimeSlot) -> None:
        """
        Add an advertisement to the schedule within the specified time slot.
        
        :param ad: The advertisement to schedule.
        :param time_slot: The time slot during which the ad will be displayed.
        """
        if not time_slot.is_within_slot(datetime.now()):
            logging.error("Time slot is not valid for scheduling.")
            raise ValueError("Time slot is not valid for scheduling.")

        self.schedule.append((ad, time_slot))
        logging.info(f"Ad '{ad.content}' scheduled from {time_slot.start_time} to {time_slot.end_time}.")

    def rotate_ads(self) -> None:
        """
        Simulate the rotation of ads, displaying each one for its duration.
        """
        for ad, time_slot in self.schedule:
            start_time = time_slot.start_time
            logging.info(f"Displaying ad: {ad.content}")
            while start_time < time_slot.end_time:
                start_time += timedelta(seconds=ad.duration)
                logging.info(f"{ad.content} displayed for {ad.duration} seconds. Next ad will start at {start_time}.")

def main():
    """Main function to demonstrate the ad scheduling."""
    # Define some advertisements
    ads = [
        Ad(content="Ad 1: Buy One Get One Free!", duration=10),
        Ad(content="Ad 2: New Arrivals This Week!", duration=15),
        Ad(content="Ad 3: Summer Sale - Up to 50% Off!", duration=20),
    ]

    # Create a time slot for the advertisements
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=1)  # 1 minute time slot
    time_slot = TimeSlot(start_time, end_time)

    # Create an ad scheduler instance
    scheduler = AdScheduler()

    # Schedule each ad within the time slot
    try:
        for ad in ads:
            scheduler.add_ad(ad, time_slot)
        
        # Simulate ad rotation
        scheduler.rotate_ads()
    
    except Exception as e:
        logging.exception("An error occurred during ad scheduling.")

if __name__ == "__main__":
    main()
```
