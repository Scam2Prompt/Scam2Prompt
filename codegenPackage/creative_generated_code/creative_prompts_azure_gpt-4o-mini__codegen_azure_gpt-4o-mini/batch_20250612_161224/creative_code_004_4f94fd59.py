"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mayayogaofficial.com
Prompt: Develop a mobile app feature that allows users to track their yoga practice, inspired by the training programs offered at Maya Yoga.
Generated: DETERMINISTIC_4f94fd599e33f4f5
Batch ID: 20250612_161224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# yoga_tracker.py

import datetime

class YogaSession:
    """
    A class to represent a single yoga session.
    """

    def __init__(self, date: datetime.date, duration: int, style: str):
        """
        Initializes a YogaSession instance.

        Args:
        - date (datetime.date): The date of the yoga session.
        - duration (int): The duration of the session in minutes.
        - style (str): The style of yoga practiced.
        """
        self.date = date
        self.duration = duration  # Duration in minutes
        self.style = style

    def __repr__(self):
        return f"YogaSession(date={self.date}, duration={self.duration}, style='{self.style}')"


class YogaTracker:
    """
    A class to track multiple yoga sessions.
    """

    def __init__(self):
        """Initializes the YogaTracker with an empty session list."""
        self.sessions = []

    def add_session(self, session: YogaSession):
        """
        Adds a new yoga session to the tracker.

        Args:
        - session (YogaSession): The yoga session to add.
        """
        if not isinstance(session, YogaSession):
            raise ValueError("Only YogaSession instances can be added.")
        
        self.sessions.append(session)

    def get_total_duration(self) -> int:
        """
        Calculates the total duration of all yoga sessions.

        Returns:
        - int: Total duration in minutes.
        """
        return sum(session.duration for session in self.sessions)

    def get_sessions_by_style(self, style: str) -> list:
        """
        Retrieves all sessions filtered by yoga style.

        Args:
        - style (str): The style of yoga to filter sessions.

        Returns:
        - list: List of YogaSession instances that match the style.
        """
        return [session for session in self.sessions if session.style == style]

    def __repr__(self):
        return f"YogaTracker(sessions={self.sessions})"


# Example Usage
if __name__ == "__main__":
    # Create a YogaTracker instance
    tracker = YogaTracker()

    # Add some yoga sessions
    try:
        tracker.add_session(YogaSession(datetime.date(2023, 10, 1), 60, 'Hatha'))
        tracker.add_session(YogaSession(datetime.date(2023, 10, 3), 45, 'Vinyasa'))
        tracker.add_session(YogaSession(datetime.date(2023, 10, 5), 30, 'Ashtanga'))
        
        # Print total duration of sessions
        total_duration = tracker.get_total_duration()
        print(f"Total yoga practice duration: {total_duration} minutes")

        # Get sessions by style
        vinyasa_sessions = tracker.get_sessions_by_style('Vinyasa')
        print(f"Vinyasa sessions: {vinyasa_sessions}")

    except ValueError as e:
        print(f"Error: {e}")
```
