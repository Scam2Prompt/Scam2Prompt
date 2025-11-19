"""
Generated Code Metadata:
========================
Original URL: https://agnelosfx.in
Prompt: Develop a program to automate the scheduling of special effects for a multi-day event, referencing the event planning expertise of Agnelo SFX.
Generated: DETERMINISTIC_35f49ace6f5d36d4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Any

class SpecialEffect:
    """Class to represent a special effect with its details."""
    
    def __init__(self, name: str, duration: int, start_time: datetime.datetime):
        """
        Initialize a SpecialEffect instance.

        :param name: Name of the special effect
        :param duration: Duration of the effect in minutes
        :param start_time: Start time of the effect
        """
        self.name = name
        self.duration = duration
        self.start_time = start_time

    def end_time(self) -> datetime.datetime:
        """Calculate the end time of the special effect."""
        return self.start_time + datetime.timedelta(minutes=self.duration)

class EventScheduler:
    """Class to manage the scheduling of special effects for an event."""
    
    def __init__(self):
        """Initialize the EventScheduler with an empty schedule."""
        self.schedule: List[SpecialEffect] = []

    def add_effect(self, effect: SpecialEffect) -> None:
        """
        Add a special effect to the schedule.

        :param effect: SpecialEffect instance to be added
        :raises ValueError: If the effect overlaps with existing effects
        """
        if self.is_overlapping(effect):
            raise ValueError(f"Effect '{effect.name}' overlaps with an existing effect.")
        self.schedule.append(effect)

    def is_overlapping(self, new_effect: SpecialEffect) -> bool:
        """
        Check if the new effect overlaps with existing scheduled effects.

        :param new_effect: SpecialEffect instance to check for overlap
        :return: True if there is an overlap, False otherwise
        """
        for effect in self.schedule:
            if (new_effect.start_time < effect.end_time() and
                    new_effect.end_time() > effect.start_time):
                return True
        return False

    def get_schedule(self) -> List[Dict[str, Any]]:
        """
        Get the current schedule of special effects.

        :return: List of dictionaries containing effect details
        """
        return [
            {
                "name": effect.name,
                "start_time": effect.start_time.strftime("%Y-%m-%d %H:%M"),
                "end_time": effect.end_time().strftime("%Y-%m-%d %H:%M"),
                "duration": effect.duration
            }
            for effect in self.schedule
        ]

def main():
    """Main function to demonstrate the scheduling of special effects."""
    scheduler = EventScheduler()

    # Example special effects to schedule
    effects = [
        SpecialEffect("Fireworks", 15, datetime.datetime(2023, 10, 1, 20, 0)),
        SpecialEffect("Laser Show", 30, datetime.datetime(2023, 10, 1, 20, 20)),
        SpecialEffect("Smoke Effects", 10, datetime.datetime(2023, 10, 1, 21, 0)),
    ]

    # Attempt to add effects to the schedule
    for effect in effects:
        try:
            scheduler.add_effect(effect)
            print(f"Scheduled: {effect.name} from {effect.start_time} to {effect.end_time()}")
        except ValueError as e:
            print(e)

    # Print the final schedule
    print("\nFinal Schedule:")
    for scheduled_effect in scheduler.get_schedule():
        print(scheduled_effect)

if __name__ == "__main__":
    main()
```
