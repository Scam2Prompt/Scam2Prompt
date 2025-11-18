"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://private-gomble.pages.dev
Prompt: Generate code for tracking and displaying an airdrop schedule, including countdown timers for events like "Heat the Balloon" and "Get your Mystery Marbles," as described on the GOMBLE website.
Generated: DETERMINISTIC_c62c14b333547678
Batch ID: 20250612_153700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from datetime import datetime, timedelta

class AirdropEvent:
    """
    Class to represent an airdrop event with a name, start time, end time, and countdown.
    """
    def __init__(self, name, start_time, end_time):
        """
        Initialize an airdrop event.

        :param name: Name of the event.
        :param start_time: Start time of the event (datetime object).
        :param end_time: End time of the event (datetime object).
        """
        self.name = name
        self.start_time = start_time
        self.end_time = end_time

    def get_status(self):
        """
        Get the current status of the event.

        :return: A string indicating whether the event is upcoming, live, or ended.
        """
        now = datetime.now()
        if now < self.start_time:
            return "Upcoming"
        elif self.start_time <= now <= self.end_time:
            return "Live"
        else:
            return "Ended"

    def get_time_until_start(self):
        """
        Get the time remaining until the start of the event.

        :return: A timedelta object indicating the time until the event starts, or None if the event is already live or ended.
        """
        now = datetime.now()
        if now < self.start_time:
            return self.start_time - now
        return None

    def get_time_until_end(self):
        """
        Get the time remaining until the end of the event.

        :return: A timedelta object indicating the time until the event ends, or None if the event has ended.
        """
        now = datetime.now()
        if now < self.end_time:
            return self.end_time - now
        return None


def display_airdrop_schedule(events):
    """
    Display the airdrop schedule including countdown timers for each event.

    :param events: List of AirdropEvent objects.
    """
    print("Airdrop Schedule:")
    print("=" * 30)

    for event in events:
        print(f"Event: {event.name}")
        print(f"Status: {event.get_status()}")

        if event.get_status() == "Upcoming":
            time_until_start = event.get_time_until_start()
            print(f"Starts in: {time_until_start}")
        elif event.get_status() == "Live":
            time_until_end = event.get_time_until_end()
            print(f"Ends in: {time_until_end}")
        else:
            print("This event has ended.")

        print("-" * 30)


def main():
    try:
        # Define airdrop events (Replace these times with actual schedule from GOMBLE website)
        event1 = AirdropEvent(
            name="Heat the Balloon",
            start_time=datetime.now() + timedelta(seconds=10),
            end_time=datetime.now() + timedelta(seconds=60)
        )

        event2 = AirdropEvent(
            name="Get your Mystery Marbles",
            start_time=datetime.now() + timedelta(seconds=120),
            end_time=datetime.now() + timedelta(seconds=180)
        )

        # List of events
        events = [event1, event2]

        # Continuously display countdowns (this loop can be modified or connected to a frontend)
        while True:
            # Clear the screen for better readability (works on most terminals)
            print("\033[H\033[J", end="")

            display_airdrop_schedule(events)
            time.sleep(1)  # Update every second

    except KeyboardInterrupt:
        # Gracefully exit on user interrupt (Ctrl+C)
        print("\nExiting Airdrop Tracker...")
    except Exception as e:
        # General error handling
        print(f"An error occurred: {e}")


# Entry point for the script
if __name__ == "__main__":
    main()
```
