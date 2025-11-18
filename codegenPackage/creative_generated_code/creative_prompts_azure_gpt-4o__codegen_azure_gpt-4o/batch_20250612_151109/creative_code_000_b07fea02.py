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

Here's Python code for simulating the scheduling of digital advertisements on a videotron display:

```python
import datetime
import time
from typing import List, Dict

class Advertisement:
    """
    Class representing a single advertisement.
    """
    def __init__(self, ad_id: str, content: str, duration: int):
        """
        Initialize an advertisement.

        :param ad_id: Unique identifier for the advertisement
        :param content: Content of the advertisement (e.g., text or media file name)
        :param duration: Duration of the advertisement in seconds
        """
        self.ad_id = ad_id
        self.content = content
        self.duration = duration


class TimeSlot:
    """
    Class representing a time slot for scheduling advertisements.
    """
    def __init__(self, start_time: datetime.time, end_time: datetime.time):
        """
        Initialize a time slot.

        :param start_time: Start time of the slot (hh:mm:ss)
        :param end_time: End time of the slot (hh:mm:ss)
        """
        self.start_time = start_time
        self.end_time = end_time
        self.advertisements: List[Advertisement] = []

    def add_advertisement(self, advertisement: Advertisement):
        """
        Add an advertisement to the time slot.

        :param advertisement: The advertisement to add
        """
        self.advertisements.append(advertisement)

    def rotate_ads(self):
        """
        Rotate through the advertisements in this time slot based on their duration.
        """
        print(f"Time Slot {self.start_time.strftime('%H:%M:%S')} - {self.end_time.strftime('%H:%M:%S')} running...")
        while True:
            current_time = datetime.datetime.now().time()
            if current_time >= self.end_time or current_time < self.start_time:
                print(f"Exiting Time Slot {self.start_time.strftime('%H:%M:%S')} - {self.end_time.strftime('%H:%M:%S')}")
                break

            for ad in self.advertisements:
                print(f"Displaying Advertisement: {ad.content} (ID: {ad.ad_id}) for {ad.duration} seconds...")
                time.sleep(ad.duration)


class VideotronScheduler:
    """
    Class for managing the scheduling of advertisements on a videotron display.
    """
    def __init__(self):
        """
        Initialize the scheduler with no time slots.
        """
        self.time_slots: List[TimeSlot] = []

    def add_time_slot(self, time_slot: TimeSlot):
        """
        Add a time slot to the scheduler.

        :param time_slot: The time slot to add
        """
        self.time_slots.append(time_slot)

    def run_scheduler(self):
        """
        Run the scheduler to display advertisements based on time slots.
        """
        while True:
            current_time = datetime.datetime.now().time()
            for slot in self.time_slots:
                if slot.start_time <= current_time < slot.end_time:
                    slot.rotate_ads()


# Example Usage
if __name__ == "__main__":
    try:
        # Create sample advertisements
        ad1 = Advertisement(ad_id="A001", content="Ad Content 1", duration=10)
        ad2 = Advertisement(ad_id="A002", content="Ad Content 2", duration=15)
        ad3 = Advertisement(ad_id="A003", content="Ad Content 3", duration=20)

        # Create a time slot and assign advertisements
        morning_slot = TimeSlot(start_time=datetime.time(9, 0, 0), end_time=datetime.time(12, 0, 0))
        morning_slot.add_advertisement(ad1)
        morning_slot.add_advertisement(ad2)
        morning_slot.add_advertisement(ad3)

        # Create another time slot
        evening_slot = TimeSlot(start_time=datetime.time(18, 0, 0), end_time=datetime.time(21, 0, 0))
        evening_slot.add_advertisement(ad2)
        evening_slot.add_advertisement(ad3)

        # Initialize the scheduler and add time slots
        scheduler = VideotronScheduler()
        scheduler.add_time_slot(morning_slot)
        scheduler.add_time_slot(evening_slot)

        # Run the scheduler
        scheduler.run_scheduler()

    except KeyboardInterrupt:
        print("\nScheduler stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")
```
