"""
Generated Code Metadata:
========================
Original URL: https://delsolmontessorihn.com
Prompt: "Develop a simple algorithm for a school event management system, prioritizing events like the Copa Montessori and Feria de Robótica, as seen on the Del Sol Montessori website."
Generated: DETERMINISTIC_4d94940490852a4d
Batch ID: 20250622_205612
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Event:
    """
    A class to represent an event in the school event management system.
    """

    def __init__(self, name, date, priority):
        """
        Initializes an Event instance.

        :param name: str - The name of the event.
        :param date: str - The date of the event in 'YYYY-MM-DD' format.
        :param priority: int - The priority level of the event (higher number means higher priority).
        """
        self.name = name
        self.date = date
        self.priority = priority

    def __repr__(self):
        return f"Event(name={self.name}, date={self.date}, priority={self.priority})"


class EventManager:
    """
    A class to manage events in the school event management system.
    """

    def __init__(self):
        """
        Initializes the EventManager with an empty event list.
        """
        self.events = []

    def add_event(self, event):
        """
        Adds an event to the event manager.

        :param event: Event - The event to be added.
        :raises ValueError: If the event is not an instance of Event.
        """
        if not isinstance(event, Event):
            raise ValueError("Only Event instances can be added.")
        self.events.append(event)

    def get_sorted_events(self):
        """
        Returns a list of events sorted by priority and date.

        :return: list - A sorted list of events.
        """
        return sorted(self.events, key=lambda e: (-e.priority, e.date))

    def display_events(self):
        """
        Displays the events in a formatted manner.
        """
        sorted_events = self.get_sorted_events()
        if not sorted_events:
            print("No events scheduled.")
            return

        print("Scheduled Events:")
        for event in sorted_events:
            print(f"{event.date}: {event.name} (Priority: {event.priority})")


# Example usage
if __name__ == "__main__":
    event_manager = EventManager()

    # Adding events with varying priorities
    try:
        event_manager.add_event(Event("Copa Montessori", "2023-05-15", priority=10))
        event_manager.add_event(Event("Feria de Robótica", "2023-06-20", priority=9))
        event_manager.add_event(Event("Science Fair", "2023-04-10", priority=5))
        event_manager.add_event(Event("Art Exhibition", "2023-07-01", priority=7))

        # Displaying the events
        event_manager.display_events()
    except ValueError as e:
        print(f"Error: {e}")
```
