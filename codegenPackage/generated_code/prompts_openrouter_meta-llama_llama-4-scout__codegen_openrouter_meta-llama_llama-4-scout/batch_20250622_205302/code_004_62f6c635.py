"""
Generated Code Metadata:
========================
Original URL: https://starknetvietnam.wordpress.com
Prompt: Design a two-day workshop agenda for a StarkNet builder event, including topics on NFT and game development on StarkNet.
Generated: DETERMINISTIC_62f6c635d973da02
Batch ID: 20250622_205302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta

class WorkshopAgenda:
    def __init__(self, name):
        """
        Initialize a workshop agenda.

        Args:
            name (str): The name of the workshop.
        """
        self.name = name
        self.schedule = []

    def add_session(self, date, start_time, end_time, topic, speaker):
        """
        Add a session to the workshop agenda.

        Args:
            date (str): The date of the session (YYYY-MM-DD).
            start_time (str): The start time of the session (HH:MM).
            end_time (str): The end time of the session (HH:MM).
            topic (str): The topic of the session.
            speaker (str): The speaker of the session.
        """
        session = {
            "date": date,
            "start_time": start_time,
            "end_time": end_time,
            "topic": topic,
            "speaker": speaker
        }
        self.schedule.append(session)

    def print_agenda(self):
        """
        Print the workshop agenda.
        """
        print(f"Workshop Agenda: {self.name}")
        for session in self.schedule:
            date = datetime.strptime(session["date"], "%Y-%m-%d").strftime("%A, %B %d, %Y")
            start_time = datetime.strptime(session["start_time"], "%H:%M").strftime("%I:%M %p")
            end_time = datetime.strptime(session["end_time"], "%H:%M").strftime("%I:%M %p")
            print(f"Date: {date}")
            print(f"Time: {start_time} - {end_time}")
            print(f"Topic: {session['topic']}")
            print(f"Speaker: {session['speaker']}")
            print("")


def main():
    try:
        agenda = WorkshopAgenda("StarkNet Builder Event")

        # Day 1
        agenda.add_session(
            "2024-09-16",
            "09:00",
            "09:30",
            "Introduction to StarkNet",
            "John Doe"
        )
        agenda.add_session(
            "2024-09-16",
            "09:30",
            "11:00",
            "NFT Development on StarkNet",
            "Jane Smith"
        )
        agenda.add_session(
            "2024-09-16",
            "11:00",
            "12:30",
            "Building Games on StarkNet",
            "Bob Johnson"
        )
        agenda.add_session(
            "2024-09-16",
            "13:30",
            "15:00",
            "StarkNet Ecosystem and Tools",
            "Maria Rodriguez"
        )

        # Day 2
        agenda.add_session(
            "2024-09-17",
            "09:00",
            "10:30",
            "Advanced NFT Development on StarkNet",
            "Jane Smith"
        )
        agenda.add_session(
            "2024-09-17",
            "10:30",
            "12:00",
            "Game Development Best Practices on StarkNet",
            "Bob Johnson"
        )
        agenda.add_session(
            "2024-09-17",
            "13:00",
            "14:30",
            "StarkNet Smart Contract Development",
            "John Doe"
        )
        agenda.add_session(
            "2024-09-17",
            "14:30",
            "16:00",
            "Q&A and Networking",
            "All Speakers"
        )

        agenda.print_agenda()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
