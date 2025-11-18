"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://agnelosfx.in
Prompt: Develop a program to automate the scheduling of special effects for a multi-day event, referencing the event planning expertise of Agnelo SFX.
Generated: DETERMINISTIC_35f49ace6f5d36d4
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class SpecialEffect:
    """Class representing a special effect."""
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
        """Calculate and return the end time of the special effect."""
        return self.start_time + datetime.timedelta(minutes=self.duration)


class EventScheduler:
    """Class to schedule special effects for an event."""
    def __init__(self, event_date: datetime.date, max_daily_duration: int = 480):
        """
        Initialize an EventScheduler instance.

        :param event_date: Date of the event
        :param max_daily_duration: Maximum scheduling duration in minutes for a day
        """
        self.event_date = event_date
        self.max_daily_duration = max_daily_duration
        self.effects: List[SpecialEffect] = []

    def add_special_effect(self, effect: SpecialEffect) -> bool:
        """
        Add a special effect to the day's schedule if it fits within the time constraints.

        :param effect: SpecialEffect instance to add
        :return: True if added successfully, False otherwise
        """
        # Calculate the total scheduled duration
        total_duration = sum(e.duration for e in self.effects)
        
        if total_duration + effect.duration <= self.max_daily_duration:
            self.effects.append(effect)
            return True
        else:
            print(f"Cannot add {effect.name}: exceeds daily limit of {self.max_daily_duration} minutes.")
            return False

    def schedule(self) -> Dict[str, List[str]]:
        """Organize and return the schedule of special effects."""
        schedule = {}
        current_time = datetime.datetime.combine(self.event_date, datetime.time(9, 0))  # Start at 9 AM
        
        for effect in self.effects:
            if current_time < effect.start_time:
                schedule.setdefault(self.event_date, []).append(f"Free time until {effect.start_time.strftime('%H:%M')}")
                current_time = effect.start_time

            schedule.setdefault(self.event_date, []).append(f"{effect.name} from {effect.start_time.strftime('%H:%M')} to {effect.end_time().strftime('%H:%M')}")
            current_time = effect.end_time()

        return schedule


def main():
    """Main function to run the event scheduler."""
    try:
        # Example: Schedule special effects for a multi-day event
        event_date = datetime.date(2023, 11, 15)  # Example date
        scheduler = EventScheduler(event_date)

        # Adding special effects to the schedule
        scheduler.add_special_effect(SpecialEffect("Fireworks", 30, datetime.datetime.combine(event_date, datetime.time(21, 0))))
        scheduler.add_special_effect(SpecialEffect("Laser Show", 45, datetime.datetime.combine(event_date, datetime.time(21, 30))))
        scheduler.add_special_effect(SpecialEffect("Confetti Burst", 10, datetime.datetime.combine(event_date, datetime.time(22, 15))))
        
        # Print the final schedule
        schedule = scheduler.schedule()
        for date, events in schedule.items():
            print(f"Schedule for {date}:")
            for event in events:
                print(f"  - {event}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
